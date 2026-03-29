# 第16章：州与省份（State）——修改地理区域

> 本章将讲解如何修改和创建州（State）和州区域（State Region），包括设置资源、人口和建筑。掌握本章内容，你将能够自定义游戏地图。

## 本章目标

完成本章学习后，你将能够：
- 理解州（State）和州区域（State Region）的区别
- 修改州的资源和人口分布
- 创建新的州或调整州边界
- 配置可耕地区域和建筑位置
- 实战修改广东省的资源分布

---

## 16.1 州的基本概念

### 16.1.1 州的层级

维多利亚3中有三个地理层级：

```pdx
州区域（State Region）
    └── 州（State）
            └── 省份（Province）

```

- **州区域**：逻辑区域，定义资源和基本属性
- **州**：实际游戏单位，属于特定国家
- **省份**：最小地图单位，多个省份组成州

### 16.1.2 文件位置

```pdx
my_mod/common/strategic_regions/      # 州区域定义
my_mod/map_data/state_regions/        # 州区域地图数据
my_mod/common/history/states/         # 州历史设置

```

---

## 16.2 州区域定义

### 16.2.1 基本结构

```pdx
# common/strategic_regions/my_mod_regions.txt

STATE_EXAMPLE = {
    id = 1                            # 唯一ID
    subsistence_building = building_subsistence_farms

    provinces = {                     # 包含的省份
        x123456 x234567 x345678
    }

    resources = {                     # 资源储量
        resource = iron
        amount = 20
    }

    arable_land = 100                 # 可耕地区域
    arable_resources = {              # 可耕地资源类型
        bg_wheat_farms
        bg_rye_farms
    }

    capped_resources = {              # 有限资源
        resource = coal
        amount = 10
    }

    naval_exit = 1234                 # 海军出口（港口）
}

```

### 16.2.2 资源设置

```pdx
STATE_GUANGDONG = {
    id = 50

    # 可耕地资源
    arable_land = 80
    arable_resources = {
        bg_rice_farms
        bg_silk_plantations
        bg_tea_plantations
    }

    # 自然资源（无限开采）
    resources = {
        resource = iron
        amount = 15
    }
    resources = {
        resource = coal
        amount = 10
    }

    # 有限资源（开采完就没了）
    capped_resources = {
        resource = oil
        amount = 5
    }

    # 海军出口（港口省份ID）
    naval_exit = 345678
}

```

### 16.2.3 可耕地区域

```pdx
STATE_SICHUAN = {
    id = 60

    # 可耕地区域数量
    arable_land = 120

    # 可种植类型
    arable_resources = {
        bg_wheat_farms
        bg_rice_farms
        bg_maize_farms
    }

    # 如果为空，则只能建生存农场
}

```

---

## 16.3 州历史设置

### 16.3.1 开局州设置

```pdx
# common/history/states/my_mod_state_setup.txt

STATES = {
    s:STATE_GUANGDONG = {
        # 所有者
        create_country = {
            country = c:CHI
        }

        # 人口设置
        set_population = {
            culture = han
            size = 20000000
        }

        # 初始建筑
        create_building = {
            building = building_rice_farm
            level = 5
        }

        create_building = {
            building = building_port
            level = 2
        }
    }
}

```

### 16.3.2 多文化人口

```pdx
s:STATE_XINJIANG = {
    create_country = {
        country = c:CHI
    }

    # 汉族
    set_population = {
        culture = han
        size = 3000000
    }

    # 维吾尔族
    set_population = {
        culture = uyghur
        size = 2000000
    }

    # 回族
    set_population = {
        culture = hui
        size = 500000
    }
}

```

### 16.3.3 初始建筑

```pdx
s:STATE_SHANDONG = {
    create_country = {
        country = c:CHI
    }

    # 农业建筑
    create_building = {
        building = building_wheat_farm
        level = 4
    }

    # 工业建筑
    create_building = {
        building = building_coal_mine
        level = 3
    }

    # 城市建筑
    create_building = {
        building = building_urban_center
        level = 2
    }

    # 港口
    create_building = {
        building = building_port
        level = 1
    }
}

```

---

## 16.4 修改广东省实战

### 16.4.1 设计思路

修改广东省，使其：
- 增加铁矿资源（模拟广东铁矿）
- 增加人口
- 添加现代工业建筑
- 设置可耕地区域

### 16.4.2 州区域修改

