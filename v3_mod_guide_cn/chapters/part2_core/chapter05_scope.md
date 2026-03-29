# 第5章：作用域系统（Scope）——Mod开发的灵魂

> 作用域是维多利亚3 Mod开发中最核心的概念。理解作用域，就理解了游戏的运作方式。本章将详细讲解作用域的概念、类型和使用方法。

## 本章目标

完成本章学习后，你将能够：
- 理解什么是作用域及其重要性
- 掌握20+种作用域类型的特点和使用场景
- 熟练进行作用域切换（在对象间"跳转"）
- 使用迭代器批量处理对象
- 在实际Mod中灵活应用作用域

---

## 5.1 什么是作用域？

### 5.1.1 生活化比喻

想象你是一家公司的CEO，现在你要发布一项命令。你发布的命令类型取决于**你站在谁的角度看问题**：

**场景1**：你站在公司层面
- 你可以说："全公司加薪10%"
- 你不能说："小明你明天来我办公室"（太具体，不是公司层面的事）

**场景2**：你站在部门经理角度
- 你可以说："销售部这个季度目标提高20%"
- 你不能说："公司要上市"（太宏大，不是部门层面的事）

**场景3**：你站在员工角度
- 你可以说："我要申请加薪"
- 你不能说："解雇整个部门"（你没有这个权限）

在维多利亚3中，**作用域（Scope）**就是你"站的位置"。不同的作用域能访问不同的信息，执行不同的操作。

### 5.1.2 技术定义

**作用域**是游戏中实际存在的对象实例，例如：
- 一个具体的国家（如"大清"）
- 一个具体的州（如"直隶州"）
- 一个具体的人群（如"北京的劳工"）

当你写代码时，必须明确告诉游戏：**我现在在操作哪个对象？**

```pdx
# 在国家作用域中
country = {
    add_treasury = 1000  # 可以给国家加钱
    # 但不能直接修改某个州的建筑
}

# 在州作用域中
state = {
    add_building = building_iron_mine  # 可以给州加建筑
    # 但不能直接给国家加钱
}

```

### 5.1.3 为什么作用域如此重要？

❌ **没有作用域的世界**（混乱）：

```pdx
# 如果不用作用域，代码会这样：
add_treasury = 1000  # 给谁加？大清？英国？所有国家？
add_building = building_iron_mine  # 在哪个州建？

```

✅ **有作用域的世界**（清晰）：

```pdx
# 明确知道操作对象
c:CHI = {  # 在大清
    add_treasury = 1000  # 给大清加1000

    every_scope_state = {  # 遍历大清的所有州
        add_building = building_iron_mine  # 每个州都建一个铁矿
    }
}

```

---

## 5.2 作用域类型概览

维多利亚3有20+种作用域类型，分为几个大类：

### 5.2.1 核心作用域（最常用）

| 作用域      | 说明    | 示例                     |
| ----------- | ------- | ------------------------ |
| `country`   | 国家    | 大清、英国、法国         |
| `state`     | 州/省份 | 直隶、江苏、广东         |
| `pop`       | 人群    | 北京的劳工、上海的资本家 |
| `building`  | 建筑    | 铁矿、纺织厂、港口       |
| `character` | 角色    | 皇帝、将军、政治家       |

### 5.2.2 政治军事作用域

| 作用域               | 说明     | 示例                 |
| -------------------- | -------- | -------------------- |
| `interest_group`     | 利益集团 | 军队、知识分子、农民 |
| `party`              | 政党     | 保守党、自由党       |
| `diplomatic_play`    | 外交博弈 | 正在进行的危机或战争 |
| `war`                | 战争     | 鸦片战争、普法战争   |
| `military_formation` | 军事编队 | 陆军军团、海军舰队   |

### 5.2.3 经济社会作用域

| 作用域     | 说明 | 示例                 |
| ---------- | ---- | -------------------- |
| `market`   | 市场 | 大清市场、英国市场   |
| `goods`    | 商品 | 铁、木材、粮食       |
| `company`  | 公司 | 东印度公司、标准石油 |
| `culture`  | 文化 | 汉族、英格兰文化     |
| `religion` | 宗教 | 佛教、基督教         |

