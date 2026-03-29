# 第二十四章：GUI界面修改

## 本章目标

学习本章后，你将能够：
- 理解GUI脚本的基本结构和语法
- 创建和修改游戏界面元素
- 使用模板和类型系统复用界面代码
- 制作自定义信息面板
- 理解界面层级和布局系统

---

## 概念讲解：界面是什么？

### 比喻：重新装修你的房子

想象一下，维多利亚3的游戏界面就像一栋精心设计的房子。每个房间（窗口）都有特定的功能：
- **国家概览面板** = 客厅，展示最重要的信息
- **科技树** = 书房，显示研究进度
- **市场界面** = 仓库，管理商品和贸易

GUI修改就像是重新装修房子：
- 你可以重新粉刷墙壁（修改颜色和样式）
- 可以添加新的家具（创建新的界面元素）
- 可以重新布置房间（调整布局）
- 甚至可以扩建新房（创建全新的窗口）

### 什么是GUI？

GUI（Graphical User Interface，图形用户界面）是玩家与游戏交互的桥梁。在维多利亚3中，所有的按钮、窗口、信息面板都是GUI的一部分。

---

## 24.1 GUI脚本基础

### 24.1.1 文件位置

GUI脚本存储在Mod的`gui/`文件夹中：

```pdx
my_mod/
├── gui/
│   ├── my_custom_window.gui      # 自定义窗口定义
│   └── scripted_widgets/
│       └── my_widgets.txt        # 注册脚本化部件

```

⚠️ **注意**：GUI文件使用`.gui`扩展名，而不是.txt。

### 24.1.2 基本语法

GUI脚本使用类似于CSS的结构，但有自己的语法规则：

```pdx
# 这是一个简单的按钮定义
widget = {
    name = my_button
    size = { 200 50 }           # 宽200像素，高50像素

    button = {
        name = button_graphics
        size = { 100% 100% }    # 填满父容器

        textbox = {
            name = button_text
            raw_text = "点击我"
        }
    }
}

```

**核心概念**：
- **widget（部件）**：界面元素的基本容器
- **container（容器）**：可以包含其他元素的盒子
- **button（按钮）**：可点击的交互元素
- **textbox（文本框）**：显示文字的区域

---

## 24.2 模板系统

### 24.2.1 什么是模板？

模板就像是装修房子的设计图纸。你定义一次样式，然后可以在多个地方复用。

💡 **比喻**：就像快餐店的装修，所有分店使用相同的设计模板，但可以根据当地情况微调。

### 24.2.2 定义模板

在`.gui`文件中定义模板：

```pdx
# 定义一个标准按钮模板
template standard_button {
    size = { 150 40 }

    button = {
        name = button_bg
        size = { 100% 100% }

        textbox = {
            name = button_label
            raw_text = "默认文字"
            align = center
        }
    }
}

```

### 24.2.3 使用模板

```pdx
widget = {
    name = my_panel

    # 使用标准按钮模板
    using = standard_button

    # 可以覆盖模板中的属性
    textbox = {
        name = button_label
        raw_text = "自定义文字"
    }
}

```

---

## 24.3 类型系统

### 24.3.1 什么是类型？

类型是比模板更强大的复用机制。它允许：
- 继承其他类型
- 覆盖特定代码块
- 扩展原有功能

### 24.3.2 定义类型

```pdx
types my_gui_types {
    # 基础按钮类型
    type base_button = widget {
        size = { 150 40 }

        button = {
            name = bg
            size = { 100% 100% }

            # 定义可覆盖的代码块
            block "text_block" {
                textbox = {
                    name = label
                    raw_text = "按钮"
                }
            }
        }
    }

    # 扩展类型：危险按钮（红色）
    type danger_button = base_button {
        # 覆盖文本块
        blockoverride "text_block" {
            textbox = {
                name = label
                raw_text = "危险操作"
                fontcolor = { 1.0 0.0 0.0 1.0 }  # 红色
            }
        }
    }
}

```

### 24.3.3 使用类型

```pdx
widget = {
    name = action_panel

    # 使用基础按钮
    base_button = {}

    # 使用危险按钮，并自定义文字
    danger_button = {
        blockoverride "text_block" {
            textbox = {
                name = label
                raw_text = "宣战"
                fontcolor = { 1.0 0.0 0.0 1.0 }
            }
        }
    }
}

```

---

## 24.4 布局系统

### 24.4.1 基本布局容器

GUI提供几种布局容器：

