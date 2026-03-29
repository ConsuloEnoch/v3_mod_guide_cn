# 第11章：事件系统（Event）——完整事件链制作

> 事件系统是维多利亚3 Mod开发中最重要、最强大的工具。本章将带你从零开始，学习如何创建简单事件，进而制作复杂的事件链，最终掌握制作完整Mod事件系统的能力。

## 本章目标

完成本章学习后，你将能够：
- 理解事件的基本结构和各个组成部分
- 熟练使用命名空间组织事件
- 掌握事件的触发、立即效果、选项等核心机制
- 设计并实现复杂的事件链
- 制作完整的Mod事件系统

---

## 11.1 什么是事件？

### 11.1.1 生活化比喻

想象你正在阅读一本互动小说：

**场景1：简单事件**
> 你走在街上，发现地上有100块钱。
>
> A. 捡起来（获得100元）
> B. 交给警察（获得好人卡）

**场景2：连锁事件**
> 第1章：你救了一只受伤的小鸟...
> 第2章（1天后）：小鸟康复了，它的主人来感谢你...
> 第3章（1周后）：主人成了你的贵人，给你介绍工作...

**场景3：条件事件**
> 只有在你有钱时才能选择"请客吃饭"
> 只有在你有武器时才能选择"战斗"

维多利亚3中的**事件**就是这样的互动系统，让玩家做出选择，推动故事发展。

### 11.1.2 技术定义

**事件**是游戏中的交互式弹窗，包含：
- **标题**：事件的名称
- **描述**：事件的详细说明
- **图片**：视觉展示
- **选项**：玩家可以选择的行动
- **效果**：选择后发生的游戏变化

```pdx
┌─────────────────────────────────┐
│  [图片]                         │
│  标题：洋务运动开始              │
│                                 │
│  描述：清朝决定开始现代化改革...│
│                                 │
│  A. 重点发展军事                 │
│  B. 重点发展经济                 │
│  C. 平衡发展                     │
└─────────────────────────────────┘

```

---

## 11.2 事件文件基础

### 11.2.1 文件位置

事件文件存放在：

```pdx
my_mod/events/                    # 主文件夹
my_mod/events/qing_events.txt     # 大清事件
my_mod/events/war_events.txt      # 战争事件

```

> 💡 **提示**：`events/`文件夹可以创建任意子文件夹来组织文件！

### 11.2.2 文件编码

**必须使用 UTF-8 BOM 编码！**

在VS Code中：
1. 点击右下角编码显示
2. 选择 "Save with Encoding"
3. 选择 "UTF-8 with BOM"

### 11.2.3 命名空间（Namespace）

**命名空间**是事件的组织标识，每个事件文件都必须以命名空间开头：

```pdx
# 在文件最开头声明命名空间
namespace = qing_reform

# 之后的事件ID格式：命名空间.编号
qing_reform.1 = {
    # 事件内容
}

qing_reform.2 = {
    # 另一个事件
}

```

**命名规范**：
- 使用小写字母和下划线
- 具有描述性
- 避免与游戏本体或其他Mod冲突

```pdx
✅ 推荐：qing_reform、my_mod_events
❌ 不推荐：event1、test

```

---

## 11.3 事件的基本结构

### 11.3.1 最小事件示例

最简单的完整事件：

```pdx
namespace = my_mod

my_mod.1 = {
    type = country_event          # 事件类型

    title = my_mod.1.t            # 标题本地化key
    desc = my_mod.1.d             # 描述本地化key

    option = {                    # 选项
        name = my_mod.1.a         # 选项文本key
        default_option = yes      # 默认选项
    }
}

```

### 11.3.2 完整事件结构

