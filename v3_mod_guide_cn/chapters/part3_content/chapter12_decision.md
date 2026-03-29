# 第12章：决策系统（Decision）——添加国家决策

> 决策系统允许你为游戏添加可点击的按钮，让玩家主动触发效果。从改革法律到发动战争，决策是实现玩家主动选择的关键工具。

## 本章目标

完成本章学习后，你将能够：
- 理解决策系统的基本概念和用途
- 掌握决策的显示条件和可用条件
- 编写决策的点击效果和AI逻辑
- 创建各种类型的决策（改革、战争、外交等）
- 将决策与事件系统结合使用

---

## 12.1 什么是决策？

### 12.1.1 生活化比喻

想象你是一家公司的CEO，你的办公桌上有一个"决策面板"：

**场景1：战略决策**
- 按钮："扩大生产线"（需要资金、可用）
- 按钮："收购竞争对手"（需要更多资金、灰色不可用）
- 按钮："上市IPO"（需要满足条件、隐藏中）

**场景2：日常运营**
- 按钮："招聘新员工"（总是可用）
- 按钮："调整薪资"（每季度限一次）
- 按钮："紧急会议"（危机时才会显示）

在维多利亚3中，**决策**就是这样的"按钮面板"，让玩家主动选择要执行的行动。

### 12.1.2 技术定义

**决策**是显示在决策面板上的可点击按钮：
- **可见性**：决定玩家是否能看到按钮
- **可用性**：决定按钮是否可以点击
- **效果**：点击后执行的游戏变化

```pdx
┌─────────────────────────────────┐
│  决策面板                        │
│                                  │
│  [推行洋务运动]        [可用]    │
│  [发动鸦片战争]        [可用]    │
│  [改革法律制度]        [灰色]    │
│                                  │
│  [宣战：英国]          [可用]    │
└─────────────────────────────────┘

```

### 12.1.3 决策 vs 事件

| 特性         | 决策（Decision）   | 事件（Event）        |
| ------------ | ------------------ | -------------------- |
| **触发方式** | 玩家主动点击       | 被动触发（条件满足） |
| **频率**     | 玩家控制           | 游戏控制             |
| **用途**     | 主动行动、长期计划 | 反应情况、剧情推进   |
| **示例**     | 改革法律、发动战争 | 自然灾害、外交危机   |

---

## 12.2 决策文件基础

### 12.2.1 文件位置

决策文件存放在：

```pdx
my_mod/common/decisions/          # 主文件夹
my_mod/common/decisions/my_mod_decisions.txt

```

### 12.2.2 基本结构

```pdx
# 决策名称
my_decision = {
    # 显示条件（是否显示在面板）
    is_shown = {
        # 触发器
    }

    # 可用条件（是否可以点击）
    possible = {
        # 触发器
    }

    # 点击时执行的效果
    when_taken = {
        # 效果
    }

    # AI选择权重
    ai_chance = {
        # AI逻辑
    }
}

```

### 12.2.3 最小决策示例

最简单的完整决策：

```pdx
# common/decisions/my_mod_decisions.txt

simple_reform = {
    is_shown = {
        exists = yes        # 总是显示
    }

    possible = {
        treasury >= 100     # 需要100资金
    }

    when_taken = {
        add_treasury = -100
        add_prestige = 50
    }
}

```

---

## 12.3 决策的各个组成部分

### 12.3.1 显示条件（is_shown）

决定决策是否显示在决策面板上：

```pdx
qing_self_strengthening = {
    # 只有大清能看到这个决策
    is_shown = {
        this = c:CHI
    }

    # ...
}

```

**常见用法**：

```pdx
# 特定国家
is_shown = {
    this = c:CHI
}

# 特定政府形式
is_shown = {
    is_monarchy = yes
}

# 特定时期
is_shown = {
    year >= 1860
    year <= 1900
}

# 组合条件
is_shown = {
    this = c:CHI
    year >= 1860
    is_at_war = no
}

```

### 12.3.2 可用条件（possible）

决定决策是否可以点击（灰色 vs 可用）：

```pdx
industrialization_reform = {
    is_shown = {
        exists = yes
    }

    # 点击条件
    possible = {
        # 需要资金
        treasury >= 1000

        # 需要科技
        has_technology_researched = railroad

        # 需要和平
        is_at_war = no

        # 需要国家等级
        OR = {
            country_rank = rank_value:great_power
            country_rank = rank_value:major_power
        }
    }

    # ...
}

```

**显示 vs 可用对比**：

