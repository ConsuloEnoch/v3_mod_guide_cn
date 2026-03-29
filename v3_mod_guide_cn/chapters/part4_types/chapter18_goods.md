# 第18章：商品（Goods）——添加新商品

> 本章将讲解如何定义新的商品类型，包括商品类别、贸易规则和消费用途。通过学习本章，你将能够扩展游戏的经济系统。

## 本章目标

完成本章学习后，你将能够：
- 理解商品定义的基本结构
- 创建新的商品类型
- 设置商品类别和贸易规则
- 定义商品的消费用途
- 实战添加"茶叶"新商品

---

## 18.1 商品基础

### 18.1.1 文件位置

```pdx
my_mod/common/goods/                  # 商品定义

```

### 18.1.2 商品类别

| 类别        | 说明         | 示例                      |
| ----------- | ------------ | ------------------------- |
| staple      | 主食         | wheat, rice               |
| industrial  | 工业原料     | iron, coal                |
| consumer    | 消费品       | furniture, clothes        |
| luxury      | 奢侈品       | luxury_clothes, porcelain |
| military    | 军用         | small_arms, artillery     |
| staple_food | 主食（特殊） | -                         |

---

## 18.2 商品定义

### 18.2.1 基本结构

```pdx
# common/goods/my_mod_goods.txt

good_example = {
    # 纹理
    texture = "gfx/interface/icons/goods_icons/good_example.dds"

    # 类别
    category = consumer

    # 基础价格
    cost = 30

    # 是否可交易
    traded = yes

    # 是否受市场波动影响
    fixed_price = no

    # 是否可消耗（用于生活水平）
    consumable = yes

    # 贸易方式
    tradeable = yes

    # 是否可以作为原材料
    usable_as_raw_material = no
}

```

### 18.2.2 完整商品定义

```pdx
good_steel = {
    texture = "gfx/interface/icons/goods_icons/steel.dds"

    category = industrial

    cost = 50

    traded = yes

    # 用于建筑生产
    usable_as_raw_material = yes
}

good_luxury_clothes = {
    texture = "gfx/interface/icons/goods_icons/luxury_clothes.dds"

    category = luxury

    cost = 120

    traded = yes
    consumable = yes          # 奢侈品消费影响生活水平
}

```

---

## 18.3🎯 **实战**：添加"茶叶"商品

### 18.3.1 设计思路

茶叶是中国传统出口商品：
- 类别：奢侈品（也是必需品在中国文化中）
- 价格：中等偏高
- 生产：种植园
- 消费：全球需求
- 历史：中国是茶叶的故乡和主要出口国

### 18.3.2 商品定义

**文件**：`common/goods/tea_good.txt`

```pdx
good_tea = {
    texture = "gfx/interface/icons/goods_icons/tea.dds"

    # 作为奢侈品，但在中国有特殊地位
    category = luxury

    # 基础价格：比咖啡略高
    cost = 60

    # 可交易
    traded = yes

    # 可消费（影响生活水平）
    consumable = yes

    # 受市场波动
    fixed_price = no

    # 不是原材料
    usable_as_raw_material = no
}

```

### 18.3.3 本地化

**文件**：`localization/simp_chinese/tea_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 good_tea:0 "茶叶"
 good_tea_desc:0 "中国的传统饮品，在全球享有盛誉。"

```

### 18.3.4 生产方式（生产茶叶）

**文件**：`common/production_methods/tea_production.txt`

```pdx
pm_tea_production = {
    texture = "gfx/interface/icons/production_method_icons/tea_plantation.dds"

    building_modifiers = {
        workforces = {
            laborers = 2000
            farmers = 500
        }
    }

    inputs = {
        fertilizer = 2
    }

    outputs = {
        tea = 8
    }
}

```

### 18.3.5 建筑定义（茶园）

**文件**：`common/buildings/tea_plantation.txt`

```pdx
building_tea_plantation = {
    building_group = bg_plantations

    texture = "gfx/interface/icons/building_icons/tea_plantation.dds"

    required_construction = construction_cost_low

    unlocking_technologies = {
        intensive_agriculture
    }

    production_method_groups = {
        pmg_base_building
        pmg_tea_production
    }

    possible = {
        # 只能在有茶园气候的地区
        OR = {
            state = { has_climate = temperate }
            state = { has_climate = tropical }
        }
    }
}

```

### 18.3.6 商品消费（人群需求）

**文件**：`common/pop_needs/tea_needs.txt`

```pdx
# 为pop_needs添加茶叶
popneed_luxury_drinks = {
    # ...

    entries = {
        # 咖啡
        {
            goods = coffee
            weight = 1.0
        }

        # 茶叶（新增）
        {
            goods = tea
            weight = 1.2          # 茶叶权重略高
        }
    }
}

# 中国人群的特殊需求
popneed_tea_ceremony = {
    category = luxury

    entries = {
        {
            goods = tea
            weight = 2.0          # 茶叶需求更高
        }
        {
            goods = porcelain
            weight = 1.0
        }
    }
}

```

### 18.3.7 历史开局设置

**文件**：`common/history/states/china_tea_production.txt`

```pdx
STATES = {
    # 福建茶叶产区
    s:STATE_FUJIAN = {
        create_country = {
            country = c:CHI
        }

        # 茶园
        create_building = {
            building = building_tea_plantation
            level = 5
        }
    }

    # 浙江茶叶产区
    s:STATE_ZHEJIANG = {
        create_country = {
            country = c:CHI
        }

        create_building = {
            building = building_tea_plantation
            level = 4
        }
    }

    # 安徽茶叶产区
    s:STATE_ANHUI = {
        create_country = {
            country = c:CHI
        }

        create_building = {
            building = building_tea_plantation
            level = 3
        }
    }
}

```

---

## 18.4 商品贸易规则

### 18.4.1 贸易路线

商品可以通过贸易路线进出口：

```pdx
# 在事件中创建贸易路线
effect = {
    create_trade_route = {
        goods = tea
        target_market = c:GBR.market
        level = 5
    }
}

```

### 18.4.2 贸易协议

```pdx
# 在条约中指定商品贸易
treaty_port = {
    # 允许英国进口茶叶
    goods = tea
    target_country = c:GBR
}

```

---

## 18.5 商品与文化

### 18.5.1 文化偏好

不同文化对商品有不同偏好：

```pdx
# 中国文化偏好茶叶
culture_han = {
    # ...

    obsessions = {
        tea           # 对茶叶的执念
        porcelain
        silk
    }
}

```

### 18.5.2 地区特产

```pdx
# 设置地区特产
state_trait_tea_region = {
    icon = "gfx/interface/icons/state_trait_icons/tea.dds"

    modifier = {
        building_group_bg_plantations_throughput_add = 0.2
    }
}

```

---

## 本章小结

- **商品定义**：在`common/goods/`中定义
- **关键属性**：category、cost、traded、consumable
- **生产**：通过建筑和相应的生产方式
- **消费**：添加到pop_needs中
- **实战案例**：完整的"茶叶"商品系统

---

## 参考

- [Victoria 3 Wiki - Goods modding](https://vic3.paradoxwikis.com/Goods_modding)
