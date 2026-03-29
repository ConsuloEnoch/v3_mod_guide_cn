# 第8章：变量系统（Variable）——存储和计算

> 变量是Mod开发中的数据存储系统，让你能够保存数值、跟踪状态、进行计算。掌握变量系统，你就能实现更复杂、更动态的Mod功能。

## 本章目标

完成本章学习后，你将能够：
- 理解三种变量类型（普通、全局、局部）的区别和用途
- 熟练使用变量进行数学运算（加减乘除、取整、限制范围）
- 使用变量列表存储和管理多个数据
- 在触发器和效果中灵活使用变量
- 实现复杂的动态系统（如进度追踪、计数器、排行榜）

---

## 8.1 什么是变量？

### 8.1.1 生活化比喻

想象你在玩一个RPG游戏：

**经验值（XP）**：
- 你击败敌人 → 获得100XP（添加到变量）
- XP达到1000 → 升级（检查变量值）
- 升级后XP归零（重置变量）

**任务进度**：
- 收集5个苹果 → 任务计数+1（修改变量）
- 计数达到5 → 任务完成（检查变量）

**排行榜**：
- 记录每个玩家的分数（变量列表）
- 按分数排序（列表排序）
- 显示前10名（取列表子集）

在维多利亚3中，**变量**就是这样的数据存储系统，让你能够：
- 保存数值（如改革进度、战争计数）
- 跟踪状态（如是否已触发某事件）
- 进行计算（如人均GDP、满意度百分比）
- 存储对象（如保存多个国家的引用）

### 8.1.2 变量的作用

**场景1：追踪事件链进度**

```pdx
# 洋务运动分5个阶段
# 使用变量记录当前阶段（1-5）
set_variable = {
    name = reform_stage
    value = 1
}

# 每完成一个阶段
change_variable = {
    name = reform_stage
    add = 1
}

# 检查是否完成全部阶段
if = {
    limit = {
        var:reform_stage >= 5
    }
    # 给予最终奖励
}

```

**场景2：计算统计数据**

```pdx
# 计算所有州的平均人口
set_variable = {
    name = total_population
    value = 0
}

every_scope_state = {
    change_variable = {
        name = total_population
        add = state_population
    }
}

# 除以州数量得到平均值
change_variable = {
    name = total_population
    divide = num_states
}

```

**场景3：记录多个国家**

```pdx
# 记录所有与我国有贸易关系的国家
every_country = {
    limit = {
        has_trade_agreement_with = root
    }
    add_to_variable_list = {
        name = trade_partners
        target = this
    }
}

```

---

## 8.2 变量类型详解

维多利亚3有三种变量类型，每种有不同的特性和用途：

### 8.2.1 变量类型对比

| 特性         | 普通变量               | 全局变量             | 局部变量               |
| ------------ | ---------------------- | -------------------- | ---------------------- |
| **作用域**   | 特定对象               | 全局（无作用域）     | 全局（临时）           |
| **持久性**   | 永久保存               | 永久保存             | 临时（事件结束后消失） |
| **引用方式** | `var:name`             | `global_var:name`    | `local_var:name`       |
| **适用场景** | 国家/州/角色的私有数据 | 全局状态、跨国家数据 | 临时计算、中间结果     |

### 8.2.2 普通变量（Regular Variable）

**特点**：绑定到特定对象（国家、州、角色等），永久保存

**使用场景**：
- 国家的改革进度
- 州的发展水平
- 角色的属性值

```pdx
# 在大清设置变量
c:CHI = {
    set_variable = {
        name = modernization_level
        value = 0
    }
}

# 访问变量
c:CHI = {
    if = {
        limit = {
            var:modernization_level >= 50
        }
        # 执行效果
    }
}

```

### 8.2.3 全局变量（Global Variable）

**特点**：不绑定到任何对象，所有国家都能访问，永久保存

**使用场景**：
- 世界范围内的计数器（如世界大战计数）
- 全局状态标记（如"工业革命已开始"）
- 跨国家共享数据

```pdx
# 设置全局变量
set_global_variable = {
    name = world_war_count
    value = 0
}

# 任何国家都能访问
if = {
    limit = {
        global_var:world_war_count >= 3
    }
    # 第三次世界大战相关效果
}

```