| 容器类型    | 说明     | 使用场景         |
| ----------- | -------- | ---------------- |
| `widget`    | 基础容器 | 通用容器         |
| `hbox`      | 水平盒子 | 横向排列元素     |
| `vbox`      | 垂直盒子 | 纵向排列元素     |
| `container` | 灵活容器 | 需要精确控制位置 |

### 24.4.2 水平布局示例

```pdx
hbox = {
    name = button_row
    spacing = 10              # 元素间距10像素

    # 三个按钮水平排列
    button = { name = btn1 raw_text = "按钮1" }
    button = { name = btn2 raw_text = "按钮2" }
    button = { name = btn3 raw_text = "按钮3" }
}

```

### 24.4.3 垂直布局示例

```pdx
vbox = {
    name = info_column
    spacing = 5
    margin = { 10 10 10 10 }  # 上右下左边距

    # 信息从上到下排列
    textbox = { raw_text = "国家：大清" }
    textbox = { raw_text = "人口：4.5亿" }
    textbox = { raw_text = "GDP：2.3亿" }
}

```

### 24.4.4 复杂嵌套布局

```pdx
widget = {
    name = main_panel
    size = { 400 300 }

    # 顶部标题栏
    widget = {
        name = header
        size = { 100% 50 }

        textbox = {
            name = title
            raw_text = "国家信息"
            align = center
        }
    }

    # 主体内容区
    hbox = {
        name = content
        position = { 0 50 }     # 在标题下方
        size = { 100% 250 }

        # 左侧信息列
        vbox = {
            name = left_col
            size = { 50% 100% }

            textbox = { raw_text = "基本信息" }
            textbox = { raw_text = "经济统计" }
            textbox = { raw_text = "军事状况" }
        }

        # 右侧操作列
        vbox = {
            name = right_col
            size = { 50% 100% }

            button = { raw_text = "查看详情" }
            button = { raw_text = "制定政策" }
            button = { raw_text = "外交行动" }
        }
    }
}

```

---

## 24.5 创建自定义面板

### 24.5.1 面板基础

创建自定义面板需要：
1. 定义面板类型
2. 注册到游戏界面
3. 添加触发逻辑（何时显示）

### 24.5.2 侧边面板示例

侧边面板是游戏中常见的界面元素（如国家概览面板）：

```pdx
# 文件：gui/my_custom_panel.gui

types my_panels {
    # 定义江南共和国信息面板
    type jiangnan_info_panel = default_block_window {
        # 层级设置，确保不覆盖其他重要界面
        layer = layer_ingame_menu

        # 可见性：通过变量系统控制
        visible = "[GetVariableSystem.HasValue('show_jiangnan_panel', 'true')]"

        # 动画设置
        blockoverride "animation_state_block" {
            state = {
                name = _show
                # 关闭其他面板后再显示
                on_finish = "[InformationPanelBar.ClosePanel]"
                on_finish = "[MapListPanelManager.CloseCurrentPanel]"
            }
        }

        # 窗口内容
        blockoverride "content" {
            vbox = {
                spacing = 10
                margin = { 20 20 20 20 }

                # 标题
                textbox = {
                    name = panel_title
                    raw_text = "江南共和国概况"
                    font = header_font
                    align = center
                }

                # 分隔线
                widget = {
                    size = { 100% 2 }
                    background = { color = { 0.5 0.5 0.5 1.0 } }
                }

                # 信息区域
                vbox = {
                    spacing = 5

                    hbox = {
                        spacing = 10
                        textbox = { raw_text = "首都：" }
                        textbox = { raw_text = "南京" }
                    }

                    hbox = {
                        spacing = 10
                        textbox = { raw_text = "人口：" }
                        textbox = { raw_text = "4500万" }
                    }

                    hbox = {
                        spacing = 10
                        textbox = { raw_text = "GDP：" }
                        textbox = { raw_text = "8000万" }
                    }
                }

                # 关闭按钮
                button = {
                    name = close_btn
                    size = { 100% 40 }
                    raw_text = "关闭"

                    # 点击时隐藏面板
                    onclick = "[GetVariableSystem.Set('show_jiangnan_panel', 'false')]"
                }
            }
        }
    }
}

```

### 24.5.3 全屏面板

全屏面板用于需要占据整个屏幕的界面（如科技树）：

```pdx
types my_panels {
    type jiangnan_fullscreen_panel = fullscreen_block_window {
        layer = layer_ingame_menu
        visible = "[GetVariableSystem.HasValue('show_fullscreen_jiangnan', 'true')]"

        blockoverride "animation_state_block" {
            state = {
                name = _show
                on_finish = "[HideAllPanels]"  # 隐藏所有其他面板
            }
        }

        # 全屏内容...
    }
}

```

