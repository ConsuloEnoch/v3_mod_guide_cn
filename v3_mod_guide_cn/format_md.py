#!/usr/bin/env python3
"""
维多利亚3 Mod开发指南 Markdown 格式化脚本
"""

import re
import os
import sys
from pathlib import Path


def format_code_blocks(content):
    """格式化代码块语言标签"""
    lines = content.split("\n")
    result = []
    in_code_block = False

    for i, line in enumerate(lines):
        code_fence_match = re.match(r"^(\s*)```(\w*)\s*$", line)
        if code_fence_match:
            if not in_code_block:
                in_code_block = True
                indent = code_fence_match.group(1)
                lang = code_fence_match.group(2)

                # 如果没有指定语言或者是txt，改为pdx
                if lang == "" or lang == "txt":
                    result.append(f"{indent}```pdx")
                else:
                    result.append(line)
            else:
                in_code_block = False
                result.append(line)
        else:
            result.append(line)

    return "\n".join(result)


def remove_trailing_whitespace(content):
    """移除行尾空格"""
    lines = content.split("\n")
    result = []
    for line in lines:
        result.append(line.rstrip())
    return "\n".join(result)


def format_tables(content):
    """格式化表格 - 确保分隔行正确"""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # 检查是否是表格行
        if "|" in line and not line.strip().startswith("```"):
            # 收集整个表格
            table_lines = [line]
            j = i + 1

            # 继续收集表格行
            while (
                j < len(lines)
                and "|" in lines[j]
                and not lines[j].strip().startswith("```")
            ):
                table_lines.append(lines[j])
                j += 1

            # 如果至少有2行，才认为是表格
            if len(table_lines) >= 2:
                # 格式化表格
                formatted_table = format_table_block(table_lines)
                result.extend(formatted_table)
                i = j
                continue
            else:
                result.append(line)
        else:
            result.append(line)

        i += 1

    return "\n".join(result)


def format_table_block(lines):
    """格式化一个表格块"""
    if not lines:
        return lines

    # 解析表格
    parsed_rows = []
    for line in lines:
        # 分割单元格
        cells = line.split("|")
        # 清理单元格
        cells = [cell.strip() for cell in cells]
        # 移除开头和结尾的空单元格
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        if cells:
            parsed_rows.append(cells)

    if not parsed_rows:
        return lines

    # 确定列数
    num_cols = max(len(row) for row in parsed_rows)

    # 标准化所有行到相同的列数
    for row in parsed_rows:
        while len(row) < num_cols:
            row.append("")

    # 检查是否有分隔行
    separator_idx = -1
    for idx, row in enumerate(parsed_rows):
        if all(re.match(r"^[-:]+$", cell) or cell == "" for cell in row):
            separator_idx = idx
            break

    # 如果没有分隔行，在第1行后添加
    if separator_idx == -1 and len(parsed_rows) > 0:
        separator_row = ["---"] * num_cols
        parsed_rows.insert(1, separator_row)
        separator_idx = 1

    # 计算每列的最大宽度
    col_widths = [0] * num_cols
    for row in parsed_rows:
        for j, cell in enumerate(row):
            # 计算显示宽度（中文字符算作2个宽度）
            width = 0
            for char in cell:
                if ord(char) > 127:
                    width += 2
                else:
                    width += 1
            col_widths[j] = max(col_widths[j], width)

    # 格式化每一行
    formatted_lines = []
    for i, row in enumerate(parsed_rows):
        formatted_cells = []
        for j, cell in enumerate(row):
            if i == separator_idx:
                # 分隔行
                formatted_cells.append("-" * max(3, col_widths[j]))
            else:
                # 普通单元格
                cell_width = 0
                for char in cell:
                    if ord(char) > 127:
                        cell_width += 2
                    else:
                        cell_width += 1
                padding = col_widths[j] - cell_width
                formatted_cells.append(cell + " " * padding)

        line = "| " + " | ".join(formatted_cells) + " |"
        line = line.rstrip()
        formatted_lines.append(line)

    return formatted_lines


def ensure_blank_lines_around_code_blocks(content):
    """确保代码块前后有空行"""
    lines = content.split("\n")
    result = []

    for i, line in enumerate(lines):
        if re.match(r"^(\s*)```\w*\s*$", line):
            if result and result[-1].strip() != "":
                if not re.match(r"^(\s*)```\s*$", result[-1]):
                    result.append("")

        result.append(line)

    return "\n".join(result)


def format_tip_box_spacing(content):
    """确保提示框emoji后没有多余空格"""
    patterns = [
        (r"(⚠️)\s+\*\*", r"\1 **"),
        (r"(💡)\s+\*\*", r"\1 **"),
        (r"(🎯)\s+\*\*", r"\1 **"),
        (r"(📖)\s+\*\*", r"\1 **"),
        (r"(❓)\s+\*\*", r"\1 **"),
    ]

    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)

    return content


def process_file(filepath):
    """处理单个文件"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    original_content = content

    content = format_code_blocks(content)
    content = format_tables(content)
    content = remove_trailing_whitespace(content)
    content = ensure_blank_lines_around_code_blocks(content)
    content = format_tip_box_spacing(content)

    if content != original_content:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[OK] Formatted: {filepath}")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    else:
        print(f"[--] No changes: {filepath}")
        return True


def main():
    """主函数"""
    base_dir = Path("v3_mod_guide")

    if not base_dir.exists():
        print(f"Error: Directory {base_dir} not found")
        sys.exit(1)

    md_files = [f for f in base_dir.rglob("*.md") if f.name != "format_md.py"]

    print(f"Found {len(md_files)} markdown files")
    print("=" * 60)

    formatted_count = 0

    for filepath in sorted(md_files):
        if process_file(filepath):
            formatted_count += 1

    print("=" * 60)
    print(f"Processed {formatted_count} files")


if __name__ == "__main__":
    main()
