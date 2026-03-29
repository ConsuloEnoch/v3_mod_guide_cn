# 第10章：脚本数值（Script Value）——可复用的计算公式

> 脚本数值允许你定义可复用的数学公式，根据游戏状态动态计算数值。它们是实现复杂算法、平衡Mod和动态调整的关键工具。

## 本章目标

完成本章学习后，你将能够：
- 理解脚本数值的概念和用途
- 创建命名脚本数值和行内脚本数值
- 使用各种运算符进行复杂计算
- 在条件、迭代器中使用脚本数值
- 创建可复用的计算公式库

---

## 10.1 什么是脚本数值？

### 10.1.1 生活化比喻

想象你在经营一家餐厅：

**场景1：动态定价**
- 原材料成本 + 人工成本 + 利润 = 菜品价格
- 每天根据市场行情自动调整

**场景2：员工绩效**
- 销售额 × 提成比例 + 基础工资 = 当月工资
- 每个人的计算方式相同，但数值不同

**场景3：库存管理**
- 预测销量 = 历史平均销量 × 季节系数 × 促销系数
- 复杂的公式，多次使用

在维多利亚3中，**脚本数值（Script Value）**就是这样的"动态计算公式"系统。

### 10.1.2 技术定义

**脚本数值**是可复用的数学公式，可以：
- 根据游戏状态动态计算数值
- 在效果、触发器、变量中使用
- 定义一次，多次使用

**两种形式**：
1. **命名脚本数值**：在`common/script_values/`文件夹中定义，可全局使用
2. **行内脚本数值**：直接在效果或触发器中定义，一次性使用

---

## 10.2 创建脚本数值

### 10.2.1 命名脚本数值

在`common/script_values/`文件夹中创建`.txt`文件：

```pdx
# common/script_values/my_mod_values.txt

# 简单的静态数值
base_construction_cost = 400
minor_construction_cost = 200
major_construction_cost = 800

# 动态计算公式
industrialization_score = {
    value = 0

    # 加上工业建筑数量
    every_scope_state = {
        every_scope_building = {
            limit = {
                OR = {
                    is_building_type = building_textile_mills
                    is_building_type = building_steel_mills
                    is_building_type = building_chemical_plants
                }
            }
            add = 5
        }
    }

    # 加上科技因素
    if = {
        limit = { has_technology_researched = railroad }
        add = 20
    }

    if = {
        limit = { has_technology_researched = steel }
        add = 20
    }
}

# 人均GDP计算
gdp_per_capita = {
    value = gdp                       # 从GDP开始
    divide = total_population         # 除以总人口
    multiply = 1000000                # 转换为"每百万人"
    round = yes                       # 四舍五入
}

```

### 10.2.2 行内脚本数值

直接在效果或触发器中使用：

```pdx
# 在效果中使用行内计算
effect = {
    add_treasury = {
        value = weekly_income         # 从周收入开始
        multiply = 4                  # 乘以4（月收入的4倍）
        min = 100                     # 至少100
        max = 10000                   # 最多10000
    }
}

# 在触发器中使用
trigger = {
    treasury >= {
        value = army_size
        multiply = 10                 # 每个士兵需要10资金
        add = 1000                    # 基础费用
    }
}

```

---

## 10.3 运算符详解

### 10.3.1 基本运算符

| 运算符     | 说明                 | 示例             |
| ---------- | -------------------- | ---------------- |
| `value`    | 设置值（覆盖之前值） | `value = 100`    |
| `add`      | 加法                 | `add = 50`       |
| `subtract` | 减法                 | `subtract = 20`  |
| `multiply` | 乘法                 | `multiply = 1.5` |
| `divide`   | 除法                 | `divide = 2`     |
| `modulo`   | 取余数               | `modulo = 10`    |

**重要**：运算符按顺序执行，**没有优先级**！

```pdx
#⚠️ **注意**：顺序执行，不是先乘除后加减！
example = {
    value = 10
    add = 5           # 10 + 5 = 15
    multiply = 2      # 15 * 2 = 30（不是10*2+5）
    subtract = 3      # 30 - 3 = 27
}

```

