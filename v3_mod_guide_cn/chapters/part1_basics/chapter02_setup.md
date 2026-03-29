# 第2章：准备工作

> 工欲善其事，必先利其器。在本章中，我们将安装必要的工具，开启调试模式，并创建你的第一个Mod。

## 本章目标

完成本章学习后，你将能够：
- 安装和配置Mod开发所需工具
- 开启游戏的调试模式
- 创建你的第一个可运行的Mod
- 理解Mod的基本文件结构

---

## 2.1 必要工具

### 2.1.1 文本编辑器

Mod开发本质上就是编写文本文件，因此你需要一个**文本编辑器**。以下是推荐选择：

#### 首选：Visual Studio Code（免费）

**下载地址**：https://code.visualstudio.com/

**优点**：
- 完全免费且开源
- 强大的扩展系统
- 代码高亮显示
- 错误提示和自动补全

**推荐扩展**：
1. **Victoria 3 Scripting** - 提供Paradox脚本语言支持
2. **Prettier** - 代码格式化
3. **Better Comments** - 更好的注释高亮

**安装扩展步骤**：
1. 打开VS Code
2. 点击左侧边栏的扩展图标（四个方块）
3. 搜索"Victoria 3"
4. 安装评价最高的Victoria 3相关扩展

#### 备选：Notepad++（免费，轻量）

**下载地址**：https://notepad-plus-plus.org/

**优点**：
- 启动速度快
- 资源占用少
- 支持多种编码格式

**缺点**：
- 没有专门的Victoria 3支持
- 功能相对简单

#### 其他选择

- **Sublime Text**：速度快，但需要付费
- **IntelliJ IDEA**：功能强大，但较重
- **Windows记事本**：不推荐，缺少代码高亮

> ⚠️ **注意**：不要使用Word、WPS等富文本编辑器！它们会添加隐藏格式，导致Mod无法正常工作。

### 2.1.2 文件管理器

Windows自带的文件资源管理器已经足够。建议：

- 开启"显示文件扩展名"（重要！）
  1. 打开文件资源管理器
  2. 点击"查看"选项卡
  3. 勾选"文件扩展名"

- 学会使用快捷键（Ctrl+C复制、Ctrl+V粘贴、F2重命名）

### 2.1.3 DDS图像工具（可选）

如果你要修改游戏贴图（如旗帜、模型），需要DDS格式的工具：

- **GIMP**（免费）+ DDS插件
- **Photoshop**（付费）+ Intel DDS插件
- **Paint.NET**（免费）+ DDS插件

---

## 2.2 找到游戏文件

### 2.2.1 Mod文件夹位置

Mod文件存放在特定位置，游戏会从这里加载Mod：

**Windows**：

```pdx
%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\

```

通常就是：

```pdx
C:\Users\[你的用户名]\Documents\Paradox Interactive\Victoria 3\mod\

```

**Linux**：

```pdx
~/.local/share/Paradox Interactive/Victoria 3/mod/

```

**Mac OS**：

```pdx
~/Documents/Paradox Interactive/Victoria 3/mod/

```

> ⚠️ **重要**：如果`mod`文件夹不存在，请手动创建它！

### 2.2.2 游戏本体文件位置

了解游戏本体文件在哪里也很重要：

**Steam版本**：

```pdx
SteamLibrary\steamapps\common\Victoria 3\game\

```

这里面包含：
- `common/` - 游戏数据定义
- `events/` - 游戏事件
- `localization/` - 本地化文本
- `map/` - 地图数据
- 等等...

> 💡 **提示**：不要直接修改游戏本体文件！你的修改会在游戏更新时被覆盖。正确做法是创建Mod来覆盖。

---

## 2.3 开启调试模式

### 2.3.1 什么是调试模式？

调试模式（Debug Mode）是开发者用来测试游戏的特殊模式。开启后：

✅ **获得的能力**：
- 使用控制台命令（如添加金钱、立即完成科技）
- 查看详细的错误日志
- 实时查看游戏变量
- 快速测试Mod效果

⚠️ **注意**：调试模式会影响成就获取，仅在开发Mod时使用。

### 2.3.2 如何开启

#### 方法一：通过Steam启动参数（推荐）

1. 在Steam库中右键点击"Victoria 3"
2. 选择"属性"
3. 在"通用"选项卡中找到"启动选项"
4. 输入：`-debug_mode`
5. 关闭属性窗口
6. 正常启动游戏

#### 方法二：通过快捷方式

1. 找到游戏的可执行文件：

   ```pdx
   SteamLibrary\steamapps\common\Victoria 3\binaries\victoria3.exe

   ```