### 5.2.4 其他作用域

| 作用域        | 说明 |
| ------------- | ---- |
| `law`         | 法律 |
| `technology`  | 科技 |
| `institution` | 机构 |
| `front`       | 战线 |
| `theater`     | 战区 |

> 📖 **完整列表**：参见附录A - 作用域完整参考

---

## 5.3 基础作用域详解

### 5.3.1 country（国家作用域）

**国家作用域**是最常用的作用域之一。在国家作用域中，你可以：

✅ **可以做的事**：
- 修改国库资金（`add_treasury`）
- 添加威望（`add_prestige`）
- 研究科技（`add_technology`）
- 修改法律（`activate_law`）
- 访问国家的州、人物、利益集团等

❌ **不能做的事**：
- 直接修改某个州的建筑（需要先切换到state作用域）
- 直接修改某个人群的属性（需要先切换到pop作用域）

**如何进入国家作用域**：

```pdx
# 方法1：使用国家代码
c:CHI = {
    # 现在在大清作用域中
    add_treasury = 1000
}

# 方法2：从事件进入
country_event = {
    # 事件默认就在国家作用域中
    add_prestige = 100
}

# 方法3：从根作用域（root）
root = {
    # root通常是触发事件的国家
    add_treasury = 1000
}

```

**实战示例**：检查国家是否有足够资金

```pdx
trigger = {
    c:CHI = {
        treasury >= 1000  # 检查大清是否有至少1000资金
    }
}

```

### 5.3.2 state（州作用域）

**州作用域**用于管理州/省份级别的内容。在州作用域中，你可以：

✅ **可以做的事**：
- 添加建筑（`add_building`）
- 修改人口（`add_pop`）
- 设置州属性（`set_state_type`）
- 访问该州的所有建筑、人群

**如何进入州作用域**：

```pdx
# 方法1：使用州区域代码
s:STATE_BEIJING = {
    # 在直隶州（北京）作用域中
    add_building = building_iron_mine
}

# 方法2：从国家遍历所有州
c:CHI = {
    every_scope_state = {  # 遍历大清的每个州
        add_building = building_iron_mine  # 每个州都建铁矿
    }
}

# 方法3：从事件进入
state_event = {
    # 事件在特定州作用域中触发
}

```

**实战示例**：给直隶州添加铁矿

```pdx
effect = {
    s:STATE_BEIJING = {
        add_building = {
            type = building_iron_mine
            level = 3
        }
    }
}

```

### 5.3.3 pop（人群作用域）

**人群作用域**管理具体的人群（劳工、工匠、资本家等）。

✅ **可以做的事**：
- 修改人群规模（`add_pop`）
- 改变人群职业（`change_pop_type`）
- 添加人群政治倾向

**如何进入人群作用域**：

```pdx
# 从州遍历所有人群
every_scope_state = {
    every_scope_pop = {  # 遍历该州的每个人群
        # 在人群作用域中
        add_pop = 1000  # 增加1000人口
    }
}

```

### 5.3.4 building（建筑作用域）

**建筑作用域**管理具体的建筑实例。

✅ **可以做的事**：
- 修改建筑等级
- 改变生产方式（`set_production_method`）
- 关闭/开启建筑

**如何进入建筑作用域**：

```pdx
# 遍历州的所有建筑
every_scope_state = {
    every_scope_building = {  # 遍历该州的每个建筑
        # 在建筑作用域中
        set_production_method = pm_steam_power
    }
}

```

### 5.3.5 character（角色作用域）

**角色作用域**管理具体的角色（皇帝、将军、政治家等）。

✅ **可以做的事**：
- 修改角色属性
- 添加特质（`add_trait`）
- 设置角色职位

**如何进入角色作用域**：

```pdx
# 方法1：从国家获取统治者
c:CHI = {
    ruler = {
        # 在统治者作用域中
        add_trait = trait_ambitious
    }
}

# 方法2：遍历所有角色
every_scope_character = {
    # 在角色作用域中
}

```