---

## 24.6 注册脚本化部件

### 24.6.1 创建脚本化部件文件

要让自定义面板在游戏中显示，需要创建脚本化部件：

```pdx
# 文件：gui/scripted_widgets/my_custom_widgets.txt

gui/my_custom_panel.gui = jiangnan_info_panel_container

```

### 24.6.2 定义容器部件

在`.gui`文件中定义容器：

```pdx
# 文件：gui/my_custom_panel.gui

widget = {
    name = jiangnan_info_panel_container
    layer = layer_ingame_menu
    size = { 100% 100% }        # 全屏大小

    # 这里放置你的面板
    jiangnan_info_panel = {}
}

```

### 24.6.3 在游戏中触发显示

可以通过事件、决策或控制台命令来显示面板：

```pdx
# 在事件中显示面板
jiangnan_info_event = {
    type = country_event

    immediate = {
        # 设置变量显示面板
        set_variable = {
            name = show_jiangnan_panel
            value = true
        }
    }

    option = {
        name = "查看详细信息"
    }
}

```

---

## 24.7 实战案例：江南共和国信息面板

### 24.7.1 目标

创建一个美观的江南共和国信息面板，显示：
- 国旗和国名
- 基本统计数据
- 特色介绍
- 关闭按钮

### 24.7.2 完整代码

```pdx
# 文件：gui/jiangnan_panel.gui

types jiangnan_gui {
    # 江南共和国面板类型
    type jiangnan_republic_panel = default_block_window {
        layer = layer_ingame_menu
        size = { 500 600 }

        # 可见性控制
        visible = "[GetVariableSystem.HasValue('jiangnan_panel_open', 'yes')]"

        # 动画设置
        blockoverride "animation_state_block" {
            state = {
                name = _show
                on_finish = "[InformationPanelBar.ClosePanel]"
                on_finish = "[MapListPanelManager.CloseCurrentPanel]"
            }
        }

        # 窗口内容
        blockoverride "content" {
            vbox = {
                spacing = 15
                margin = { 25 25 25 25 }

                # ===== 标题区域 =====
                hbox = {
                    spacing = 15
                    align = center

                    # 国旗占位符（可用图标代替）
                    widget = {
                        name = flag_placeholder
                        size = { 80 60 }
                        background = { color = { 0.2 0.4 0.8 1.0 } }
                    }

                    textbox = {
                        name = country_name
                        raw_text = "江南共和国"
                        font = header_font
                    }
                }

                # 分隔线
                widget = {
                    size = { 100% 3 }
                    background = { color = { 0.7 0.5 0.2 1.0 } }
                }

                # ===== 统计数据区域 =====
                vbox = {
                    spacing = 10

                    textbox = {
                        raw_text = "国家概况"
                        font = subheader_font
                    }

                    gridbox = {
                        name = stats_grid
                        datamodel = "[GetJiangnanStats]"
                        flipdirection = yes

                        item = {
                            hbox = {
                                spacing = 10
                                textbox = { text = "[JiangnanStat.GetName]" }
                                textbox = { text = "[JiangnanStat.GetValue]" }
                            }
                        }
                    }
                }

                # ===== 特色介绍 =====
                vbox = {
                    spacing = 8

                    textbox = {
                        raw_text = "国家特色"
                        font = subheader_font
                    }

                    textbox = {
                        raw_text = "洋务运动的先锋，现代化的先行者"
                        multiline = yes
                    }

                    textbox = {
                        raw_text = "拥有发达的纺织业和造船业"
                        multiline = yes
                    }

                    textbox = {
                        raw_text = "面临传统势力和外国列强的双重挑战"
                        multiline = yes
                    }
                }

                expand = {}  # 填充剩余空间

                # ===== 关闭按钮 =====
                button = {
                    name = close_button
                    size = { 100% 50 }

                    background = {
                        texture = "gfx/interface/buttons/button_200_50.dds"
                    }

                    textbox = {
                        name = button_text
                        raw_text = "关闭面板"
                        align = center
                        fontcolor = { 1.0 1.0 1.0 1.0 }
                    }

                    # 点击关闭
                    onclick = "[GetVariableSystem.Set('jiangnan_panel_open', 'no')]"
                }
            }
        }
    }
}

# 主容器
widget = {
    name = jiangnan_panel_root
    layer = layer_ingame_menu
    size = { 100% 100% }

    hbox = {
| parentanchor = top | left |
| ------------------ | ---- |
        layoutpolicy_horizontal = expanding
        layoutpolicy_vertical = expanding
        margin_top = 85

        widget = {
            layoutpolicy_horizontal = expanding
            layoutpolicy_vertical = expanding

            hbox = {
                layoutpolicy_horizontal = expanding
                layoutpolicy_vertical = expanding

                jiangnan_republic_panel = {}
                expand = {}
            }
        }
    }
}

```

