# 第二十八章：On Actions

## 本章目标

学习本章后，你将能够：
- 理解On Actions的工作原理
- 使用常用On Actions触发效果
- 创建自定义On Actions
- 区分On Actions与常规事件
- 掌握On Actions的最佳实践

---

## 概念讲解：On Actions是什么？

### 比喻：自动触发器

想象你家中有这些自动化设备：
- **人体感应灯** = 检测到人（条件）→ 开灯（动作）
- **自动浇水系统** = 土壤干燥（条件）→ 浇水（动作）
- **闹钟** = 到达时间（条件）→ 响铃（动作）

On Actions就是这样的自动触发器：
- **特定条件发生时** → **自动执行预设动作**

### 与常规事件的区别

| 特性     | 常规事件          | On Actions         |
| -------- | ----------------- | ------------------ |
| 触发方式 | 手动/特定条件检查 | 系统自动调用       |
| 触发时机 | 玩家操作时        | 游戏引擎层面       |
| 频率     | 按需触发          | 固定时间点         |
| 用途     | 叙事、决策        | 系统逻辑、数据更新 |

**比喻**：
- 常规事件 = 你主动打开冰箱拿饮料
- On Actions = 冰箱自动检测温度并启动制冷

---

## 28.1 On Actions基础

### 28.1.1 文件位置

```pdx
my_mod/
└── common/
    └── on_actions/
        ├── 00_my_on_actions.txt
        └── 01_monthly_updates.txt

```

### 28.1.2 基本语法

```pdx
# 当某个On Action被触发时执行
on_action_name = {
    effect = {
        # 要执行的效果
    }
}

```

### 28.1.3 简单示例

```pdx
# 每月1日执行
on_monthly_pulse = {
    effect = {
        # 给每个国家增加一些金币
        every_country = {
            add_treasury = 100
        }
    }
}

```

---

## 28.2 常用On Actions

### 28.2.1 时间类On Actions

| On Action          | 触发时机 | 使用场景           |
| ------------------ | -------- | ------------------ |
| `on_daily_pulse`   | 每天     | 高频更新、实时计算 |
| `on_weekly_pulse`  | 每周     | 常规数据更新       |
| `on_monthly_pulse` | 每月     | 月度统计、AI决策   |
| `on_yearly_pulse`  | 每年     | 年度报告、长期效果 |
| `on_decade_pulse`  | 每十年   | 长期趋势、时代变迁 |

**示例：月度税收检查**

```pdx
on_monthly_pulse = {
    effect = {
        # 给玩家国家增加提示
        if = {
            limit = {
                is_player = yes
            }

            # 如果国库低于1000，显示提示
            if = {
                limit = {
                    gold < 1000
                }
                post_notification = low_treasury_warning
            }
        }
    }
}

```

### 28.2.2 国家类On Actions

| On Action                           | 触发时机     | 使用场景     |
| ----------------------------------- | ------------ | ------------ |
| `on_country_formed`                 | 国家成立时   | 初始化新国家 |
| `on_country_released`               | 国家被释放时 | 附庸国设置   |
| `on_country_annexed`                | 国家被吞并时 | 清理数据     |
| `on_country_government_type_change` | 政体改变时   | 政体相关效果 |
| `on_country_rank_change`            | 等级改变时   | 地位相关效果 |

**示例：新国家成立奖励**

```pdx
on_country_formed = {
    effect = {
        # 给新成立的国家一些初始资金
        add_treasury = 10000

        # 如果是江南共和国，添加特殊修正器
        if = {
            limit = {
                country_has_primary_culture = cu:han
                capital = state:STATE_JIANGNAN
            }
            add_modifier = {
                name = new_jiangnan_republic
                months = 12
            }
        }
    }
}

```

### 28.2.3 战争与外交类

| On Action             | 触发时机       | 使用场景   |
| --------------------- | -------------- | ---------- |
| `on_war_begins`       | 战争开始时     | 战争初始化 |
| `on_war_ends`         | 战争结束时     | 战后处理   |
| `on_diplo_play_start` | 外交博弈开始时 | 博弈设置   |
| `on_diplo_play_end`   | 外交博弈结束时 | 结果处理   |
| `on_treaty_signed`    | 条约签署时     | 条约效果   |

**示例：战争开始时的动员**

```pdx
on_war_begins = {
    effect = {
        # 记录战争开始时间
        set_variable = {
            name = war_start_date
            value = current_date
        }

        # 如果是对外战争，增加民族主义
        if = {
            limit = {
                is_defender = yes
            }
            add_modifier = {
                name = defending_homeland
                months = 6
            }
        }
    }
}

```

### 28.2.4 建筑与科技类

| On Action                  | 触发时机       | 使用场景 |
| -------------------------- | -------------- | -------- |
| `on_building_built`        | 建筑建成时     | 建筑奖励 |
| `on_building_destroyed`    | 建筑被毁时     | 损失处理 |
| `on_technology_researched` | 科技研究完成时 | 科技效果 |
| `on_law_enacted`           | 法律通过时     | 法律效果 |
| `on_law_repealed`          | 法律废除时     | 清理效果 |

