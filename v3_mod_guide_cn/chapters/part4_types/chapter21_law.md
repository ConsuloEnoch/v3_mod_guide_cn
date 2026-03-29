# 第21章：法律（Law）——添加新法律

> 本章将讲解如何定义新的法律和制度，包括法律组、法律等级和效果。通过学习本章，你将能够创建全新的政治制度。

## 本章目标

完成本章学习后，你将能够：
- 理解法律系统的基本结构
- 创建法律组和法律定义
- 设置法律的激活和废除效果
- 配置法律的前置条件
- 实战添加"君主立宪制"新法律

---

## 21.1 法律基础

### 21.1.1 文件位置

```pdx
my_mod/common/laws/                   # 法律定义
my_mod/common/law_groups/             # 法律组定义

```

### 21.1.2 法律系统结构

```pdx
法律组（Law Group）
    ├── 法律1（Law）
    ├── 法律2（Law）
    └── 法律3（Law）

```

每个法律组内的法律是**互斥**的（只能选一个）。

---

## 21.2 法律组定义

### 21.2.1 基本结构

```pdx
# common/law_groups/my_mod_groups.txt

law_group_governance = {
    # 法律组类型
    law_group_category = power_structure

    # 基础法律（如果没有其他法律激活）
    base_law = law_autocracy

    # 切换法律时的限制
    change_allowed_trigger = {
        custom_tooltip = {
            text = "can_change_governance_law"

            # 不能在内战中修改
            NOR = {
                has_civil_war = yes
                has_revolution = yes
            }
        }
    }

    # 是否可废除
    can_be_abolished = no
}

```

### 21.2.2 法律组类别

| 类别                  | 说明     | 示例             |
| --------------------- | -------- | ---------------- |
| power_structure       | 权力结构 | 政体、权力分配   |
| economy               | 经济     | 贸易、税收       |
| human_rights          | 人权     | 奴隶制、妇女权利 |
| distribution_of_power | 权力分配 | 选举权           |

---

## 21.3 法律定义

### 21.3.1 基本结构

```pdx
# common/laws/my_mod_laws.txt

law_example = {
    # 所属法律组
    group = law_group_governance

    # 纹理
    texture = "gfx/interface/icons/law_icons/example.dds"

    # 解锁条件
    unlocking_laws = {
        law_monarchy
    }

    unlocking_technologies = {
        nationalism
    }

    # 激活效果
    on_activate = {
        add_modifier = {
            name = example_law_modifier
        }
    }

    # 废除效果
    on_deactivate = {
        remove_modifier = example_law_modifier
    }

    # 激活条件（持续检查）
    possible_political_movements = {
        # 可以推动修改该法律的运动
    }

    # AI权重
    ai_will_do = {
        base = 10
    }

    # 推进该法律的社会运动
    pop_support = {
        value = 0

        add = {
            desc = "POP_CAPITALISTS"
            if = {
                limit = { is_pop_type = capitalists }
                value = 0.5
            }
        }
    }
}

```

---

## 21.4🎯 **实战**：添加"君主立宪制"法律

### 21.4.1 设计思路

创建"君主立宪制"，介于绝对君主制和共和制之间：
- 保留君主作为国家元首
- 议会拥有实际立法权
- 平衡传统与现代化
- 历史：英国、日本、德国模式

### 21.4.2 法律组定义

**文件**：`common/law_groups/constitutional_monarchy_group.txt`

```pdx
# 治理方式法律组（修改现有组，添加新法律）
law_group_governance = {
    law_group_category = power_structure

    base_law = law_autocracy

    # 修改限制：不能在战争期间更换政体
    change_allowed_trigger = {
        custom_tooltip = {
            text = "cannot_change_during_war"
            is_at_war = no
        }
    }

    can_be_abolished = no
}

```

### 21.4.3 君主立宪制法律

**文件**：`common/laws/constitutional_monarchy.txt`