### 10.3.2 限制运算符

| 运算符 | 说明       | 示例        |
| ------ | ---------- | ----------- |
| `max`  | 最大值限制 | `max = 100` |
| `min`  | 最小值限制 | `min = 0`   |

```pdx
# 将数值限制在0-100之间
clamped_value = {
    value = raw_value
    min = 0
    max = 100
}

```

### 10.3.3 取整运算符

| 运算符     | 说明           | 示例            |
| ---------- | -------------- | --------------- |
| `round`    | 四舍五入       | `round = yes`   |
| `ceiling`  | 向上取整       | `ceiling = yes` |
| `floor`    | 向下取整       | `floor = yes`   |
| `round_to` | 按指定精度取整 | `round_to = 10` |

```pdx
# 四舍五入到整数
rounded = {
    value = 3.7
    round = yes           # 结果：4
}

# 向上取整
ceiled = {
    value = 3.1
    ceiling = yes         # 结果：4
}

# 向下取整
floored = {
    value = 3.9
    floor = yes           # 结果：3
}

# 四舍五入到10的倍数
round_to_ten = {
    value = 47
    round_to = 10         # 结果：50
}

```

### 10.3.4 随机数运算符

| 运算符          | 说明     | 示例                                    |
| --------------- | -------- | --------------------------------------- |
| `fixed_range`   | 随机小数 | `fixed_range = { min = 0.5 max = 1.5 }` |
| `integer_range` | 随机整数 | `integer_range = { min = 1 max = 10 }`  |

```pdx
# 随机奖励
random_bonus = {
    integer_range = { min = 100 max = 500 }
}

# 随机波动
random_fluctuation = {
    value = 100
    multiply = {
        fixed_range = { min = 0.8 max = 1.2 }
    }
}

```

### 10.3.5 幂运算

```pdx
# 平方
squared = {
    value = 5
    pow = 2                   # 5^2 = 25
}

# 平方根
square_root = {
    value = 25
    pow = 0.5                 # 25^0.5 = 5
}

```

---

## 10.4 条件计算

### 10.4.1 if语句

```pdx
# 根据条件调整数值
tech_boosted_income = {
    value = income

    if = {
        limit = { has_technology_researched = railroad }
        multiply = 1.1                # 有铁路科技，收入+10%
    }

    if = {
        limit = { has_technology_researched = steel }
        multiply = 1.1                # 有钢铁科技，再+10%
    }

    if = {
        limit = { has_technology_researched = electricity }
        multiply = 1.15               # 有电力科技，再+15%
    }
}

```

### 10.4.2 if-else语句

```pdx
# 根据政府形式给予不同加成
government_bonus = {
    if = {
        limit = { has_law = law_type:law_monarchy }
        value = 20                    # 君主制：+20
    }
    else_if = {
        limit = { has_law = law_type:law_presidential }
        value = 15                    # 总统制：+15
    }
    else_if = {
        limit = { has_law = law_type:law_parliamentary }
        value = 10                    # 议会制：+10
    }
    else = {
        value = 5                     # 其他：+5
    }
}

```

---

## 10.5 在迭代器中计算

### 10.5.1 遍历累加

```pdx
# 计算全国总工业产值
total_industrial_output = {
    value = 0

    every_scope_state = {
        every_scope_building = {
            limit = {
                OR = {
                    is_building_type = building_textile_mills
                    is_building_type = building_steel_mills
                    is_building_type = building_chemical_plants
                }
            }
            add = building_level      # 累加每个工业建筑的等级
        }
    }
}

```

### 10.5.2 计算平均值

```pdx
# 计算平均州人口
average_state_population = {
    value = 0

    every_scope_state = {
        add = state_population        # 累加所有州人口
    }

    divide = num_states               # 除以州数量
    round = yes                       # 四舍五入
}

```

### 10.5.3 计数满足条件的对象

```pdx
# 统计沿海州数量
coastal_states_count = {
    value = 0

    every_scope_state = {
        limit = { is_coastal = yes }
        add = 1                       # 每个沿海州加1
    }
}

```

