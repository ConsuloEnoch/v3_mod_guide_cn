# 第6章：触发器（Trigger）——什么时候发生

> 触发器是维多利亚3的条件判断系统，用于决定事件是否发生、决策是否可用、效果是否执行。掌握触发器，你就能精确控制Mod的逻辑流程。

## 本章目标

完成本章学习后，你将能够：
- 理解触发器的工作原理和重要性
- 熟练使用比较运算符进行数值判断
- 使用逻辑组合（AND、OR、NOT）构建复杂条件
- 掌握常用触发器的分类和使用方法
- 编写复杂的条件判断逻辑

---

## 6.1 什么是触发器？

### 6.1.1 生活化比喻

想象你是一个智能家居系统的程序员，你需要设定各种条件来控制设备：

**场景1**：自动开灯

```pdx
如果（天黑 AND 有人进入房间）{
    开灯
}

```

**场景2**：空调控制

```pdx
如果（温度 > 28°C AND 有人在家）{
    开空调
}

```

**场景3**：安全警报

```pdx
如果（门窗被打开 AND 系统处于警戒模式 AND NOT 主人回家）{
    触发警报
}

```

在维多利亚3中，**触发器（Trigger）**就是这样的条件判断系统。它检查游戏状态，决定"是否允许某事发生"。

### 6.1.2 技术定义

**触发器**是返回"真"（true）或"假"（false）的条件语句：

- **真（true）**：条件满足，允许执行
- **假（false）**：条件不满足，不允许执行

```pdx
# 简单的触发器示例
trigger = {
    treasury > 1000  # 国库是否大于1000？
}

# 结果为真：国库有1500 → 条件通过
# 结果为假：国库有500  → 条件不通过

```

### 6.1.3 触发器的作用

触发器在Mod中的主要用途：

| 用途           | 说明               | 示例                       |
| -------------- | ------------------ | -------------------------- |
| **事件触发**   | 决定事件是否能触发 | 只有大清且国库>1000时触发  |
| **决策可用**   | 决定决策是否可点击 | 只有科技已解锁时可用       |
| **选项显示**   | 决定选项是否显示   | 只有满足条件才显示某个选项 |
| **效果执行**   | 决定效果是否执行   | if语句中的条件判断         |
| **迭代器过滤** | 过滤迭代器目标     | 只处理满足条件的州         |

---

## 6.2 比较运算符

### 6.2.1 基本比较运算符

比较运算符用于比较两个数值或对象：

| 运算符 | 含义     | 示例               | 说明       |
| ------ | -------- | ------------------ | ---------- |
| `=`    | 等于     | `treasury = 1000`  | 严格等于   |
| `!=`   | 不等于   | `is_at_war != yes` | 不等于     |
| `<`    | 小于     | `treasury < 1000`  | 严格小于   |
| `<=`   | 小于等于 | `treasury <= 1000` | 小于或等于 |
| `>`    | 大于     | `treasury > 1000`  | 严格大于   |
| `>=`   | 大于等于 | `treasury >= 1000` | 大于或等于 |

### 6.2.2 数值比较示例

```pdx
# 检查国库资金
trigger = {
    treasury >= 1000        # 国库至少1000
    weekly_income > 100     # 每周收入超过100
    debt < 5000             # 债务少于5000
}

# 检查人口
trigger = {
    total_population > 1000000      # 总人口超过100万
    average_sol >= 15               # 平均生活水平至少15
    literacy_rate > 0.3             # 识字率超过30%
}

# 检查军队
trigger = {
    army_size >= 50                 # 军队规模至少50个营
    navy_size > 20                  # 海军规模超过20艘
    generals >= 5                   # 至少有5个将军
}

```

### 6.2.3 对象比较示例

除了数值，还可以比较游戏对象：

