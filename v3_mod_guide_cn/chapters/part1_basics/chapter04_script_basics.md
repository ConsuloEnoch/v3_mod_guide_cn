# 第4章：脚本语言基础

> 本章为零基础读者介绍维多利亚3的脚本语言基础。你将学习代码的基本结构、语法规则和常见错误，为后续学习核心系统打下坚实基础。

## 本章目标

完成本章学习后，你将能够：
- 理解维多利亚3脚本语言的基本语法
- 掌握缩进、括号、等号等核心概念
- 学会编写和阅读简单的脚本代码
- 识别和修复常见语法错误

---

## 4.1 代码是什么？

### 4.1.1 生活化比喻

想象你在给一位外国朋友写信，告诉他如何制作一杯奶茶：

```pdx
1. 准备材料：茶叶、牛奶、糖
2. 烧开水
3. 放入茶叶泡3分钟
4. 加入牛奶
5. 根据口味加糖

```

**代码**就是给电脑的"说明书"。只不过电脑非常"死板"，必须严格按照规定的格式书写，它才能理解。

### 4.1.2 维多利亚3脚本语言的特点

维多利亚3使用的是**声明式脚本语言**，这意味着：

✅ **优点**：
- 语法相对简单，不需要编程基础
- 直接描述"要什么"，而非"怎么做"
- 修改即时生效，无需编译

📋 **基本规则**：
1. 使用**缩进**表示层级关系
2. 使用**花括号** `{}` 包含代码块
3. 使用**等号** `=` 连接名称和值
4. 使用**井号** `#` 添加注释

---

## 4.2 基本语法元素

### 4.2.1 缩进 - 代码的层级

**缩进**是维多利亚3脚本最重要的特征。它表示代码之间的包含关系。

#### 正确示例

```pdx
# 国家定义示例
country = {
    name = "大清"
    capital = "北京"

    government = {
        type = "君主制"
        ruler = "道光帝"
    }
}

```

**解释**：
- `country` 是顶层
- `name`、`capital`、`government` 都属于 `country`
- `type` 和 `ruler` 属于 `government`

#### 缩进规则

| 规则             | 说明             | 示例                        |
| ---------------- | ---------------- | --------------------------- |
| 使用Tab或空格    | 保持一致即可     | 推荐每级4个空格             |
| 相同层级相同缩进 | 同级内容对齐     | `name` 和 `capital` 对齐    |
| 子内容更缩进     | 下级内容缩进一级 | `type` 比 `government` 缩进 |

> ⚠️ **注意**：混合使用Tab和空格可能导致错误！建议统一使用4个空格。

### 4.2.2 花括号 `{}` - 代码块

**花括号**用于定义代码块的范围，表示"这里面是一组相关内容"。

#### 基本结构

```pdx
name = {
    # 花括号内的内容
    key1 = value1
    key2 = value2
}

```

#### 多层嵌套

```pdx
# 多层嵌套示例
country = {
    name = "大清"

    states = {
        state = {
            name = "直隶"
            population = 1000000
        }
        state = {
            name = "江苏"
            population = 800000
        }
    }
}

```

**可视化层级**：

```pdx
country ──┬── name = "大清"
          │
          └── states ──┬── state ──┬── name = "直隶"
                       │           └── population = 1000000
                       │
                       └── state ──┬── name = "江苏"
                                   └── population = 800000

```

#### 常见错误

❌ 错误：括号不匹配

```pdx
country = {
    name = "大清"
    # 缺少右括号！

```

❌ 错误：多余括号

```pdx
country = {
    name = "大清"
}
}  # 多余的右括号！

```

✅ 正确：括号成对出现

```pdx
country = {
    name = "大清"
}

```

### 4.2.3 等号 `=` - 赋值与连接

**等号**在维多利亚3脚本中有多种用途：

#### 1. 赋值（最常见）

```pdx
name = "大清"           # 将"大清"赋值给name
treasury = 1000         # 将1000赋值给treasury
is_at_war = yes         # 将yes赋值给is_at_war

```

