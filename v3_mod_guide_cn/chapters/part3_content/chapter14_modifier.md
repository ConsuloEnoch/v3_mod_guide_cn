# 第14章：修正器（Modifier）——游戏效果buff

> 修正器是维多利亚3中用于修改游戏数值的系统，可以为国家和州添加各种增益或减益效果。本章将讲解如何创建和使用修正器。

## 本章目标

完成本章学习后，你将能够：
- 理解修正器的基本概念和用途
- 创建静态修正器和动态修正器
- 使用修正器类型定义
- 在事件、决策中应用修正器
- 设计平衡的修正器系统

---

## 14.1 什么是修正器？

### 14.1.1 生活化比喻

想象RPG游戏中的状态效果：

**增益效果（Buff）**：
- "力量药水"：攻击力+20%，持续5分钟
- "防御姿态"：防御力+50%，移动速度-30%

**减益效果（Debuff）**：
- "中毒"：每秒损失5HP，持续30秒
- "疲劳"：攻击力-30%，经验获取-50%

在维多利亚3中，**修正器（Modifier）**就是这样的状态效果系统。

### 14.1.2 技术定义

**修正器**是修改游戏数值的效果，可以：
- 增加或减少各种属性
- 设置持续时间（临时）或永久生效
- 应用于国家、州、建筑等

```pdx
# 示例：工业化修正器
add_modifier = {
    name = industrialization_boost
    months = 24                    # 持续24个月
}

# 效果：
# - 建造速度+20%
# - 工厂产出+15%
# - 研究速度+10%

```

---

## 14.2 修正器文件基础

### 14.2.1 文件位置

修正器定义文件：

```pdx
my_mod/common/modifiers/           # 主文件夹
my_mod/common/modifiers/my_mod_modifiers.txt

```

### 14.2.2 基本结构

```pdx
# 修正器名称
modifier_name = {
    # 图标
    icon = "gfx/interface/icons/modifiers/modifier_industry.dds"

    # 修正效果
    country_construction_add = 0.2          # 建造速度+20%
    building_group_bg_industry_throughput_add = 0.15  # 工业产出+15%
    country_tech_spread_add = 0.1           # 研究速度+10%

    # 正负标记（用于AI判断）
    good = yes                              # 正面效果
}

```

---

## 14.3 修正器类型

### 14.3.1 国家修正器

应用于整个国家：

```pdx
industrialization_boost = {
    icon = "gfx/interface/icons/modifiers/modifier_industry.dds"

    # 经济
    country_construction_add = 0.2
    building_group_bg_industry_throughput_add = 0.15

    # 科技
    country_tech_spread_add = 0.1

    good = yes
}

war_fatigue = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_negative.dds"

    # 负面效果
    country_prestige_add = -20
    state_radicals_from_sol_change_mult = 0.2
    country_construction_add = -0.1

    good = no
}

```

### 14.3.2 州修正器

应用于特定州：

```pdx
mining_boom = {
    icon = "gfx/interface/icons/modifiers/modifier_pickaxe.dds"

    # 州级效果
    building_group_bg_mining_throughput_add = 0.25
    state_infrastructure_add = 5

    good = yes
}

famine = {
    icon = "gfx/interface/icons/modifiers/modifier_wheat_negative.dds"

    state_population_growth_add = -0.02
    state_radicals_from_sol_change_mult = 0.3

    good = no
}

```

### 14.3.3 建筑修正器

应用于特定建筑：

```pdx
efficient_production = {
    icon = "gfx/interface/icons/modifiers/modifier_gear.dds"

    building_throughput_add = 0.1
    building_laborers_mortality_mult = -0.05

    good = yes
}

```

---

## 14.4 常用修正效果

### 14.4.1 经济类

```pdx
# 建造速度
country_construction_add = 0.2           # +20%
country_construction_add = -0.1          # -10%

# 税收
country_tax_income_add = 0.15            # +15%

# 产出
building_group_bg_industry_throughput_add = 0.1
building_output_mult = 0.05

# 商品效率
building_input_goods_cost_mult = -0.1    # 投入成本-10%
building_output_goods_cost_mult = 0.05   # 产出价格+5%

```

### 14.4.2 军事类

```pdx
# 军队属性
unit_offense_mult = 0.1                  # 攻击力+10%
unit_defense_mult = 0.15                 # 防御力+15%
unit_morale_recovery_mult = 0.2          # 士气恢复+20%

# 军队规模
country_max_battalions_add = 10          # 最大营数+10

# 战争支持
country_war_exhaustion_mult = -0.1       # 战争疲劳-10%

```

### 14.4.3 政治类

```pdx
# 威望
country_prestige_add = 50
country_prestige_mult = 0.1              # +10%

# 权威
country_authority_add = 100
country_authority_mult = 0.15

# 恶名
country_infamy_decay_mult = 0.2          # 恶名衰减+20%

# 利益集团
country_ig_attraction_ig_industrialists_mult = 0.1

```

### 14.4.4 社会类

```pdx
# 人口
state_birth_rate_mult = 0.05
state_mortality_mult = -0.1

# 激进/忠诚
state_radicals_from_sol_change_mult = 0.1
state_loyalists_from_sol_change_mult = 0.15

# 生活水平
state_standard_of_living_add = 1

```

### 14.4.5 科技类

```pdx
# 研究速度
country_tech_spread_add = 0.1
country_research_speed_add = 0.15

# 科技成本
country_tech_research_cost_mult = -0.1   # 研究成本-10%

```

---

## 14.5 在脚本中使用修正器

