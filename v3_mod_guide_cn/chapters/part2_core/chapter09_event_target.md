# 第9章：事件目标（Event Target）——跨作用域引用

> 事件目标允许你保存作用域并在后续使用，是实现复杂事件链和跨对象引用的关键工具。本章将详细讲解事件目标的使用方法和高级技巧。

## 本章目标

完成本章学习后，你将能够：
- 理解事件目标的概念和用途
- 熟练使用`save_scope_as`保存作用域
- 使用`scope:`引用已保存的作用域
- 掌握点链语法进行复杂的作用域跳转
- 实现跨国家、跨州的事件交互

---

## 9.1 什么是事件目标？

### 9.1.1 生活化比喻

想象你在组织一场国际会议：

**场景1：保存联系人信息**
- 你遇到一位重要人物
- 你保存他的名片（save_scope_as）
- 之后你可以随时联系他（scope:引用）

**场景2：多方会谈**
- 你需要同时与多个国家代表交谈
- 你保存每个代表的联系方式
- 之后可以在不同场合引用他们

**场景3：转介绍**
- A介绍B给你认识
- 你保存了B的信息
- 之后你可以让C去联系B

在维多利亚3中，**事件目标**就是这样的"名片保存系统"，让你能够：
- 保存当前作用域供后续使用
- 在不同效果块之间传递对象引用
- 实现跨作用域的复杂交互

### 9.1.2 技术定义

**事件目标（Event Target）**是保存的作用域引用，可以在事件的不同部分使用：

```pdx
# 在immediate中保存作用域
immediate = {
    c:CHI = {
        save_scope_as = great_qing     # 保存大清作用域
    }
}

# 在option中引用
option = {
    scope:great_qing = {               # 使用保存的作用域
        add_treasury = 1000
    }
}

```

### 9.1.3 事件目标 vs 变量

| 特性         | 事件目标           | 变量                 |
| ------------ | ------------------ | -------------------- |
| **存储内容** | 作用域（对象引用） | 数值或作用域         |
| **修改**     | 不能修改           | 可以修改（数值运算） |
| **引用方式** | `scope:name`       | `var:name`           |
| **用途**     | 跨效果块传递对象   | 存储和计算数值       |
| **持久性**   | 事件期间有效       | 永久保存（除非移除） |

**关键区别**：
- **事件目标**：保存"谁"，用于引用对象
- **变量**：保存"多少"，用于存储数值

---

## 9.2 基本用法

### 9.2.1 保存作用域

使用`save_scope_as`保存当前作用域：

```pdx
# 保存国家作用域
c:CHI = {
    save_scope_as = qing_empire
}

# 保存州作用域
s:STATE_BEIJING = {
    save_scope_as = beijing_state
}

# 保存角色作用域
c:CHI = {
    ruler = {
        save_scope_as = qing_emperor
    }
}

# 保存利益集团作用域
c:CHI = {
    ig:ig_industrialists = {
        save_scope_as = industrialists_ig
    }
}

```

### 9.2.2 引用作用域

使用`scope:`前缀引用已保存的作用域：

```pdx
# 引用国家
scope:qing_empire = {
    add_treasury = 1000
}

# 引用州
scope:beijing_state = {
    add_building = building_steel_mills
}

# 引用角色
scope:qing_emperor = {
    add_trait = trait_enlightened
}

# 引用利益集团
scope:industrialists_ig = {
    add_modifier = {
        name = ig_empowered
        months = 12
    }
}

```

### 9.2.3 在触发器中使用

```pdx
trigger = {
    # 检查保存的国家
    scope:qing_empire = {
        treasury >= 1000
    }

    # 检查保存的州
    scope:beijing_state = {
        is_coastal = yes
    }
}

```

### 9.2.4 完整示例

```pdx
qing_reform.1 = {
    type = country_event
    title = qing_reform.1.t
    desc = qing_reform.1.d

    immediate = {
        # 保存大清
        c:CHI = {
            save_scope_as = great_qing

            # 保存统治者
            ruler = {
                save_scope_as = emperor
            }

            # 保存首都
            capital = {
                save_scope_as = beijing
            }

            # 保存一个强大的利益集团
            ordered_interest_group = {
                order_by = ig_clout
                position = 0
                save_scope_as = leading_ig
            }
        }

        # 保存一个随机的沿海州
        c:CHI = {
            random_scope_state = {
                limit = { is_coastal = yes }
                save_scope_as = coastal_state
            }
        }
    }

    option = {
        name = qing_reform.1.a
        default_option = yes

        # 使用保存的作用域
        scope:great_qing = {
            add_treasury = -500
        }

        scope:emperor = {
            add_prestige = 100
        }

        scope:beijing = {
            add_building = building_arms_industry
        }

        scope:coastal_state = {
            add_building = building_port
        }

        scope:leading_ig = {
            add_modifier = {
                name = ig_supports_reform
                months = 24
            }
        }
    }
}

```