```pdx
# 检查国家身份
trigger = {
    this = c:CHI            # 是否是大清？
    is_subject = no         # 不是附属国？
    country_rank = rank_value:great_power  # 是列强？
}

# 检查法律
trigger = {
    has_law = law_type:law_monarchy       # 有君主制法律？
    NOT = { has_law = law_type:law_slavery }  # 没有奴隶制？
}

# 检查科技
trigger = {
    has_technology_researched = railroad        # 已研究铁路？
    NOT = { has_technology_researched = steel } # 还没研究钢铁？
}

```

> ❓ **解释**：对象比较通常使用 `=` 或 `!=`，返回布尔值（是/否）。

---

## 6.3 逻辑组合

### 6.3.1 AND（与）- 所有条件都必须满足

**AND** 表示"并且"，所有条件都必须为真，整体才为真。

```pdx
# 语法：AND = { 条件1 条件2 条件3 ... }
# 或者简写：{ 条件1 条件2 条件3 ... }（花括号默认就是AND）

trigger = {
    AND = {
        treasury >= 1000        # 国库至少1000
        is_at_war = no          # 不在战争中
        year >= 1860            # 年份至少1860
    }
}

# 简写形式（推荐）
trigger = {
    treasury >= 1000
    is_at_war = no
    year >= 1860
}

```

**逻辑表**：

| 条件1 | 条件2 | 条件3 | AND结果 |
| ----- | ----- | ----- | ------- |
| 真    | 真    | 真    | ✅ 真   |
| 真    | 真    | 假    | ❌ 假   |
| 真    | 假    | 真    | ❌ 假   |
| 假    | 真    | 真    | ❌ 假   |

**生活化比喻**：去餐厅吃饭需要满足：有钱 AND 有食欲 AND 餐厅营业。缺少任何一个都不行。

### 6.3.2 OR（或）- 任一条件满足即可

**OR** 表示"或者"，只要有一个条件为真，整体就为真。

```pdx
# 语法：OR = { 条件1 条件2 条件3 ... }

trigger = {
    OR = {
        country_rank = rank_value:great_power       # 是列强
        country_rank = rank_value:major_power       # 或是次强
        country_rank = rank_value:unrecognized_major_power  # 或是未认可大国
    }
}

```

**逻辑表**：

| 条件1 | 条件2 | 条件3 | OR结果 |
| ----- | ----- | ----- | ------ |
| 真    | 假    | 假    | ✅ 真  |
| 假    | 真    | 假    | ✅ 真  |
| 假    | 假    | 真    | ✅ 真  |
| 假    | 假    | 假    | ❌ 假  |

**生活化比喻**：周末可以去公园 OR 去电影院 OR 在家休息。只要选一个就行。

### 6.3.3 NOT（非）- 条件取反

**NOT** 表示"非"，将条件结果反转。

```pdx
# 语法：NOT = { 条件 }

trigger = {
    NOT = { is_at_war = yes }           # 不在战争中
    NOT = { has_law = law_type:law_slavery }  # 没有奴隶制
    NOT = { is_subject = yes }          # 不是附属国
}

# 简写：使用 !=
trigger = {
    is_at_war != yes           # 同上
    is_subject != yes          # 同上
}

```

**逻辑表**：

| 原条件 | NOT结果 |
| ------ | ------- |
| 真     | ❌ 假   |
| 假     | ✅ 真   |

**生活化比喻**：NOT 饿了 = 不饿。NOT 下雨 = 不下雨。

### 6.3.4 NOR（或非）- 所有条件都不满足

**NOR** 是 OR 的否定，表示"所有条件都不满足"。

```pdx
# 语法：NOR = { 条件1 条件2 条件3 ... }

trigger = {
    NOR = {
        is_at_war = yes             # 不在战争中
        has_revolution = yes        # 没有革命
        has_civil_war = yes         # 没有内战
    }
}
# 意思：既不在战争中，也没有革命，也没有内战

```

### 6.3.5 NAND（与非）- 不是所有条件都满足

**NAND** 是 AND 的否定，表示"不是所有条件都满足"。