**示例：特殊建筑完工奖励**

```pdx
on_building_built = {
    effect = {
        # 检查是否是江南制造局
        if = {
            limit = {
                building = building_jiangnan_arsenal
            }

            # 触发特殊事件
            trigger_event = {
                id = jiangnan_arsenal.1
            }

            # 添加修正器
            add_modifier = {
                name = jiangnan_arsenal_built
                months = -1  # 永久
            }
        }
    }
}

```

### 28.2.5 人群与角色类

| On Action                  | 触发时机       | 使用场景     |
| -------------------------- | -------------- | ------------ |
| `on_pop_growth`            | 人口增长时     | 人口相关效果 |
| `on_pop_migration`         | 人口迁移时     | 迁移处理     |
| `on_character_death`       | 角色死亡时     | 继承、哀悼   |
| `on_character_birth`       | 角色出生时     | 庆祝、记录   |
| `on_character_role_change` | 角色职位改变时 | 职位相关效果 |

---

## 28.3 带条件的On Actions

### 28.3.1 添加触发条件

On Actions可以添加条件，只在满足条件时执行：

```pdx
on_monthly_pulse = {
    # 条件：只有玩家国家触发
    trigger = {
        is_player = yes
    }

    effect = {
        # 玩家专属的月度效果
        add_treasury = 500
    }
}

```

### 28.3.2 多重条件

```pdx
on_yearly_pulse = {
    trigger = {
        # 必须是列强
        is_great_power = yes

        # 必须有殖民地
        any_scope_state = {
            is_colonial = yes
        }

        # 年份必须是1860年后
        year >= 1860
    }

    effect = {
        # 给予殖民奖励
        add_modifier = {
            name = colonial_empire
            months = 12
        }
    }
}

```

---

## 28.4 高级用法

### 28.4.1 随机触发

```pdx
on_monthly_pulse = {
    effect = {
        # 每月有10%概率触发
        random = {
            chance = 10

            # 随机事件
            trigger_event = {
                id = random_event.1
            }
        }
    }
}

```

### 28.4.2 计数器和追踪

```pdx
on_monthly_pulse = {
    effect = {
        # 追踪连续和平月数
        if = {
            limit = {
                is_at_war = no
            }

            change_variable = {
                name = peace_months
                add = 1
            }
        }
        else = {
            set_variable = {
                name = peace_months
                value = 0
            }
        }

        # 如果和平超过24个月，给予奖励
        if = {
            limit = {
                var:peace_months >= 24
            }

            add_modifier = {
                name = prolonged_peace
                months = 12
            }
        }
    }
}

```

### 28.4.3 跨作用域操作

```pdx
on_war_begins = {
    effect = {
        # 记录战争双方
        set_global_variable = {
            name = current_war_attacker
            value = war_attacker
        }

        set_global_variable = {
            name = current_war_defender
            value = war_defender
        }

        # 通知所有列强
        every_country = {
            limit = {
                is_great_power = yes
            }

            post_notification = great_power_war_notification
        }
    }
}

```

---

## 28.5🎯 **实战**：江南Mod的On Actions

### 28.5.1 洋务运动进度追踪

```pdx
# 文件：common/on_actions/jiangnan_on_actions.txt

# 每月检查洋务运动进度
on_monthly_pulse = {
    effect = {
        # 只对有洋务运动日志的国家生效
        every_country = {
            limit = {
                has_journal_entry = je_self_strengthening
            }

            # 检查工业建筑数量
            set_variable = {
                name = industrial_building_count
                value = 0
            }

            every_scope_state = {
                every_scope_building = {
                    limit = {
                        OR = {
                            is_building_type = building_textile_mills
                            is_building_type = building_steel_mills
                            is_building_type = building_chemical_plants
                            is_building_type = building_tooling_workshops
                        }
                    }

                    root = {
                        change_variable = {
                            name = industrial_building_count
                            add = 1
                        }
                    }
                }
            }

            # 如果达到目标，推进日志进度
            if = {
                limit = {
                    var:industrial_building_count >= 10
                }

                add_journal_entry_progress = {
                    journal_entry = je_self_strengthening
                    amount = 5
                }
            }
        }
    }
}

```

### 28.5.2 新国家检查

```pdx
# 国家成立时的初始化
on_country_formed = {
    effect = {
        # 江南共和国特殊处理
        if = {
            limit = {
                country_has_primary_culture = cu:han
                any_scope_state = {
                    state_region = s:STATE_JIANGNAN
                }
            }

            # 添加初始修正器
            add_modifier = {
                name = jiangnan_republic_founded
                months = 24
            }

            # 设置初始关系
            every_country = {
                limit = {
                    country_has_primary_culture = cu:manchu
                }

                change_relations = {
                    country = prev
                    value = -50
                }
            }

            # 触发建国事件
            trigger_event = {
                id = jiangnan_founding.1
            }
        }
    }
}

```

### 28.5.3 建筑完工追踪