---

## 9.3 点链语法（Dot Chaining）

### 9.3.1 什么是点链语法？

**点链语法**允许你通过`.`操作符在作用域之间跳转：

```pdx
# 基本语法：作用域.属性
# 返回新的作用域

c:CHI.ruler              # 从国家到统治者
c:CHI.capital           # 从国家到首都州
state.owner             # 从州到所属国家
character.interest_group # 从角色到所属利益集团

```

### 9.3.2 常用跳转路径

**从国家（country）出发**：

| 语法               | 目标      | 说明                   |
| ------------------ | --------- | ---------------------- |
| `country.ruler`    | character | 国家元首               |
| `country.heir`     | character | 继承人                 |
| `country.capital`  | state     | 首都州                 |
| `country.market`   | market    | 所属市场               |
| `country.overlord` | country   | 宗主国（如果是附属国） |

**从州（state）出发**：

| 语法           | 目标         | 说明           |
| -------------- | ------------ | -------------- |
| `state.owner`  | country      | 拥有该州的国家 |
| `state.market` | market       | 所属市场       |
| `state.region` | state_region | 州区域         |

**从角色（character）出发**：

| 语法                       | 目标           | 说明         |
| -------------------------- | -------------- | ------------ |
| `character.owner`          | country        | 所属国家     |
| `character.interest_group` | interest_group | 所属利益集团 |
| `character.party`          | party          | 所属政党     |

**从利益集团（interest_group）出发**：

| 语法                     | 目标      | 说明     |
| ------------------------ | --------- | -------- |
| `interest_group.country` | country   | 所属国家 |
| `interest_group.leader`  | character | 领导人   |

### 9.3.3 链式跳转

可以进行多次跳转：

```pdx
# 从国家 → 统治者 → 所属利益集团
c:CHI.ruler.interest_group

# 从州 → 所属国家 → 统治者
s:STATE_BEIJING.owner.ruler

# 从角色 → 所属国家 → 首都州
character.owner.capital

```

### 9.3.4 在触发器中使用

```pdx
trigger = {
    # 检查大清统治者的特质
    c:CHI.ruler = {
        has_trait = trait_ambitious
    }

    # 检查首都州的人口
    c:CHI.capital = {
        state_population >= 1000000
    }

    # 比较两个国家的统治者
    c:CHI.ruler.popularity > c:GBR.ruler.popularity
}

```

### 9.3.5 在效果中使用

```pdx
effect = {
    # 给大清统治者添加特质
    c:CHI.ruler = {
        add_trait = trait_enlightened
    }

    # 在英国首都建建筑
    c:GBR.capital = {
        add_building = building_university
    }

    # 给某角色的所属国家加威望
    scope:my_character.owner = {
        add_prestige = 100
    }
}

```

---

## 9.4 实战案例

### 案例1：复杂的国际事件

```pdx
# 三国同盟事件
namespace = triple_alliance

triple_alliance.1 = {
    type = country_event
    title = triple_alliance.1.t
    desc = triple_alliance.1.d

    trigger = {
        this = c:GER        # 德国触发
        year >= 1880
    }

    immediate = {
        # 保存三个国家
        c:GER = {
            save_scope_as = germany
        }
        c:AHM = {
            save_scope_as = austria_hungary
        }
        c:ITA = {
            save_scope_as = italy
        }

        # 保存各国统治者
        c:GER = {
            ruler = {
                save_scope_as = german_kaiser
            }
        }
        c:AHM = {
            ruler = {
                save_scope_as = austrian_emperor
            }
        }
        c:ITA = {
            ruler = {
                save_scope_as = italian_king
            }
        }
    }

    option = {
        name = triple_alliance.1.a
        default_option = yes

        # 创建三国同盟
        scope:germany = {
            create_diplomatic_pact = {
                country = scope:austria_hungary
                type = alliance
            }
            create_diplomatic_pact = {
                country = scope:italy
                type = alliance
            }
        }

        # 给所有参与国加威望
        scope:germany = { add_prestige = 100 }
        scope:austria_hungary = { add_prestige = 100 }
        scope:italy = { add_prestige = 100 }

        # 给统治者添加特质
        scope:german_kaiser = {
            add_trait = trait_diplomat
        }
        scope:austrian_emperor = {
            add_trait = trait_diplomat
        }
        scope:italian_king = {
            add_trait = trait_diplomat
        }

        # 触发事件给其他两国
        scope:austria_hungary = {
            trigger_event = {
                id = triple_alliance.2
                days = 7
            }
        }
        scope:italy = {
            trigger_event = {
                id = triple_alliance.2
                days = 7
            }
        }
    }
}

# 其他两国收到的事件
triple_alliance.2 = {
    type = country_event
    title = triple_alliance.2.t
    desc = triple_alliance.2.d

    immediate = {
        # 保存德国
        c:GER = {
            save_scope_as = alliance_leader
        }
    }

    option = {
        name = triple_alliance.2.a

        # 改善与德国的关系
        change_relations = {
            country = scope:alliance_leader
            value = 50
        }

        # 德国也改善与我国的关系
        scope:alliance_leader = {
            change_relations = {
                country = root
                value = 50
            }
        }
    }
}

```