### 8.2.4 局部变量（Local Variable）

**特点**：不绑定到任何对象，临时存在（事件/效果执行结束后自动消失）

**使用场景**：
- 临时计算中间值
- 事件链中的临时标记
- 不需要长期保存的数据

```pdx
immediate = {
    # 计算临时值
    set_local_variable = {
        name = temp_calculation
        value = 100
    }

    # 使用临时值
    add_treasury = local_var:temp_calculation

    # 事件结束后自动消失，无需手动清理
}

```

---

## 8.3 变量的基本操作

### 8.3.1 设置变量

```pdx
# 普通变量
set_variable = my_flag                    # 设为1（布尔值）
set_variable = {
    name = my_variable
    value = 100                           # 设为100
}

# 全局变量
set_global_variable = {
    name = global_counter
    value = 0
}

# 局部变量
set_local_variable = {
    name = temp_value
    value = 50
}

```

### 8.3.2 检查变量是否存在

```pdx
# 在触发器中检查
if = {
    limit = {
        has_variable = my_variable        # 检查普通变量
        has_global_variable = global_var  # 检查全局变量
        has_local_variable = local_var    # 检查局部变量
    }
    # 变量存在时执行
}

# 检查变量不存在
if = {
    limit = {
        NOT = { has_variable = my_variable }
    }
    # 变量不存在时执行
}

```

### 8.3.3 移除变量

```pdx
# 普通变量
remove_variable = my_variable

# 全局变量
remove_global_variable = global_counter

# 局部变量（通常不需要手动移除）
remove_local_variable = temp_value

```

---

## 8.4 变量的数学运算

### 8.4.1 基本运算

```pdx
# 加法
change_variable = {
    name = my_var
    add = 10                    # 加10
}

# 减法
change_variable = {
    name = my_var
    subtract = 5                # 减5
}

# 乘法
change_variable = {
    name = my_var
    multiply = 2                # 乘2
}

# 除法
change_variable = {
    name = my_var
    divide = 3                  # 除3
}

```

### 8.4.2 使用变量值进行运算

```pdx
# 将一个变量的值加到另一个变量
change_variable = {
    name = total_score
    add = var:bonus_points      # 加上bonus_points的值
}

# 复杂的链式计算
c:CHI = {
    set_variable = {
        name = base_income
        value = 1000
    }

    # 加10%
    set_variable = {
        name = bonus
        value = var:base_income
    }
    change_variable = {
        name = bonus
        multiply = 0.1
    }

    # total = base + bonus
    set_variable = {
        name = total_income
        value = var:base_income
    }
    change_variable = {
        name = total_income
        add = var:bonus
    }
}

```

### 8.4.3 取整运算

```pdx
# 四舍五入到最接近的整数
round_variable = {
    name = my_var
    value = 1                   # 精度为1（整数）
}

# 四舍五入到最接近的10
round_variable = {
    name = my_var
    value = 10
}

# 四舍五入到小数点后2位
round_variable = {
    name = my_var
    value = 0.01
}

```

### 8.4.4 限制范围（Clamp）

```pdx
# 将变量限制在最小值和最大值之间
clamp_variable = {
    name = satisfaction
    min = 0                     # 最小0
    max = 100                   # 最大100
}

# 确保变量不小于0
clamp_variable = {
    name = debt
    min = 0
}

# 确保变量不超过上限
clamp_variable = {
    name = progress
    max = 100
}

```

---

## 8.5 变量列表（Variable Lists）

### 8.5.1 什么是变量列表？

**变量列表**是存储多个值的容器，可以用来：
- 记录多个国家/州/角色
- 实现排行榜功能
- 批量处理对象

### 8.5.2 添加元素到列表

```pdx
# 普通变量列表（绑定到特定对象）
c:CHI = {
    # 添加国家到列表
    add_to_variable_list = {
        name = allies
        target = c:GBR          # 添加英国
    }

    add_to_variable_list = {
        name = allies
        target = c:FRA          # 添加法国
    }
}

# 全局变量列表
set_global_variable = {
    name = great_powers
    value = 0                   # 初始化为空列表
}

add_to_global_variable_list = {
    name = great_powers
    target = c:GBR
}

add_to_global_variable_list = {
    name = great_powers
    target = c:FRA
}

# 局部变量列表（临时）
set_local_variable = {
    name = temp_list
    value = 0
}

add_to_local_variable_list = {
    name = temp_list
    target = c:RUS
}

```