---

## 10.6 使用游戏数值

### 10.6.1 基本游戏数值

```pdx
# 使用游戏内置数值
country_strength = {
    value = army_size               # 从军队规模开始
    add = navy_size                 # 加上海军规模
    multiply = 1.5                  # 加权
    add = gdp                       # 加上GDP
    divide = 1000                   # 缩小数量级
}

```

### 10.6.2 跨作用域引用

```pdx
# 使用其他国家的数值
relative_strength = {
    value = army_size               # 我国军队
    divide = c:GBR.army_size        # 除以英国军队
    multiply = 100                  # 转换为百分比
    round = yes
}

```

### 10.6.3 在特定作用域计算

```pdx
# 在首都计算
capital_development = {
    c:CHI.capital = {               # 在大清首都作用域
        value = num_buildings
        add = state_population
        divide = 10000
    }
}

```

---

## 10.7 临时值保存

### 10.7.1 使用save_temporary_value_as

```pdx
# 复杂的分步计算
industrial_synergy = {
    # 第一步：统计钢厂数量
    value = 0
    every_scope_state = {
        every_scope_building = {
            limit = { is_building_type = building_steel_mills }
            add = building_level
        }
    }
    save_temporary_value_as = steel_mill_count

    # 第二步：统计煤矿数量
    value = 0
    every_scope_state = {
        every_scope_building = {
            limit = { is_building_type = building_coal_mine }
            add = building_level
        }
    }
    save_temporary_value_as = coal_mine_count

    # 第三步：计算协同效应
    value = var:steel_mill_count
    multiply = var:coal_mine_count
    divide = 10
    min = 1                         # 至少1
}

```

---

## 10.8 实战案例

### 案例1：综合国力指数

```pdx
# common/script_values/national_power.txt

# 综合国力指数
comprehensive_national_power = {
    value = 0

    # 经济因素（40%）
    add = {
        value = gdp
        divide = 1000000            # 转换为百万
        multiply = 0.4              # 40%权重
    }

    # 军事因素（30%）
    add = {
        value = army_size
        add = navy_size
        multiply = 0.3              # 30%权重
    }

    # 科技因素（20%）
    add = {
        value = num_researched_technologies
        multiply = 10               # 每项科技10分
        multiply = 0.2              # 20%权重
    }

    # 人口因素（10%）
    add = {
        value = total_population
        divide = 1000000            # 转换为百万
        multiply = 0.1              # 10%权重
    }

    round = yes
}

# 相对国力（相对于列强的百分比）
relative_power_percentage = {
    value = comprehensive_national_power
    divide = {
        c:GBR = {                   # 以英国为基准
            value = comprehensive_national_power
        }
    }
    multiply = 100
    min = 1                         # 至少1%
    round = yes
}

```

### 案例2：战争赔款计算

```pdx
# common/script_values/war_reparations.txt

# 基础战争赔款
base_war_reparations = {
    # 根据GDP计算
    value = gdp
    divide = 10                     # GDP的10%

    # 根据战争持续时间调整
    if = {
        limit = { war_duration < 365 }
        multiply = 0.5              # 少于1年，减半
    }
    else_if = {
        limit = { war_duration < 730 }
        multiply = 0.75             # 1-2年，75%
    }
    else = {
        multiply = 1.0              # 超过2年，全额
    }

    # 根据失败程度调整
    if = {
        limit = { war_score < -50 }
        multiply = 1.5              # 大败，增加50%
    }
    else_if = {
        limit = { war_score < -25 }
        multiply = 1.2              # 中等失败，增加20%
    }

    max = {
        value = treasury            # 不超过国库
        multiply = 2                # 最多2倍国库
    }

    min = 1000                      # 至少1000
    round = yes
}

# 年度赔款（分10年支付）
annual_reparation_payment = {
    value = base_war_reparations
    divide = 10                     # 分10年
    round = yes
}

```

### 案例3：满意度动态计算