---

## 5.4 作用域切换（Scope Jumping）

### 5.4.1 什么是作用域切换？

**作用域切换**是指从一个作用域"跳"到另一个作用域。这是Mod开发中最重要的技能之一。

**生活化比喻**：
想象你是一家公司的CEO，你需要：
1. 先查看公司整体财务状况（公司层面）
2. 然后查看某个部门的业绩（部门层面）
3. 最后与某个员工谈话（员工层面）

你不断地在不同"层面"间切换，这就是作用域切换。

### 5.4.2 使用点链语法切换

**点链语法**（Dot Chaining）是最常用的切换方式：

```pdx
# 语法：作用域.属性
# 返回新的作用域

c:CHI.ruler  # 从国家切换到统治者
c:CHI.capital  # 从国家切换到首都州
state.buildings  # 从州切换到该州的所有建筑

```

**实战示例**：获取大清统治者的名字

```pdx
c:CHI = {
    # 保存统治者作用域
    ruler = {
        save_scope_as = qing_ruler
    }
}

# 在本地化中使用
# [SCOPE.sCharacter('qing_ruler').GetFullName]

```

### 5.4.3 使用事件目标（Event Target）切换

**事件目标**允许你保存作用域，稍后再使用：

```pdx
immediate = {
    # 保存大清作用域
    c:CHI = {
        save_scope_as = great_qing
    }

    # 保存直隶州作用域
    s:STATE_BEIJING = {
        save_scope_as = beijing_state
    }

    # 保存统治者作用域
    c:CHI.ruler = {
        save_scope_as = qing_emperor
    }
}

# 之后使用保存的作用域
option = {
    name = my_event.1.a

    # 使用保存的大清作用域
    scope:great_qing = {
        add_treasury = 1000
    }

    # 使用保存的直隶州作用域
    scope:beijing_state = {
        add_building = building_iron_mine
    }

    # 使用保存的统治者作用域
    scope:qing_emperor = {
        add_trait = trait_enlightened
    }
}

```

### 5.4.4 常用作用域跳转路径

以下是常用的作用域跳转方式：

**从国家（country）可以跳转到**：

| 目标作用域   | 语法                       | 说明         |
| ------------ | -------------------------- | ------------ |
| 统治者       | `country.ruler`            | 国家元首     |
| 继承人       | `country.heir`             | 王位继承人   |
| 首都州       | `country.capital`          | 首都所在的州 |
| 所有州       | `every_scope_state`        | 遍历所有州   |
| 所有角色     | `every_scope_character`    | 遍历所有角色 |
| 所有利益集团 | `every_interest_group`     | 遍历所有IG   |
| 所有军队     | `every_military_formation` | 遍历所有军队 |

**从州（state）可以跳转到**：

| 目标作用域 | 语法                   | 说明           |
| ---------- | ---------------------- | -------------- |
| 所属国家   | `state.owner`          | 拥有该州的国家 |
| 所有建筑   | `every_scope_building` | 遍历所有建筑   |
| 所有人群   | `every_scope_pop`      | 遍历所有人群   |

**从角色（character）可以跳转到**：

| 目标作用域   | 语法                       | 说明         |
| ------------ | -------------------------- | ------------ |
| 所属国家     | `character.owner`          | 角色所在国家 |
| 所属利益集团 | `character.interest_group` | 角色所属IG   |

---

## 5.5 迭代器（Iterators）

### 5.5.1 什么是迭代器？

**迭代器**允许你批量处理多个对象。想象你需要给公司所有员工发奖金：

❌ **不用迭代器**（逐个操作）：

```pdx
employee_1 = { give_bonus = yes }
employee_2 = { give_bonus = yes }
employee_3 = { give_bonus = yes }
# ... 如果有1000个员工呢？

```

✅ **使用迭代器**（批量操作）：

```pdx
every_employee = {
    give_bonus = yes  # 自动给每个员工发奖金
}

```