| 情况           | is_shown | possible | 显示状态     |
| -------------- | -------- | -------- | ------------ |
| 完全满足       | ✅ 真    | ✅ 真    | 可用（亮色） |
| 只满足is_shown | ✅ 真    | ❌ 假    | 显示但灰色   |
| 都不满足       | ❌ 假    | -        | 不显示       |

### 12.3.3 点击效果（when_taken）

玩家点击决策后执行的效果：

```pdx
promote_industry = {
    is_shown = { exists = yes }
    possible = { treasury >= 500 }

    when_taken = {
        # 扣除资金
        add_treasury = -500

        # 研究科技
        add_technology = steel

        # 在首都建工厂
        capital = {
            add_building = building_steel_mills
        }

        # 添加修正器
        add_modifier = {
            name = industrial_boost
            months = 24
        }

        # 添加激进派（改革的代价）
        add_radicals_in_country = {
            value = 0.02
        }

        # 触发事件
        trigger_event = {
            id = industrialization.1
            days = 30
        }

        # 设置变量（防止重复）
        set_variable = {
            name = industry_promoted
            value = 1
        }
    }
}

```

### 12.3.4 AI权重（ai_chance）

控制AI国家如何选择决策：

```pdx
qing_self_strengthening = {
    is_shown = { this = c:CHI }
    possible = { treasury >= 1000 }
    when_taken = { ... }

    ai_chance = {
        # 基础权重
        base = 10

        # 修正器1：国库充足时更倾向
        modifier = {
            add = 20
            trigger = {
                treasury > 2000
            }
        }

        # 修正器2：有改革派领导人时更倾向
        modifier = {
            add = 30
            trigger = {
                ruler = { has_trait = trait_enlightened }
            }
        }

        # 修正器3：保守派领导人时减少
        modifier = {
            add = -20
            trigger = {
                ruler = { has_trait = trait_conservative }
            }
        }

        # 修正器4：战争时期不选择
        modifier = {
            factor = 0
            trigger = {
                is_at_war = yes
            }
        }
    }
}

```

**AI权重计算**：
- 基础值 + 所有满足条件的add值 = 最终权重
- AI选择权重最高的可用决策
- `factor = 0` 表示AI不会选择

---

## 12.4 决策类型示例

### 12.4.1 改革决策

```pdx
# 推行洋务运动
qing_self_strengthening = {
    is_shown = {
        this = c:CHI
        year >= 1860
        year <= 1880
    }

    possible = {
        treasury >= 1000
        is_at_war = no
        NOT = { has_variable = self_strengthening_started }
    }

    when_taken = {
        add_treasury = -1000
        set_variable = self_strengthening_started

        add_technology = railroad
        add_technology = steel

        add_modifier = {
            name = self_strengthening
            months = 60
        }

        trigger_event = {
            id = qing_reform.1
            days = 7
        }
    }

    ai_chance = {
        base = 20
        modifier = {
            add = 30
            treasury > 2000
        }
        modifier = {
            factor = 0
            is_at_war = yes
        }
    }
}

```

### 12.4.2 外交决策

```pdx
# 建立同盟
create_alliance_decision = {
    is_shown = {
        is_independent = yes
        country_rank >= rank_value:minor_power
    }

    possible = {
        # 需要有一个潜在盟友
        any_country = {
            NOT = { this = root }
            relations_with = {
                target = root
                value >= 50
            }
        }

        # 不在战争中
        is_at_war = no
    }

    when_taken = {
        # 随机选择一个友好国家
        random_country = {
            limit = {
                NOT = { this = root }
                relations_with = {
                    target = root
                    value >= 50
                }
            }
            save_scope_as = potential_ally
        }

        # 创建同盟
        create_diplomatic_pact = {
            country = scope:potential_ally
            type = alliance
        }

        # 通知对方
        scope:potential_ally = {
            trigger_event = {
                id = alliance_formed.1
                days = 3
            }
        }
    }
}

```

### 12.4.3 战争决策

```pdx
# 收复失地
reclaim_territory = {
    is_shown = {
        any_country = {
            NOT = { this = root }
            any_scope_state = {
                # 曾经属于我国
                has_claim = root
            }
        }
    }

    possible = {
        # 需要足够强大
        army_size >= 50
        treasury >= 500

        # 不在战争中
        is_at_war = no

        # 目标不是附属国
        any_country = {
            limit = {
                any_scope_state = {
                    has_claim = root
                }
            }
            is_subject = no
        }
    }

    when_taken = {
        # 找到目标国家
        random_country = {
            limit = {
                any_scope_state = {
                    has_claim = root
                }
            }
            save_scope_as = target_country
        }

        # 发动外交博弈
        create_diplomatic_play = {
            target_country = scope:target_country
            war_goal = return_state
        }

        add_infamy = 5
    }

    ai_chance = {
        base = 5
        modifier = {
            add = 15
            army_size >= 100
        }
        modifier = {
            add = 10
            country_rank = rank_value:great_power
        }
    }
}

```

