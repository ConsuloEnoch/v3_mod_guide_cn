# 第17章：建筑（Building）——添加新建筑

> 本章将讲解如何定义新的建筑类型，包括生产方式、建筑组和解锁条件。通过学习本章，你将能够为游戏添加自定义建筑。

## 本章目标

完成本章学习后，你将能够：
- 理解建筑定义的基本结构
- 创建新的建筑类型
- 设置生产方式和效率
- 定义解锁条件和限制
- 实战添加"江南制造局"特殊建筑

---

## 17.1 建筑基础

### 17.1.1 文件位置

```pdx
my_mod/common/buildings/              # 建筑类型定义
my_mod/common/building_groups/        # 建筑组定义
my_mod/common/production_methods/     # 生产方式

```

### 17.1.2 建筑类型

| 类型     | 说明         | 示例                       |
| -------- | ------------ | -------------------------- |
| 城市中心 | 提供基础设施 | urban_center               |
| 港口     | 贸易和海军   | port                       |
| 农场     | 农业生产     | wheat_farm, rice_farm      |
| 种植园   | 经济作物     | cotton_plantation          |
| 矿场     | 资源开采     | coal_mine, iron_mine       |
| 工厂     | 工业制造     | steel_mills, textile_mills |
| 军事     | 武器装备     | arms_industry              |
| 政府     | 行政设施     | government_administration  |

---

## 17.2 建筑定义

### 17.2.1 基本结构

```pdx
# common/buildings/my_mod_buildings.txt

building_example = {
    # 建筑组
    building_group = bg_industry

    # 纹理
    texture = "gfx/interface/icons/building_icons/building_example.dds"

    # 所需技术（可选）
    required_technology = steel

    # 建筑类型
    city_type = city                  # 城市类型
    levels_per_mesh = 5               # 每级换一个模型

    # 解锁条件
    unlocking_technologies = {
        steel
        mechanical_tools
    }

    # 生产方式
    production_method_groups = {
        pmg_base_building
        pmg_automation
    }

    # 建筑标志
    possible = {
        # 条件
    }

    # 需要的商品
    required_goods = {
        iron
        coal
    }
}

```

### 17.2.2 建筑组

建筑组定义建筑的类别和规则：

```pdx
# common/building_groups/my_mod_groups.txt

bg_industry = {
    category = urban                  # 城市类别

    # 劳动类型
    labour_type = qualified           # 需要合格劳工

    # 是否可建设
    is_mintable = yes

    # 基础设施需求
    infrastructure_usage_per_level = 1

    # 是否可自动扩展
    auto_expand = yes
}

bg_military = {
    category = government

    # 只有政府可以建设
    is_mintable = no

    # 自动扩展
    auto_expand = no
}

```

---

## 17.3 生产方式

### 17.3.1 什么是生产方式？

**生产方式（Production Method）**决定了建筑如何运作：
- 使用什么技术
- 消耗什么原料
- 产出什么商品
- 雇佣什么职业

### 17.3.2 生产方式定义

```pdx
# common/production_methods/my_mod_pm.txt

pm_steam_power = {
    texture = "gfx/interface/icons/production_method_icons/steam_power.dds"

    # 解锁条件
    unlocking_technologies = {
        steam_engine
    }

    # 建筑修饰
    building_modifiers = {
        workforces = {
            engineers = 200
            laborers = 800
        }
    }

    # 投入（消耗）
    inputs = {
        coal = 5
        iron = 2
    }

    # 产出
    outputs = {
        steel = 10
    }
}

```

### 17.3.3 生产方式组

```pdx
pmg_automation = {
    texture = "gfx/interface/icons/production_method_icons/automation.dds"

    production_methods = {
        pm_hand_tools
        pm_mechanized
        pm_automated
    }

    ai_selection = most_productive
}

```

---

## 17.4🎯 **实战**：添加"江南制造局"

### 17.4.1 设计思路

创建"江南制造局"——清朝洋务运动的代表企业：
- 类型：综合性军工企业
- 产出：武器、钢铁、机械
- 特点：需要政府建造，成本高但效率好
- 历史：1865年李鸿章创办

### 17.4.2 建筑组定义

**文件**：`common/building_groups/jiangnan_groups.txt`

```pdx
# 江南制造局建筑组
bg_jiangnan_arsenal = {
    category = government

    # 政府建筑，普通资本家不能建
    is_mintable = no

    # 不需要基础设施
    infrastructure_usage_per_level = 0

    # 不自动扩展
    auto_expand = no

    # 特殊标志
    lens = government
}

```

### 17.4.3 生产方式

**文件**：`common/production_methods/jiangnan_pm.txt`