### 8.5.3 从列表中移除元素

```pdx
# 移除特定元素
remove_list_variable = {
    name = allies
    target = c:GBR              # 移除英国
}

# 清空整个列表
clear_variable_list = allies
clear_global_variable_list = great_powers
clear_local_variable_list = temp_list

```

### 8.5.4 遍历列表

```pdx
# 遍历普通变量列表
c:CHI = {
    every_in_list = {
        variable = allies         # 遍历allies列表

        # 对每个元素执行效果
        add_opinion = {
            target = this         # this代表列表中的当前元素
            value = 10
        }
    }
}

# 遍历全局变量列表
every_in_global_list = {
    variable = great_powers

    add_modifier = {
        name = great_power_bonus
        months = 12
    }
}

# 在触发器中检查列表
trigger = {
    any_in_list = {
        variable = allies
        count >= 2                # 至少有2个盟友
        this = c:GBR              # 其中一个是英国
    }
}

```

### 8.5.5 列表大小和检查

```pdx
# 检查列表大小
trigger = {
    variable_list_size = {
        target = allies
        value >= 3                # 至少有3个元素
    }
}

# 检查元素是否在列表中
trigger = {
    is_target_in_variable_list = {
        name = allies
        target = c:GBR            # 英国是否在盟友列表中
    }
}

```

### 8.5.6 排序列表

```pdx
# 按GDP排序国家列表
sort_global_variable_list = {
    name = countries_by_gdp
    order_by = gdp              # 按GDP排序
    max = 10                    # 只保留前10名
}

# 按人口排序
sort_variable_list = {
    name = my_states
    order_by = state_population
}

```

---

## 8.6 实战案例

### 案例1：改革进度追踪系统

```pdx
# 洋务运动进度追踪
namespace = qing_reform

qing_reform.1 = {
    type = country_event
    title = qing_reform.1.t
    desc = qing_reform.1.d

    trigger = {
        this = c:CHI
        NOT = { has_variable = qing_reform_stage }
    }

    immediate = {
        # 初始化进度系统
        set_variable = {
            name = qing_reform_stage
            value = 1                 # 第1阶段
        }
        set_variable = {
            name = qing_reform_progress
            value = 0                 # 当前阶段进度0%
        }
        set_variable = {
            name = qing_reform_total_investment
            value = 0                 # 总投资
        }
    }

    option = {
        name = qing_reform.1.a

        # 开始投资
        add_treasury = -200
        change_variable = {
            name = qing_reform_total_investment
            add = 200
        }

        # 增加进度
        change_variable = {
            name = qing_reform_progress
            add = 20                  # 每次增加20%
        }

        # 检查阶段完成
        if = {
            limit = {
                var:qing_reform_progress >= 100
            }
            # 阶段完成，进入下一阶段
            change_variable = {
                name = qing_reform_stage
                add = 1
            }
            set_variable = {
                name = qing_reform_progress
                value = 0               # 重置进度
            }

            # 根据阶段给予奖励
            if = {
                limit = {
                    var:qing_reform_stage = 2
                }
                add_technology = railroad
            }
            else_if = {
                limit = {
                    var:qing_reform_stage = 3
                }
                add_technology = steel
            }
            else_if = {
                limit = {
                    var:qing_reform_stage = 4
                }
                add_technology = electricity
            }
            else_if = {
                limit = {
                    var:qing_reform_stage = 5
                }
                # 最终阶段完成
                add_prestige = 500
                remove_variable = qing_reform_stage
                remove_variable = qing_reform_progress
            }
        }

        # 触发下一次投资事件
        trigger_event = {
            id = qing_reform.1
            days = 180
        }
    }
}

```

### 案例2：国家满意度调查系统