```pdx
namespace = example

example.1 = {
    # ========== 基本信息 ==========
    type = country_event          # 事件类型
    placement = root              # 地图上的位置

    # ========== 显示内容 ==========
    title = example.1.t           # 标题
    desc = example.1.d            # 描述
    flavor = example.1.f          # 风味文本（可选）

    event_image = {               # 事件图片
        video = "gfx/event_pictures/industrialization.bk2"
    }

    icon = "gfx/interface/icons/event_icons/event_industry.dds"

    on_opened_soundeffect = "event:/SFX/UI/Alerts/event_appear"

    duration = 3                  # 持续月数（0=无限）

    # ========== 触发条件 ==========
    trigger = {
        # 触发条件
    }

    # ========== 取消条件 ==========
    cancellation_trigger = {
        # 满足则取消事件
    }

    # ========== 冷却时间 ==========
    cooldown = {
        months = 12
    }

    # ========== 立即效果 ==========
    immediate = {
        # 事件触发时立即执行
    }

    # ========== 选项 ==========
    option = {
        name = example.1.a
        default_option = yes

        trigger = {               # 选项显示条件
            # 条件
        }

        # 选项效果
    }

    option = {
        name = example.1.b

        # 另一个选项
    }

    # ========== 后续效果 ==========
    after = {
        # 选项选择后执行
    }
}

```

### 11.3.3 事件类型

| 类型              | 说明                 | 作用域    |
| ----------------- | -------------------- | --------- |
| `country_event`   | 国家事件（最常用）   | country   |
| `state_event`     | 州事件               | state     |
| `character_event` | 角色事件             | character |
| `news_event`      | 新闻事件（全球可见） | none      |
| `minor_event`     | 次要事件（小弹窗）   | country   |

```pdx
# 国家事件示例
country_event = {
    type = country_event
    # root = 触发事件的国家
}

# 州事件示例
state_event = {
    type = state_event
    # root = 触发事件的州
}

# 角色事件示例
character_event = {
    type = character_event
    # root = 触发事件的角色
}

```

---

## 11.4 事件的各个组成部分

### 11.4.1 标题、描述和风味文本

```pdx
title = qing_reform.1.t           # 标题
desc = qing_reform.1.d            # 主描述
flavor = qing_reform.1.f          # 风味文本（可选）

```

**本地化文件**：

```yaml
l_simp_chinese:
 qing_reform.1.t:0 "洋务运动开始"
 qing_reform.1.d:0 "在恭亲王等人的建议下，朝廷决定开始一项 ambitious 的现代化改革计划..."
 qing_reform.1.f:0 "\"师夷长技以制夷\" —— 魏源"

```

**动态描述**：根据条件显示不同文本

```pdx
desc = {
    first_valid = {
        triggered_desc = {
            desc = qing_reform.1.d_ruler
            trigger = {
                ruler = { has_trait = trait_enlightened }
            }
        }
        triggered_desc = {
            desc = qing_reform.1.d_conservative
            trigger = {
                ruler = { has_trait = trait_conservative }
            }
        }
        triggered_desc = {
            desc = qing_reform.1.d_default
        }
    }
}

```

### 11.4.2 事件图片和图标

**视频图片**：

```pdx
event_image = {
    video = "gfx/event_pictures/asia_meiji_restoration.bk2"
}

```

**静态图片**：

```pdx
event_image = {
    texture = "gfx/event_pictures/my_custom_event.dds"
}

```

**图标**：

```pdx
icon = "gfx/interface/icons/event_icons/event_industry.dds"

```

### 11.4.3 触发条件（Trigger）

决定事件能否触发：

```pdx
qing_reform.1 = {
    type = country_event

    trigger = {
        this = c:CHI              # 必须是大清
        year >= 1860              # 年份至少1860
        year <= 1880              # 年份最多1880
        treasury >= 500           # 国库至少500
        is_at_war = no            # 不在战争中
        NOT = { has_variable = qing_reform_started }
    }

    # ...
}

```

> 📖 **详细内容**：参见第6章《触发器》

### 11.4.4 立即效果（Immediate）

事件触发时立即执行，不等待玩家选择：

