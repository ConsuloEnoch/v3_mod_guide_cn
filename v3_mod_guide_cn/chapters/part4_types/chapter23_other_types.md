# 第23章：其他类型（Other Types）

> 本章将简要介绍其他重要的游戏类型定义，包括机构、利益集团、法令、外交等。这些类型虽然内容相对较少，但对于完善Mod同样重要。

## 本章目标

完成本章学习后，你将能够：
- 理解机构、利益集团等系统的基本结构
- 创建新的机构类型
- 修改利益集团的属性
- 了解外交、条约、战争目标等系统的基本框架

---

## 23.1 机构（Institution）

### 23.1.1 什么是机构？

**机构**是国家层面的长期建设项目，需要持续投入资金和官僚资源。

**示例**：
- 学校系统
- 警察系统
- 医疗系统
- 社会保障

### 23.1.2 文件位置

```pdx
my_mod/common/institutions/           # 机构定义

```

### 23.1.3 机构定义示例

```pdx
# common/institutions/my_mod_institutions.txt

institution_example = {
    # 图标
    icon = "gfx/interface/icons/institution_icons/example.dds"

    # 背景图
    background_texture = "gfx/interface/illustrations/institutions/example.dds"

    # 描述
    desc = institution_example_desc

    # 修正效果
    modifier = {
        state_education_access_add = 0.1
    }

    # 每级的成本
    country_modifier = {
        country_bureaucracy_add = -100
    }

    # 最大等级
    max_level = 5

    # 解锁条件
    unlocking_laws = {
        law_public_schools
    }

    # 是否需要特定法律激活
    required_laws = {
        law_public_schools
    }
}

```

---

## 23.2 利益集团（Interest Group）

### 23.2.1 什么是利益集团？

**利益集团**代表特定社会阶层的政治力量，影响国家法律和政策。

**示例**：
- 军队（Armed Forces）
- 工业家（Industrialists）
- 地主（Landowners）
- 知识分子（Intelligentsia）

### 23.2.2 文件位置

```pdx
my_mod/common/interest_groups/        # 利益集团定义

```

### 23.2.3 利益集团定义示例

```pdx
# common/interest_groups/my_mod_igs.txt

ig_merchants = {
    # 图标
    texture = "gfx/interface/icons/ig_icons/merchants.dds"

    # 优先级（影响力）
    priority = 10

    # 支持的意识形态
    ideologies = {
        ideology_mercantilist
        ideology_republican
    }

    # 吸引哪些职业
    pop_attraction = {
        pop_type = shopkeepers
        weight = 2.0
    }

    pop_attraction = {
        pop_type = capitalists
        weight = 1.5
    }

    # 支持哪些法律
    law_support = {
        law_mercantilism = strongly_support
        law_free_trade = oppose
        law_interventionism = support
    }

    # 领袖特质倾向
    leader_weight = {
        trait = ambitious
        weight = 2.0
    }
}

```

---

## 23.3 法令（Decree）

### 23.3.1 什么是法令？

**法令**是针对特定州的临时政策，需要消耗权威值。

### 23.3.2 文件位置

```pdx
my_mod/common/decrees/                # 法令定义

```

### 23.3.3 法令定义示例

```pdx
# common/decrees/my_mod_decrees.txt

decree_example = {
    # 纹理
    texture = "gfx/interface/icons/decree_icons/example.dds"

    # 权威成本
    cost = 100

    # 持续时间（月）
    duration = 12

    # 验证条件
    valid = {
        state_owner = {
            country_rank >= rank_value:minor_power
        }
    }

    # 效果
    modifier = {
        building_group_bg_agriculture_throughput_add = 0.2
    }

    # AI使用权重
    ai_weight = {
        value = 10
    }
}

```

---

## 23.4 外交（Diplomacy）

### 23.4.1 外交行动

```pdx
# common/diplomatic_actions/my_mod_actions.txt

diplomatic_action_example = {
    # 类型
    type = economic

    # 允许的条件
    allow = {
        is_subject = no
        relations_with = {
            target = scope:target_country
            value >= 50
        }
    }

    # 效果
    effect = {
        create_trade_agreement = scope:target_country
    }
}

```

---

## 23.5 条约（Treaty）

### 23.5.1 条约定义

```pdx
# common/treaties/my_mod_treaties.txt

treaty_example = {
    # 名称
    name = treaty_example_name

    # 持续时间（-1 = 永久）
    duration = -1

    # 对签署国的效果
    effect = {
        add_modifier = {
            name = treaty_modifier
        }
    }

    # 是否可单方面废除
    can_break = yes

    # 废除的惩罚
    break_effect = {
        add_infamy = 10
    }
}

```

---