```pdx
law_constitutional_monarchy = {
    group = law_group_governance

    texture = "gfx/interface/icons/law_icons/constitutional_monarchy.dds"

    # 名称和描述
    name = law_constitutional_monarchy_name
    desc = law_constitutional_monarchy_desc

    # 解锁条件
    unlocking_laws = {
        law_monarchy          # 必须从君主制转变
    }

    unlocking_technologies = {
        nationalism
        philosophy_idealism
    }

    # 国家类型限制
    unlocking_country_types = {
        recognized
        unrecognized
    }

    # 激活效果
    on_activate = {
        # 给予稳定性
        add_modifier = {
            name = constitutional_stability
            months = -1              # 永久
        }

        # 增加权威
        add_modifier = {
            name = constitutional_authority
            months = -1
        }

        # 获得政治合法性
        add_prestige = 100

        # 触发事件
        trigger_event = {
            id = constitutional_reform.1
            days = 7
        }

        # 记录变量
        set_variable = {
            name = constitutional_monarchy_adopted
            value = 1
        }
    }

    # 废除效果
    on_deactivate = {
        remove_modifier = constitutional_stability
        remove_modifier = constitutional_authority

        add_radicals_in_country = {
            value = 0.02
        }
    }

    # 可推动修改该法律的政治运动
    possible_political_movements = {
        ig_industrialists
        ig_intelligentsia
        ig_landowners
    }

    # AI权重
    ai_will_do = {
        base = 20

        # 工业化国家更倾向
        modifier = {
            add = 20
            gdp_per_capita >= 20
        }

        # 有改革派领导人时
        modifier = {
            add = 30
            ruler = { has_trait = trait_enlightened }
        }

        # 革命压力高时
        modifier = {
            add = 40
            any_political_movement = {
                is_revolutionary = yes
            }
        }
    }

    # 人群支持度
    pop_support = {
        value = 0

        # 资本家支持
        add = {
            desc = "POP_CAPITALISTS"
            if = {
                limit = { is_pop_type = capitalists }
                value = 0.4
            }
        }

        # 知识分子支持
        add = {
            desc = "POP_ACADEMICS"
            if = {
                limit = { is_pop_type = academics }
                value = 0.3
            }
        }

        # 贵族反对
        add = {
            desc = "POP_ARISTOCRATS"
            if = {
                limit = { is_pop_type = aristocrats }
                value = -0.3
            }
        }
    }
}

```

### 21.4.4 修正器

**文件**：`common/modifiers/constitutional_modifiers.txt`

```pdx
constitutional_stability = {
    icon = "gfx/interface/icons/modifiers/modifier_flag_positive.dds"

    # 政治稳定
    country_legitimacy_add = 10

    # 权威略微减少（与专制相比）
    country_authority_add = -20

    # 增加合法性
    country_prestige_add = 25

    # 减少激进派产生
    state_radicals_from_sol_change_mult = -0.05

    good = yes
}

constitutional_authority = {
    icon = "gfx/interface/icons/modifiers/modifier_scroll.dds"

    # 增加政治参与
    country_political_movement_support_add = 0.1

    good = yes
}

```

### 21.4.5 本地化

**文件**：`localization/simp_chinese/constitutional_laws_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 law_constitutional_monarchy:0 "君主立宪制"
 law_constitutional_monarchy_desc:0 "国家元首为世袭君主，但实际权力由宪法和议会限制。这种制度兼顾传统权威与现代治理，能够有效平衡各阶层利益。"
 law_constitutional_monarchy_tooltip:0 "建立君主立宪制政府"

 constitutional_stability:0 "宪政稳定"
 constitutional_stability_desc:0 "君主立宪制带来了政治稳定性和合法性。"

 constitutional_authority:0 "宪政权威"
 constitutional_authority_desc:0 "宪法限制了君主的绝对权力，同时保障了国家的稳定。"

 cannot_change_during_war:0 "战争期间不能更改治理方式"

```

### 21.4.6 历史开局应用

**文件**：`common/history/countries/constitutional_countries.txt`

```pdx
# 英国（已经是君主立宪制）
GBR = {
    activate_law = law_type:law_constitutional_monarchy

    # 补充法律
    activate_law = law_type:law_landed_voting
    activate_law = law_type:law_freedom_of_conscience
}

# 日本（明治维新后可采用）
JAP = {
    # 默认绝对君主制
    # 通过事件或决策转变为君主立宪制
}

# 清朝（假设洋务运动后改革成功）
CHI = {
    # 通过事件链可选择
}

```

---

## 21.5 法律效果详解

### 21.5.1 即时效果（on_activate）

```pdx
on_activate = {
    # 添加修正器
    add_modifier = { ... }

    # 添加威望
    add_prestige = 100

    # 触发事件
    trigger_event = { ... }

    # 设置变量
    set_variable = { ... }

    # 修改关系
    change_relations = { ... }
}

```

### 21.5.2 持续效果（modifier）

```pdx
modifier = {
    country_authority_add = 50
    country_tech_spread_add = 0.1
}

```

### 21.5.3 废除效果（on_deactivate）

```pdx
on_deactivate = {
    # 清理修正器
    remove_modifier = ...

    # 减少威望
    add_prestige = -50

    # 增加激进派
    add_radicals = { ... }
}

```

---

## 本章小结

- **法律组**：定义在`common/law_groups/`，法律互斥
- **法律定义**：在`common/laws/`，包含激活/废除效果
- **关键属性**：group、unlocking_conditions、on_activate、on_deactivate
- **人群支持**：pop_support影响AI和玩家决策
- **实战案例**：完整的"君主立宪制"法律系统

---

## 参考

- [Victoria 3 Wiki - Law modding](https://vic3.paradoxwikis.com/Law_modding)