```pdx
# 语法：NAND = { 条件1 条件2 条件3 ... }

trigger = {
    NAND = {
        treasury > 10000        # 国库不超过10000
        army_size > 100         # 或军队规模不超过100
        is_at_war = no          # 或不在和平状态
    }
}
# 意思：不同时满足（国库>10000 AND 军队>100 AND 和平）

```

### 6.3.6 复杂逻辑组合

#### 示例1：多重条件判断

```pdx
# 条件：国家是列强或次强，且不在战争中，且年份在1860-1900之间
trigger = {
    OR = {
        country_rank = rank_value:great_power
        country_rank = rank_value:major_power
    }
    is_at_war = no
    year >= 1860
    year <= 1900
}

```

#### 示例2：嵌套逻辑

```pdx
# 条件：(是列强 OR 是次强) AND (不在战争中 OR 战争已持续超过1年)
trigger = {
    OR = {
        country_rank = rank_value:great_power
        country_rank = rank_value:major_power
    }
    OR = {
        is_at_war = no
        war_duration >= 365
    }
}

```

#### 示例3：否定复杂条件

```pdx
# 条件：不是(是附属国 AND 有奴隶制)
# 即：只要不是同时满足"是附属国"和"有奴隶制"即可
trigger = {
    NOT = {
        AND = {
            is_subject = yes
            has_law = law_type:law_slavery
        }
    }
}

# 简写形式（更推荐）
trigger = {
    NAND = {
        is_subject = yes
        has_law = law_type:law_slavery
    }
}

```

#### 示例4：复杂的现实场景

```pdx
# 条件：触发"工业革命"事件
# 需要满足：
# 1. 是列强或次强
# 2. 研究了铁路科技
# 3. 至少有5个工业建筑
# 4. 不在内战中
# 5. 年份在1840-1880之间

trigger = {
    # 1. 列强或次强
    OR = {
        country_rank = rank_value:great_power
        country_rank = rank_value:major_power
    }

    # 2. 已研究铁路
    has_technology_researched = railroad

    # 3. 至少5个工业建筑
    any_scope_state = {
        count >= 5
        any_scope_building = {
            OR = {
                is_building_type = building_textile_mills
                is_building_type = building_steel_mills
                is_building_type = building_chemical_plants
                is_building_type = building_motor_industry
            }
        }
    }

    # 4. 不在内战中
    has_civil_war = no

    # 5. 年份在1840-1880
    year >= 1840
    year <= 1880
}

```

---

## 6.4 常用触发器分类详解

### 6.4.1 国家相关触发器（Country Scope）

#### 基本信息类

```pdx
# 国家身份
trigger = {
    exists = c:CHI              # 国家是否存在
    this = c:CHI                # 是否是大清
    is_subject = yes/no         # 是否是附属国
    is_independent = yes/no     # 是否独立
}

# 国家等级
trigger = {
    country_rank = rank_value:great_power           # 列强
    country_rank = rank_value:major_power           # 次强
    country_rank = rank_value:minor_power           # 小国
    country_rank = rank_value:unrecognized_power    # 未认可国家
}

# 政府形式
trigger = {
    has_law = law_type:law_monarchy         # 君主制
    has_law = law_type:law_presidential     # 总统制
    has_law = law_type:law_parliamentary    # 议会制
    is_democracy = yes/no                   # 是否民主
    is_monarchy = yes/no                    # 是否君主制
}

```

#### 经济类

```pdx
# 国库和收入
trigger = {
    treasury >= 1000                    # 国库资金
    weekly_income > 100                 # 每周收入
    weekly_expenses < 50                # 每周支出
    debt > 0                            # 有债务
}

# GDP和经济规模
trigger = {
    gdp >= 1000000                      # GDP
    gdp_per_capita > 20                 # 人均GDP
    total_population > 1000000          # 总人口
}

# 贸易
trigger = {
    has_trade_route = yes               # 有贸易路线
    is_market_leader = yes              # 是市场领导者
}

```

#### 军事类