```pdx
qing_reform.1 = {
    # ...

    immediate = {
        # 设置变量，标记事件已开始
        set_variable = qing_reform_started

        # 扣除资金
        add_treasury = -500

        # 保存统治者作用域
        ruler = {
            save_scope_as = reform_ruler
        }

        # 添加修正器
        add_modifier = {
            name = qing_reform_modifier
            months = 60
        }

        # 记录日志
        log = "Qing Reform started in [GetYear]"
    }

    # ...
}

```

### 11.4.5 取消条件（Cancellation Trigger）

如果条件满足，事件会自动消失：

```pdx
qing_reform.1 = {
    # ...

    cancellation_trigger = {
        # 如果开始内战，取消改革事件
        has_civil_war = yes
    }

    # ...
}

```

### 11.4.6 冷却时间（Cooldown）

防止事件频繁触发：

```pdx
qing_reform.1 = {
    # ...

    cooldown = {
        years = 5                 # 5年内不会再次触发
    }

    # ...
}

```

---

## 11.5 选项系统

### 11.5.1 基本选项

```pdx
option = {
    name = qing_reform.1.a        # 选项文本
    default_option = yes          # 默认选项（AI会优先选择）

    # 效果
    add_prestige = 100
}

```

### 11.5.2 选项触发条件

控制选项是否显示：

```pdx
option = {
    name = qing_reform.1.b

    trigger = {
        # 只有国库大于1000时才显示
        treasury >= 1000
    }

    # 花费资金
    add_treasury = -1000
    add_technology = railroad
}

```

### 11.5.3 选项效果

```pdx
option = {
    name = qing_reform.1.c

    # 添加科技
    add_technology = steel
    add_technology = railroad

    # 在建筑
    capital = {
        add_building = building_steel_mills
    }

    # 添加修正器
    add_modifier = {
        name = rapid_industrialization
        months = 24
    }

    # 触发后续事件
    trigger_event = {
        id = qing_reform.2
        days = 180
    }
}

```

### 11.5.4 AI权重

控制AI如何选择：

```pdx
option = {
    name = qing_reform.1.a

    ai_chance = {
        base = 10                   # 基础概率10

        modifier = {
            add = 20                # 增加20
            trigger = {
                ruler = { has_trait = trait_enlightened }
            }
        }

        modifier = {
            add = -15               # 减少15
            trigger = {
                ruler = { has_trait = trait_conservative }
            }
        }
    }

    # ...
}

```

### 11.5.5 显示效果提示

```pdx
option = {
    name = qing_reform.1.a

    # 显示效果但不实际执行
    show_as_tooltip = {
        c:GBR = {
            add_opinion = {
                target = root
                value = 10
            }
        }
    }

    # 实际执行的效果
    add_prestige = 100
}

```

---

## 11.6 事件链设计

### 11.6.1 什么是事件链？

**事件链**是一系列相互关联的事件，通常有时间延迟：

```pdx
事件1 →（30天后）→ 事件2 →（60天后）→ 事件3 → 结束
  ↓
分支A → 事件4
  ↓
分支B → 事件5

```

### 11.6.2 创建简单事件链

```pdx
namespace = qing_reform

# 事件1：改革开始
qing_reform.1 = {
    type = country_event
    title = qing_reform.1.t
    desc = qing_reform.1.d

    immediate = {
        set_variable = {
            name = reform_stage
            value = 1
        }
    }

    option = {
        name = qing_reform.1.a

        # 触发下一步
        trigger_event = {
            id = qing_reform.2
            days = 30
        }
    }
}

# 事件2：改革进展
qing_reform.2 = {
    type = country_event
    title = qing_reform.2.t
    desc = qing_reform.2.d

    immediate = {
        change_variable = {
            name = reform_stage
            add = 1
        }
    }

    option = {
        name = qing_reform.2.a

        # 触发下一步
        trigger_event = {
            id = qing_reform.3
            days = 60
        }
    }
}

# 事件3：改革完成
qing_reform.3 = {
    type = country_event
    title = qing_reform.3.t
    desc = qing_reform.3.d

    immediate = {
        remove_variable = reform_stage
    }

    option = {
        name = qing_reform.3.a
        add_prestige = 500
    }
}

```

