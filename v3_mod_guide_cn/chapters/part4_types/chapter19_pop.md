# 第19章：人群（Pop）——修改人口构成

> 本章将讲解人群系统的定义和修改，包括职业类型、人群需求和政治倾向。通过学习本章，你将能够自定义游戏的人口结构。

## 本章目标

完成本章学习后，你将能够：
- 理解人群系统的基本概念
- 修改人群的职业类型和需求
- 调整人群的政治倾向
- 配置人群在地图上的分布
- 实战修改特定州的人群构成

---

## 19.1 人群基础

### 19.1.1 什么是人群（Pop）？

**人群**是维多利亚3的基本人口单位，按以下维度划分：
- **文化**：汉族、英格兰、法兰西等
- **宗教**：佛教、基督教、伊斯兰教等
- **职业**：劳工、工匠、资本家等

### 19.1.2 文件位置

```pdx
my_mod/common/pop_types/              # 职业类型定义
my_mod/common/pop_needs/              # 人群需求
my_mod/common/history/pops/           # 开局人口分布

```

---

## 19.2 职业类型（Pop Types）

### 19.2.1 基本职业类型

| 职业        | 说明             | 典型工作场所 |
| ----------- | ---------------- | ------------ |
| aristocrats | 贵族             | 种植园、政府 |
| capitalists | 资本家           | 工厂、矿业   |
| clergy      | 教士             | 教堂、大学   |
| clerks      | 职员             | 工厂、办公室 |
| engineers   | 工程师           | 工厂、铁路   |
| farmers     | 农民             | 农场         |
| laborers    | 劳工             | 工厂、矿业   |
| machinists  | 机械师           | 工厂         |
| officers    | 军官             | 军队         |
| peasants    | 农民（生存农业） | 生存农场     |
| soldiers    | 士兵             | 军营         |
| shopkeepers | 店主             | 商业中心     |
| slaves      | 奴隶             | 种植园       |

### 19.2.2 职业定义

```pdx
# common/pop_types/my_mod_pops.txt

pop_type_example = {
    # 纹理
    texture = "gfx/interface/icons/pop_types/example.dds"

    # 颜色
    color = hsv{ 0.5 0.7 0.8 }

    # 是否允许失业
    can_be_unemployed = yes

    # 是否可迁徙
    can_migrate = yes

    # 工作资格
    workplace_qualifications = {
        literacy_rate >= 0.2
    }

    # 生活水平需求
    dependent_wage_mult = 0.5
}

```

---

## 19.3 人群需求（Pop Needs）

### 19.3.1 需求层次

人群有不同层次的需求：

1. **基本需求**（生存）
   - 食物：谷物、鱼类
   - 衣物：织物
   - 取暖：木材、煤炭

2. **日常需求**
   - 肉类、水果
   - 家具、陶器
   - 服务

3. **奢侈品需求**
   - 茶叶、咖啡
   - 奢侈品衣物
   - 艺术、娱乐

### 19.3.2 需求定义

```pdx
# common/pop_needs/my_mod_needs.txt

popneed_basic_food = {
    category = staple

    entries = {
        {
            goods = grain
            weight = 1.0
        }
        {
            goods = fish
            weight = 0.8
        }
    }
}

popneed_luxury_drinks = {
    category = luxury

    entries = {
        {
            goods = tea
            weight = 1.0
        }
        {
            goods = coffee
            weight = 1.0
        }
        {
            goods = wine
            weight = 0.8
        }
    }
}

```

---

## 19.4🎯 **实战**：修改特定州的人群构成

### 19.4.1 设计思路

修改广东省的人群构成：
- 增加商人比例（模拟商业繁荣）
- 增加产业工人（模拟早期工业化）
- 减少农民比例（城市化）
- 添加少量外国人群（广州贸易）

### 19.4.2 人群设置文件

**文件**：`common/history/pops/guangdong_pops.txt`