### 5.5.2 迭代器类型

维多利亚3有4种迭代器，分为触发器迭代器和效果迭代器：

#### 触发器迭代器（Trigger Iterators）- `any_`

用于检查是否有任何对象满足条件：

```pdx
trigger = {
    # 检查大清是否有至少10个州
    c:CHI = {
        any_scope_state = {
            count >= 10
        }
    }

    # 检查是否有任何州有铁矿
    any_scope_state = {
        any_scope_building = {
            is_building_type = building_iron_mine
        }
    }
}

```

#### 效果迭代器（Effect Iterators）- `every_`

用于对所有对象执行效果：

```pdx
effect = {
    # 给大清的所有州添加铁矿
    c:CHI = {
        every_scope_state = {
            add_building = building_iron_mine
        }
    }
}

```

#### 随机迭代器（Random Iterator）- `random_`

用于随机选择一个对象：

```pdx
effect = {
    # 随机选择大清的一个州
    c:CHI = {
        random_scope_state = {
            add_building = building_iron_mine  # 只在一个随机州建铁矿
        }
    }
}

```

#### 排序迭代器（Ordered Iterator）- `ordered_`

用于按特定顺序选择对象：

```pdx
effect = {
    # 选择人口最多的前3个州
    c:CHI = {
        ordered_scope_state = {
            order_by = state_population
            position = 0
            max = 3
            add_building = building_iron_mine
        }
    }
}

```

### 5.5.3 常用迭代器一览

| 迭代器前缀 | 用途                         | 示例                  |
| ---------- | ---------------------------- | --------------------- |
| `any_`     | 检查是否有任何满足条件的对象 | `any_scope_state`     |
| `every_`   | 对所有对象执行效果           | `every_scope_state`   |
| `random_`  | 随机选择一个对象             | `random_scope_state`  |
| `ordered_` | 按顺序选择对象               | `ordered_scope_state` |

**完整迭代器列表**：

| 迭代器                         | 来源作用域              | 目标作用域         |
| ------------------------------ | ----------------------- | ------------------ |
| `any/every_scope_state`        | country                 | state              |
| `any/every_scope_building`     | state, country          | building           |
| `any/every_scope_pop`          | state, country, culture | pop                |
| `any/every_scope_character`    | country, interest_group | character          |
| `any/every_interest_group`     | country                 | interest_group     |
| `any/every_military_formation` | country, front          | military_formation |
| `any/every_country`            | none                    | country            |
| `any/every_state`              | none                    | state              |

### 5.5.4 使用 limit 过滤

你可以使用 `limit` 来过滤迭代器的目标：

```pdx
effect = {
    # 只给有铁矿的州添加建筑
    c:CHI = {
        every_scope_state = {
            limit = {
                any_scope_building = {
                    is_building_type = building_iron_mine
                }
            }
            add_building = building_steel_mills  # 只在这些州建钢厂
        }
    }
}

```

### 5.5.5 使用 count 和 percent

触发器迭代器可以使用 `count` 或 `percent` 来指定数量要求：

```pdx
trigger = {
    # 至少有5个州满足条件
    any_scope_state = {
        count >= 5
        has_building = building_iron_mine
    }

    # 至少30%的州满足条件
    any_scope_state = {
        percent >= 0.3
        has_building = building_textile_mills
    }
}

```

---

## 5.6 实战案例

### 案例1：检查大清是否有现代化工业

```pdx
# 触发器：检查大清是否有至少5个工业建筑
trigger = {
    c:CHI = {
        any_scope_state = {
            count >= 5
            any_scope_building = {
                OR = {
                    is_building_type = building_textile_mills
                    is_building_type = building_steel_mills
                    is_building_type = building_chemical_plants
                }
            }
        }
    }
}

```

### 案例2：给所有列强添加修正器

```pdx
# 效果：给所有列强（Great Powers）添加修正器
effect = {
    every_country = {
        limit = {
            country_rank = rank_value:great_power
        }
        add_modifier = {
            name = great_power_modifier
            months = 12
        }
    }
}

```