### 11.6.3 分支事件链

```pdx
# 事件1：做出选择
qing_reform.1 = {
    type = country_event
    # ...

    option = {
        name = qing_reform.1.military

        # 军事路线
        trigger_event = {
            id = qing_reform.military.1
            days = 30
        }
    }

    option = {
        name = qing_reform.1.economic

        # 经济路线
        trigger_event = {
            id = qing_reform.economic.1
            days = 30
        }
    }
}

# 军事路线事件
qing_reform.military.1 = {
    type = country_event
    # ...
}

# 经济路线事件
qing_reform.economic.1 = {
    type = country_event
    # ...
}

```

### 11.6.4 使用变量控制事件链

```pdx
# 主事件
qing_reform.1 = {
    type = country_event
    # ...

    immediate = {
        set_variable = {
            name = reform_progress
            value = 0
        }
    }

    option = {
        name = qing_reform.1.continue

        change_variable = {
            name = reform_progress
            add = 25
        }

        # 根据进度触发不同事件
        if = {
            limit = {
                var:reform_progress < 100
            }
            trigger_event = {
                id = qing_reform.1      # 继续改革
                days = 90
            }
        }
        else = {
            trigger_event = {
                id = qing_reform.complete   # 改革完成
                days = 30
            }
        }
    }
}

```

---

## 11.7🎯 **实战**：制作"太平天国起义"事件链

### 11.7.1 设计思路

**历史背景**：
- 1850-1864年，中国历史上规模最大的农民起义
- 起因：清朝腐败、外国入侵、自然灾害
- 过程：金田起义 → 定都天京 → 北伐西征 → 天京事变 → 最终失败

**Mod设计**：
- 事件1：起义爆发（1850-1853年间随机触发）
- 事件2：北伐选择（是否支持北伐）
- 事件3：天京事变（1856年，内部清洗）
- 事件4：外国干预（英法是否介入）
- 事件5：结局（成功或失败）

### 11.7.2 创建事件文件

**文件**：`my_mod/events/taiping_rebellion.txt`

