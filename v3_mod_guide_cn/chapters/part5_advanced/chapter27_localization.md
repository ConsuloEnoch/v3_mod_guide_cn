# 第二十七章：本地化系统

## 本章目标

学习本章后，你将能够：
- 理解本地化文件格式
- 正确设置UTF-8 BOM编码
- 为Mod添加多语言支持
- 使用变量插入动态文本
- 掌握本地化的最佳实践

---

## 概念讲解：本地化是什么？

### 比喻：翻译官的工作

想象你是一位国际会议的翻译官：
- **代码键** = 发言人的母语（如"hello_world"）
- **本地化文件** = 翻译字典
- **游戏界面** = 听众听到的翻译

没有翻译官（本地化），听众（玩家）就听不懂发言（代码）。

### 为什么需要本地化？

1. **多语言支持**：让不同语言的玩家都能游玩
2. **内容显示**：将代码转换为可读文本
3. **动态内容**：根据游戏状态显示不同文本
4. **维护便利**：集中管理所有文本，便于修改

---

## 27.1 本地化基础

### 27.1.1 文件位置

本地化文件存储在`localization/`文件夹：

```pdx
my_mod/
├── localization/
│   ├── english/              # 英语
│   │   ├── my_mod_l_english.yml
│   │   └── content_l_english.yml
│   ├── chinese/              # 简体中文
│   │   ├── my_mod_l_chinese.yml
│   │   └── content_l_chinese.yml
│   └── spanish/              # 西班牙语
│       └── my_mod_l_spanish.yml

```

### 27.1.2 文件命名规范

**标准格式**：`[名称]_l_[语言代码].yml`

**常用语言代码**：

| 语言     | 代码     | 文件夹名 |
| -------- | -------- | -------- |
| 英语     | english  | english  |
| 简体中文 | chinese  | chinese  |
| 繁体中文 | tchinese | tchinese |
| 日语     | japanese | japanese |
| 德语     | german   | german   |
| 法语     | french   | french   |
| 西班牙语 | spanish  | spanish  |
| 俄语     | russian  | russian  |
| 韩语     | korean   | korean   |

### 27.1.3 文件结构

```yaml
l_english:
  KEY_NAME: "显示的文本"
  ANOTHER_KEY: "另一个文本"
  KEY_WITH_FORMAT: "数值: $VALUE$"

```

**关键要点**：
- 以语言代码开头（如`l_english:`）
- 使用YAML格式
- 键名使用大写字母和下划线
- 文本用双引号包裹
- 缩进使用两个空格

---

## 27.2 编码要求

### 27.2.1 什么是UTF-8 BOM？

⚠️ **这是最重要的技术细节！**

UTF-8 BOM（Byte Order Mark）是文件开头的特殊标记，告诉游戏"这是一个UTF-8编码的文件"。

**错误症状**：
- 中文显示为方框或乱码
- 特殊字符无法显示
- 文件被游戏忽略

### 27.2.2 如何保存为UTF-8 BOM

**VS Code**：
1. 点击右下角编码显示（如"UTF-8"）
2. 选择"通过编码保存"
3. 选择"UTF-8 with BOM"

**Notepad++**：
1. 编码菜单
2. 选择"转为UTF-8-BOM编码"
3. 保存文件

**Sublime Text**：
1. File → Save with Encoding
2. UTF-8 with BOM

**Windows记事本**：
1. 另存为
2. 编码选择"UTF-8"
3. ⚠️ 但记事本的UTF-8不包含BOM，不推荐使用！

### 27.2.3 验证编码

**使用Notepad++**：
- 右下角会显示当前编码
- 应为"UTF-8-BOM"

**使用VS Code**：
- 右下角显示"UTF-8 with BOM"

**使用十六进制编辑器**：
- 文件开头应该有`EF BB BF`三个字节

---

## 27.3 基本本地化

### 27.3.1 简单文本

```yaml
l_chinese:
  # 事件标题
  jiangnan_revolution_title: "江南革命"

  # 事件描述
  jiangnan_revolution_desc: "江南地区的民众对清政府的统治日益不满，一场革命正在酝酿。"

  # 选项
  jiangnan_revolution_option_a: "镇压叛乱"
  jiangnan_revolution_option_b: "谈判解决"

```

### 27.3.2 在代码中使用

```pdx
# 事件定义
jiangnan_revolution_event = {
    type = country_event

    title = jiangnan_revolution_title      # 引用本地化键
    desc = jiangnan_revolution_desc

    option = {
        name = jiangnan_revolution_option_a
        # ...
    }

    option = {
        name = jiangnan_revolution_option_b
        # ...
    }
}

```

