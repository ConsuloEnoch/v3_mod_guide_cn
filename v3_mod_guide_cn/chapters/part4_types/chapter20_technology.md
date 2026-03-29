# 第20章：科技（Technology）——添加新科技

> 本章将讲解如何定义新的科技，包括科技树结构、解锁效果和前置条件。通过学习本章，你将能够扩展游戏的科技系统。

## 本章目标

完成本章学习后，你将能够：
- 理解科技树的基本结构
- 创建新的科技定义
- 设置科技时代和解锁效果
- 配置科技的前置条件
- 实战添加"近代海军"科技

---

## 20.1 科技基础

### 20.1.1 文件位置

```pdx
my_mod/common/technology/             # 科技定义
my_mod/common/technology/eras/        # 科技时代

```

### 20.1.2 科技时代（Eras）

维多利亚3的科技分为5个时代：

| 时代  | 年份      | 特点           |
| ----- | --------- | -------------- |
| era_1 | 1836-1860 | 早期工业化     |
| era_2 | 1860-1880 | 第一次工业革命 |
| era_3 | 1880-1900 | 第二次工业革命 |
| era_4 | 1900-1920 | 电气时代       |
| era_5 | 1920+     | 现代           |

---

## 20.2 科技定义

### 20.2.1 基本结构

```pdx
# common/technology/my_mod_tech.txt

tech_example = {
    # 纹理
    texture = "gfx/interface/icons/technology_icons/tech_example.dds"

    # 类别
    category = production          # 生产类

    # 时代
    era = era_2

    # 文本
    name = tech_example_name
    desc = tech_example_desc

    # 解锁效果
    modifier = {
        building_group_bg_industry_throughput_add = 0.1
    }

    # 解锁建筑/生产方式
    unlocking_buildings = {
        building_advanced_factory
    }

    unlocking_production_methods = {
        pm_advanced_production
    }

    # 前置科技
    prerequisites = {
        steel
        mechanical_tools
    }

    # 可以解锁的科技（UI显示用）
    can_research = yes
}

```

### 20.2.2 科技类别

| 类别       | 说明 | 示例           |
| ---------- | ---- | -------------- |
| production | 生产 | 钢铁、电力     |
| military   | 军事 | 来复枪、榴弹炮 |
| society    | 社会 | 民族主义、医学 |
| technology | 科技 | 铁路、电报     |

---

## 20.3🎯 **实战**：添加"近代海军"科技

### 20.3.1 设计思路

创建"近代海军"科技，代表19世纪后期海军技术的飞跃：
- 时代：era_3（1880-1900）
- 前置：蒸汽船、钢铁
- 效果：解锁现代战舰、增加海军能力
- 历史：1880年代，无畏舰时代的前夜

### 20.3.2 科技定义

**文件**：`common/technology/modern_navy_tech.txt`

```pdx
tech_modern_navy = {
    texture = "gfx/interface/icons/technology_icons/modern_navy.dds"

    category = military

    era = era_3

    name = tech_modern_navy_name
    desc = tech_modern_navy_desc

    # 海军能力增强
    modifier = {
        # 海军进攻
        unit_navy_offense_mult = 0.15

        # 海军防御
        unit_navy_defense_mult = 0.15

        # 海军士气
        unit_navy_morale_recovery_mult = 0.1

        # 造船速度
        country_shipyards_max_level_add = 2
    }

    # 解锁建筑
    unlocking_buildings = {
        building_dreadnought_dockyards    # 无畏舰船坞
    }

    # 解锁生产方式
    unlocking_production_methods = {
        pm_modern_warship_production
        pm_armored_cruisers
    }

    # 解锁法律
    unlocking_laws = {
        law_type:law_two_year_conscription    # 两年兵役制
    }

    # 前置科技
    prerequisites = {
        steamers              # 蒸汽船
        steel                 # 钢铁
        artillery             # 火炮
    }

    # 未来科技（UI连线显示）
    leads_to = {
        tech_dreadnoughts     # 无畏舰
        tech_submarines       # 潜艇
    }

    can_research = yes
}

```

### 20.3.3 本地化

**文件**：`localization/simp_chinese/navy_tech_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 tech_modern_navy_name:0 "近代海军"
 tech_modern_navy_desc:0 "蒸汽动力、钢铁装甲和现代火炮的结合，开启了海军 warfare 的新纪元。装甲巡洋舰和防护巡洋舰成为海上力量的象征。"

```

### 20.3.4 生产方式

**文件**：`common/production_methods/modern_navy_pm.txt`

```pdx
# 现代战舰生产
pm_modern_warship_production = {
    texture = "gfx/interface/icons/production_method_icons/modern_warships.dds"

    unlocking_technologies = {
        modern_navy
    }

    building_modifiers = {
        workforces = {
            engineers = 500
            machinists = 1000
            laborers = 500
        }
    }

    inputs = {
        steel = 20
        coal = 10
        engines = 5
        artillery = 3
    }

    outputs = {
        warships = 2
        convoys = 5
    }
}

# 装甲巡洋舰
pm_armored_cruisers = {
    texture = "gfx/interface/icons/production_method_icons/armored_cruisers.dds"

    unlocking_technologies = {
        modern_navy
    }

    inputs = {
        steel = 30
        coal = 15
        engines = 8
    }

    outputs = {
        warships = 3
    }
}

```

### 20.3.5 建筑定义

**文件**：`common/buildings/dreadnought_dockyards.txt`

```pdx
building_dreadnought_dockyards = {
    building_group = bg_heavy_industry

    texture = "gfx/interface/icons/building_icons/dreadnought_dockyards.dds"

    required_technology = modern_navy

    required_construction = construction_cost_very_high

    production_method_groups = {
        pmg_base_building
        pmg_modern_shipbuilding
    }

    city_type = city

    levels_per_mesh = 2

    possible = {
        state = {
            is_coastal = yes
        }
    }
}

```

### 20.3.6 历史开局设置

**文件**：`common/history/countries/naval_powers_setup.txt`

```pdx
# 英国（已经研究）
GBR = {
    effect = {
        set_technology = { modern_navy = 1 }
    }
}

# 法国（研究中）
FRA = {
    effect = {
        # 未研究，需要从era_3开始研究
    }
}

# 德国（1880年代开始研究）
PRU = {
    effect = {
        # 通过触发事件在研究
    }
}

```

---

## 20.4 科技树整合

### 20.4.1 前置科技链

```pdx
蒸汽船(steamers)
    ↓
钢铁(steel) + 火炮(artillery)
    ↓
近代海军(modern_navy)
    ↓
无畏舰(dreadnoughts)

```

### 20.4.2 科技效果联动

```pdx
# 近代海军解锁后触发事件
tech_modern_navy = {
    # ...

    on_researched = {
        trigger_event = {
            id = naval_reform.1
            days = 30
        }
    }
}

```

---

## 本章小结

- **科技定义**：在`common/technology/`中定义
- **关键属性**：category、era、modifier、prerequisites
- **解锁效果**：建筑、生产方式、法律
- **科技树**：通过prerequisites和leads_to构建
- **实战案例**：完整的"近代海军"科技系统

---

## 参考

- [Victoria 3 Wiki - Technology modding](https://vic3.paradoxwikis.com/Technology_modding)