```pdx
# 计算全国平均满意度
country_event = {
    immediate = {
        # 重置计数器
        set_variable = {
            name = total_satisfaction
            value = 0
        }
        set_variable = {
            name = state_count
            value = 0
        }

        # 遍历所有州，累加满意度
        every_scope_state = {
            root = {
                change_variable = {
                    name = total_satisfaction
                    add = var:state_satisfaction  # 假设每个州有state_satisfaction变量
                }
                change_variable = {
                    name = state_count
                    add = 1
                }
            }
        }

        # 计算平均值
        set_variable = {
            name = average_satisfaction
            value = var:total_satisfaction
        }
        change_variable = {
            name = average_satisfaction
            divide = var:state_count
        }

        # 四舍五入到整数
        round_variable = {
            name = average_satisfaction
            value = 1
        }

        # 限制在0-100范围
        clamp_variable = {
            name = average_satisfaction
            min = 0
            max = 100
        }

        # 清理临时变量
        remove_variable = total_satisfaction
        remove_variable = state_count
    }
}

```

### 案例3：列强排行榜系统

```pdx
# 维护一个列强排行榜
country_event = {
    type = country_event
    hidden = yes

    # 每年触发一次
    trigger = {
        year >= 1836
    }

    immediate = {
        # 清空旧列表
        clear_global_variable_list = great_powers_ranking

        # 遍历所有国家，按GDP排序
        every_country = {
            limit = {
                country_rank = rank_value:great_power
            }
            add_to_global_variable_list = {
                name = great_powers_ranking
                target = this
            }
        }

        # 按GDP排序
        sort_global_variable_list = {
            name = great_powers_ranking
            order_by = gdp
            max = 8                   # 只保留前8名
        }

        # 给前3名特殊奖励
        every_in_global_list = {
            variable = great_powers_ranking

            if = {
                limit = {
                    # 检查位置
                    list_position = 0           # 第1名
                }
                add_prestige = 100              # 最高奖励
            }
            else_if = {
                limit = {
                    list_position = 1           # 第2名
                }
                add_prestige = 75
            }
            else_if = {
                limit = {
                    list_position = 2           # 第3名
                }
                add_prestige = 50
            }
            else = {
                add_prestige = 25               # 其他列强
            }
        }
    }
}

```

### 案例4：战争损失统计系统

```pdx
# 记录战争中的损失
namespace = war_statistics

war_statistics.1 = {
    type = country_event
    hidden = yes

    # 战争开始时初始化统计
    trigger = {
        is_at_war = yes
        NOT = { has_variable = war_start_date }
    }

    immediate = {
        # 记录开始时间
        set_variable = {
            name = war_start_date
            value = current_date
        }

        # 初始化损失统计
        set_variable = {
            name = casualties_inflicted
            value = 0
        }
        set_variable = {
            name = casualties_suffered
            value = 0
        }
        set_variable = {
            name = battles_won
            value = 0
        }
        set_variable = {
            name = battles_lost
            value = 0
        }
        set_variable = {
            name = war_expenditure
            value = 0
        }
    }
}

# 每次战斗后更新统计
war_statistics.2 = {
    type = country_event
    hidden = yes

    immediate = {
        # 增加战斗胜利计数
        if = {
            limit = { is_battle_winner = yes }
            change_variable = {
                name = battles_won
                add = 1
            }
        }
        else = {
            change_variable = {
                name = battles_lost
                add = 1
            }
        }

        # 增加伤亡统计
        change_variable = {
            name = casualties_inflicted
            add = enemy_casualties
        }
        change_variable = {
            name = casualties_suffered
            add = own_casualties
        }

        # 增加战争开支
        change_variable = {
            name = war_expenditure
            add = weekly_military_spending
        }
    }
}

# 战争结束时生成报告
war_statistics.3 = {
    type = country_event

    trigger = {
        is_at_war = no
        has_variable = war_start_date
    }

    immediate = {
        # 计算战争持续时间
        set_variable = {
            name = war_duration
            value = current_date
        }
        change_variable = {
            name = war_duration
            subtract = var:war_start_date
        }

        # 计算胜率
        set_variable = {
            name = win_ratio
            value = var:battles_won
        }
        change_variable = {
            name = win_ratio
            divide = var:battles_lost
        }

        # 保存统计供后续显示
        save_scope_as = war_stats_scope
    }

    option = {
        name = war_statistics.3.a

        # 清理变量
        remove_variable = war_start_date
        remove_variable = casualties_inflicted
        remove_variable = casualties_suffered
        remove_variable = battles_won
        remove_variable = battles_lost
        remove_variable = war_expenditure
        remove_variable = war_duration
        remove_variable = win_ratio
    }
}

```