```pdx
# common/script_values/pop_satisfaction.txt

# 基础满意度
base_satisfaction = {
    value = 50                      # 基础50分

    # 生活水平影响（±30分）
    add = {
        value = average_sol
        subtract = 10               # 减去基准值
        multiply = 3                # 每点生活水平3分
        max = 30
        min = -30
    }

    # 失业率影响（-20分）
    subtract = {
        value = unemployment_rate
        multiply = 100              # 转换为百分比
        multiply = 0.2              # 每1%失业扣0.2分
        max = 20                    # 最多扣20分
    }

    # 税收影响（-15分）
    subtract = {
        value = tax_rate
        multiply = 15               # 税率影响
        max = 15
    }

    # 战争影响（-10分）
    if = {
        limit = { is_at_war = yes }
        subtract = 10
    }

    # 限制范围
    max = 100
    min = 0
    round = yes
}

# 满意度等级
satisfaction_level = {
    if = {
        limit = { base_satisfaction >= 80 }
        value = 5                   # 非常满意
    }
    else_if = {
        limit = { base_satisfaction >= 60 }
        value = 4                   # 满意
    }
    else_if = {
        limit = { base_satisfaction >= 40 }
        value = 3                   # 一般
    }
    else_if = {
        limit = { base_satisfaction >= 20 }
        value = 2                   # 不满意
    }
    else = {
        value = 1                   # 非常不满意
    }
}

```

### 案例4：建筑成本动态调整

```pdx
# common/script_values/building_costs.txt

# 动态建筑成本
dynamic_construction_cost = {
    value = base_construction_cost  # 基础成本

    # 根据市场钢材价格调整
    multiply = {
        value = market_price_steel
        divide = base_price_steel   # 相对于基础价格
        min = 0.5                   # 最多便宜50%
        max = 2.0                   # 最多贵100%
    }

    # 根据科技调整
    if = {
        limit = { has_technology_researched = steel }
        multiply = 0.9              # 钢铁科技降低成本
    }

    if = {
        limit = { has_technology_researched = concrete }
        multiply = 0.9              # 混凝土科技降低成本
    }

    # 根据经济规模调整（规模效应）
    if = {
        limit = { building_levels > 50 }
        multiply = 0.95             # 大规模建设有折扣
    }

    round = yes
}

# 铁路建设成本
railway_construction_cost = {
    value = dynamic_construction_cost
    multiply = 1.5                  # 铁路比普通建筑贵50%

    # 在地形复杂的州更贵
    if = {
        limit = { has_terrain = mountain }
        multiply = 1.3              # 山地+30%
    }
    else_if = {
        limit = { has_terrain = forest }
        multiply = 1.1              # 森林+10%
    }

    round = yes
}

```

---

## 10.9 @值（At Values）

### 10.9.1 什么是@值？

**@值**是一种简单的常量定义，只能在同一文件中使用：

```pdx
# 在同一文件的顶部定义
@base_cost = 400
@multiplier = 1.5
@max_value = 100

# 在脚本中使用
custom_value = {
    value = @base_cost
    multiply = @multiplier
    max = @max_value
}

```

### 10.9.2 @值的数学运算

```pdx
# 定义时可以进行简单计算
@third = @[1/3]                    # 0.333...
@two_thirds = @[@third*2]          # 0.666...
@pi_approx = @[22/7]               # 3.142...

# 使用复杂表达式
@complex = @[ (100 + 50) * 2 - 25 ]  # 275

```

> ⚠️ **注意**：`@[ ]`中的运算遵循标准数学优先级（先乘除后加减）。

---

## 10.10 常见错误与最佳实践

### 10.10.1 常见错误

#### 错误1：循环依赖

❌ **错误**：

```pdx
# A依赖B，B又依赖A（无限循环）
value_a = {
    value = value_b
}

value_b = {
    value = value_a
}

```

✅ **正确**：

```pdx
# 确保没有循环依赖
value_a = {
    value = army_size               # 只依赖游戏数值
}

value_b = {
    value = value_a                 # B依赖A，但A不依赖B
    add = 10
}

```

#### 错误2：除以零

❌ **错误**：

```pdx
# 如果num_states为0，会出错
average = {
    value = total_population
    divide = num_states
}

```

