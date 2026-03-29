# 第二十九章：调试与测试

## 本章目标

学习本章后，你将能够：
- 使用调试模式和控制台命令
- 阅读和理解错误日志
- 诊断和修复常见错误
- 使用调试工具定位问题
- 掌握性能优化技巧

---

## 概念讲解：调试是什么？

### 比喻：医生诊断

想象你是一位医生：
- **症状** = 游戏中的异常现象（崩溃、不触发、显示错误）
- **诊断工具** = 控制台、错误日志、调试命令
- **治疗方案** = 修复代码错误

调试就是找出"病因"并"治疗"的过程。

### 为什么要调试？

1. **发现问题**：在玩家报告前修复
2. **理解行为**：确认代码按预期工作
3. **学习成长**：从错误中理解游戏机制
4. **提高质量**：让Mod更稳定可靠

---

## 29.1 调试模式

### 29.1.1 开启调试模式

**Steam方法**：
1. 在Steam中右键维多利亚3
2. 选择"属性"
3. 启动选项中添加：`-debug_mode`
4. 启动游戏

**快捷方式方法**：
1. 创建游戏快捷方式
2. 右键→属性
3. 目标后添加：`-debug_mode`
4. 使用此快捷方式启动

### 29.1.2 调试模式功能

开启调试模式后可用功能：

| 功能     | 说明           | 快捷键     |
| -------- | -------------- | ---------- |
| 控制台   | 输入调试命令   | `~` 或 `^` |
| 调试菜单 | 各种调试选项   | 右键菜单   |
| 信息覆盖 | 显示隐藏数据   |            |
| 自由相机 | 无限制移动视角 |            |
| 即时建造 | 建筑瞬间完成   |            |

---

## 29.2 控制台命令

### 29.2.1 打开控制台

按 **`~`**（数字1左边的键）或 **`^`** 打开控制台。

如果无法打开，检查：
- 是否已开启调试模式
- 键盘布局是否正确
- 是否按对了键

### 29.2.2 常用控制台命令

**游戏控制命令**：

| 命令              | 功能           | 示例         |
| ----------------- | -------------- | ------------ |
| `help`            | 显示所有命令   | help         |
| `cash [数量]`     | 增加金钱       | cash 10000   |
| `prestige [数量]` | 增加威望       | prestige 100 |
| `annex [国家TAG]` | 吞并国家       | annex QNG    |
| `own [省份ID]`    | 获得省份       | own 1234     |
| `yesmen`          | AI总是接受提议 | yesmen       |
| `fullscreen`      | 切换全屏       | fullscreen   |

**时间控制命令**：

| 命令                   | 功能         |               |
| ---------------------- | ------------ | ------------- |
| `date [日期]`          | 设置日期     | date 1850.1.1 |
| `time`                 | 显示当前时间 |               |
| `ticks_per_day [数值]` | 设置游戏速度 |               |

**调试命令**：

| 命令                  | 功能         |               |
| --------------------- | ------------ | ------------- |
| `debug_mode`          | 切换调试模式 |               |
| `debug_assert`        | 开启断言检查 |               |
| `debug_info`          | 显示调试信息 |               |
| `reload [文件名]`     | 重载文件     | reload events |
| `reload localization` | 重载本地化   |               |
| `reload texture`      | 重载纹理     |               |

### 29.2.3 重载命令详解

**重载脚本文件**：

```pdx
reload events              # 重载事件
reload decisions           # 重载决策
reload common              # 重载common文件夹
reload history             # 重载历史文件

```

**重载图形资源**：

```pdx
reload texture             # 重载纹理
reload gui                 # 重载GUI
reload map                 # 重载地图

```

**重载本地化**：

```pdx
reload localization        # 重载所有本地化

```

💡 **提示**：重载命令允许你修改文件后不需要重启游戏就能看到效果！

### 29.2.4 国家相关命令

```pdx
tag [TAG]                  # 切换到指定国家
tag_color [颜色]           # 切换到有指定颜色的国家
observe                    # 进入观察者模式

```

**示例**：

```pdx
tag QNG                    # 切换到大清
tag JNG                    # 切换到江南共和国（如果有）

```

### 29.2.5 事件命令