### 12.4.4 重复性决策

```pdx
# 宣传运动（可重复）
propaganda_campaign = {
    is_shown = {
        exists = yes
    }

    possible = {
        treasury >= 200

        # 冷却时间：1年
        custom_tooltip = {
            text = "has_not_done_propaganda_recently"
            NOT = { has_variable = recent_propaganda }
        }
    }

    when_taken = {
        add_treasury = -200

        add_loyalists_in_country = {
            value = 0.03
        }

        add_prestige = 25

        # 设置冷却变量（1年）
        set_variable = {
            name = recent_propaganda
            value = 1
            years = 1
        }
    }
}

```

---

## 12.5 本地化文件

决策需要在本地化文件中定义文本：

**文件**：`my_mod/localization/simp_chinese/decisions_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 # 决策名称
 qing_self_strengthening:0 "推行洋务运动"
 qing_self_strengthening_desc:0 "开始一项 ambitious 的现代化改革计划，学习西方技术，增强国力。"
 qing_self_strengthening_tooltip:0 "这将花费1000资金，并启动改革事件链。"

 promote_industry:0 "促进工业发展"
 promote_industry_desc:0 "投资工业建设，推动经济现代化。"

 create_alliance_decision:0 "寻求盟友"
 create_alliance_decision_desc:0 "与一个友好国家建立军事同盟。"

 reclaim_territory:0 "收复失地"
 reclaim_territory_desc:0 "夺回曾经属于我们的领土。"

 propaganda_campaign:0 "开展宣传运动"
 propaganda_campaign_desc:0 "通过宣传提高民众对政府的支持。"

 # 提示文本
 has_not_done_propaganda_recently:0 "最近一年内未进行过宣传"

```

---

## 12.6 决策与事件结合

### 12.6.1 决策触发事件

```pdx
# 决策
start_reform = {
    is_shown = { ... }
    possible = { ... }

    when_taken = {
        # 触发事件开始改革
        trigger_event = {
            id = reform_event.1
            days = 7
        }
    }
}

# 事件
reform_event.1 = {
    type = country_event
    title = reform_event.1.t
    desc = reform_event.1.d

    option = {
        name = reform_event.1.a
        # 选项效果
    }

    option = {
        name = reform_event.1.b
        # 另一个选项
    }
}

```

### 12.6.2 事件触发决策

```pdx
# 事件给予决策权限
crisis_event.1 = {
    type = country_event
    # ...

    immediate = {
        # 添加一个临时决策
        set_variable = emergency_powers_granted
    }

    option = {
        name = crisis_event.1.a
    }
}

# 临时决策
emergency_measures = {
    is_shown = {
        has_variable = emergency_powers_granted
    }

    possible = {
        treasury >= 500
    }

    when_taken = {
        add_treasury = -500
        add_modifier = {
            name = emergency_boost
            months = 6
        }

        # 移除决策权限
        remove_variable = emergency_powers_granted
    }
}

```

---

## 12.7 实战案例：完整改革系统

### 12.7.1 设计思路

创建一个"洋务运动"完整决策系统：
- 主决策：启动洋务运动
- 子决策：军事改革、经济改革、教育改革
- 每个改革有前置条件和效果
- 所有改革完成后获得大奖励

### 12.7.2 决策文件

**文件**：`common/decisions/qing_reform_decisions.txt`