#### 2. 定义代码块

```pdx
government = {          # government是一个代码块
    type = "君主制"
}

```

#### 3. 比较运算（在触发器中）

```pdx
trigger = {
    treasury >= 1000    # 比较：国库是否大于等于1000
    is_at_war = no      # 比较：是否不在战争中
}

```

> ❓ **解释**：等号在不同上下文中有不同含义。在赋值时是"设置为"，在触发器中是"等于"。

### 4.2.4 注释 `#` - 给人类看的说明

**注释**是代码中不会被电脑执行的部分，用于给开发者（包括你自己）看的说明。

#### 单行注释

```pdx
# 这是注释，解释下面的代码
add_treasury = 1000  # 这也是注释，解释这行代码

```

#### 注释的用途

```pdx
# ============================================================================
# 文件：qing_reform.txt
# 描述：清朝洋务运动事件
# 作者：张三
# 日期：2026-03-29
# ============================================================================

namespace = qing_reform    # 命名空间，用于组织事件

# 洋务运动开始事件
qing_reform.1 = {          # 事件ID，使用namespace.编号格式
    type = country_event   # 事件类型：国家事件

    title = qing_reform.1.t    # 标题的本地化key
    desc = qing_reform.1.d     # 描述的本地化key

    # 触发条件：只能由大清触发
    trigger = {
        this = c:CHI       # 当前国家必须是大清
    }

    # 立即效果
    immediate = {
        add_treasury = -500    # 花费500国库资金
        # TODO: 添加更多效果
    }
}

```

> 💡 **提示**：养成写注释的好习惯！三个月后回头看自己的代码，你会感谢现在的自己。

---

## 4.3 数据类型

维多利亚3脚本中常用的数据类型：

### 4.3.1 字符串（String）

**字符串**是文本数据，用双引号包裹。

```pdx
name = "大清"
description = "这是一个很长的描述文本..."

```

> ⚠️ **注意**：字符串区分大小写。`"China"` 和 `"china"` 是不同的。

### 4.3.2 数字（Number）

**数字**可以是整数或小数。

```pdx
treasury = 1000         # 整数
population = 1500000    # 大整数
growth_rate = 0.05      # 小数（5%）

```

### 4.3.3 布尔值（Boolean）

**布尔值**表示"是/否"、"真/假"。

```pdx
is_at_war = yes         # 是
is_subject = no         # 否
is_monarchy = yes       # 是

```

可用的布尔值：
- `yes` / `true` - 真/是
- `no` / `false` - 假/否

### 4.3.4 标识符（Identifier）

**标识符**是游戏中预定义的名称，通常不带引号。

```pdx
country = CHI           # 国家标识符：大清
state = STATE_BEIJING   # 州标识符：北京
building = building_iron_mine  # 建筑标识符：铁矿
culture = han           # 文化标识符：汉族

```

> 📖 **参考**：所有标识符列表可在游戏文件的`common/`文件夹中找到。

---

## 4.4 代码结构实战

让我们通过一个完整的事件示例，理解代码结构：

```pdx
# ============================================================================
# 事件：洋务运动开始
# 描述：清朝开始进行现代化改革
# ============================================================================

namespace = qing_reform

qing_reform.1 = {
    # ===== 事件基本信息 =====
    type = country_event
    placement = root

    title = qing_reform.1.t
    desc = qing_reform.1.d

    event_image = {
        video = "gfx/event_pictures/event_industrialization.bk2"
    }

    icon = "gfx/interface/icons/event_icons/event_industry.dds"
    duration = 3

    # ===== 触发条件 =====
    trigger = {
        exists = c:CHI
        this = c:CHI
        year >= 1860
        NOT = { has_variable = qing_reform_started }
    }

    # ===== 立即效果 =====
    immediate = {
        set_variable = qing_reform_started

        add_treasury = -500

        add_modifier = {
            name = qing_reform_modifier
            months = 60
        }
    }

    # ===== 选项 =====
    option = {
        name = qing_reform.1.a
        default_option = yes

        add_technology = steam_engine

        custom_tooltip = qing_reform.1.a.tt
    }

    option = {
        name = qing_reform.1.b

        trigger = {
            treasury >= 1000
        }

        add_treasury = -1000
        add_technology = railroad
        add_technology = steam_engine
    }
}

```