---

## 8.7 高级技巧

### 8.7.1 使用变量进行复杂计算

```pdx
# 计算人均GDP
country_event = {
    immediate = {
        # GDP / 人口
        set_variable = {
            name = gdp_per_capita
            value = gdp
        }
        change_variable = {
            name = gdp_per_capita
            divide = total_population
        }

        # 四舍五入到2位小数
        round_variable = {
            name = gdp_per_capita
            value = 0.01
        }
    }
}

```

### 8.7.2 使用变量存储作用域

```pdx
# 记录最强大的利益集团
country_event = {
    immediate = {
        # 初始化
        set_variable = {
            name = strongest_ig_clout
            value = 0
        }

        # 遍历所有IG，找到最强大的
        every_interest_group = {
            if = {
                limit = {
                    ig_clout > var:strongest_ig_clout
                }
                root = {
                    set_variable = {
                        name = strongest_ig_clout
                        value = prev.ig_clout
                    }
                }
                save_scope_as = strongest_ig
            }
        }
    }
}

```

### 8.7.3 变量作为开关

```pdx
# 使用变量作为功能开关
country_event = {
    trigger = {
        global_var:enable_special_features = 1
    }

    # 特殊功能事件
}

# 在Mod配置中设置
country_event = {
    hidden = yes

    immediate = {
        set_global_variable = {
            name = enable_special_features
            value = 1           # 开启特殊功能
        }
    }
}

```

---

## 本章小结

- **三种变量类型**：普通（对象绑定）、全局（全局可见）、局部（临时）
- **基本操作**：设置（set）、检查（has）、移除（remove）
- **数学运算**：加、减、乘、除、取整（round）、限制范围（clamp）
- **变量列表**：存储多个对象，支持添加、移除、遍历、排序
- **应用场景**：进度追踪、数据统计、排行榜、开关控制
- **最佳实践**：及时清理不需要的变量，使用有意义的命名

---

## 常见问题

**Q：变量可以存储什么类型的数据？**

A：变量可以存储：
- 数字（整数或小数）
- 布尔值（yes/no，实际存储为1/0）
- 游戏对象（作为作用域引用）

**Q：变量有大小限制吗？**

A：理论上没有硬性限制，但建议保持合理范围。极大的数值可能会导致计算精度问题。

**Q：如何查看变量的当前值？**

A：
1. 开启调试模式（`-debug_mode`）
2. 使用控制台命令`debug_mode`显示调试信息
3. 在脚本中使用`log`效果输出变量值：

   ```pdx
   log = "Variable value: [var:my_variable]"

   ```

**Q：变量和事件目标（save_scope_as）有什么区别？**

A：
- **变量**：存储数值或作用域，可以修改
- **事件目标**：只存储作用域，用于临时引用，不能修改

**Q：全局变量会保存到存档中吗？**

A：是的，普通变量和全局变量都会保存到存档中。局部变量不会保存。

**Q：两个Mod可以使用相同名称的变量吗？**

A：可以，但可能会导致冲突。建议使用Mod前缀，如`my_mod_variable_name`。

---

## 练习建议

1. **基础练习**：创建一个计数器系统
   - 初始化计数器为0
   - 每次事件触发时+1
   - 达到10时触发特殊效果

2. **中级练习**：创建州发展度系统
   - 为每个州设置发展度变量（0-100）
   - 定期增加发展度
   - 根据发展度给予不同奖励

3. **高级练习**：创建复杂的排行榜系统
   - 记录所有国家的GDP
   - 按GDP排序
   - 给前5名特殊奖励
   - 每年更新一次

4. **综合练习**：创建完整的"现代化指数"系统
   - 科技贡献分
   - 工业贡献分
   - 教育贡献分
   - 综合计算总分
   - 根据总分给予国家等级

---

> 📖 **下一章预告**：在下一章，我们将学习**事件目标（Event Target）**——保存和引用作用域的高级技巧。

---

## 参考

- [Victoria 3 Wiki - Variable](https://vic3.paradoxwikis.com/Variable)
- 附录E - 变量与脚本值完整参考