### 27.3.3 命名规范

**推荐格式**：`[命名空间]_[类型]_[名称]`

| 类型   | 示例               | 说明       |
| ------ | ------------------ | ---------- |
| 事件   | `myevent.1.t`      | 事件标题   |
| 事件   | `myevent.1.d`      | 事件描述   |
| 事件   | `myevent.1.a`      | 事件选项A  |
| 决策   | `my_decision`      | 决策名称   |
| 日志   | `my_journal_title` | 日志标题   |
| 修正器 | `my_modifier`      | 修正器名称 |

---

## 27.4 变量插入

### 27.4.1 什么是变量插入？

允许在文本中动态显示游戏数值。

```yaml
l_chinese:
  # $COUNTRY$ 将被替换为国家名称
  war_declared: "$COUNTRY$向我们宣战了！"

  # $VALUE$ 将被替换为数值
  gold_received: "我们收到了$VALUE$£gold£金币"

```

### 27.4.2 脚本中的变量传递

```pdx
event = {
    type = country_event

    title = war_declared
    desc = gold_received

    # 设置变量值
    immediate = {
        set_local_variable = {
            name = country_name
            value = ROOT.GetName
        }
        set_local_variable = {
            name = gold_amount
            value = 1000
        }
    }
}

```

### 27.4.3 常用变量类型

**国家相关**：

```yaml
$COUNTRY$          # 国家名称
$RULER$            # 统治者
$CAPITAL$          # 首都
$YEAR$             # 当前年份

```

**数值相关**：

```yaml
$VALUE$            # 一般数值
$AMOUNT$           # 数量
$PERCENT$          # 百分比

```

**自定义变量**：

```yaml
$[变量名]$         # 在脚本中定义的变量

```

### 27.4.4 图标插入

使用`£`符号插入图标：

```yaml
l_chinese:
  has_gold: "拥有£gold£1000"
  is_powerful: "是£great_power£列强"
  has_ideology: "支持£socialist£社会主义"

```

**常用图标**：

| 图标代码            | 显示     |
| ------------------- | -------- |
| £gold£            | 金币     |
| £prestige£        | 威望     |
| £bureaucracy£     | 行政力   |
| £manpower£        | 人力     |
| £diplomatic_play£ | 外交博弈 |
| £war£             | 战争     |
| £construction£    | 建造     |

---

## 27.5 多语言支持

### 27.5.1 创建多语言文件

为每种语言创建对应的yml文件：

```yaml
# localization/english/my_mod_l_english.yml
l_english:
  welcome_message: "Welcome to the mod!"
  start_game: "Start Game"

# localization/chinese/my_mod_l_chinese.yml
l_chinese:
  welcome_message: "欢迎使用本Mod！"
  start_game: "开始游戏"

# localization/german/my_mod_l_german.yml
l_german:
  welcome_message: "Willkommen bei der Mod!"
  start_game: "Spiel starten"

```

### 27.5.2 缺失本地化处理

如果某种语言缺少某个键，游戏会：
1. 尝试使用英语版本
2. 如果英语也没有，显示键名本身

**最佳实践**：
- 始终先完成英语版本
- 其他语言可以逐步添加
- 使用相同的键名结构

### 27.5.3 翻译工作流

```pdx
1. 提取文本
   ↓ 收集所有需要翻译的键
2. 创建英语母版
   ↓ 确保所有键都有英语文本
3. 翻译到其他语言
   ↓ 保持相同的文件结构
4. 测试验证
   ↓ 每种语言都进行游戏测试
5. 维护更新
   ↓ 新增内容时同步更新所有语言

```

---

## 27.6 高级本地化技巧

### 27.6.1 条件文本

使用脚本值显示条件文本：

```pdx
# 脚本值定义
is_great_power_text = {
    if = {
        limit = { is_great_power = yes }
        value = "是列强"
    }
    else = {
        value = "不是列强"
    }
}

```

```yaml
l_chinese:
  power_status: "我国[is_great_power_text]"

```

### 27.6.2 复数形式

虽然维多利亚3不支持标准的复数规则，但可以通过条件模拟：

```pdx
# 自定义本地化
custom_loc_population = {
    type = country

    text = {
        localization_key = one_million_pop
        trigger = {
            total_population < 1000000
        }
    }

    text = {
        localization_key = many_millions_pop
        trigger = {
            total_population >= 1000000
        }
    }
}

```