```pdx
# 军队规模
trigger = {
    army_size >= 50                     # 陆军规模（营数）
    navy_size >= 20                     # 海军规模（舰船数）
    battalions > 100                    # 营总数
}

# 军事状态
trigger = {
    is_at_war = yes/no                  # 是否在战争中
    is_at_war_with = c:GBR              # 是否与英国交战
    war_duration >= 365                 # 战争持续时间（天）
    has_civil_war = yes/no              # 是否有内战
    has_revolution = yes/no             # 是否有革命
}

# 将领
trigger = {
    num_generals >= 5                   # 将军数量
    num_admirals >= 3                   # 海军将领数量
}

```

#### 科技类

```pdx
# 科技研究
trigger = {
    has_technology_researched = railroad        # 已研究铁路
    has_technology_researched = steel           # 已研究钢铁
    NOT = { has_technology_researched = electricity }  # 未研究电力
}

# 科技时代
trigger = {
    era = era_1     # 第一时代（1836-1860）
    era = era_2     # 第二时代（1860-1880）
    era = era_3     # 第三时代（1880-1900）
}

```

#### 外交类

```pdx
# 外交关系
trigger = {
    has_diplomatic_pact = {
        country = c:GBR
        type = alliance
    }
    has_truce_with = c:FRA              # 与法国有停战协议
    has_rivalry_with = c:RUS            # 与俄罗斯敌对
    relations_with = {
        target = c:GBR
        value >= 50
    }
}

# 势力范围
trigger = {
    is_in_power_bloc = yes              # 是否在势力集团中
    is_power_bloc_leader = yes          # 是否是势力集团领袖
    power_bloc_rank >= 2                # 势力集团排名
}

```

### 6.4.2 州相关触发器（State Scope）

```pdx
# 州的基本信息
trigger = {
    state_population >= 100000          # 州人口
    state_unemployment_rate > 0.1       # 失业率超过10%
    average_sol_in_state >= 10          # 平均生活水平
}

# 建筑
trigger = {
    has_building = building_iron_mine   # 有铁矿
    num_buildings >= 10                 # 建筑数量
    has_active_building = building_steel_mills  # 有活跃的钢厂
}

# 资源
trigger = {
    has_resource = iron                 # 有铁矿资源
    has_resource = coal                 # 有煤炭资源
}

# 地理位置
trigger = {
    is_coastal = yes                    # 是否沿海
    is_incorporated = yes               # 是否已整合
    is_colonial = yes                   # 是否殖民地
}

```

### 6.4.3 人群相关触发器（Pop Scope）

```pdx
# 人群类型
trigger = {
    is_pop_type = laborers              # 是劳工
    is_pop_type = capitalists           # 是资本家
    is_pop_type = aristocrats           # 是贵族
}

# 人口规模
trigger = {
    pop_size >= 10000                   # 人群规模
    pop_growth >= 0.01                  # 人口增长率
}

# 生活水平
trigger = {
    standard_of_living >= 15            # 生活水平
    expected_sol >= 20                  # 期望生活水平
}

# 政治倾向
trigger = {
    pop_supports_political_movement = yes   # 支持政治运动
    is_radical = yes                    # 是否激进
    is_loyalist = yes                   # 是否忠诚
}

```

### 6.4.4 角色相关触发器（Character Scope）

```pdx
# 角色身份
trigger = {
    is_ruler = yes                      # 是统治者
    is_heir = yes                       # 是继承人
    is_general = yes                    # 是将军
    is_admiral = yes                    # 是海军将领
    is_politician = yes                 # 是政治家
}

# 角色属性
trigger = {
    has_trait = trait_ambitious         # 有雄心勃勃特质
    age >= 50                           # 年龄
    popularity >= 50                    # 受欢迎度
}

# 所属关系
trigger = {
    is_in_government = yes              # 在政府中
    is_member_of = ig:ig_armed_forces   # 属于军队利益集团
}

```

### 6.4.5 利益集团相关触发器（Interest Group Scope）