## 23.6 战争目标（War Goal）

### 23.6.1 战争目标定义

```pdx
# common/war_goals/my_mod_war_goals.txt

war_goal_example = {
    # 纹理
    texture = "gfx/interface/icons/war_goal_icons/example.dds"

    # 战争目标类型
    type = conquer_state

    # 添加战争目标的必要条件
    possible = {
        any_scope_state = {
            owner = scope:target
        }
    }

    # 效果
    effect = {
        transfer_state = scope:target_state
    }

    # 战争支持度成本
    war_support_cost = 50

    # 恶名
    infamy = 5
}

```

---

## 23.7 势力集团（Power Bloc）

### 23.7.1 势力集团定义

```pdx
# common/power_blocs/my_mod_blocs.txt

power_bloc_example = {
    # 图标
    icon = "gfx/interface/icons/power_bloc_icons/example.dds"

    # 名称
    name = power_bloc_example_name

    # 领袖必要条件
    leader_requirements = {
        country_rank >= rank_value:great_power
    }

    # 成员要求
    member_requirements = {
        relations_with = {
            target = scope:leader
            value >= 30
        }
    }

    # 成员效果
    member_modifier = {
        country_prestige_add = 20
    }
}

```

---

## 23.8🎯 **实战**：创建完整的"江南制造局"系统

### 23.8.1 系统概述

综合本章和前几章的内容，创建一个完整的"江南制造局"系统：

1. **建筑**：江南制造局（第17章）
2. **利益集团**：军工集团
3. **机构**：军事现代化
4. **法令**：军工优先

### 23.8.2 军工集团

**文件**：`common/interest_groups/military_industrial.txt`

```pdx
ig_military_industrial = {
    texture = "gfx/interface/icons/ig_icons/military_industrial.dds"

    priority = 8

    ideologies = {
        ideology_nationalist
        ideology_statist
    }

    # 吸引军人、工程师
    pop_attraction = {
        pop_type = officers
        weight = 3.0
    }

    pop_attraction = {
        pop_type = engineers
        weight = 2.0
    }

    pop_attraction = {
        pop_type = machinists
        weight = 1.5
    }

    # 支持军事法律
    law_support = {
        law_professional_army = strongly_support
        law_interventionism = support
        law_mercantilism = support
    }
}

```

### 23.8.3 军事现代化机构

**文件**：`common/institutions/military_modernization.txt`

```pdx
institution_military_modernization = {
    icon = "gfx/interface/icons/institution_icons/military_modernization.dds"

    background_texture = "gfx/interface/illustrations/institutions/military.dds"

    desc = institution_military_modernization_desc

    # 每级增加军队能力
    modifier = {
        unit_offense_mult = 0.05
        unit_defense_mult = 0.05
    }

    country_modifier = {
        country_bureaucracy_add = -150
    }

    max_level = 5

    unlocking_laws = {
        law_professional_army
        law_mass_conscription
    }
}

```

### 23.8.4 军工优先法令

**文件**：`common/decrees/military_priority.txt`

```pdx
decree_military_priority = {
    texture = "gfx/interface/icons/decree_icons/military_priority.dds"

    cost = 150
    duration = 12

    valid = {
        any_scope_building = {
            OR = {
                is_building_type = building_arms_industry
                is_building_type = building_military_shipyard
            }
        }
    }

    modifier = {
        building_group_bg_military_throughput_add = 0.25
    }

    ai_weight = {
        value = 20
        modifier = {
            factor = 0
            is_at_war = no
        }
    }
}

```

### 23.8.5 本地化

```yaml
l_simp_chinese:
 ig_military_industrial:0 "军工集团"
 ig_military_industrial_desc:0 "由军事官员、工程师和军火商组成的利益集团，主张军事现代化和国家工业化。"

 institution_military_modernization:0 "军事现代化"
 institution_military_modernization_desc:0 "投资于军队现代化，引进先进武器装备和训练方法。"

 decree_military_priority:0 "军工优先"
 decree_military_priority_desc:0 "优先保障军事工业的资源供应，提高武器装备产量。"

```

---

## 本章小结

- **机构**：国家层面的长期建设，需要持续投入
- **利益集团**：代表特定阶层的政治力量
- **法令**：针对特定州的临时政策
- **外交/条约/战争目标**：国际关系的机制
- **实战案例**：完整的"江南制造局"系统整合

---

## 参考

- [Victoria 3 Wiki - Institution modding](https://vic3.paradoxwikis.com/Institution_modding)
- [Victoria 3 Wiki - Interest group modding](https://vic3.paradoxwikis.com/Interest_group_modding)
- [Victoria 3 Wiki - Decree modding](https://vic3.paradoxwikis.com/Decree_modding)