### 案例2：领土争端事件

```pdx
# 领土争端事件链
namespace = territorial_dispute

territorial_dispute.1 = {
    type = country_event
    title = territorial_dispute.1.t
    desc = territorial_dispute.1.d

    trigger = {
        any_scope_state = {
            any_neighbouring_state = {
                owner = {
                    NOT = { this = root }
                    relations_with = {
                        target = root
                        value < -20
                    }
                }
            }
        }
    }

    immediate = {
        # 保存有争议的州
        random_scope_state = {
            limit = {
                any_neighbouring_state = {
                    owner = {
                        NOT = { this = root }
                    }
                }
            }
            save_scope_as = disputed_state

            # 保存邻国
            random_neighbouring_state = {
                save_scope_as = neighboring_state

                owner = {
                    save_scope_as = rival_country
                }
            }
        }
    }

    option = {
        name = territorial_dispute.1.a
        default_option = yes

        # 对争议州进行投资
        scope:disputed_state = {
            add_building = building_fort
            add_modifier = {
                name = border_fortification
                months = 24
            }
        }

        # 恶化与邻国关系
        scope:rival_country = {
            change_relations = {
                target = root
                value = -20
            }
        }
    }

    option = {
        name = territorial_dispute.1.b

        # 尝试外交解决
        scope:rival_country = {
            trigger_event = {
                id = territorial_dispute.2
                days = 14
            }
        }

        # 保存作用域供对方事件使用
        set_variable = {
            name = dispute_initiator
            value = 1
        }
    }
}

territorial_dispute.2 = {
    type = country_event
    title = territorial_dispute.2.t
    desc = territorial_dispute.2.d

    option = {
        name = territorial_dispute.2.a

        # 接受谈判
        change_relations = {
            target = c:CHI       # 假设争端发起者是大清
            value = 10
        }
    }

    option = {
        name = territorial_dispute.2.b

        # 拒绝谈判，开始外交博弈
        create_diplomatic_play = {
            target_country = c:CHI
            war_goal = conquer_state
            target_state = s:STATE_EXAMPLE
        }
    }
}

```

### 案例3：王朝联姻事件

```pdx
namespace = dynastic_marriage

dynastic_marriage.1 = {
    type = country_event
    title = dynastic_marriage.1.t
    desc = dynastic_marriage.1.d

    trigger = {
        is_monarchy = yes
        has_heir = yes
    }

    immediate = {
        # 保存本国统治者
        ruler = {
            save_scope_as = our_ruler
        }

        # 保存继承人
        heir = {
            save_scope_as = our_heir
        }

        # 找一个合适的联姻对象（随机选择）
        random_country = {
            limit = {
                is_monarchy = yes
                has_heir = yes
                relations_with = {
                    target = root
                    value >= 30
                }
                NOT = { this = root }
            }
            save_scope_as = marriage_partner

            ruler = {
                save_scope_as = partner_ruler
            }

            heir = {
                save_scope_as = partner_heir
            }
        }
    }

    option = {
        name = dynastic_marriage.1.a
        default_option = yes

        # 改善两国关系
        scope:marriage_partner = {
            change_relations = {
                target = root
                value = 30
            }
        }

        # 创建同盟
        create_diplomatic_pact = {
            country = scope:marriage_partner
            type = alliance
        }

        # 给两位统治者添加特质
        scope:our_ruler = {
            add_trait = trait_diplomat
        }
        scope:partner_ruler = {
            add_trait = trait_diplomat
        }

        # 给对方发送事件
        scope:marriage_partner = {
            trigger_event = {
                id = dynastic_marriage.2
                days = 7
            }
        }
    }

    option = {
        name = dynastic_marriage.1.b

        # 拒绝联姻
        scope:marriage_partner = {
            change_relations = {
                target = root
                value = -10
            }
        }
    }
}

dynastic_marriage.2 = {
    type = country_event
    title = dynastic_marriage.2.t
    desc = dynastic_marriage.2.d

    option = {
        name = dynastic_marriage.2.a

        # 接受联姻
        add_prestige = 50
    }
}

```

---

## 9.5 常见错误与最佳实践

### 9.5.1 常见错误

