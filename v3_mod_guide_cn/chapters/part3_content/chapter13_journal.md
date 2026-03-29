# 第13章：日志系统（Journal Entry）——长期任务追踪

> 日志系统是维多利亚3中用于追踪长期目标、任务进度和持续状况的工具。本章将讲解如何创建日志条目，追踪玩家的长期目标。

## 本章目标

完成本章学习后，你将能够：
- 理解日志系统的概念和用途
- 创建基本的日志条目
- 设置完成、失败和当前进度条件
- 制作长期追踪任务
- 将日志与事件、决策系统结合

---

## 13.1 什么是日志条目？

### 13.1.1 生活化比喻

想象你在玩RPG游戏时的任务日志：

**主线任务**：
- "成为王国守护者"
- 进度：已完成2/5个试炼
- 当前目标：找到圣剑

**支线任务**：
- "收集10个草药"
- 进度：7/10
- 奖励：恢复药水×5

**限时任务**：
- "在30天内击败魔王"
- 剩余时间：15天
- 失败惩罚：王国毁灭

维多利亚3中的**日志条目（Journal Entry）**就是这样的长期目标追踪系统。

### 13.1.2 技术定义

**日志条目**是显示在日志面板中的长期目标：
- **名称**：日志的标题
- **描述**：详细说明
- **目标**：完成条件
- **进度**：当前状态追踪
- **奖励/惩罚**：完成或失败的结果

```pdx
┌─────────────────────────────────┐
│ 日志条目                        │
│                                  │
│ 洋务运动进程                    │
│ [==========>    ] 60%          │
│                                  │
│ 当前目标：                      │
│ - 完成军事改革 ✓               │
│ - 完成经济改革 ✓               │
│ - 完成教育改革 ⏳              │
│ - 完成海军改革 ⏸               │
│                                  │
│ 奖励：+500威望                  │
└─────────────────────────────────┘

```

---

## 13.2 日志文件基础

### 13.2.1 文件位置

日志文件存放在：

```pdx
my_mod/common/journal_entries/     # 主文件夹
my_mod/common/journal_entries/qing_reform.txt

```

### 13.2.2 基本结构

```pdx
# 日志条目名称
my_journal_entry = {
    # 基本信息
    icon = "gfx/interface/icons/journal_icons/economy.dds"

    # 名称和描述
    name = my_journal_entry_name
    desc = my_journal_entry_desc

    # 出现条件
    is_shown_when_inactive = {
        # 触发器
    }

    # 激活条件
    possible = {
        # 触发器
    }

    # 完成条件
    complete = {
        # 触发器
    }

    # 失败条件
    fail = {
        # 触发器
    }

    # 当前状态（持续效果）
    current_value = {
        # 脚本数值
    }

    # 目标值
    goal_add_value = {
        # 脚本数值
    }

    # 完成效果
    on_complete = {
        # 效果
    }

    # 失败效果
    on_fail = {
        # 效果
    }

    # 每月效果
    on_monthly_pulse = {
        # 效果
    }
}

```

### 13.2.3 最小示例

最简单的日志条目：

```pdx
simple_goal = {
    icon = "gfx/interface/icons/journal_icons/military.dds"

    name = simple_goal_name
    desc = simple_goal_desc

    # 激活条件
    possible = {
        exists = yes
    }

    # 完成条件
    complete = {
        army_size >= 50
    }

    # 完成效果
    on_complete = {
        add_prestige = 100
    }
}

```

---

## 13.3 日志的各个组成部分

### 13.3.1 基本信息

```pdx
my_journal = {
    # 图标
    icon = "gfx/interface/icons/journal_icons/industry.dds"

    # 名称和描述
    name = my_journal_name
    desc = my_journal_desc

    # 持续时间（月），0=无限
    duration = 60

    # 是否显示在信息栏
    show_in_outliner = yes
}

```

### 13.3.2 显示和激活条件

```pdx
my_journal = {
    # 何时显示（未激活时也显示）
    is_shown_when_inactive = {
        this = c:CHI
        year >= 1860
    }

    # 激活条件
    possible = {
        is_at_war = no
        treasury >= 500
    }

    # ...
}

```

### 13.3.3 完成条件

```pdx
my_journal = {
    # ...

    # 完成条件
    complete = {
        # 科技条件
        has_technology_researched = railroad
        has_technology_researched = steel

        # 建筑条件
        any_scope_state = {
            count >= 3
            has_building = building_steel_mills
        }
    }

    # ...
}

```

### 13.3.4 失败条件

```pdx
my_journal = {
    # ...

    # 失败条件
    fail = {
        OR = {
            # 时间过长
            journal_entry_age > 1825    # 5年

            # 被击败
            has_civil_war = yes

            # 失去领土
            any_scope_state = {
                NOT = { owner = root }
            }
        }
    }

    # ...
}

```

### 13.3.5 进度追踪

```pdx
my_journal = {
    # ...

    # 当前进度值（0-100）
    current_value = {
        value = 0

        # 每完成一个改革+25
        if = {
            limit = { has_variable = military_reform_done }
            add = 25
        }
        if = {
            limit = { has_variable = economic_reform_done }
            add = 25
        }
        if = {
            limit = { has_variable = education_reform_done }
            add = 25
        }
        if = {
            limit = { has_variable = naval_reform_done }
            add = 25
        }
    }

    # 目标值
    goal_add_value = {
        value = 100
    }

    # ...
}

```