```pdx
# 传统手工生产
pm_arsenal_traditional = {
    texture = "gfx/interface/icons/production_method_icons/hand_tools.dds"

    building_modifiers = {
        workforces = {
            machinists = 500
            laborers = 2500
        }
    }

    inputs = {
        iron = 10
        coal = 5
    }

    outputs = {
        small_arms = 5
        artillery = 2
    }
}

# 机械化生产
pm_arsenal_mechanized = {
    texture = "gfx/interface/icons/production_method_icons/mechanized.dds"

    unlocking_technologies = {
        mechanical_tools
        steel
    }

    building_modifiers = {
        workforces = {
            engineers = 300
            machinists = 700
            laborers = 1500
        }
    }

    inputs = {
        iron = 15
        coal = 10
        steel = 5
    }

    outputs = {
        small_arms = 15
        artillery = 8
        steamers = 2
    }
}

# 现代生产
pm_arsenal_modern = {
    texture = "gfx/interface/icons/production_method_icons/automated.dds"

    unlocking_technologies = {
        electricity
        assembly_lines
    }

    building_modifiers = {
        workforces = {
            engineers = 500
            machinists = 1000
            laborers = 1000
        }
    }

    inputs = {
        iron = 20
        coal = 15
        steel = 10
        electricity = 5
    }

    outputs = {
        small_arms = 30
        artillery = 20
        steamers = 5
        railways = 2
    }
}

```

### 17.4.4 建筑定义

**文件**：`common/buildings/jiangnan_arsenal.txt`

```pdx
building_jiangnan_arsenal = {
    building_group = bg_jiangnan_arsenal

    texture = "gfx/interface/icons/building_icons/jiangnan_arsenal.dds"

    # 需要科技
    required_technology = percussion_cap

    # 解锁条件
    unlocking_technologies = {
        percussion_cap
        steel
    }

    # 生产方式组
    production_method_groups = {
        pmg_arsenal_production
    }

    # 建设条件
    possible = {
        owner = {
            OR = {
                this = c:CHI
                this = c:JNP      # 江南共和国也可以
            }
        }

        # 只能在沿海州建设
        state = {
            is_coastal = yes
        }
    }

    # 所需基础设施
    required_construction = construction_cost_medium

    # 特殊标志
    unique = yes                      # 每个国家只能建一个

    # 基础等级
    levels_per_mesh = 1

    # 是否可降级
    can_downsize = yes
}

```

### 17.4.5 生产方式组

```pdx
pmg_arsenal_production = {
    texture = "gfx/interface/icons/production_method_icons/arsenal.dds"

    production_methods = {
        pm_arsenal_traditional
        pm_arsenal_mechanized
        pm_arsenal_modern
    }

    ai_selection = most_productive
}

```

### 17.4.6 本地化

**文件**：`localization/simp_chinese/jiangnan_buildings_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 building_jiangnan_arsenal:0 "江南制造局"
 building_jiangnan_arsenal_desc:0 "洋务运动的代表性企业，生产现代化的武器装备。"

 pm_arsenal_traditional:0 "传统手工生产"
 pm_arsenal_traditional_desc:0 "使用传统手工技艺生产武器，效率较低。"

 pm_arsenal_mechanized:0 "机械化生产"
 pm_arsenal_mechanized_desc:0 "引进西方机器设备，大幅提高生产效率。"

 pm_arsenal_modern:0 "现代化生产"
 pm_arsenal_modern_desc:0 "使用电力和流水线，达到世界先进水平。"

 bg_jiangnan_arsenal:0 "军工企业"
 pmg_arsenal_production:0 "生产方式"

```

### 17.4.7 历史开局设置

**文件**：`common/history/states/jiangnan_setup.txt`

```pdx
STATES = {
    s:STATE_SHANGHAI = {
        create_country = {
            country = c:CHI
        }

        # 1865年李鸿章在上海创办江南制造局
        create_building = {
            building = building_jiangnan_arsenal
            level = 1

            # 设置生产方式
            production_methods = {
                pm_arsenal_traditional    # 1865年还是传统生产
            }
        }
    }
}

```

---

## 17.5 建筑解锁条件

### 17.5.1 科技解锁

```pdx
building_advanced_factory = {
    # 需要特定科技
    required_technology = electricity

    # 解锁科技列表
    unlocking_technologies = {
        electricity
        assembly_lines
    }
}

```

### 17.5.2 法律解锁

```pdx
building_public_school = {
    possible = {
        owner = {
            has_law = law_type:law_public_schools
        }
    }
}

```

### 17.5.3 事件解锁

通过事件添加建筑：

```pdx
event_option = {
    name = my_event.1.a

    effect = {
        capital = {
            add_building = building_special_facility
        }
    }
}

```

---

## 本章小结

- **建筑定义**：在`common/buildings/`中定义
- **建筑组**：决定建筑类别和规则
- **生产方式**：决定建筑的投入产出
- **解锁条件**：科技、法律、事件等
- **实战案例**：完整的"江南制造局"建筑

---

## 参考

- [Victoria 3 Wiki - Building modding](https://vic3.paradoxwikis.com/Building_modding)