```pdx
namespace = taiping_rebellion

# ========== 事件1：金田起义 ==========
taiping_rebellion.1 = {
    type = country_event

    title = taiping_rebellion.1.t
    desc = taiping_rebellion.1.d

    event_image = {
        video = "gfx/event_pictures/asia_chinese_warlords.bk2"
    }

    icon = "gfx/interface/icons/event_icons/event_skull.dds"

    # 触发条件
    trigger = {
        this = c:CHI
        year >= 1850
        year <= 1853

        # 清朝内部不稳定
        OR = {
            average_sol < 10
            has_law = law_type:law_slavery
            any_interest_group = {
                is_insurrectionary = yes
            }
        }

        # 防止重复触发
        NOT = { has_variable = taiping_started }
    }

    immediate = {
        # 标记起义已开始
        set_variable = taiping_started
        set_variable = {
            name = taiping_strength
            value = 50
        }
        set_variable = {
            name = taiping_territory
            value = 1
        }

        # 创建太平天国（通过外交博弈）
        save_scope_as = qing_empire
    }

    # 选项
    option = {
        name = taiping_rebellion.1.a
        default_option = yes

        # 立即镇压
        add_war_exhaustion = 10
        add_radicals_in_country = {
            value = 0.05
        }

        # 触发战争事件
        trigger_event = {
            id = taiping_rebellion.war.1
            days = 7
        }
    }

    option = {
        name = taiping_rebellion.1.b

        # 暂时观望
        add_prestige = -50

        change_variable = {
            name = taiping_strength
            add = 20
        }

        trigger_event = {
            id = taiping_rebellion.2
            days = 90
        }
    }

    option = {
        name = taiping_rebellion.1.c

        trigger = {
            treasury >= 1000
        }

        # 收买人心
        add_treasury = -1000
        add_loyalists_in_country = {
            value = 0.03
        }

        change_variable = {
            name = taiping_strength
            add = -15
        }

        trigger_event = {
            id = taiping_rebellion.2
            days = 180
        }
    }
}

# ========== 事件2：定都天京 ==========
taiping_rebellion.2 = {
    type = country_event

    title = taiping_rebellion.2.t
    desc = taiping_rebellion.2.d

    trigger = {
        has_variable = taiping_started
        NOT = { has_variable = taiping_capital_set }
    }

    immediate = {
        set_variable = taiping_capital_set
        change_variable = {
            name = taiping_territory
            add = 3
        }
    }

    option = {
        name = taiping_rebellion.2.a

        # 北伐
        add_war_exhaustion = 5
        change_variable = {
            name = taiping_strength
            add = 10
        }

        trigger_event = {
            id = taiping_rebellion.3
            days = 180
        }
    }

    option = {
        name = taiping_rebellion.2.b

        # 固守南方
        add_treasury = -500
        add_modifier = {
            name = defensive_preparations
            months = 24
        }

        change_variable = {
            name = taiping_strength
            add = -5
        }

        trigger_event = {
            id = taiping_rebellion.4
            days = 365
        }
    }
}

# ========== 事件3：天京事变 ==========
taiping_rebellion.3 = {
    type = country_event

    title = taiping_rebellion.3.t
    desc = taiping_rebellion.3.d

    trigger = {
        has_variable = taiping_started
        year >= 1856
        NOT = { has_variable = taiping_tianjing_incident }
    }

    immediate = {
        set_variable = taiping_tianjing_incident
        change_variable = {
            name = taiping_strength
            add = -20
        }
    }

    option = {
        name = taiping_rebellion.3.a

        # 趁乱进攻
        add_war_exhaustion = 5
        add_army_experience = 100

        change_variable = {
            name = taiping_strength
            add = -15
        }

        trigger_event = {
            id = taiping_rebellion.4
            days = 180
        }
    }

    option = {
        name = taiping_rebellion.3.b

        # 继续观望
        add_prestige = -30

        trigger_event = {
            id = taiping_rebellion.4
            days = 365
        }
    }
}

# ========== 事件4：外国干预 ==========
taiping_rebellion.4 = {
    type = country_event

    title = taiping_rebellion.4.t
    desc = taiping_rebellion.4.d

    trigger = {
        has_variable = taiping_started
        year >= 1860
        NOT = { has_variable = taiping_foreign_intervention }
    }

    immediate = {
        set_variable = taiping_foreign_intervention

        # 保存列强作用域
        c:GBR = { save_scope_as = britain }
        c:FRA = { save_scope_as = france }
    }

    option = {
        name = taiping_rebellion.4.a

        # 寻求外国帮助
        add_treasury = -2000

        scope:britain = {
            add_opinion = {
                target = root
                value = 20
            }
        }
        scope:france = {
            add_opinion = {
                target = root
                value = 20
            }
        }

        change_variable = {
            name = taiping_strength
            add = -25
        }

        trigger_event = {
            id = taiping_rebellion.5
            days = 365
        }
    }

    option = {
        name = taiping_rebellion.4.b

        # 独自应对
        add_prestige = 50

        trigger_event = {
            id = taiping_rebellion.5
            days = 365
        }
    }
}

# ========== 事件5：结局 ==========
taiping_rebellion.5 = {
    type = country_event

    title = taiping_rebellion.5.t
    desc = taiping_rebellion.5.d

    trigger = {
        has_variable = taiping_started
        year >= 1864
    }

    immediate = {
        remove_variable = taiping_started
        remove_variable = taiping_strength
        remove_variable = taiping_territory
        remove_variable = taiping_capital_set
        remove_variable = taiping_tianjing_incident
        remove_variable = taiping_foreign_intervention
    }

    option = {
        name = taiping_rebellion.5.victory
        trigger = {
            var:taiping_strength <= 20
        }

        # 成功镇压
        add_prestige = 200
        add_modifier = {
            name = restored_order
            months = 60
        }
    }

    option = {
        name = taiping_rebellion.5.stalemate
        trigger = {
            var:taiping_strength > 20
            var:taiping_strength < 80
        }

        # 僵持
        add_war_exhaustion = 20
        add_modifier = {
            name = prolonged_rebellion
            months = 36
        }

        # 继续事件链
        trigger_event = {
            id = taiping_rebellion.5
            days = 730
        }
    }

    option = {
        name = taiping_rebellion.5.defeat
        trigger = {
            var:taiping_strength >= 80
        }

        # 起义成功（分裂国家）
        add_prestige = -300
        add_radicals_in_country = {
            value = 0.1
        }

        # 触发分裂事件
        trigger_event = {
            id = taiping_rebellion.secession
            days = 30
        }
    }
}

# ========== 战争事件 ==========
taiping_rebellion.war.1 = {
    type = country_event
    hidden = yes

    immediate = {
        # 创建外交博弈/战争
        create_diplomatic_play = {
            target_country = c:TPG       # 假设太平天国存在
            war_goal = crush_revolution
        }
    }
}

```