```pdx
# ========== 主决策：启动洋务运动 ==========
start_self_strengthening = {
    is_shown = {
        this = c:CHI
        year >= 1860
        year <= 1880
        NOT = { has_variable = self_strengthening_active }
    }

    possible = {
        treasury >= 1000
        is_at_war = no
        has_technology_researched = nationalism
    }

    when_taken = {
        add_treasury = -1000
        set_variable = self_strengthening_active
        set_variable = {
            name = reform_progress
            value = 0
        }

        add_modifier = {
            name = self_strengthening
            months = 60
        }

        trigger_event = {
            id = qing_reform_decision.1
            days = 7
        }
    }

    ai_chance = {
        base = 30
        modifier = { add = 20 treasury > 2000 }
        modifier = { factor = 0 is_at_war = yes }
    }
}

# ========== 子决策1：军事改革 ==========
military_reform = {
    is_shown = {
        has_variable = self_strengthening_active
        NOT = { has_variable = military_reform_done }
    }

    possible = {
        treasury >= 800
        is_at_war = no
    }

    when_taken = {
        add_treasury = -800
        set_variable = military_reform_done

        change_variable = {
            name = reform_progress
            add = 25
        }

        add_technology = breech_loading_artillery
        add_technology = percussion_cap

        capital = {
            add_building = building_arms_industry
        }

        add_army_experience = 100

        # 检查是否完成所有改革
        trigger_event = {
            id = qing_reform_decision.check_completion
            days = 1
        }
    }

    ai_chance = {
        base = 20
        modifier = { add = 15 army_size > 50 }
    }
}

# ========== 子决策2：经济改革 ==========
economic_reform = {
    is_shown = {
        has_variable = self_strengthening_active
        NOT = { has_variable = economic_reform_done }
    }

    possible = {
        treasury >= 1000
        has_technology_researched = railroad
    }

    when_taken = {
        add_treasury = -1000
        set_variable = economic_reform_done

        change_variable = {
            name = reform_progress
            add = 25
        }

        add_technology = steel
        add_technology = chemical_processes

        every_scope_state = {
            limit = { is_coastal = yes }
            add_building = building_textile_mills
        }

        trigger_event = {
            id = qing_reform_decision.check_completion
            days = 1
        }
    }

    ai_chance = {
        base = 20
        modifier = { add = 15 treasury > 1500 }
    }
}

# ========== 子决策3：教育改革 ==========
education_reform = {
    is_shown = {
        has_variable = self_strengthening_active
        NOT = { has_variable = education_reform_done }
    }

    possible = {
        treasury >= 600
        literacy_rate > 0.1
    }

    when_taken = {
        add_treasury = -600
        set_variable = education_reform_done

        change_variable = {
            name = reform_progress
            add = 25
        }

        add_technology = compulsory_primary_school

        capital = {
            add_building = building_university
        }

        add_modifier = {
            name = education_boost
            months = 36
        }

        trigger_event = {
            id = qing_reform_decision.check_completion
            days = 1
        }
    }

    ai_chance = {
        base = 15
        modifier = { add = 10 literacy_rate < 0.3 }
    }
}

# ========== 子决策4：海军改革 ==========
naval_reform = {
    is_shown = {
        has_variable = self_strengthening_active
        NOT = { has_variable = naval_reform_done }
    }

    possible = {
        treasury >= 1200
        any_scope_state = { is_coastal = yes }
    }

    when_taken = {
        add_treasury = -1200
        set_variable = naval_reform_done

        change_variable = {
            name = reform_progress
            add = 25
        }

        add_technology = steamers
        add_technology = screw_frigates

        add_navy_experience = 100

        trigger_event = {
            id = qing_reform_decision.check_completion
            days = 1
        }
    }

    ai_chance = {
        base = 15
        modifier = { add = 10 any_scope_state = { is_coastal = yes } }
    }
}

```

### 12.7.3 完成检查事件

```pdx
# 检查是否完成所有改革
qing_reform_decision.check_completion = {
    type = country_event
    hidden = yes

    trigger = {
        var:reform_progress >= 100
    }

    immediate = {
        remove_variable = self_strengthening_active
        remove_variable = reform_progress
        remove_variable = military_reform_done
        remove_variable = economic_reform_done
        remove_variable = education_reform_done
        remove_variable = naval_reform_done

        add_prestige = 500
        add_modifier = {
            name = successful_reform
            months = 60
        }

        # 触发完成庆祝事件
        trigger_event = {
            id = qing_reform_decision.completion
            days = 7
        }
    }
}

# 完成庆祝事件
qing_reform_decision.completion = {
    type = country_event
    title = qing_reform_decision.completion.t
    desc = qing_reform_decision.completion.d

    option = {
        name = qing_reform_decision.completion.a
        add_prestige = 200
    }
}

```

### 12.7.4 本地化

```yaml
l_simp_chinese:
 start_self_strengthening:0 "启动洋务运动"
 start_self_strengthening_desc:0 "开始一项全面的现代化改革计划，增强国家实力。"
 start_self_strengthening_tooltip:0 "花费1000资金，开启4个改革决策。"

 military_reform:0 "军事改革"
 military_reform_desc:0 "引进西方军事技术，建立近代化军队。"

 economic_reform:0 "经济改革"
 economic_reform_desc:0 "发展工业，建设铁路，促进贸易。"

 education_reform:0 "教育改革"
 education_reform_desc:0 "建立新式学堂，派遣留学生，提高识字率。"

 naval_reform:0 "海军改革"
 naval_reform_desc:0 "建立近代海军，购置军舰，保护海疆。"

| reform_progress_tt:0 "改革进度：[var:reform_progress | 0]/100" |
| ---------------------------------------------------- | ------- |

```