```pdx
event [事件ID]             # 触发指定事件
events                     # 显示可用事件
events [数量]              # 显示指定数量的事件

```

**示例**：

```pdx
event jiangnan_revolution.1    # 触发江南起义事件
event 100                      # 触发事件ID 100

```

### 29.2.6 自定义命令

在`common/console_commands/`中可以创建自定义命令：

```pdx
# 文件：common/console_commands/my_commands.txt

jiangnan_test = {
    effect = {
        every_country = {
            limit = {
                country_has_primary_culture = cu:han
            }

            add_treasury = 10000
            add_modifier = {
                name = test_modifier
                months = 12
            }
        }
    }
}

```

然后在控制台输入：`jiangnan_test`

---

## 29.3 错误日志

### 29.3.1 错误日志位置

```pdx
文档/Victoria 3/logs/
├── error.log              # 主要错误日志
├── game.log               # 游戏运行日志
├── system.log             # 系统日志
└── setup.log              # 初始化日志

```

### 29.3.2 常见错误类型

**语法错误**：

```pdx
[error][pdx_persistent.cpp:1234]: Failed to parse file: my_mod/events/test.txt
[error][pdx_persistent.cpp:1234]: Line 5: Expected '=', got 'effect'

```

**含义**：第5行语法错误，期望`=`但得到了`effect`

**解决方法**：
1. 打开文件，检查第5行
2. 确认语法结构正确
3. 检查括号是否匹配

**文件未找到**：

```pdx
[error][virtualfilesystem.cpp:567]: Could not find file: gfx/interface/icons/my_icon.dds

```

**含义**：游戏找不到指定文件

**解决方法**：
1. 检查文件路径是否正确
2. 确认文件扩展名正确
3. 检查文件名拼写

**作用域错误**：

```pdx
[error][effect.cpp:890]: Invalid scope for effect 'add_treasury'

```

**含义**：在错误的作用域使用了效果

**解决方法**：
1. 确认当前作用域支持该效果
2. 使用`owner = { }`或`prev = { }`切换作用域

**触发器错误**：

```pdx
[error][trigger.cpp:567]: Unknown trigger 'is_great_powr'

```

**含义**：使用了不存在的触发器（可能是拼写错误）

**解决方法**：
1. 检查触发器拼写
2. 参考触发器参考手册

### 29.3.3 如何阅读错误日志

**错误日志格式**：

```pdx
[时间戳][错误级别][文件名:行号]: 错误信息

```

**示例分析**：

```pdx
[2026-03-30 10:30:15][error][events.cpp:456]:
Event jiangnan_revolution.1 has invalid option

```

**解读**：
- 时间：2026年3月30日 10:30:15
- 级别：error（错误）
- 位置：events.cpp 第456行
- 内容：事件jiangnan_revolution.1有无效选项

### 29.3.4 常见错误速查表

| 错误信息                | 可能原因   | 解决方法           |
| ----------------------- | ---------- | ------------------ |
| Failed to parse file    | 语法错误   | 检查文件语法       |
| Could not find file     | 路径错误   | 检查文件路径和名称 |
| Invalid scope           | 作用域错误 | 确认当前作用域     |
| Unknown trigger         | 拼写错误   | 检查触发器名称     |
| Unknown effect          | 拼写错误   | 检查效果名称       |
| Missing closing bracket | 括号不匹配 | 检查括号配对       |
| Invalid value           | 值错误     | 检查数值或字符串   |
| Duplicate key           | 键重复     | 删除重复定义       |

---

## 29.4 调试技巧

### 29.4.1 分步调试法

当遇到问题时，使用"分而治之"策略：

```pdx
1. 确认问题范围
   ↓ 是整个Mod还是特定文件？
2. 隔离问题代码
   ↓ 注释掉一半代码，看问题是否还存在
3. 逐步缩小范围
   ↓ 反复二分，直到找到问题代码
4. 修复并验证
   ↓ 修改后测试确认解决

```

### 29.4.2 使用debug_log

在脚本中添加调试输出：

```pdx
event = {
    immediate = {
        # 输出调试信息
        debug_log = "事件触发，当前国家：[Country.GetName]"
        debug_log = "变量值为：[Country.GetVariable('my_var')]"
        debug_log = "当前年份：[GetYear]"
    }
}

```