```pdx
# 广东省人群构成

POPS = {
    s:STATE_GUANGDONG = {
        # 汉族主体人口
        pop = {
            culture = han
            religion = mahayana
            size = 18000000

            # 职业分布
            pop_type = laborers
            proportion = 0.35           # 35%劳工
        }

        pop = {
            culture = han
            religion = mahayana
            size = 8000000

            pop_type = farmers
            proportion = 0.25           # 25%农民
        }

        pop = {
            culture = han
            religion = mahayana
            size = 4000000

            pop_type = shopkeepers      # 商人（广东特色）
            proportion = 0.15           # 15%商人
        }

        pop = {
            culture = han
            religion = mahayana
            size = 3000000

            pop_type = machinists       # 产业工人
            proportion = 0.12           # 12%机械师
        }

        pop = {
            culture = han
            religion = mahayana
            size = 2000000

            pop_type = clerks
            proportion = 0.08           # 8%职员
        }

        pop = {
            culture = han
            religion = mahayana
            size = 1000000

            pop_type = capitalists      # 资本家
            proportion = 0.04           # 4%资本家
        }

        pop = {
            culture = han
            religion = mahayana
            size = 300000

            pop_type = aristocrats      # 贵族
            proportion = 0.01           # 1%贵族
        }

        # 外国商人群体（广州贸易）
        pop = {
            culture = british
            religion = protestant
            size = 50000

            pop_type = shopkeepers
        }

        pop = {
            culture = british
            religion = protestant
            size = 20000

            pop_type = capitalists
        }

        pop = {
            culture = yue
            religion = mahayana
            size = 2000000

            pop_type = farmers
        }
    }
}

```

### 19.4.3 职业分布对比

**原版广东省** vs **修改后**：

| 职业   | 原版比例 | 修改后比例 | 变化 |
| ------ | -------- | ---------- | ---- |
| 农民   | 60%      | 25%        | -35% |
| 劳工   | 20%      | 35%        | +15% |
| 商人   | 5%       | 15%        | +10% |
| 机械师 | 2%       | 12%        | +10% |
| 其他   | 13%      | 13%        | 不变 |

### 19.4.4 文化分布

```pdx
# 广东省文化分布
s:STATE_GUANGDONG = {
    # 汉族主体
    pop = {
        culture = han
        size = 23000000            # 95.8%
    }

    # 粤语人群
    pop = {
        culture = yue
        size = 2000000             # 8.3%
    }

    # 客家人
    pop = {
        culture = hakka
        size = 800000              # 3.3%
    }

    # 外国商人
    pop = {
        culture = british
        size = 70000               # 0.3%
    }

    pop = {
        culture = american
        size = 30000               # 0.1%
    }
}

```

---

## 19.5 人群政治倾向

### 19.5.1 职业与利益集团

不同职业倾向支持不同利益集团：

| 职业   | 倾向支持  | 原因     |
| ------ | --------- | -------- |
| 贵族   | 地主      | 土地利益 |
| 资本家 | 工业家    | 资本利益 |
| 劳工   | 工会/小农 | 工人权益 |
| 教士   | 教会      | 宗教权威 |

### 19.5.2 修改政治倾向

```pdx
# common/pop_types/modified_pops.txt

pop_type_capitalists = {
    # 默认定义...

    # 修改政治权重
    political_engagement = {
        # 更倾向支持工业家
        ig_industrialists = 2.0

        # 反对工会
        ig_trade_unions = -1.0
    }
}

```

---

## 19.6 高级人群修改

### 19.6.1 迁移规则

```pdx
# 修改特定人群的迁移倾向
pop_type_laborers = {
    # ...

    # 迁移吸引力
    migration_attraction = {
        state = {
            has_building = building_steel_mills
        }
        value = 1.5
    }
}

```

### 19.6.2 人口增长

```pdx
# 修改人口增长率
state = {
    modifier = {
        state_birth_rate_mult = 0.1     # +10%出生率
    }
}

```

---

## 本章小结

- **职业类型**：在`common/pop_types/`中定义
- **人群需求**：在`common/pop_needs/`中配置
- **开局分布**：在`common/history/pops/`中设置
- **实战案例**：修改广东省人群构成，增加商业人口
- **政治倾向**：不同职业支持不同利益集团

---

## 参考

- [Victoria 3 Wiki - Pop modding](https://vic3.paradoxwikis.com/Pop_modding)