```pdx
# 影响力
trigger = {
    ig_clout >= 0.2                     # 影响力超过20%
    is_powerful = yes                   # 是否有影响力
    is_marginal = no                    # 是否非边缘化
}

# 政治立场
trigger = {
    is_in_government = yes              # 在政府中
    ig_approval >= 0                    # 满意度
    supports_political_movement = yes   # 支持政治运动
}

# 类型
trigger = {
    is_interest_group_type = ig_armed_forces    # 军队利益集团
    is_interest_group_type = ig_industrialists  # 工业家利益集团
}

```

### 6.4.6 外交博弈相关触发器（Diplomatic Play Scope）

```pdx
# 博弈状态
trigger = {
    is_war = yes                        # 已升级为战争
    escalation > 50                     # 升级程度
    has_play_goal = conquer_state       # 战争目标类型
}

# 参与方
trigger = {
    initiator_is = c:CHI                # 发起者是大清
    target_is = c:GBR                   # 目标是英国
    any_scope_play_involved = {
        this = c:FRA                    # 法国参与
    }
}

```

---

## 6.5 特殊触发器

### 6.5.1 随机触发器

用于添加随机性：

```pdx
# 50%概率触发
trigger = {
    random = 0.5
}

# 在条件满足时，有30%概率触发
trigger = {
    treasury > 1000
    random = 0.3
}

```

### 6.5.2 年份和日期触发器

```pdx
# 年份
trigger = {
    year >= 1860                # 年份至少1860
    year <= 1900                # 年份最多1900
    year = 1860                 # 特定年份
}

# 月份
trigger = {
    month >= 6                  # 6月或之后
    month <= 9                  # 9月或之前
}

# 日期范围
trigger = {
    date >= 1860.1.1            # 1860年1月1日之后
    date <= 1900.12.31          # 1900年12月31日之前
}

```

### 6.5.3 变量触发器

```pdx
# 检查变量
trigger = {
    has_variable = my_variable              # 是否有变量
    var:my_variable >= 100                  # 变量值>=100
    is_variable_equal = {
        name = my_variable
        value = 50
    }
}

# 检查全局变量
trigger = {
    has_global_variable = global_var
    global_var:global_var >= 10
}

```

### 6.5.4 迭代器触发器

```pdx
# 检查是否有任何州满足条件
trigger = {
    any_scope_state = {
        state_population > 1000000
    }
}

# 检查是否所有州都满足条件
trigger = {
    any_scope_state = {
        count = all
        has_building = building_railway
    }
}

# 检查至少5个州满足条件
trigger = {
    any_scope_state = {
        count >= 5
        is_incorporated = yes
    }
}

```

---

## 6.6 实战案例

### 案例1："洋务运动"事件触发条件

```pdx
# 洋务运动事件
# 触发条件：
# 1. 是大清
# 2. 年份在1860-1880之间
# 3. 国库至少500
# 4. 不在战争中
# 5. 至少有5个沿海州
# 6. 还没有开始洋务运动（通过变量检查）

trigger = {
    # 1. 必须是大清
    this = c:CHI

    # 2. 年份范围
    year >= 1860
    year <= 1880

    # 3. 经济基础
    treasury >= 500

    # 4. 和平状态
    is_at_war = no

    # 5. 地理条件：至少5个沿海州
    any_scope_state = {
        count >= 5
        is_coastal = yes
    }

    # 6. 只触发一次
    NOT = { has_variable = qing_reform_started }
}

```

### 案例2："工业补贴"决策可用条件

```pdx
# 工业补贴决策
# 可用条件：
# 1. 是列强或次强
# 2. 研究了铁路科技
# 3. 至少有3个工业建筑
# 4. 国库至少1000
# 5. 不在内战中

trigger = {
    # 1. 列强或次强
    OR = {
        country_rank = rank_value:great_power
        country_rank = rank_value:major_power
    }

    # 2. 科技条件
    has_technology_researched = railroad

    # 3. 工业基础
    any_scope_state = {
        count >= 3
        any_scope_building = {
            OR = {
                is_building_type = building_textile_mills
                is_building_type = building_steel_mills
                is_building_type = building_chemical_plants
            }
        }
    }

    # 4. 经济能力
    treasury >= 1000

    # 5. 政治稳定
    has_civil_war = no
    has_revolution = no
}

```