### 案例3：在人口最多的州建大学

```pdx
# 效果：在国家人口最多的州建大学
effect = {
    root = {
        ordered_scope_state = {
            order_by = state_population
            position = 0  # 第1名（人口最多）
            add_building = building_university
        }
    }
}

```

### 案例4：获取邻国信息

```pdx
# 在事件的 immediate 中保存邻国
country_event = {
    immediate = {
        # 保存一个邻国
        random_country = {
            limit = {
                is_neighbor = root
            }
            save_scope_as = neighbor_country
        }
    }

    option = {
        name = my_event.1.a

        # 使用保存的邻国
        scope:neighbor_country = {
            add_opinion = {
                target = root
                value = 10
            }
        }
    }
}

```

### 案例5：复杂的嵌套作用域

```pdx
# 遍历国家的每个利益集团
# 然后遍历每个利益集团的领导人
# 给每个领导人添加特质
effect = {
    root = {
        every_interest_group = {
            limit = {
                is_marginal = no  # 只处理非边缘化的IG
            }

            leader = {  # 切换到领导人作用域
                add_trait = trait_political_operator

                # 如果领导人是将军，再加点别的
                if = {
                    limit = {
                        is_general = yes
                    }
                    add_trait = trait_military_leader
                }
            }
        }
    }
}

```

---

## 5.7 常见错误与解决方案

### 错误1：在错误的作用域中使用触发器/效果

❌ **错误**：

```pdx
state = {
    add_treasury = 1000  # 错误！州没有国库
}

```

✅ **正确**：

```pdx
country = {
    add_treasury = 1000  # 国库是国家属性
}

```

### 错误2：忘记切换作用域

❌ **错误**：

```pdx
every_scope_state = {
    add_treasury = 1000  # 还在州作用域，不是国家
}

```

✅ **正确**：

```pdx
every_scope_state = {
    owner = {  # 切换到该州所属的国家
        add_treasury = 1000
    }
}

```

### 错误3：作用域链断裂

❌ **错误**：

```pdx
c:CHI = {
    every_scope_state = {
        ruler = {  # 错误！州没有统治者
            add_trait = trait_example
        }
    }
}

```

✅ **正确**：

```pdx
c:CHI = {
    every_scope_state = {
        owner = {  # 回到国家
            ruler = {  # 现在可以访问统治者
                add_trait = trait_example
            }
        }
    }
}

```

### 错误4：混淆迭代器和单数作用域

❌ **错误**：

```pdx
any_scope_state = {  # any_ 是触发器迭代器
    add_building = building_iron_mine  # 不能在触发器中使用效果
}

```

✅ **正确**：

```pdx
every_scope_state = {  # every_ 是效果迭代器
    add_building = building_iron_mine
}

```

### 错误5：忘记保存作用域

❌ **错误**：

```pdx
immediate = {
    c:CHI.ruler = {
        # 没有保存，之后在option中无法访问
    }
}

option = {
    c:CHI.ruler = {  # 重新获取，可能已经不是同一个人
        add_trait = trait_example
    }
}

```

✅ **正确**：

```pdx
immediate = {
    c:CHI.ruler = {
        save_scope_as = qing_ruler  # 保存作用域
    }
}

option = {
    scope:qing_ruler = {  # 使用保存的作用域
        add_trait = trait_example
    }
}

```

---

## 5.8 进阶技巧

### 技巧1：多重作用域保存

```pdx
immediate = {
    # 保存多个相关作用域
    c:CHI = {
        save_scope_as = great_qing

        ruler = {
            save_scope_as = qing_emperor
        }

        capital = {
            save_scope_as = beijing
        }
    }

    c:GBR = {
        save_scope_as = great_britain
        ruler = {
            save_scope_as = british_monarch
        }
    }
}

```

### 技巧2：在本地化中使用作用域

```pdx
# 在事件中保存作用域
immediate = {
    c:CHI = {
        save_scope_as = china
        ruler = {
            save_scope_as = emperor
        }
    }
}

```