**结构分析**：

```pdx
qing_reform.1 (事件ID)
├── 基本信息 (type, title, desc...)
├── 触发条件 (trigger)
├── 立即效果 (immediate)
└── 选项 (option)
    ├── 选项A
    └── 选项B (带条件)

```

---

## 4.5 常见错误排查

### 4.5.1 语法错误一览

| 错误类型       | 错误示例                 | 正确写法                   |
| -------------- | ------------------------ | -------------------------- |
| **括号不匹配** | `country = { name = "A"` | `country = { name = "A" }` |
| **引号不匹配** | `name = "大清`           | `name = "大清"`            |
| **缺少等号**   | `name "大清"`            | `name = "大清"`            |
| **多余逗号**   | `treasury = 1000,`       | `treasury = 1000`          |
| **中文引号**   | `name = "大清"`          | `name = "大清"`            |
| **缩进错误**   | 混合Tab和空格            | 统一使用4个空格            |

### 4.5.2 如何查找错误

#### 1. 查看错误日志

```pdx
Documents\Paradox Interactive\Victoria 3\logs\error.log

```

常见错误信息：

```pdx
[error] Missing closing bracket in file: my_mod.txt, line 15
[error] Unknown identifier: 'CHI' in file: my_mod.txt, line 23
[error] Unexpected token: '=' in file: my_mod.txt, line 30

```

#### 2. 使用在线JSON验证器

虽然维多利亚3脚本不是JSON，但结构类似。可以将代码粘贴到在线JSON验证器检查括号匹配。

#### 3. 逐段测试

如果Mod不生效，尝试：
1. 注释掉一半代码
2. 测试是否有效
3. 逐步取消注释，定位问题

```pdx
# 注释掉不测试的部分
/*
qing_reform.2 = {
    ...
}
*/

```

> ⚠️ **注意**：维多利亚3不支持`/* */`多行注释，只能用`#`逐行注释。

### 4.5.3 调试技巧

#### 添加测试事件

```pdx
# 创建一个测试事件，验证Mod是否正确加载
test_event.1 = {
    type = country_event
    hidden = yes

    immediate = {
        # 如果看到这行日志，说明Mod已加载
        log = "My mod is loaded!"
    }
}

```

#### 使用控制台

在游戏中按`` ` ``打开控制台：

```pdx
event test_event.1    # 触发测试事件
reload my_mod         # 重新加载Mod
debug_mode            # 显示调试信息

```

---

## 4.6 命名规范

### 4.6.1 文件命名

```pdx
✅ 推荐：qing_reform_events.txt
✅ 推荐：my_mod_buildings.txt
❌ 不推荐：Qing Reform Events.txt  (有空格和大写)
❌ 不推荐：events.txt              (太通用，易冲突)

```

### 4.6.2 ID命名

```pdx
✅ 推荐：qing_reform.1
✅ 推荐：my_mod_industrial_event
❌ 不推荐：event1                  (无前缀，易冲突)
❌ 不推荐：QingReformEvent         (使用驼峰命名)

```

### 4.6.3 本地化Key命名

```yaml
✅ 推荐：qing_reform.1.t
✅ 推荐：qing_reform.1.d
✅ 推荐：qing_reform.1.a
❌ 不推荐：event_title_1           (无前缀)