```yaml
l_chinese:
  one_million_pop: "不到一百万人"
  many_millions_pop: "超过一百万人"

```

### 27.6.3 颜色文本

使用颜色代码给文本上色：

```yaml
l_chinese:
  good_news: "#P 好消息#!"        # 正面（绿色）
  bad_news: "#N 坏消息#!"         # 负面（红色）
  warning: "#Y 警告#!"            # 警告（黄色）
  info: "#L 信息#!"               # 信息（蓝色）

```

**颜色代码**：

| 代码 | 颜色 | 用途      |
| ---- | ---- | --------- |
| #P   | 绿色 | 正面      |
| #N   | 红色 | 负面      |
| #Y   | 黄色 | 警告/注意 |
| #L   | 蓝色 | 信息/提示 |
| #V   | 紫色 | 特殊      |

---

## 27.7🎯 **实战**：江南Mod完整本地化

### 27.7.1 文件结构

```pdx
localization/
├── english/
│   ├── jiangnan_events_l_english.yml
│   ├── jiangnan_decisions_l_english.yml
│   ├── jiangnan_countries_l_english.yml
│   └── jiangnan_modifiers_l_english.yml
└── chinese/
    ├── jiangnan_events_l_chinese.yml
    ├── jiangnan_decisions_l_chinese.yml
    ├── jiangnan_countries_l_chinese.yml
    └── jiangnan_modifiers_l_chinese.yml

```

### 27.7.2 事件本地化

```yaml
# localization/chinese/jiangnan_events_l_chinese.yml
# 编码：UTF-8 with BOM

l_chinese:
  # 江南起义事件
  jiangnan_revolution.1.t: "江南起义"
  jiangnan_revolution.1.d: "长期以来，江南地区的士绅和商人对清政府的腐败无能深感不满。今日，以南京为中心的抗议活动演变为武装起义，他们宣布建立江南共和国，要求脱离清朝统治。"
  jiangnan_revolution.1.a: "镇压叛乱！"
  jiangnan_revolution.1.b: "承认其自治权"
  jiangnan_revolution.1.c: "放任不管"

  # 洋务运动事件
  self_strengthening.1.t: "洋务运动的兴起"
  self_strengthening.1.d: "面对西方列强的坚船利炮，一些有识之士提出了"师夷长技以制夷"的主张。曾国藩和李鸿章等人开始筹划建立近代工业，以增强国力。"
  self_strengthening.1.a: "全力支持洋务运动"
  self_strengthening.1.b: "有限度地支持"
  self_strengthening.1.c: "这是离经叛道"

  # 江南制造局完工
  jiangnan_arsenal.1.t: "江南制造局竣工"
  jiangnan_arsenal.1.d: "经过多年的建设，江南制造局终于竣工。这座现代化的兵工厂将大大提升我们的军事工业能力，为国防事业做出贡献。"
  jiangnan_arsenal.1.a: "这是伟大的成就"

```

### 27.7.3 决策本地化

```yaml
# localization/chinese/jiangnan_decisions_l_chinese.yml
# 编码：UTF-8 with BOM

l_chinese:
  # 决策名称
  establish_jiangnan_republic: "建立江南共和国"
  establish_jiangnan_republic_desc: "江南地区资源丰富、人口众多，完全有能力建立一个独立的国家。我们可以借此机会脱离腐朽的清朝统治。"

  promote_self_strengthening: "推行洋务运动"
  promote_self_strengthening_desc: "通过引进西方技术和建立近代工业，我们可以快速缩小与列强的差距。这需要大量的资金投入，但回报将是巨大的。"

  build_jiangnan_arsenal: "建设江南制造局"
  build_jiangnan_arsenal_desc: "在上海建立一座现代化的兵工厂，生产枪支、弹药和军舰。这将大大增强我们的军事力量。"

  # 决策提示
  decision_requirement_not_met: "#R 不满足决策条件#!"
  decision_cost_treasury: "花费£gold£$AMOUNT$"
  decision_cost_bureaucracy: "需要£bureaucracy£$AMOUNT$"

```

### 27.7.4 国家本地化