✅ **正确**：

```pdx
# 确保除数不为零
average = {
    if = {
        limit = { num_states > 0 }
        value = total_population
        divide = num_states
    }
    else = {
        value = 0
    }
}

```

#### 错误3：忘记顺序执行

❌ **错误理解**：

```pdx
# 错误地以为是：(10 + 5) * 2 = 30
# 实际上：10 + 5 = 15, 15 * 2 = 30（这次碰巧正确）
example = {
    value = 10
    add = 5
    multiply = 2
}

```

❌ **实际错误**：

```pdx
# 想要：10 * 2 + 5 = 25
# 实际：10 * 2 = 20, 20 + 5 = 25（这次也碰巧正确）
example = {
    value = 10
    multiply = 2
    add = 5
}

```

✅ **最佳实践**：

```pdx
# 明确计算顺序，必要时使用括号逻辑
# 使用多个步骤或临时变量确保正确

```

### 10.10.2 最佳实践

#### 1. 使用描述性名称

```pdx
# 好
industrialization_score
gdp_per_capita
war_reparation_amount

# 不好
value1
calc2
x

```

#### 2. 添加注释说明

```pdx
# 计算工业化程度
# 基于工业建筑数量和科技水平
industrialization_score = {
    # ...
}

```

#### 3. 模块化设计

```pdx
# 将复杂计算分解为多个小公式
base_cost = 400
tech_multiplier = {
    # 计算科技加成
}
market_adjustment = {
    # 计算市场调整
}

final_cost = {
    value = base_cost
    multiply = tech_multiplier
    multiply = market_adjustment
}

```

#### 4. 测试边界条件

```pdx
# 测试最大值、最小值、零值、负值
# 确保公式在所有情况下都能正常工作

```

---

## 本章小结

- **脚本数值**是可复用的数学公式，支持动态计算
- **两种形式**：命名脚本数值（全局使用）和行内脚本数值（一次性使用）
- **运算符**：value、add、subtract、multiply、divide、max、min、round等
- **条件计算**：使用if/else/elseif根据条件调整公式
- **迭代器**：在公式中遍历对象进行累加或计数
- **@值**：文件内的常量定义，支持简单数学运算
- **最佳实践**：避免循环依赖、防止除零、使用描述性名称

---

## 常见问题

**Q：脚本数值和变量有什么区别？**

A：
- **脚本数值**：公式定义，每次使用时重新计算
- **变量**：存储固定值，可以修改但不会在每次访问时重新计算

**Q：脚本数值可以在哪些地方使用？**

A：大多数接受数值的效果、触发器和变量中都可以使用脚本数值。

**Q：脚本数值有性能影响吗？**

A：如果计算很复杂且在频繁调用的地方使用（如GUI、本地化），可能会影响性能。建议将结果保存到变量中。

**Q：如何调试脚本数值？**

A：
1. 使用`debug_mode`查看计算结果
2. 将结果保存到变量，然后使用`log`输出
3. 简化公式，逐步验证

**Q：可以跨Mod使用脚本数值吗？**

A：可以引用其他Mod定义的脚本数值，但建议避免依赖，使用唯一的命名空间。

---

## 练习建议

1. **基础练习**：创建简单的脚本数值
   - 计算税收收入（基础值 × 税率）
   - 计算军队维护费（士兵数 × 每人费用）

2. **中级练习**：创建条件脚本数值
   - 根据政府形式给予不同加成
   - 根据科技水平调整效率

3. **高级练习**：创建综合计算公式
   - 国家实力指数（经济+军事+科技+人口）
   - 动态建筑成本（基础成本 × 市场因素 × 科技因素）

4. **综合练习**：创建一个完整的经济系统
   - GDP计算公式
   - 人均收入计算
   - 满意度动态计算
   - 税收收入预测

---

> 📖 **下一章预告**：在下一章，我们将进入**第五阶段：内容系统实战**，学习如何制作完整的事件系统。

---

## 参考

- [Victoria 3 Wiki - Script Value](https://vic3.paradoxwikis.com/Script_value)
- 附录E - 变量与脚本值完整参考