调试信息会输出到`game.log`文件。

### 29.4.3 测试事件触发

**方法1：控制台直接触发**

```pdx
event my_event.1

```

**方法2：使用调试决策**

```pdx
# 创建一个测试决策
debug_trigger_event = {
    is_shown = {
        is_player = yes
    }

    when_taken = {
        trigger_event = my_event.1
    }
}

```

### 29.4.4 验证触发条件

添加临时选项来验证条件：

```pdx
event = {
    option = {
        name = "调试：检查条件"

        # 输出条件检查结果
        if = {
            limit = { is_great_power = yes }
            debug_log = "是列强"
        }
        else = {
            debug_log = "不是列强"
        }
    }
}

```

---

## 29.5 常见错误及解决方案

### 29.5.1 事件不触发

**可能原因**：
1. 触发条件不满足
2. 事件文件路径错误
3. 事件ID冲突
4. 触发器语法错误

**排查步骤**：

```pdx
1. 检查error.log是否有错误
2. 在控制台手动触发：event [ID]
3. 检查触发条件是否正确
4. 检查事件文件是否在正确位置

```

**示例修复**：

```pdx
# ❌ 错误：缺少event关键字
jiangnan_revolution.1 = {
    type = country_event
}

# ✅ 正确
namespace = jiangnan_revolution

jiangnan_revolution.1 = {
    type = country_event
}

```

### 29.5.2 本地化不显示

**可能原因**：
1. 编码不是UTF-8 with BOM
2. 文件路径错误
3. 键名拼写错误
4. YAML语法错误

**排查步骤**：

```pdx
1. 确认文件编码为UTF-8 with BOM
2. 检查文件名格式：name_l_language.yml
3. 使用reload localization命令
4. 检查游戏内其他Mod是否覆盖

```

### 29.5.3 决策不显示

**可能原因**：
1. `is_shown`条件不满足
2. `possible`条件不满足
3. 决策文件未加载
4. 与国家类型不匹配

**排查方法**：

```pdx
debug_decision = {
    # 移除条件限制
    is_shown = {
        always = yes    # 始终显示，用于测试
    }

    possible = {
        always = yes    # 始终可用
    }

    when_taken = {
        # 决策效果
    }
}

```

### 29.5.4 效果不生效

**可能原因**：
1. 作用域错误
2. 效果拼写错误
3. 参数类型错误
4. 条件判断阻止

**排查方法**：

```pdx
# 添加调试输出
effect = {
    debug_log = "效果开始执行"

    # 确认作用域
    debug_log = "当前作用域：[GetScope]"

    add_treasury = 1000

    debug_log = "效果执行完成"
}

```

### 29.5.5 游戏崩溃

**常见原因**：
1. 无限循环
2. 除以零
3. 空指针引用
4. 内存溢出

**排查方法**：

```pdx
1. 查看error.log最后几条记录
2. 检查最近修改的文件
3. 逐步回退修改，找到崩溃点
4. 检查是否有循环引用

```

**预防无限循环**：

```pdx
# ❌ 危险：可能导致无限循环
while = {
    limit = { gold < 1000 }
    add_treasury = 100
}

# ✅ 安全：设置上限
set_variable = { name = loop_count value = 0 }

while = {
    limit = {
        gold < 1000
        var:loop_count < 100    # 限制循环次数
    }
    add_treasury = 100
    change_variable = { name = loop_count add = 1 }
}

```

---

## 29.6 性能优化

### 29.6.1 识别性能问题

**症状**：
- 游戏卡顿
- 加载时间长
- 自动保存慢
- CPU占用高

**诊断方法**：
1. 使用`debug_time`命令查看执行时间
2. 检查是否有高频的On Actions
3. 查看日志中的性能警告

### 29.6.2 优化建议

**事件优化**：

```pdx
# ❌ 低效：每次检查所有国家
event = {
    trigger = {
        every_country = {
            # 复杂计算
        }
    }
}

# ✅ 高效：先快速筛选
event = {
    trigger = {
        # 快速检查
        is_great_power = yes

        # 只有通过了才进行复杂计算
        custom_tooltip = {
            every_country = {
                limit = { is_player = yes }
                # 复杂计算
            }
        }
    }
}

```