### 14.5.1 添加临时修正器

```pdx
# 在事件中添加
event_option = {
    name = my_event.1.a

    add_modifier = {
        name = industrialization_boost
        months = 24                # 持续24个月
    }
}

# 在决策中添加
decision = {
    when_taken = {
        add_modifier = {
            name = reform_bonus
            years = 5              # 持续5年
        }
    }
}

```

### 14.5.2 添加衰减修正器

```pdx
add_modifier = {
    name = temporary_boost
    months = 12
    is_decaying = yes              # 随时间衰减
}

```

### 14.5.3 添加永久修正器

```pdx
# 不设置时间 = 永久
add_modifier = {
    name = permanent_bonus
}

# 或明确设置
add_modifier = {
    name = permanent_bonus
    months = -1                    # -1表示永久
}

```

### 14.5.4 移除修正器

```pdx
# 移除特定修正器
remove_modifier = industrialization_boost

# 移除所有同类修正器
remove_modifier_category = country_modifiers

```

### 14.5.5 给州添加修正器

```pdx
effect = {
    every_scope_state = {
        limit = { is_coastal = yes }
        add_modifier = {
            name = coastal_prosperity
            months = 36
        }
    }
}

```

---

## 14.6 实战案例

### 14.6.1 改革修正器系统

**文件**：`common/modifiers/reform_modifiers.txt`

```pdx
# 洋务运动修正器
self_strengthening = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_positive.dds"

    country_construction_add = 0.15
    building_group_bg_industry_throughput_add = 0.1
    country_tech_spread_add = 0.1
    country_authority_add = 50

    good = yes
}

# 改革成功奖励
successful_reform = {
    icon = "gfx/interface/icons/modifiers/modifier_star.dds"

    country_prestige_add = 50
    country_construction_add = 0.1
    building_group_bg_industry_throughput_add = 0.05
    state_loyalists_from_sol_change_mult = 0.05

    good = yes
}

# 改革失败惩罚
failed_reform = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_negative.dds"

    country_prestige_add = -30
    country_authority_add = -50
    state_radicals_from_sol_change_mult = 0.1

    good = no
}

# 军事改革效果
military_reform_bonus = {
    icon = "gfx/interface/icons/modifiers/modifier_rifle_positive.dds"

    unit_offense_mult = 0.1
    unit_defense_mult = 0.1
    country_max_battalions_add = 10

    good = yes
}

# 经济改革效果
economic_reform_bonus = {
    icon = "gfx/interface/icons/modifiers/modifier_coins_positive.dds"

    building_group_bg_industry_throughput_add = 0.15
    building_group_bg_agriculture_throughput_add = 0.1
    country_tax_income_add = 0.05

    good = yes
}

# 教育改革效果
education_reform_bonus = {
    icon = "gfx/interface/icons/modifiers/modifier_book_positive.dds"

    country_tech_spread_add = 0.15
    country_research_speed_add = 0.1
    state_education_access_add = 0.1

    good = yes
}

```

### 14.6.2 事件中的应用

```pdx
# 事件选项中应用修正器
qing_reform.1 = {
    type = country_event
    # ...

    option = {
        name = qing_reform.1.military

        # 添加军事改革修正器
        add_modifier = {
            name = military_reform_bonus
            months = 36
        }

        # 添加总体改革修正器
        if = {
            limit = { NOT = { has_modifier = self_strengthening } }
            add_modifier = {
                name = self_strengthening
                months = 60
            }
        }
    }
}

```

### 14.6.3 决策中的应用

```pdx
# 决策中应用修正器
military_reform_decision = {
    is_shown = { ... }
    possible = { ... }

    when_taken = {
        add_treasury = -800

        # 添加修正器
        add_modifier = {
            name = military_reform_bonus
            months = 36
        }

        # 给所有州添加效果
        every_scope_state = {
            add_modifier = {
                name = state_military_focus
                months = 24
            }
        }
    }
}

```

---

## 14.7 平衡设计建议

### 14.7.1 数值平衡原则

1. **小幅度调整**：单项修正通常在±5%到±25%之间
2. **成本匹配**：强大的修正器应该有相应的成本
3. **时间限制**：强力修正器应该有持续时间
4. **副作用**：强大的增益可以有轻微副作用

### 14.7.2 示例平衡

```pdx
# 平衡的设计
balanced_boost = {
    # +20%正面效果
    country_construction_add = 0.2

    # -5%轻微副作用
    country_authority_add = -0.05

    good = yes
}

# 强力但临时的设计
powerful_temporary = {
    # 很强的正面效果
    unit_offense_mult = 0.3
    unit_defense_mult = 0.3

    # 但只持续6个月
    # 使用时添加：months = 6

    good = yes
}

```

---

## 本章小结

- **修正器**是修改游戏数值的效果系统
- **类型**：国家修正器、州修正器、建筑修正器
- **使用**：add_modifier添加，remove_modifier移除
- **平衡**：合理设置数值、成本和时间
- **与事件/决策结合**：实现丰富的游戏效果

---

## 常见问题

**Q：修正器可以叠加吗？**

A：可以，同类修正器的效果会叠加。

**Q：如何查看当前有哪些修正器？**

A：在游戏的UI界面可以看到当前生效的修正器列表。

**Q：修正器和法律有什么区别？**

A：
- **修正器**：临时或永久的数值修改
- **法律**：游戏机制的根本改变

---

## 参考

- [Victoria 3 Wiki - Modifier modding](https://vic3.paradoxwikis.com/Modifier_modding)
- 附录H - 修正器类型大全