```yaml
# localization/chinese/jiangnan_countries_l_chinese.yml
# 编码：UTF-8 with BOM

l_chinese:
  # 国家名称
  JNG: "江南共和国"
  JNG_ADJ: "江南"

  # 国家类型变体
  JNG_republic: "江南共和国"
  JNG_republic_adj: "江南"
  JNG_monarchy: "江南王国"
  JNG_monarchy_adj: "江南"
  JNG_socialist: "江南人民共和国"
  JNG_socialist_adj: "江南"
  JNG_fascist: "江南帝国"
  JNG_fascist_adj: "江南"

  # 领导人
  JNG_ruler_1: "李鸿章"
  JNG_ruler_2: "曾国藩"
  JNG_ruler_3: "张之洞"

  # 地区
  state_jiangnan: "江南"
  state_jiangsu: "江苏"
  state_zhejiang: "浙江"

```

### 27.7.5 修正器本地化

```yaml
# localization/chinese/jiangnan_modifiers_l_chinese.yml
# 编码：UTF-8 with BOM

l_chinese:
  # 洋务运动修正器
  modifier_self_strengthening: "洋务运动"
  modifier_self_strengthening_desc: "我们正在积极推行现代化改革，这带来了工业化进程的加速。"

  modifier_western_influence: "西方影响"
  modifier_western_influence_desc: "西方的技术和思想正在改变我们的社会。"

  modifier_jiangnan_arsenal: "江南制造局"
  modifier_jiangnan_arsenal_desc: "拥有现代化的兵工厂，我们的军工生产能力大大提升。"

  modifier_taiping_legacy: "太平天国遗产"
  modifier_taiping_legacy_desc: "这片地区经历过太平天国运动的洗礼，社会秩序仍需恢复。"

  # 动态修正器
  modifier_industrializing: "工业化进程中"
| modifier_industrializing_desc: "工业化率为$PERCENTAGE | 0%$，正在快速发展。" |
| ----------------------------------------------------- | -------------------- |

  # 自定义描述
  jiangnan_modifiers_custom_desc: "#L 江南地区特色修正#!"

```

### 27.7.6 日志条目本地化

```yaml
# localization/chinese/jiangnan_journal_l_chinese.yml
# 编码：UTF-8 with BOM

l_chinese:
  # 洋务运动日志
  journal_self_strengthening: "洋务运动"
  journal_self_strengthening_desc: "一场旨在通过学习西方技术来增强国力的运动正在进行中。我们需要在工业化和军事现代化方面取得实质性进展。"
  journal_self_strengthening_complete: "洋务运动取得巨大成功！我们的国力显著增强。"
  journal_self_strengthening_fail: "洋务运动失败了，保守派的阻力太大。"

  # 江南统一日志
  journal_jiangnan_unification: "统一江南"
  journal_jiangnan_unification_desc: "江南地区分裂已久，现在是我们统一这片土地的时候了。"
  journal_jiangnan_unification_complete: "江南统一完成！"

```

---

## 常见问题

**Q1：中文显示为方框或乱码？**

解决步骤：
1. 确认文件保存为UTF-8 with BOM
2. 检查文件开头是否有BOM标记（EF BB BF）
3. 确保使用双引号包裹文本
4. 避免使用特殊控制字符

**Q2：本地化键在游戏中不显示？**

检查：
1. 文件路径是否正确
2. 文件名格式是否正确（`_l_语言.yml`）
3. 文件头是否为`l_语言:`
4. 缩进是否正确（2个空格）

**Q3：如何引用其他Mod的本地化？**

不能直接引用其他Mod的本地化。如果需要：
1. 在自己的Mod中重新定义
2. 或使用相同的键名覆盖

**Q4：可以实时修改本地化吗？**

可以！修改yml文件后，在控制台输入：`reload localization`

**Q5：变量插入不工作？**

检查：
1. 变量名是否正确（使用`$变量名$`格式）
2. 变量是否在脚本中正确定义
3. 变量类型是否匹配

---

## 本章小结

本章学习了本地化的核心知识：

1. **文件格式**：YAML格式，以语言代码开头
2. **编码要求**：必须使用UTF-8 with BOM
3. **键名规范**：大写字母和下划线
4. **变量插入**：使用`$变量名$`格式
5. **多语言**：为每种语言创建对应文件
6. **高级技巧**：条件文本、颜色代码、图标

💡 **提示**：本地化是Mod的门面，精心编写的文本能大大提升游戏体验。务必使用正确的编码！

---

## 练习建议

1. **练习1**：为简单事件创建中英文本地化
2. **练习2**：测试不同编码格式的显示效果
3. **练习3**：使用变量插入显示动态数值
4. **练习4**：创建带图标的本地化文本
5. **练习5**：为一个Mod创建完整的多语言支持

📖 **参考**：完整的图标列表和颜色代码请参考游戏Wiki。