2. 右键创建快捷方式

3. 右键快捷方式 → 属性

4. 在"目标"字段末尾添加空格和`-debug_mode`：

   ```pdx
   "...\victoria3.exe" -debug_mode

   ```

5. 通过快捷方式启动游戏

#### 验证是否成功

进入游戏后，按下**`键**（键盘左上角，ESC下方），如果弹出控制台，说明调试模式已开启！

### 2.3.3 常用控制台命令

以下是Mod开发时常用的命令：

| 命令               | 作用           | 示例            |
| ------------------ | -------------- | --------------- |
| `cash [数量]`      | 添加国库资金   | `cash 1000`     |
| `prestige [数量]`  | 添加威望       | `prestige 100`  |
| `annex [国家代码]` | 吞并国家       | `annex CHI`     |
| `observe`          | 进入观察者模式 | `observe`       |
| `fastbuild`        | 建筑瞬间完成   | `fastbuild`     |
| `debug_mode`       | 显示调试信息   | `debug_mode`    |
| `reload [文件名]`  | 重新加载文件   | `reload my_mod` |

> 📖 **完整列表**：参见附录J - 控制台命令大全

---

## 2.4 你的第一个Mod

现在让我们动手创建第一个Mod！我们将在10分钟内完成一个简单的Mod，让大清开局就拥有额外1000国库资金。

### 2.4.1 创建Mod文件夹

1. 打开Mod文件夹位置：

   ```pdx
   Documents\Paradox Interactive\Victoria 3\mod\

   ```

2. 创建新文件夹，命名为：

   ```pdx
   my_first_mod

   ```

### 2.4.2 创建metadata.json

1. 在`my_first_mod`文件夹内创建`.metadata`文件夹（注意前面有个点）

2. 在`.metadata`文件夹内创建`metadata.json`文件

3. 用文本编辑器打开，粘贴以下内容：

```json
{
  "name": "我的第一个Mod",
  "id": "com.example.my_first_mod",
  "version": "1.0.0",
  "game_id": "victoria3",
  "supported_game_version": "1.8.*",
  "short_description": "给大清增加开局资金",
  "tags": ["balance"],
  "relationships": [],
  "game_custom_data": {
    "multiplayer_synchronized": true
  }
}

```

**参数说明**：

| 参数                     | 说明                          | 示例                     |
| ------------------------ | ----------------------------- | ------------------------ |
| `name`                   | Mod显示名称                   | 我的第一个Mod            |
| `id`                     | 唯一标识符，用反向域名格式    | com.example.my_first_mod |
| `version`                | Mod版本号                     | 1.0.0                    |
| `supported_game_version` | 支持的游戏版本，`*`表示通配符 | 1.8.*                    |
| `short_description`      | 简短描述                      | 给大清增加开局资金       |
| `tags`                   | 标签，最多5个                 | ["balance", "gameplay"]  |

### 2.4.3 创建效果文件

1. 在`my_first_mod`文件夹内创建文件夹结构：

   ```pdx
   my_first_mod/
   ├── .metadata/
   │   └── metadata.json
   └── common/
       └── history/
           └── countries/

   ```

2. 在`countries`文件夹内创建`my_mod_countries.txt`文件

3. 打开文件，粘贴以下内容：

```pdx
# 修改大清开局设置
CHI = {
    # 添加1000国库资金
    add_treasury = 1000
}

```

**代码解释**：

- `CHI`：国家的代码，代表大清（China）
- `=`：设置该国家的属性
- `{}`：花括号内包含对该国家的所有修改
- `add_treasury = 1000`：效果命令，增加1000国库资金

### 2.4.4 创建本地化文件

为了让Mod显示中文名称，我们添加本地化：

1. 在`my_first_mod`内创建文件夹结构：

   ```pdx
   my_first_mod/
   └── localization/
       └── simp_chinese/

   ```

2. 在`simp_chinese`文件夹内创建`my_mod_l_english.yml`文件

3. 打开文件，粘贴以下内容（**注意**：文件必须以UTF-8 BOM编码保存！）：

```yaml
l_simp_chinese:
 my_first_mod_name:0 "我的第一个Mod"
 my_first_mod_desc:0 "给大清增加1000开局国库资金。"