**文件**：`common/strategic_regions/modified_guangdong.txt`

```pdx
# 修改广东省
STATE_GUANGDONG = {
    id = 50

    subsistence_building = building_subsistence_farms

    provinces = {
        # 原有省份
        x345678 x456789 x567890
        # 新增省份（假设从广西划入）
        x678901
    }

    # 增加可耕地区域
    arable_land = 100        # 原为80，增加20
    arable_resources = {
        bg_rice_farms
        bg_silk_plantations
        bg_tea_plantations
        bg_tobacco_plantations    # 新增：烟草
    }

    # 增加铁矿资源
    resources = {
        resource = iron
        amount = 25              # 原为15，增加10
    }

    # 增加煤炭资源
    resources = {
        resource = coal
        amount = 15              # 原为10，增加5
    }

    # 新增：石油资源
    capped_resources = {
        resource = oil
        amount = 8               # 有限资源
    }

    naval_exit = 345678
}

```

### 16.4.3 历史设置修改

**文件**：`common/history/states/guangdong_setup.txt`

```pdx
STATES = {
    s:STATE_GUANGDONG = {
        create_country = {
            country = c:CHI
        }

        # 增加人口（原为2000万，增加到2500万）
        set_population = {
            culture = han
            size = 25000000
        }

        # 少数民族：客家人
        set_population = {
            culture = hakka
            size = 3000000
        }

        # 农业建筑
        create_building = {
            building = building_rice_farm
            level = 6              # 增加1级
        }

        create_building = {
            building = building_silk_plantation
            level = 3
        }

        # 工业建筑（新增）
        create_building = {
            building = building_iron_mine
            level = 2
        }

        create_building = {
            building = building_steel_mills
            level = 1
        }

        create_building = {
            building = building_textile_mills
            level = 2
        }

        # 基础设施
        create_building = {
            building = building_port
            level = 3              # 增加1级
        }

        create_building = {
            building = building_urban_center
            level = 3
        }
    }
}

```

### 16.4.4 创建新州：海南岛

**州区域定义**：

```pdx
# common/strategic_regions/hainan.txt

STATE_HAINAN = {
    id = 999                          # 新ID，确保唯一

    subsistence_building = building_subsistence_farms

    provinces = {
        x999001 x999002 x999003      # 新省份ID
    }

    # 可耕地
    arable_land = 30
    arable_resources = {
        bg_rice_farms
        bg_coffee_plantations        # 热带作物
        bg_sugar_plantations
    }

    # 资源
    resources = {
        resource = iron
        amount = 5
    }

    naval_exit = 999001
}

```

**历史设置**：

```pdx
# common/history/states/hainan_setup.txt

s:STATE_HAINAN = {
    create_country = {
        country = c:CHI
    }

    set_population = {
        culture = han
        size = 2000000
    }

    set_population = {
        culture = li
        size = 500000
    }

    create_building = {
        building = building_rice_farm
        level = 2
    }

    create_building = {
        building = building_port
        level = 1
    }
}

```

---

## 16.5 地图修改基础

### 16.5.1 省份数据

```pdx
map_data/provinces.png        # 省份颜色图
map_data/heightmap.png        # 高度图
map_data/rivers.png           # 河流图
map_data/trees.png            # 植被图

```

> ⚠️ **警告**：修改地图数据需要图像编辑软件和地图编辑器，超出本章范围。

### 16.5.2 州边界调整

调整州边界需要修改：
1. `state_regions/`中的省份列表
2. `provinces.png`中的颜色分配
3. 高度图和河流图

---

## 16.6 常见错误

### 16.6.1 ID冲突

❌ **错误**：州ID重复

✅ **解决**：确保每个州有唯一的ID

### 16.6.2 省份不存在

❌ **错误**：引用了不存在的省份ID

✅ **解决**：检查`provinces.png`中是否存在该颜色

### 16.6.3 资源数值不合理

❌ **错误**：资源数量过大或过小

✅ **解决**：参考原版游戏数值，保持平衡

---

## 本章小结

- **州区域**：定义在`common/strategic_regions/`
- **关键属性**：id、provinces、resources、arable_land
- **历史设置**：在`common/history/states/`中配置人口和建筑
- **实战**：修改广东省资源，创建海南岛
- **注意**：地图修改需要图像编辑工具

---

## 参考

- [Victoria 3 Wiki - State modding](https://vic3.paradoxwikis.com/State_modding)