```yaml
# 在本地化中使用
l_simp_chinese:
 my_event.1.t:0 "[SCOPE.sCountry('china').GetName]的消息"
 my_event.1.d:0 "[SCOPE.sCharacter('emperor').GetFullName]陛下传来消息..."

```

### 技巧3：条件作用域切换

```pdx
effect = {
    if = {
        limit = {
            is_monarchy = yes
        }
        ruler = {
            add_trait = trait_monarch
        }
    }
    else = {
        ig:ig_ruling_party = {
            leader = {
                add_trait = trait_president
            }
        }
    }
}

```

### 技巧4：组合多个迭代器

```pdx
# 遍历所有国家
# 然后遍历每个国家的所有州
# 然后遍历每个州的所有建筑
# 最后给特定类型的建筑添加修正器
effect = {
    every_country = {
        every_scope_state = {
            every_scope_building = {
                limit = {
                    is_building_type = building_steel_mills
                }
                add_modifier = {
                    name = steel_production_bonus
                    months = 6
                }
            }
        }
    }
}

```

---

## 本章小结

- **作用域**是你当前操作的"位置"，决定了你能访问什么信息、执行什么操作
- 维多利亚3有20+种作用域：国家、州、人群、建筑、角色等
- **作用域切换**允许你在不同对象间"跳转"，使用点链语法或事件目标
- **迭代器**允许你批量处理对象：`any_`、`every_`、`random_`、`ordered_`
- 常见错误：在错误作用域使用功能、忘记切换、混淆迭代器类型
- 使用 `save_scope_as` 保存作用域，确保后续能访问同一对象

---

## 常见问题

**Q：我如何知道某个效果需要在什么作用域中使用？**

A：查看附录B（触发器）和附录C（效果），每个都标注了所需作用域。或者在游戏文件中搜索该效果的官方使用示例。

**Q：`root`和`this`有什么区别？**

A：
- `root`：事件最初被触发的国家（通常是玩家国家）
- `this`：当前作用域的对象

在事件开始时，`root`和`this`通常是相同的。

**Q：为什么我保存的作用域在事件结束后消失了？**

A：作用域只在事件处理期间有效。如果需要长期保存，使用变量（`set_variable`）或全局变量（`set_global_variable`）。

**Q：如何在触发器中检查作用域是否存在？**

A：使用 `exists` 触发器：

```pdx
trigger = {
    exists = c:CHI  # 检查大清是否存在
    c:CHI = {
        exists = ruler  # 检查是否有统治者
    }
}

```

**Q：`c:`、`s:`、`ig:` 这些前缀是什么意思？**

A：这些是作用域类型前缀：
- `c:` - country（国家）
- `s:` - state region（州区域）
- `ig:` - interest group（利益集团）
- `cu:` - culture（文化）
- `rel:` - religion（宗教）

---

## 练习建议

1. **绘制作用域地图**：画出大清的作用域结构图：
   - 国家 → 州 → 建筑/人群
   - 国家 → 利益集团 → 领导人
   - 国家 → 统治者/继承人

2. **编写遍历代码**：尝试编写代码遍历大清的所有内容：
   - 所有州
   - 每个州的所有建筑
   - 每个州的所有人群
   - 所有利益集团
   - 所有角色

3. **作用域切换练习**：练习从不同作用域跳转到其他国家：
   - 从大清获取英国的统治者
   - 从直隶州跳转到江苏州
   - 从一个人群跳转到其所属国家

4. **创建复杂事件**：创建一个事件，要求：
   - 检查大清是否有至少5个州
   - 在这些州中随机选择一个
   - 给该州添加建筑
   - 同时给该州的所有人群添加人口

---

> 📖 **下一章预告**：在下一章，我们将学习**触发器（Trigger）**——决定"什么时候发生"的条件判断系统。

---

## 参考

- [Victoria 3 Wiki - Scope](https://vic3.paradoxwikis.com/Scope)
- [Victoria 3 Wiki - Event target](https://vic3.paradoxwikis.com/Event_target)
- 附录A - 作用域完整参考