```

> ⚠️ **重要**：YAML文件必须使用**UTF-8 BOM编码**！
> - VS Code：点击右下角编码 → "Save with Encoding" → "UTF-8 with BOM"
> - Notepad++：编码 → 转为UTF-8-BOM编码

### 2.4.5 在启动器中启用Mod

1. 启动Paradox启动器
2. 在"Mods"选项卡中找到"我的第一个Mod"
3. 勾选启用该Mod
4. 点击"Play"启动游戏

### 2.4.6 验证Mod效果

1. 在游戏主菜单选择"新游戏"
2. 选择1836年开局
3. 选择"大清"（Qing）
4. 进入游戏后查看国库，应该比正常开局多1000

🎉 **恭喜你！你已经成功创建了第一个Mod！**

---

## 2.5 常见错误排查

如果Mod没有生效，检查以下几点：

### 错误1：文件夹位置不对

**症状**：启动器中没有显示Mod

**检查**：确认Mod文件夹放在正确的位置：

```pdx
Documents\Paradox Interactive\Victoria 3\mod\my_first_mod\

```

### 错误2：metadata.json格式错误

**症状**：Mod显示但无法启用

**检查**：
- JSON格式是否正确（每个参数后有逗号，除了最后一个）
- 是否使用了中文引号`""`而不是英文引号`""`
- 文件编码是否为UTF-8

### 错误3：文件路径错误

**症状**：Mod启用但游戏内容未改变

**检查**：
- 文件夹结构是否正确
- 文件名拼写是否正确
- 是否有多余或缺少的文件夹层级

### 错误4：编码问题

**症状**：游戏中显示乱码

**解决**：确保所有.yml文件使用**UTF-8 BOM编码**

### 查看错误日志

如果游戏崩溃或Mod不生效，查看错误日志：

```pdx
Documents\Paradox Interactive\Victoria 3\logs\error.log

```

> 📖 **更多信息**：参见第29章《调试与测试》和附录K《错误代码与解决方案》

---

## 2.6 文件命名规范

### 2.6.1 Mod前缀

为避免与其他Mod冲突，建议给文件名添加Mod前缀：

```pdx
my_mod_events.txt      # 好
my_mod_buildings.txt   # 好
events.txt             # 不推荐（可能与游戏文件或其他Mod冲突）

```

### 2.6.2 命名建议

- 使用小写字母
- 单词间用下划线分隔
- 文件名应具有描述性

**示例**：

```pdx
my_mod_qing_reform_events.txt      # 好
myModQingReformEvents.txt          # 不推荐
qing_reform.txt                    # 可接受但不够具体

```

---

## 本章小结

- 推荐使用**Visual Studio Code**作为文本编辑器
- Mod文件夹位于`Documents\Paradox Interactive\Victoria 3\mod\`
- 通过添加`-debug_mode`启动参数开启调试模式
- 创建Mod需要`metadata.json`和实际的游戏内容文件
- **UTF-8 BOM编码**对本地化文件至关重要
- 学会查看`error.log`进行错误排查

---

## 常见问题

**Q：为什么我创建的Mod在启动器中不显示？**

A：检查以下几点：
1. Mod文件夹是否在正确的位置
2. `.metadata`文件夹是否创建正确（注意前面的点）
3. `metadata.json`文件名是否拼写正确
4. JSON格式是否正确（可以用在线JSON验证器检查）

**Q：如何知道国家的代码（如CHI代表大清）？**

A：可以在游戏文件中找到：

```pdx
SteamLibrary\steamapps\common\Victoria 3\game\common\countries\

```
每个.txt文件的文件名就是国家代码。

**Q：我可以给其他国家也添加资金吗？**

A：可以！在`my_mod_countries.txt`中添加：

```pdx
CHI = { add_treasury = 1000 }
GBR = { add_treasury = 1000 }  # 英国
FRA = { add_treasury = 1000 }  # 法国

```

**Q：如何修改其他开局设置？**

A：可以修改科技、法律、人口等。例如：

```pdx
CHI = {
    add_treasury = 1000
    set_technology = { railroad = 1 }  # 解锁铁路科技
}

```

---

## 练习建议

1. **修改数值**：尝试修改`add_treasury`的数值，观察效果
2. **添加更多国家**：给英国、法国也添加开局资金
3. **探索游戏文件**：打开游戏本体的`common\history\countries\`文件夹，看看官方是如何设置开局的
4. **备份重要**：在继续学习前，确保你能重复创建这个简单的Mod

---

> 📖 **下一章预告**：在下一章，我们将详细学习Mod文件结构，了解每个文件夹的作用，掌握文件覆盖和加载顺序的奥秘。

---

## 参考

- [Victoria 3 Wiki - Mod Structure](https://vic3.paradoxwikis.com/Mod_structure)
- [Victoria 3 Wiki - Console Commands](https://vic3.paradoxwikis.com/Console_commands)