### 案例3：复杂的选项条件

```pdx
# 事件选项：建立军事同盟
# 选项A：与英国结盟（条件较宽松）
option = {
    name = my_event.1.a

    trigger = {
        # 关系良好
        relations_with = {
            target = c:GBR
            value >= 30
        }
    }

    # 效果：建立同盟
    create_diplomatic_pact = {
        country = c:GBR
        type = alliance
    }
}

# 选项B：与法国结盟（条件更严格，但收益更大）
option = {
    name = my_event.1.b

    trigger = {
        # 关系很好
        relations_with = {
            target = c:FRA
            value >= 50
        }
        # 有共同敌人
        any_country = {
            is_rival_of = ROOT
            is_rival_of = c:FRA
        }
    }

    # 效果：建立防御同盟+贸易协议
    create_diplomatic_pact = {
        country = c:FRA
        type = defensive_pact
    }
    create_diplomatic_pact = {
        country = c:FRA
        type = trade_agreement
    }
}

# 选项C：保持中立（总是可用）
option = {
    name = my_event.1.c
    default_option = yes

    # 无trigger = {}，表示总是可用

    add_prestige = 50
}

```

### 案例4：使用if语句的条件效果

```pdx
# 根据条件执行不同效果
effect = {
    # 如果是列强，获得更多威望
    if = {
        limit = {
            country_rank = rank_value:great_power
        }
        add_prestige = 200
    }
    # 如果是次强，获得中等威望
    else_if = {
        limit = {
            country_rank = rank_value:major_power
        }
        add_prestige = 100
    }
    # 其他情况，获得少量威望
    else = {
        add_prestige = 50
    }

    # 如果已经完成工业化，额外奖励
    if = {
        limit = {
            has_variable = industrialization_complete
        }
        add_treasury = 500
    }
}

```

### 案例5：复杂的迭代器过滤

```pdx
# 给所有满足条件的州添加建筑
effect = {
    every_scope_state = {
        limit = {
            # 过滤条件：沿海、已整合、人口超过50万
            is_coastal = yes
            is_incorporated = yes
            state_population >= 500000

            # 且没有港口
            NOT = { has_building = building_port }
        }

        # 效果：添加港口
        add_building = building_port
    }
}

```

---

## 6.7 常见错误与最佳实践

### 6.7.1 常见错误

#### 错误1：忘记作用域

❌ **错误**：

```pdx
trigger = {
    treasury >= 1000    # 错误！没有指定是哪个国家的国库
}

```

✅ **正确**：

```pdx
trigger = {
    c:CHI = {           # 明确指定作用域
        treasury >= 1000
    }
}

```

#### 错误2：混淆 `=` 和 `>`/`<`

❌ **错误**：

```pdx
trigger = {
    treasury > 1000 = yes   # 错误语法
}

```

✅ **正确**：

```pdx
trigger = {
    treasury > 1000         # 正确
}

```

#### 错误3：逻辑错误

❌ **错误**：

```pdx
# 想表达"不在战争中或战争已持续1年以上"
# 实际表达的是"不在战争中且战争已持续1年以上"（不可能同时满足）
trigger = {
    is_at_war = no
    war_duration >= 365
}

```

✅ **正确**：

```pdx
trigger = {
    OR = {
        is_at_war = no
        war_duration >= 365
    }
}

```

#### 错误4：忘记 NOT

❌ **错误**：

```pdx
# 想检查"没有奴隶制"
trigger = {
    has_law = law_type:law_slavery   # 这表示"有奴隶制"
}

```

✅ **正确**：

```pdx
trigger = {
    NOT = { has_law = law_type:law_slavery }
}

```

### 6.7.2 最佳实践

#### 1. 使用注释解释复杂逻辑