### 13.3.6 完成和失败效果

```pdx
my_journal = {
    # ...

    # 完成时
    on_complete = {
        add_prestige = 500
        add_modifier = {
            name = successful_reform
            months = 60
        }

        # 触发庆祝事件
        trigger_event = {
            id = journal_complete.1
            days = 7
        }
    }

    # 失败时
    on_fail = {
        add_prestige = -200
        add_radicals_in_country = {
            value = 0.05
        }

        trigger_event = {
            id = journal_fail.1
            days = 7
        }
    }

    # 每月执行
    on_monthly_pulse = {
        # 持续效果
        if = {
            limit = { treasury < 0 }
            change_variable = {
                name = reform_progress
                add = -1
            }
        }
    }
}

```

---

## 13.4 实战案例：洋务运动日志

### 13.4.1 日志定义

**文件**：`common/journal_entries/qing_self_strengthening.txt`

```pdx
qing_self_strengthening_journal = {
    icon = "gfx/interface/icons/journal_icons/industry.dds"

    name = qing_self_strengthening_journal_name
    desc = qing_self_strengthening_journal_desc

    # 显示条件
    is_shown_when_inactive = {
        this = c:CHI
        year >= 1860
        year <= 1880
    }

    # 激活条件
    possible = {
        is_at_war = no
        treasury >= 500
        NOT = { has_variable = self_strengthening_journal_active }
    }

    # 完成条件（至少完成3项改革）
    complete = {
        custom_tooltip = "complete_at_least_3_reforms"
        calc_true_if = {
            amount >= 3
            has_variable = military_reform_done
            has_variable = economic_reform_done
            has_variable = education_reform_done
            has_variable = naval_reform_done
        }
    }

    # 失败条件
    fail = {
        OR = {
            journal_entry_age > 3650      # 10年
            has_civil_war = yes
            is_subject = yes
        }
    }

    # 当前进度
    current_value = {
        value = 0
        if = { limit = { has_variable = military_reform_done } add = 1 }
        if = { limit = { has_variable = economic_reform_done } add = 1 }
        if = { limit = { has_variable = education_reform_done } add = 1 }
        if = { limit = { has_variable = naval_reform_done } add = 1 }
    }

    # 目标值
    goal_add_value = {
        value = 3
    }

    # 立即效果
    immediate = {
        set_variable = self_strengthening_journal_active
    }

    # 完成效果
    on_complete = {
        remove_variable = self_strengthening_journal_active
        remove_variable = military_reform_done
        remove_variable = economic_reform_done
        remove_variable = education_reform_done
        remove_variable = naval_reform_done

        add_prestige = 500
        add_modifier = {
            name = successful_self_strengthening
            months = 60
        }
    }

    # 失败效果
    on_fail = {
        remove_variable = self_strengthening_journal_active
        remove_variable = military_reform_done
        remove_variable = economic_reform_done
        remove_variable = education_reform_done
        remove_variable = naval_reform_done

        add_prestige = -300
        add_radicals_in_country = {
            value = 0.05
        }
    }

    # 每月检查
    on_monthly_pulse = {
        # 如果资金不足，提醒玩家
        if = {
            limit = { treasury < 200 }
            trigger_event = {
                id = qing_journal.1      # 资金警告事件
                days = 1
            }
        }
    }
}

```

### 13.4.2 与决策结合

```pdx
# 决策完成时标记日志进度
military_reform = {
    is_shown = { ... }
    possible = { ... }

    when_taken = {
        set_variable = military_reform_done

        # 增加日志进度
        if = {
            limit = {
                has_active_journal_entry = qing_self_strengthening_journal
            }
            change_variable = {
                name = qing_journal_progress
                add = 1
            }
        }
    }
}

```

### 13.4.3 本地化

```yaml
l_simp_chinese:
 qing_self_strengthening_journal_name:0 "洋务运动进程"
 qing_self_strengthening_journal_desc:0 "推动全面的现代化改革，包括军事、经济、教育和海军四个方面。完成至少3项改革以获得最终奖励。"

 complete_at_least_3_reforms:0 "完成至少3项改革"

 successful_self_strengthening:0 "洋务运动成功"
 successful_self_strengthening_desc:0 "改革大大增强了国家实力。"

```

---

## 13.5 常见错误与最佳实践

### 13.5.1 常见错误

#### 错误1：忘记清理变量

❌ **错误**：日志结束后变量仍然存在

✅ **正确**：在`on_complete`和`on_fail`中清理

#### 错误2：进度计算错误

❌ **错误**：进度不更新或计算错误

✅ **正确**：使用`current_value`和`goal_add_value`明确计算

### 13.5.2 最佳实践

1. **清晰的进度显示**
2. **合理的完成时间**
3. **明确的奖励和惩罚**
4. **与事件、决策联动**

---

## 本章小结

- **日志条目**用于追踪长期目标和任务进度
- **组成部分**：名称、描述、完成条件、失败条件、进度追踪
- **与决策结合**：决策完成推进日志进度
- **实战案例**：洋务运动改革日志

---

## 参考

- [Victoria 3 Wiki - Journal modding](https://vic3.paradoxwikis.com/Journal_modding)