### 11.7.3 创建本地化文件

**文件**：`my_mod/localization/simp_chinese/taiping_rebellion_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 # 事件1：金田起义
 taiping_rebellion.1.t:0 "金田起义"
 taiping_rebellion.1.d:0 "1851年，洪秀全领导的拜上帝会在广西金田村发动起义，号称'太平天国'。起义军迅速壮大，清朝统治面临严重威胁。朝廷必须立即采取行动！"
 taiping_rebellion.1.a:0 "立即调集大军镇压"
 taiping_rebellion.1.b:0 "暂时观望局势发展"
 taiping_rebellion.1.c:0 "用银两收买人心"

 # 事件2：定都天京
 taiping_rebellion.2.t:0 "定都天京"
 taiping_rebellion.2.d:0 "太平军攻占了江宁（今南京），改名天京，定为首都。起义军势力日益壮大，已占据江南数省。朝廷必须决定下一步战略。"
 taiping_rebellion.2.a:0 "立即组织北伐"
 taiping_rebellion.2.b:0 "固守江淮防线"

 # 事件3：天京事变
 taiping_rebellion.3.t:0 "天京事变"
 taiping_rebellion.3.d:0 "太平天国内部发生严重内讧，东王杨秀清被杀，翼王石达开出走。这是镇压起义的绝佳机会！"
 taiping_rebellion.3.a:0 "趁乱发动全面进攻"
 taiping_rebellion.3.b:0 "继续积蓄力量"

 # 事件4：外国干预
 taiping_rebellion.4.t:0 "洋人的态度"
 taiping_rebellion.4.d:0 "英国和法国正在观望局势。他们既担心太平天国破坏贸易，也对清朝的软弱感到失望。我们可以寻求他们的支持..."
 taiping_rebellion.4.a:0 "用利益换取支持"
 taiping_rebellion.4.b:0 "这是中国人的内政"

 # 事件5：结局
 taiping_rebellion.5.t:0 "太平天国的命运"
 taiping_rebellion.5.d:0 "经过多年的征战，这场规模空前的起义终于迎来了结局..."
 taiping_rebellion.5.victory:0 "叛乱被成功镇压"
 taiping_rebellion.5.stalemate:0 "战争陷入僵局"
 taiping_rebellion.5.defeat:0 "天下大乱"

 # 修正器
 restored_order:0 "恢复秩序"
 restored_order_desc:0 "太平天国起义被成功镇压，朝廷威望大增。"
 prolonged_rebellion:0 "长期战乱"
 prolonged_rebellion_desc:0 "持续的战乱严重消耗了国力。"
 defensive_preparations:0 "防御准备"
 defensive_preparations_desc:0 "我们在关键地区建立了坚固的防线。"

```

### 11.7.4 创建修正器

**文件**：`my_mod/common/modifiers/my_mod_modifiers.txt`