### 24.7.3 注册脚本化部件

```pdx
# 文件：gui/scripted_widgets/jiangnan_widgets.txt

gui/jiangnan_panel.gui = jiangnan_panel_root

```

### 24.7.4 通过事件触发

```pdx
# 文件：events/jiangnan_events.txt

namespace = jiangnan_gui

# 显示面板事件
jiangnan_gui.1 = {
    type = country_event

    title = jiangnan_panel_title
    desc = jiangnan_panel_desc

    immediate = {
        set_variable = {
            name = jiangnan_panel_open
            value = yes
        }
    }

    option = {
        name = "查看详情"
    }
}

```

---

## 24.8 常用GUI元素参考

### 24.8.1 基本元素

| 元素      | 语法             | 用途       |
| --------- | ---------------- | ---------- |
| widget    | `widget = {}`    | 通用容器   |
| button    | `button = {}`    | 可点击按钮 |
| textbox   | `textbox = {}`   | 文字显示   |
| icon      | `icon = {}`      | 图标显示   |
| container | `container = {}` | 灵活容器   |
| hbox      | `hbox = {}`      | 水平布局   |
| vbox      | `vbox = {}`      | 垂直布局   |

### 24.8.2 常用属性

| 属性       | 说明     | 示例                       |
| ---------- | -------- | -------------------------- |
| `size`     | 大小     | `size = { 200 100 }`       |
| `position` | 位置     | `position = { 50 50 }`     |
| `margin`   | 边距     | `margin = { 10 10 10 10 }` |
| `spacing`  | 间距     | `spacing = 5`              |
| `visible`  | 可见性   | `visible = yes`            |
| `enabled`  | 是否启用 | `enabled = yes`            |
| `align`    | 对齐     | `align = center`           |

### 24.8.3 颜色格式

颜色使用RGBA格式（0.0-1.0）：

```pdx
# 红色
fontcolor = { 1.0 0.0 0.0 1.0 }

# 白色
fontcolor = { 1.0 1.0 1.0 1.0 }

# 半透明黑色
background = { color = { 0.0 0.0 0.0 0.5 } }

```

---

## 常见问题

**Q1：我的面板显示不出来怎么办？**

检查以下几点：
1. 脚本化部件是否正确注册
2. `visible`条件是否满足
3. 文件路径是否正确
4. 语法是否有错误（检查error.log）

**Q2：如何获取当前国家的数据？**

使用事件目标系统：

```pdx
textbox = {
    text = "[Country.GetName]"  # 显示国家名称
text = "[Country.GetPopulation]"  # 显示人口
}

```

**Q3：面板位置不对，如何调整？**

使用`position`属性或调整布局容器：

```pdx
widget = {
    position = { x坐标 y坐标 }
| parentanchor = top | left  # 相对于父容器的锚点 |
| ------------------ | -------------------------- |
}

```

**Q4：如何修改现有游戏界面？**

1. 找到原版界面文件（在game/gui/中）
2. 复制到Mod的gui/文件夹
3. 使用`blockoverride`覆盖特定部分
4. 保持文件结构和命名一致

---

## 本章小结

本章学习了GUI界面修改的核心知识：

1. **GUI基础**：文件位置、基本语法、核心元素
2. **模板系统**：定义可复用的界面模板
3. **类型系统**：继承、覆盖、扩展界面类型
4. **布局系统**：hbox/vbox嵌套、定位、边距
5. **自定义面板**：创建和注册脚本化部件
6. **实战案例**：江南共和国信息面板的完整实现

💡 **提示**：GUI修改需要大量试错。建议先在简单面板上练习，逐步掌握布局技巧。

---

## 练习建议

1. **练习1**：创建一个显示国家基本信息的简单面板
2. **练习2**：修改国家概览面板，添加自定义按钮
3. **练习3**：创建一个事件触发的弹出窗口
4. **练习4**：尝试修改科技树界面的布局

📖 **参考**：详细GUI语法参考请查看附录中的GUI脚本参考部分。