**On Actions优化**：

```pdx
# ❌ 低效：每天检查所有国家
on_daily_pulse = {
    effect = {
        every_country = {
            # 复杂计算
        }
    }
}

# ✅ 高效：每月检查，且只检查相关国家
on_monthly_pulse = {
    effect = {
        every_country = {
            limit = {
                # 只检查满足条件的国家
                has_variable = my_mod_active
            }
            # 复杂计算
        }
    }
}

```

**变量使用**：

```pdx
# ❌ 低效：重复计算
effect = {
    if = {
        limit = {
            gdp > 1000000
        }
        # ...
    }

    if = {
        limit = {
            gdp > 1000000    # 重复计算
        }
        # ...
    }
}

# ✅ 高效：缓存结果
effect = {
    set_variable = { name = gdp_check value = gdp }

    if = {
        limit = { var:gdp_check > 1000000 }
        # ...
    }

    if = {
        limit = { var:gdp_check > 1000000 }
        # ...
    }
}

```

### 29.6.3 文件组织优化

**原则**：
- 将大型文件拆分为小文件
- 使用子文件夹组织
- 删除未使用的代码
- 压缩图片资源

---

## 29.7 测试清单

### 29.7.1 发布前测试

**功能测试**：
- [ ] 所有事件能正常触发
- [ ] 所有决策能正常显示和使用
- [ ] 所有日志条目能正常出现
- [ ] 修正器效果正确
- [ ] 本地化显示正常

**兼容性测试**：
- [ ] 与原版游戏兼容
- [ ] 不与常用Mod冲突
- [ ] 存档能正常加载
- [ ] 不影响游戏性能

**边界测试**：
- [ ] 极端数值下正常工作
- [ ] 多国家同时使用
- [ ] 不同年份正常运作
- [ ] 各种政体都适用

### 29.7.2 自动化测试

使用`common/scripted_tests/`创建自动化测试：

```pdx
# 文件：common/scripted_tests/my_tests.txt

test_jiangnan_events = {
    # 测试事件触发
    trigger = {
        exists = event:jiangnan_revolution.1
    }

    # 测试事件执行
    effect = {
        trigger_event = jiangnan_revolution.1
    }

    # 验证结果
    validate = {
        has_modifier = jiangnan_revolution_started
    }
}

```

---

## 常见问题

**Q1：如何快速找到错误位置？**

方法：
1. 打开error.log，查看最后一个错误
2. 找到文件路径和行号
3. 使用文本编辑器的"转到行"功能

**Q2：游戏崩溃但没有错误日志？**

可能原因：
- 内存不足
- 驱动问题
- 与其他程序冲突
- 游戏文件损坏

解决方法：
1. 降低游戏画质
2. 更新显卡驱动
3. 验证游戏文件完整性
4. 关闭其他程序

**Q3：如何测试特定条件？**

使用控制台命令快速设置条件：

```pdx
cash 1000000              # 增加金钱
prestige 1000             # 增加威望
annex QNG                 # 吞并国家

```

**Q4：Mod突然不工作了？**

排查步骤：
1. 游戏更新后可能需要更新Mod
2. 检查是否与其他Mod冲突
3. 查看error.log
4. 尝试禁用其他Mod测试

---

## 本章小结

本章学习了调试与测试的核心知识：

1. **调试模式**：开启方法和可用功能
2. **控制台命令**：常用命令和重载功能
3. **错误日志**：位置、格式和解读方法
4. **常见错误**：语法错误、作用域错误等
5. **调试技巧**：分步调试、debug_log
6. **性能优化**：识别和解决性能问题
7. **测试清单**：发布前完整测试

💡 **提示**：调试是Mod开发的必备技能。善于使用工具能快速定位和解决问题。

---

## 练习建议

1. **练习1**：故意制造一个语法错误，练习从error.log中找出问题
2. **练习2**：使用控制台命令测试事件触发
3. **练习3**：为一个复杂效果添加debug_log输出
4. **练习4**：创建完整的测试清单，测试你的Mod

📖 **参考**：完整的控制台命令列表请参阅附录J。