```pdx
restored_order = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_positive.dds"

    country_prestige_add = 50
    country_authority_add = 100
    state_loyalists_from_sol_change_mult = 0.1
}

prolonged_rebellion = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_negative.dds"

    country_prestige_add = -30
    country_tax_income_add = -0.1
    state_radicals_from_sol_change_mult = 0.15
}

defensive_preparations = {
    icon = "gfx/interface/icons/modifiers/modifier_rifle_positive.dds"

    unit_defense_mult = 0.1
    state_building_barracks_max_level_add = 2
}

```

---

## 11.8 隐藏事件

### 11.8.1 什么是隐藏事件？

**隐藏事件**不显示给玩家，只执行效果。用于：
- 自动触发战争
- 设置变量和标记
- 复杂的后台计算

### 11.8.2 创建隐藏事件

```pdx
my_event.hidden = {
    type = country_event
    hidden = yes                    # 隐藏事件

    trigger = {
        # 触发条件
    }

    immediate = {
        # 只执行效果，不显示
        set_variable = hidden_marker
        add_treasury = 1000
    }

    # 不需要选项！
}

```

---

## 11.9 事件调试技巧

### 11.9.1 使用控制台测试

```pdx
event taiping_rebellion.1      # 手动触发事件
event taiping_rebellion.2
event taiping_rebellion.3

```

### 11.9.2 添加调试信息

```pdx
immediate = {
    # 输出调试信息
    log = "Taiping Rebellion triggered for [GetCountryName] in [GetYear]"
    log = "Strength: [var:taiping_strength]"

    set_variable = taiping_started
}

```

### 11.9.3 常见错误排查

| 错误       | 原因           | 解决方案           |
| ---------- | -------------- | ------------------ |
| 事件不触发 | 触发条件不满足 | 检查触发器逻辑     |
| 事件不显示 | 事件ID重复     | 检查命名空间       |
| 乱码       | 编码错误       | 使用UTF-8 BOM      |
| 效果不生效 | 作用域错误     | 检查效果所在作用域 |
| 无限循环   | 事件A触发事件A | 添加变量检查       |

---

## 本章小结

- **事件**是Mod的核心，让玩家与游戏互动
- **命名空间**用于组织事件，避免ID冲突
- **事件结构**：类型、标题、描述、触发条件、立即效果、选项
- **事件链**通过`trigger_event`实现，可以有时间延迟
- **隐藏事件**用于后台逻辑，不显示给玩家
- **实战案例**：太平天国起义事件链展示了完整的设计流程

---

## 常见问题

**Q：事件为什么不触发？**

A：检查：
1. 触发条件是否满足？
2. 文件编码是否正确？
3. 事件ID是否重复？
4. 是否在`events/`文件夹中？

**Q：如何让事件只触发一次？**

A：使用变量标记：

```pdx
trigger = {
    NOT = { has_variable = event_fired }
}
immediate = {
    set_variable = event_fired
}

```

**Q：AI如何选择选项？**

A：通过`ai_chance`控制，可以设置基础值和修正器。

**Q：事件链太长会不会有问题？**

A：建议单个事件链不超过10个事件，太长会导致玩家疲劳。可以分成多个并行的事件链。

---

## 练习建议

1. **基础练习**：创建简单事件
   - 一个关于发现金矿的事件
   - 包含3个选项：私吞、上交、分享
   - 每个选项有不同的效果

2. **中级练习**：创建事件链
   - 3-5个连续事件
   - 有时间延迟
   - 使用变量记录进度

3. **高级练习**：创建分支事件链
   - 初始事件有2-3个分支
   - 每个分支有3-4个后续事件
   - 不同的选择导致不同结局

4. **综合练习**：制作完整的历史事件
   - 选择一个历史事件（如明治维新、美国内战）
   - 研究历史背景和关键节点
   - 设计5-8个事件的事件链
   - 添加本地化、修正器等配套文件

---

> 📖 **下一章预告**：在下一章，我们将学习**决策系统（Decision）**——添加可点击的国家决策。

---

## 参考

- [Victoria 3 Wiki - Event modding](https://vic3.paradoxwikis.com/Event_modding)
- 官方事件文件：`Victoria 3/game/events/`