```pdx
# 特殊建筑完工处理
on_building_built = {
    effect = {
        # 江南制造局完工
        if = {
            limit = {
                building = building_jiangnan_arsenal
            }

            # 触发完工事件
            owner = {
                trigger_event = {
                    id = jiangnan_arsenal.1
                }

                # 添加永久修正器
                add_modifier = {
                    name = jiangnan_arsenal_operational
                    months = -1
                }

                # 记录成就
                set_variable = {
                    name = has_jiangnan_arsenal
                    value = yes
                }
            }
        }

        # 洋务学院完工
        if = {
            limit = {
                building = building_self_strengthening_academy
            }

            owner = {
                add_modifier = {
                    name = self_strengthening_academy_built
                    months = -1
                }

                # 增加科技进度
                add_technology_progress = {
                    technology = tech_modern_naval
                    progress = 1000
                }
            }
        }
    }
}

```

### 28.5.4 年度统计

```pdx
# 年度综合统计
on_yearly_pulse = {
    effect = {
        every_country = {
            limit = {
                is_player = yes
            }

            # 计算年度GDP增长
            set_variable = {
                name = gdp_growth
                value = gdp
            }

            change_variable = {
                name = gdp_growth
                subtract = var:last_year_gdp
            }

            divide_variable = {
                name = gdp_growth
                divide = var:last_year_gdp
            }

            multiply_variable = {
                name = gdp_growth
                multiply = 100
            }

            # 记录今年GDP
            set_variable = {
                name = last_year_gdp
                value = gdp
            }

            # 如果增长超过5%，给予奖励
            if = {
                limit = {
                    var:gdp_growth > 5
                }

                add_modifier = {
                    name = economic_boom
                    months = 12
                }
            }
        }
    }
}

```

---

## 28.6 On Actions最佳实践

### 28.6.1 性能考虑

❌ **避免**：
- 在`on_daily_pulse`中执行复杂计算
- 频繁遍历所有国家/州/建筑
- 不必要的随机检查

✅ **推荐**：
- 使用`on_monthly_pulse`或更低频率
- 添加触发条件限制范围
- 使用变量缓存计算结果

### 28.6.2 调试技巧

```pdx
on_monthly_pulse = {
    effect = {
        # 调试输出
        if = {
            limit = {
                is_player = yes
            }

            # 使用调试日志
            debug_log = "Monthly pulse triggered for [Country.GetName]"
            debug_log = "Variable value: [Country.GetVariable('my_var')]"
        }
    }
}

```

### 28.6.3 模块化设计

```pdx
# 将复杂逻辑拆分为多个文件

# 00_jiangnan_core.txt - 核心功能
on_monthly_pulse = {
    effect = {
        every_country = {
            limit = {
                has_variable = jiangnan_active
            }

            # 调用效果文件
            jiangnan_monthly_update = yes
        }
    }
}

# 在 scripted_effects 中定义具体逻辑

```

---

## 常见问题

**Q1：On Actions和事件有什么区别？**

主要区别：
- **触发时机**：On Actions由系统自动调用，事件由条件触发或手动触发
- **频率**：On Actions按固定时间间隔运行，事件按需运行
- **用途**：On Actions适合系统逻辑和数据更新，事件适合叙事和决策

**Q2：On Actions可以触发事件吗？**

可以！使用`trigger_event`效果：

```pdx
on_monthly_pulse = {
    effect = {
        trigger_event = {
            id = my_event.1
        }
    }
}

```

**Q3：多个Mod的On Actions会冲突吗？**

不会直接冲突，但要⚠️ **注意**：
- 相同键名的On Actions会合并效果
- 如果相互依赖，注意加载顺序
- 避免性能问题（多个Mod都使用高频On Actions）

**Q4：如何调试On Actions？**

方法：
1. 使用`debug_log`输出信息
2. 检查error.log文件
3. 使用控制台命令手动触发
4. 添加临时触发条件缩小范围

**Q5：On Actions支持哪些作用域？**

取决于具体的On Action：
- `on_monthly_pulse`：root = 国家
- `on_building_built`：root = 建筑，owner = 国家
- `on_war_begins`：war_attacker/war_defender可用

---

## 本章小结

本章学习了On Actions的核心知识：

1. **基本概念**：系统自动触发的逻辑处理器
2. **时间类**：daily/weekly/monthly/yearly/decade pulse
3. **国家类**：国家成立、吞并、政体改变
4. **战争外交类**：战争开始/结束、外交博弈、条约
5. **建筑科技类**：建筑完工、科技研究、法律变更
6. **高级用法**：条件触发、随机触发、计数器、跨作用域

💡 **提示**：On Actions是Mod的"后台引擎"，适合处理系统级逻辑。合理使用能大大减少重复代码。

---

## 练习建议

1. **练习1**：创建一个每月给玩家增加100金币的On Action
2. **练习2**：创建建筑完工时触发奖励的On Action
3. **练习3**：使用变量追踪某个统计数据的年度变化
4. **练习4**：创建战争开始时给防御方加buff的On Action

📖 **参考**：完整On Actions列表请参阅Wiki和附录G。