#### 错误1：保存作用域后对象消失

❌ **错误**：

```pdx
immediate = {
    random_scope_state = {
        save_scope_as = my_state
    }
    # my_state可能指向不同的州了！
}

```

✅ **正确**：

```pdx
immediate = {
    ordered_scope_state = {
        order_by = state_population
        position = 0              # 明确指定第1名
        save_scope_as = my_state
    }
}

```

#### 错误2：在错误的作用域保存

❌ **错误**：

```pdx
immediate = {
    c:CHI = {
        ruler = {
            save_scope_as = emperor
        }
    }
    # 实际上保存的是ruler的owner（CHI），不是ruler本身
}

```

✅ **正确**：

```pdx
immediate = {
    c:CHI = {
        ruler = {
            save_scope_as = emperor
        }
    }
}
# 这样保存的就是ruler角色

```

#### 错误3：忘记检查对象是否存在

❌ **错误**：

```pdx
immediate = {
    c:CHI = {
        heir = {
            save_scope_as = crown_prince
        }
        # 如果没有继承人，会出错
    }
}

```

✅ **正确**：

```pdx
immediate = {
    c:CHI = {
        if = {
            limit = {
                exists = heir
            }
            heir = {
                save_scope_as = crown_prince
            }
        }
    }
}

```

### 9.5.2 最佳实践

#### 1. 使用有意义的名称

```pdx
# 好
save_scope_as = rival_country
save_scope_as = disputed_province
save_scope_as = marriage_partner

# 不好
save_scope_as = sc1
save_scope_as = temp
save_scope_as = x

```

#### 2. 添加注释说明用途

```pdx
immediate = {
    # 保存发动战争的国家
    c:GBR = {
        save_scope_as = war_initiator
    }

    # 保存战争目标
    s:STATE_HONG_KONG = {
        save_scope_as = war_target
    }
}

```

#### 3. 验证作用域有效性

```pdx
option = {
    name = my_event.1.a

    trigger = {
        # 确保作用域有效
        exists = scope:target_country
    }

    scope:target_country = {
        add_treasury = 1000
    }
}

```

#### 4. 及时清理（如果需要）

```pdx
# 如果事件目标不再需要，可以清除
#⚠️ **注意**：通常不需要手动清除，事件结束后会自动释放
# 但如果是长期保存的，可能需要清理

after = {
    # 清理事件目标（如果需要）
    #⚠️ **注意**：实际上无法手动清除，只能不再引用
}

```

---

## 本章小结

- **事件目标**：保存作用域引用，用于跨效果块传递对象
- **保存**：使用`save_scope_as = name`
- **引用**：使用`scope:name`
- **点链语法**：通过`.`在作用域间跳转（country.ruler、state.owner等）
- **应用场景**：国际事件、领土争端、王朝联姻、复杂事件链
- **与变量的区别**：事件目标保存"谁"，变量保存"多少"

---

## 常见问题

**Q：事件目标和变量可以互相转换吗？**

A：
- 可以将作用域保存到变量：`set_variable = { name = my_var value = flag:country }`
- 但不能直接将变量转换为事件目标
- 建议根据用途选择：频繁引用用事件目标，数值计算用变量

**Q：事件目标在事件结束后还能用吗？**

A：不能。事件目标只在当前事件处理期间有效。如果需要长期保存，使用全局变量或设置标记。

**Q：可以保存多少个事件目标？**

A：理论上没有限制，但建议保持合理数量（<20），过多可能影响性能。

**Q：事件目标可以跨Mod使用吗？**

A：不能。事件目标只在当前Mod的事件中有效。

**Q：如何调试事件目标？**

A：
1. 使用`debug_mode`查看当前作用域
2. 使用`log`输出信息：`log = "Country: [scope:my_country.GetName]"`
3. 检查`error.log`文件

---

## 练习建议

1. **基础练习**：创建一个简单事件
   - 保存你的国家和邻国
   - 在选项中给两个国家都添加效果

2. **中级练习**：创建多方会谈事件
   - 保存3-4个国家
   - 每个国家都有独特的选项效果
   - 触发事件给其他国家

3. **高级练习**：创建复杂的领土争端系统
   - 自动识别争议领土
   - 保存争端双方
   - 提供外交和军事两种解决方案
   - 不同选择触发不同后续事件

4. **综合练习**：创建王朝系统
   - 追踪多个王室
   - 保存统治者、继承人信息
   - 实现联姻、继承、战争等互动

---

> 📖 **下一章预告**：在下一章，我们将学习**脚本数值（Script Value）**——可复用的计算公式系统。

---

## 参考

- [Victoria 3 Wiki - Event Target](https://vic3.paradoxwikis.com/Event_target)
- 附录D - 事件目标完整参考