---

## 12.8 常见错误与最佳实践

### 12.8.1 常见错误

#### 错误1：混淆is_shown和possible

❌ **错误理解**：

```pdx
# 错误：用possible控制可见性
my_decision = {
    is_shown = { exists = yes }     # 总是显示
    possible = { this = c:CHI }     # 只有大清可以点击
}

```

✅ **正确**：

```pdx
# 正确：is_shown控制可见性
my_decision = {
    is_shown = { this = c:CHI }     # 只有大清能看到
    possible = { treasury >= 1000 } # 资金足够时可以点击
}

```

#### 错误2：没有冷却机制

❌ **问题**：决策可以无限重复点击

✅ **解决**：

```pdx
my_decision = {
    possible = {
        NOT = { has_variable = recently_done }
    }

    when_taken = {
        set_variable = {
            name = recently_done
            value = 1
            months = 12        # 12个月冷却
        }
    }
}

```

#### 错误3：AI权重不合理

❌ **问题**：AI从不选择或总是选择

✅ **解决**：

```pdx
ai_chance = {
    base = 10                       # 合理的基础值

    modifier = {
        factor = 0                  # 明确禁用的情况
        trigger = { is_at_war = yes }
    }

    modifier = {
        add = 20                    # 鼓励的情况
        trigger = { treasury > 2000 }
    }
}

```

### 12.8.2 最佳实践

#### 1. 清晰的命名和描述

```pdx
# 好的命名
promote_industrialization
create_defensive_alliance
reform_education_system

# 好的描述
promote_industrialization_desc:0 "投资工业建设，推动经济现代化。"

```

#### 2. 合理的成本和收益

```pdx
when_taken = {
    # 成本应该与收益匹配
    add_treasury = -1000        # 高成本
    add_technology = steel      # 高价值科技
    add_prestige = 100          # 适当威望
    add_modifier = { ... }      # 长期收益
}

```

#### 3. 提供多种路径

```pdx
# 玩家可以选择不同策略
- 军事改革路线
- 经济改革路线
- 平衡发展路线

```

#### 4. 使用变量追踪进度

```pdx
# 使用变量记录状态
set_variable = reform_started
change_variable = { name = reform_progress add = 25 }

```

---

## 本章小结

- **决策**是玩家主动触发的按钮，显示在决策面板
- **is_shown**：控制是否显示
- **possible**：控制是否可点击
- **when_taken**：点击后执行的效果
- **ai_chance**：AI选择权重
- 决策可以与事件系统结合，实现复杂玩法
- 实战案例：洋务运动改革系统（1主决策+4子决策）

---

## 常见问题

**Q：决策和事件有什么区别？**

A：
- **决策**：玩家主动点击触发
- **事件**：满足条件自动触发

**Q：为什么我的决策不显示？**

A：检查：
1. 文件是否在`common/decisions/`文件夹
2. `is_shown`条件是否满足
3. 本地化文件是否正确

**Q：如何让AI更聪明地选择决策？**

A：
1. 设置合理的`ai_chance`基础值
2. 添加情境化的修正器
3. 使用`factor = 0`明确禁用不合理情况

**Q：决策可以隐藏吗？**

A：可以，当`is_shown`返回假时，决策完全不显示。

**Q：决策的图标如何设置？**

A：在本地化文件中使用`_icon`后缀指定图标路径。

---

## 练习建议

1. **基础练习**：创建简单决策
   - 花费资金获得威望
   - 有冷却时间
   - 特定国家才能使用

2. **中级练习**：创建决策链
   - 启动某个计划的主决策
   - 3-4个子决策
   - 完成后给予大奖励

3. **高级练习**：创建战略决策
   - 军事/经济/外交三种路线
   - 互斥选择（选A就不能选B）
   - 长期影响（修正器、变量）

4. **综合练习**：创建完整的改革系统
   - 参考洋务运动案例
   - 5-6个相关决策
   - 与事件系统结合
   - 合理的AI逻辑

---

> 📖 **下一章预告**：在下一章，我们将学习**日志系统（Journal Entry）**——长期任务追踪系统。

---

## 参考

- [Victoria 3 Wiki - Decision modding](https://vic3.paradoxwikis.com/Decision_modding)
- 官方决策文件：`Victoria 3/game/common/decisions/`