```

---

## 4.7 实战练习

### 练习1：识别错误

找出以下代码中的错误：

```pdx
my_event.1 = {
    type = country_event
    title = my_event.1.t
    desc = my_event.1.d

    trigger = {
        this = c:CHI
        treasury >= 1000
    }

    immediate = {
        add_treasury = -500
        set_variable = my_event_fired
    }

    option = {
        name = my_event.1.a
        add_prestige = 100
    }
# 缺少右括号！

```

**答案**：最后一行缺少 `}` 来关闭 `my_event.1` 代码块。

### 练习2：补全代码

补全以下事件代码：

```pdx
my_event.2 = {
    type = country_event
    title = my_event.2.t
    desc = my_event.2.d

    trigger = {
        # 条件：国库大于500且不在战争中
        ________________
        ________________
    }

    immediate = {
        # 添加500国库
        ________________
    }

    option = {
        name = my_event.2.a
        default_option = yes
        # 添加100威望
        ________________
    }
}

```

**参考答案**：

```pdx
trigger = {
    treasury > 500
    is_at_war = no
}

immediate = {
    add_treasury = 500
}

option = {
    name = my_event.2.a
    default_option = yes
    add_prestige = 100
}

```

### 练习3：创建你的第一个事件

创建一个简单的事件，要求：
1. 事件ID：`my_first_event.1`
2. 触发条件：任意国家都可以触发
3. 立即效果：添加100国库
4. 一个选项，添加50威望

**参考答案**：

```pdx
namespace = my_first_event

my_first_event.1 = {
    type = country_event
    title = my_first_event.1.t
    desc = my_first_event.1.d

    immediate = {
        add_treasury = 100
    }

    option = {
        name = my_first_event.1.a
        default_option = yes
        add_prestige = 50
    }
}

```

对应的本地化文件：

```yaml
l_simp_chinese:
 my_first_event.1.t:0 "我的第一个事件"
 my_first_event.1.d:0 "这是一个测试事件。"
 my_first_event.1.a:0 "太好了！"

```

---

## 本章小结

- **代码**是给电脑的指令，必须严格按照语法书写
- **缩进**表示代码层级，统一使用4个空格
- **花括号** `{}` 定义代码块范围，必须成对出现
- **等号** `=` 用于赋值和比较（上下文决定含义）
- **井号** `#` 用于添加注释，不会被游戏执行
- 常见数据类型：字符串、数字、布尔值、标识符
- 使用`error.log`和控制台命令进行调试

---

## 常见问题

**Q：我可以用中文写代码吗？**

A：代码关键字（如`type`、`trigger`）必须用英文，但字符串值可以用中文。本地化文件应该使用中文。

**Q：代码对大小写敏感吗？**

A：是的！`Type` 和 `type` 是不同的。建议使用全部小写。

**Q：一行可以写多个语句吗？**

A：不推荐。每个语句单独一行，便于阅读和调试。

**Q：如何快速检查括号是否匹配？**

A：使用VS Code等现代编辑器，它们会自动高亮匹配的括号。

**Q：脚本和编程语言有什么区别？**

A：脚本语言不需要编译，直接运行；编程语言需要编译成机器码。维多利亚3脚本是声明式的，你描述"要什么"，游戏引擎决定"怎么做"。

---

## 练习建议

1. **阅读官方代码**：打开游戏本体的`events/`文件夹，阅读官方事件代码，尝试理解其结构。

2. **模仿练习**：选择一个简单的事件，复制其结构，修改ID和内容，创建你自己的版本。

3. **错误排查**：故意制造一些语法错误（如删除括号），观察游戏报错，学会解读错误信息。

4. **建立代码库**：收集常用的代码片段，建立自己的"代码片段库"，方便日后使用。

---

> 📖 **下一章预告**：在下一章，我们将学习**作用域系统（Scope）**——这是维多利亚3 Mod开发的核心概念，也是理解游戏对象关系的关键。

---

## 参考

- [Victoria 3 Wiki - Event modding](https://vic3.paradoxwikis.com/Event_modding)
- [Victoria 3 Wiki - Trigger](https://vic3.paradoxwikis.com/Trigger)
- [Victoria 3 Wiki - Scope](https://vic3.paradoxwikis.com/Scope)