```pdx
trigger = {
    # 基本条件：是列强或次强
    OR = {
        country_rank = rank_value:great_power
        country_rank = rank_value:major_power
    }

    # 经济条件：有足够的资金
    treasury >= 1000

    # 政治条件：不在重大冲突中
    NOR = {
        is_at_war = yes
        has_civil_war = yes
        has_revolution = yes
    }
}

```

#### 2. 先检查简单条件，再检查复杂条件

```pdx
trigger = {
    # 先检查简单的布尔条件
    is_at_war = no

    # 再检查数值条件
    treasury >= 1000

    # 最后检查需要遍历的复杂条件
    any_scope_state = {
        count >= 5
        is_coastal = yes
    }
}

```

#### 3. 使用有意义的变量名

```pdx
immediate = {
    # 保存作用域时使用有意义的名称
    save_scope_as = target_country      # 好
    save_scope_as = tc                  # 不好，太简短
    save_scope_as = scope_1             # 不好，无意义
}

```

#### 4. 测试边界条件

```pdx
# 如果条件是 treasury >= 1000
# 测试：
# - treasury = 999（应该失败）
# - treasury = 1000（应该通过）
# - treasury = 1001（应该通过）

```

---

## 本章小结

- **触发器**是条件判断系统，返回真（通过）或假（不通过）
- **比较运算符**：`=`, `!=`, `<`, `<=`, `>`, `>=` 用于比较数值和对象
- **逻辑组合**：
  - `AND`（默认）：所有条件都必须满足
  - `OR`：任一条件满足即可
  - `NOT`：条件取反
  - `NOR`：所有条件都不满足
  - `NAND`：不是所有条件都满足
- **常用触发器分类**：国家、州、人群、角色、利益集团等
- **特殊触发器**：随机、年份、变量、迭代器
- **最佳实践**：使用注释、合理安排检查顺序、测试边界条件

---

## 常见问题

**Q：我可以在触发器中使用效果吗？**

A：不可以。触发器只能检查状态，不能修改状态。要修改状态，使用`immediate`或`option`中的效果。

**Q：为什么我的触发器总是不通过？**

A：检查以下几点：
1. 是否在正确的作用域中？
2. 逻辑是否正确（AND/OR/NOT）？
3. 数值比较是否使用了正确的运算符？
4. 使用`debug_mode`查看详细日志

**Q：如何调试复杂的触发器？**

A：
1. 分解复杂条件，逐个测试
2. 使用`log`效果输出变量值
3. 在控制台使用`test_trigger`命令测试
4. 查看`error.log`文件

**Q：`=` 和 `==` 有什么区别？**

A：在维多利亚3中，只有 `=` 用于比较。没有 `==` 运算符。

**Q：如何检查"介于A和B之间"？**

A：

```pdx
trigger = {
    value >= 10     # 大于等于10
    value <= 20     # 小于等于20
}
# 结果是：10 <= value <= 20

```

---

## 练习建议

1. **逻辑练习**：用真值表验证复杂逻辑
   - 写出 `A AND (B OR C)` 的真值表
   - 写出 `NOT (A AND B)` 等价于什么

2. **条件设计**：为以下场景设计触发器：
   - 只有民主国家且识字率>50%才能触发的事件
   - 只有在和平时期且有至少10个州才能使用的决策
   - 只有与英国关系良好或同为列强才能显示的选项

3. **错误排查**：分析以下触发器的问题：

   ```pdx
   trigger = {
       this = c:CHI
       OR = {
           has_law = law_type:law_monarchy
           has_law = law_type:law_presidential
       }
       is_at_war = no
       treasury > 1000
   }

   ```

4. **实战编写**：编写一个"工业革命"事件的触发器，要求：
   - 年份在1840-1880之间
   - 是列强或次强
   - 已研究铁路
   - 至少有5个工业建筑
   - 不在内战中
   - 只触发一次

---

> 📖 **下一章预告**：在下一章，我们将学习**效果（Effect）**——实际改变游戏的命令系统。

---

## 参考

- [Victoria 3 Wiki - Trigger](https://vic3.paradoxwikis.com/Trigger)
- 附录B - 触发器大全
