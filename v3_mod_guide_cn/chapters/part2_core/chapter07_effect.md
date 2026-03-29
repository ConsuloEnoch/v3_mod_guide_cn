# 第7章：效果（Effect）——实际改变游戏

> 如果说触发器是"检查条件"，那么效果就是"执行操作"。本章将详细讲解如何使用效果命令实际修改游戏状态，从添加资金到创建国家，从修改变量到触发事件。

## 本章目标

完成本章学习后，你将能够：
- 理解效果命令的基本语法和使用方式
- 掌握国家、州、人群、建筑等各类效果
- 熟练使用变量系统存储和操作数据
- 创建和删除游戏对象
- 组合使用效果实现复杂的Mod功能

---

## 7.1 什么是效果？

### 7.1.1 生活化比喻

回到智能家居的例子：

**触发器**是"如果..."：

```pdx
如果（天黑 AND 有人进入房间）{
    // 触发器部分：检查条件
}

```

**效果**是"就执行..."：

```pdx
如果（天黑 AND 有人进入房间）{
    开灯                    // 效果1
    播放欢迎音乐            // 效果2
    调整温度到25度          // 效果3
}

```

在维多利亚3中：
- **触发器**：检查"国库是否大于1000？"
- **效果**："给国库添加500资金"

### 7.1.2 技术定义

**效果（Effect）**是修改游戏状态的命令。与触发器不同，效果会实际改变游戏数据：

```pdx
# 触发器：只检查，不改变
trigger = {
    treasury > 1000     # 检查国库，不修改
}

# 效果：实际改变游戏状态
effect = {
    add_treasury = 500  # 实际给国库添加500
}

```

### 7.1.3 效果的作用位置

效果可以出现在以下位置：

| 位置                    | 用途                   | 示例                 |
| ----------------------- | ---------------------- | -------------------- |
| **immediate**           | 事件触发时立即执行     | 设置变量、保存作用域 |
| **option**              | 玩家选择选项后执行     | 添加资金、触发新事件 |
| **after**               | 选项选择后执行（清理） | 设置完成标记         |
| **decision when_taken** | 决策被点击时执行       | 改革效果             |
| **if/else**             | 条件执行               | 根据条件执行不同效果 |

---

## 7.2 基本效果语法

### 7.2.1 效果的基本结构

```pdx
# 单个效果
effect_name = value

# 多个效果（使用代码块）
{
    effect1 = value1
    effect2 = value2
    effect3 = value3
}

# 带参数的效果
effect_name = {
    param1 = value1
    param2 = value2
}

```

### 7.2.2 效果执行顺序

效果按从上到下的顺序依次执行：

```pdx
effect = {
    add_treasury = 500      # 第1步：加500资金
    add_prestige = 100      # 第2步：加100威望
    add_modifier = {        # 第3步：添加修正器
        name = my_modifier
        months = 12
    }
}

```

> 💡 **提示**：效果执行是顺序的，前一个效果的结果会影响后一个效果。

---

## 7.3 国家效果（Country Scope Effects）

### 7.3.1 资金和威望

```pdx
# 国库资金
add_treasury = 1000             # 添加1000资金
add_treasury = -500             # 减少500资金（负数）

# 威望
add_prestige = 100              # 添加100威望
add_prestige = -50              # 减少50威望

# 恶名
add_infamy = 10                 # 添加10恶名
add_infamy = -5                 # 减少5恶名

```

### 7.3.2 科技和研究

```pdx
# 研究科技
add_technology = railroad               # 研究铁路
add_technology = steel                  # 研究钢铁
add_technology_researched = electricity # 研究电力（别名）

# 添加科技进度（部分进度）
add_technology_progress = {
    technology = railroad
    progress = 0.5          # 添加50%进度
}

```

### 7.3.3 法律和改革

```pdx
# 激活法律
activate_law = law_type:law_monarchy            # 实行君主制
activate_law = law_type:law_presidential        # 实行总统制
activate_law = law_type:law_no_slavery          # 废除奴隶制

# 废除法律（实行相反的法律）
# 实际上是用activate_law实行相反的法律

# 修改法律
change_law = {
    law_type = law_type:law_slavery
    option = law_slavery_banned    # 改为禁止奴隶制
}

```

### 7.3.4 外交关系

```pdx
# 创建外交协定
create_diplomatic_pact = {
    country = c:GBR                 # 目标国家
    type = alliance                 # 类型：同盟
}

create_diplomatic_pact = {
    country = c:FRA
    type = defensive_pact           # 防御协定
}

create_diplomatic_pact = {
    country = c:RUS
    type = trade_agreement          # 贸易协定
}

# 结束外交协定
end_diplomatic_pact = {
    country = c:GBR
    type = alliance
}

# 改变关系
change_relations = {
    country = c:GBR
    value = 20                      # 增加20关系值
}

# 建立敌对关系
add_rivalry = c:RUS                 # 与俄罗斯敌对
remove_rivalry = c:RUS              # 结束敌对

# 建立附属关系
create_subject = {
    country = c:KOR                 # 目标国家
    type = subject_type:puppet      # 类型：傀儡国
}

```

### 7.3.5 战争和军事

```pdx
# 发动外交博弈
create_diplomatic_play = {
    target_country = c:CHI
    war_goal = conquer_state
    target_state = s:STATE_BEIJING
}

# 宣战（直接开始战争）
declare_war = {
    country = c:CHI
    war_goal = conquer_state
}

# 结束战争
end_war = {
    winner = root                   # 胜利方
    loser = c:CHI                   # 失败方
}

# 征召军队
conscript_battalions = 10           # 征召10个营

# 解散军队
demobilize_army = yes

```

### 7.3.6 修正器（Modifiers）

```pdx
# 添加临时修正器
add_modifier = {
    name = industrialization_boost  # 修正器名称
    months = 12                     # 持续12个月
}

add_modifier = {
    name = economic_boom
    months = normal_modifier_time   # 使用预定义的时间值
    is_decaying = yes               # 随时间衰减
}

# 移除修正器
remove_modifier = industrialization_boost

# 添加永久修正器
add_modifier = {
    name = permanent_bonus
}

```

### 7.3.7 人口和政治

```pdx
# 添加激进派/忠诚派
add_radicals = {
    pop_type = laborers             # 人群类型
    value = 10000                   # 数量
}

add_loyalists = {
    pop_type = capitalists
    value = 5000
}

# 在全国范围内添加
add_radicals_in_country = {
    value = 0.05                    # 5%的人口
}

add_loyalists_in_country = {
    value = 0.03                    # 3%的人口
}

```

---

## 7.4 州效果（State Scope Effects）

### 7.4.1 建筑和基础设施

```pdx
# 添加建筑
add_building = {
    type = building_iron_mine       # 建筑类型
    level = 3                       # 等级3
}

add_building = {
    type = building_steel_mills
    level = 2
    production_method = pm_steam_power  # 指定生产方式
}

# 添加特定建筑组
add_building = building_railway     # 简写形式

# 升级建筑
upgrade_building = {
    type = building_iron_mine
    level = 2                       # 升2级
}

# 移除建筑
remove_building = building_iron_mine

```

### 7.4.2 人口

```pdx
# 添加人口
add_pop = 10000                     # 添加10000人口（当前人群类型）

# 添加特定类型人口
create_pop = {
    pop_type = laborers             # 人群类型
    size = 5000                     # 数量
    culture = han                   # 文化
    religion = buddhist             # 宗教
}

create_pop = {
    pop_type = capitalists
    size = 100
    culture = han
}

```

### 7.4.3 州属性

```pdx
# 设置州类型
set_state_type = incorporated       # 设为整合州
set_state_type = unincorporated     # 设为未整合州
set_state_type = colony             # 设为殖民地

# 添加/移除资源
add_resource = {
    type = iron                     # 资源类型
    amount = 20                     # 数量
}

remove_resource = coal

```

### 7.4.4 在州中添加修正器

```pdx
# 给州添加修正器
add_modifier = {
    name = state_development_boost
    months = 24
}

# 添加激进派/忠诚派
add_radicals_in_state = {
    pop_type = laborers
    value = 1000
}

add_loyalists_in_state = {
    pop_type = capitalists
    value = 500
}

```

---

## 7.5 人群效果（Pop Scope Effects）

### 7.5.1 人口操作

```pdx
# 改变人群规模
change_pop_size = 1000              # 增加1000人
change_pop_size = -500              # 减少500人

# 改变人群类型（升迁/降职）
change_pop_type = capitalists       # 变为资本家
change_pop_type = laborers          # 变为劳工

# 改变文化（同化）
change_culture = han                # 变为汉族
change_culture = british            # 变为英格兰文化

# 改变宗教（改宗）
change_religion = buddhist          # 变为佛教
change_religion = catholic          # 变为天主教

```

### 7.5.2 人群属性

```pdx
# 添加政治倾向
add_political_strength = {
    interest_group = ig_industrialists
    value = 0.1                     # 增加10%政治力量
}

# 添加激进/忠诚
add_radicals = 100                  # 100人变为激进
add_loyalists = 50                  # 50人变为忠诚

```

---

## 7.6 角色效果（Character Scope Effects）

### 7.6.1 角色属性

```pdx
# 添加特质
add_trait = trait_ambitious
add_trait = trait_reckless
add_trait = trait_brave

# 移除特质
remove_trait = trait_ambitious

# 设置角色职位
set_character_role = general        # 设为将军
set_character_role = admiral        # 设为海军将领
set_character_role = politician     # 设为政治家

```

### 7.6.2 角色关系

```pdx
# 设置角色所属利益集团
set_character_interest_group = ig_armed_forces

# 流放角色
exile_character = yes

# 召回流放角色
recall_exile_character = yes

# 杀死角色（自然死亡）
kill_character = yes

```

---

## 7.7 变量系统

### 7.7.1 设置变量

变量用于存储数据，可在后续使用。

```pdx
# 设置普通变量（国家级别）
set_variable = my_variable
set_variable = {
    name = my_variable
    value = 100                 # 设置值为100
}

# 设置带持续时间的变量
set_variable = {
    name = temporary_bonus
    value = 1
    days = 365                  # 持续365天
}

# 设置全局变量（所有国家可见）
set_global_variable = {
    name = world_war_started
    value = 1
}

# 设置局部变量（临时）
set_local_variable = {
    name = temp_value
    value = 50
}

```

### 7.7.2 修改变量

```pdx
# 改变变量值
change_variable = {
    name = my_variable
    add = 10                    # 加10
}

change_variable = {
    name = my_variable
    subtract = 5                # 减5
}

change_variable = {
    name = my_variable
    multiply = 2                # 乘2
}

change_variable = {
    name = my_variable
    divide = 2                  # 除2
}

# 直接设置新值
set_variable = {
    name = my_variable
    value = 200                 # 设为200（覆盖原值）
}

```

### 7.7.3 移除变量

```pdx
# 移除变量
remove_variable = my_variable
remove_global_variable = world_war_started
remove_local_variable = temp_value

```

### 7.7.4 使用变量

```pdx
# 在效果中使用变量值
add_treasury = var:my_variable      # 添加变量值的金额

# 在比较中使用
if = {
    limit = {
        var:my_variable >= 100
    }
    # 执行效果
}

```

---

## 7.8 创建和删除对象

### 7.8.1 创建国家

```pdx
# 创建新国家
create_country = {
    tag = JAP                     # 国家代码
    origin = c:CHI                # 来源国家
    state = s:STATE_BEIJING       # 首都在哪个州
    culture = han                 # 主要文化
}

# 创建附属国
create_subject = {
    country = c:KOR
    type = subject_type:puppet
}

```

### 7.8.2 创建角色

```pdx
# 创建角色
create_character = {
    first_name = "John"
    last_name = "Smith"
    age = 35
    culture = british
    religion = protestant
    ig_leader = yes               # 设为利益集团领袖
    interest_group = ig_industrialists
    ideology = ideology_liberal
    traits = {
        trait_ambitious
        trait_expert_politician
    }
}

# 创建将军
create_character = {
    first_name = "Arthur"
    last_name = "Wellesley"
    culture = british
    is_general = yes
    commander_rank = 3            # 指挥官等级
    traits = {
        trait_defensive_expert
    }
}

```

### 7.8.3 触发事件

```pdx
# 触发事件（当前国家）
trigger_event = {
    id = my_event.2               # 事件ID
}

# 延迟触发
trigger_event = {
    id = my_event.3
    days = 30                     # 30天后触发
}

# 触发事件给其他国家
c:GBR = {
    trigger_event = {
        id = my_event.4
        popup = yes               # 弹出显示
    }
}

# 随机事件
random_events = {
    50 = my_event.5               # 50%概率触发
    30 = my_event.6               # 30%概率触发
    20 = 0                        # 20%概率不触发
}

```

### 7.8.4 添加日志条目

```pdx
# 添加日志条目
add_journal_entry = {
    type = my_journal_entry       # 日志条目类型
}

# 结束日志条目
end_journal_entry = my_journal_entry

```

---

## 7.9 条件效果（If/Else）

### 7.9.1 基本If语句

```pdx
# 如果条件满足，执行效果
if = {
    limit = {
        treasury > 1000
    }
    add_prestige = 100
}

```

### 7.9.2 If-Else语句

```pdx
# 如果满足条件执行A，否则执行B
if = {
    limit = {
        country_rank = rank_value:great_power
    }
    add_prestige = 200          # 列强获得200威望
}
else = {
    add_prestige = 100          # 其他国家获得100威望
}

```

### 7.9.3 多分支If-ElseIf-Else

```pdx
# 多条件判断
if = {
    limit = {
        country_rank = rank_value:great_power
    }
    add_treasury = 1000         # 列强
}
else_if = {
    limit = {
        country_rank = rank_value:major_power
    }
    add_treasury = 500          # 次强
}
else_if = {
    limit = {
        country_rank = rank_value:minor_power
    }
    add_treasury = 250          # 小国
}
else = {
    add_treasury = 100          # 其他
}

```

### 7.9.4 嵌套If语句

```pdx
# 嵌套条件
if = {
    limit = {
        is_at_war = no
    }

    if = {
        limit = {
            treasury > 1000
        }
        add_technology = railroad
    }
    else = {
        add_treasury = 200
    }
}

```

---

## 7.10 实战案例

### 案例1：完整的洋务运动事件

```pdx
namespace = qing_reform

qing_reform.1 = {
    type = country_event
    title = qing_reform.1.t
    desc = qing_reform.1.d

    # 触发条件
    trigger = {
        this = c:CHI
        year >= 1860
        year <= 1880
        treasury >= 500
        is_at_war = no
        NOT = { has_variable = qing_reform_started }
    }

    # 立即效果
    immediate = {
        set_variable = qing_reform_started

        # 花费资金
        add_treasury = -500

        # 添加修正器
        add_modifier = {
            name = qing_self_strengthening
            months = 60
        }

        # 保存统治者
        ruler = {
            save_scope_as = reform_emperor
        }
    }

    # 选项A：重点发展军事
    option = {
        name = qing_reform.1.a
        default_option = yes

        # 研究军事科技
        add_technology = percussion_cap
        add_technology = breech_loading_artillery

        # 在首都建兵工厂
        capital = {
            add_building = building_arms_industry
        }

        # 添加军事修正器
        add_modifier = {
            name = qing_military_focus
            months = 36
        }
    }

    # 选项B：重点发展经济
    option = {
        name = qing_reform.1.b

        trigger = {
            treasury >= 300     # 需要额外资金
        }

        # 花费额外资金
        add_treasury = -300

        # 研究经济科技
        add_technology = railroad
        add_technology = steel

        # 在沿海州建工厂
        every_scope_state = {
            limit = { is_coastal = yes }
            add_building = building_textile_mills
        }

        # 添加经济修正器
        add_modifier = {
            name = qing_economic_focus
            months = 36
        }
    }

    # 选项C：平衡发展（需要更高条件）
    option = {
        name = qing_reform.1.c

        trigger = {
            treasury >= 800
            any_scope_state = {
                count >= 5
                is_coastal = yes
            }
        }

        # 花费大量资金
        add_treasury = -800

        # 研究多项科技
        add_technology = railroad
        add_technology = steel
        add_technology = percussion_cap

        # 在全国建建筑
        every_scope_state = {
            limit = { is_coastal = yes }
            add_building = building_textile_mills
        }

        capital = {
            add_building = building_arms_industry
            add_building = building_steel_mills
        }

        # 添加综合修正器
        add_modifier = {
            name = qing_balanced_reform
            months = 48
        }

        # 触发后续事件
        trigger_event = {
            id = qing_reform.2
            days = 365
        }
    }
}

```

### 案例2：工业化决策

```pdx
# 决策定义
my_mod_industrialization = {
    is_shown = {
        exists = yes
    }

    possible = {
        country_rank = rank_value:great_power
        has_technology_researched = railroad
        treasury >= 1000
        is_at_war = no
    }

    when_taken = {
        # 花费资金
        add_treasury = -1000

        # 研究工业科技
        if = {
            limit = {
                NOT = { has_technology_researched = steel }
            }
            add_technology = steel
        }

        # 在所有工业州建工厂
        every_scope_state = {
            limit = {
                any_scope_building = {
                    OR = {
                        is_building_type = building_coal_mine
                        is_building_type = building_iron_mine
                    }
                }
            }

            add_building = building_steel_mills
            add_building = building_chemical_plants
        }

        # 添加工业化修正器
        add_modifier = {
            name = rapid_industrialization
            months = 24
        }

        # 添加激进派（工业化代价）
        add_radicals_in_country = {
            value = 0.02
        }

        # 设置变量防止重复
        set_variable = {
            name = industrialization_started
            value = 1
        }
    }

    ai_chance = {
        base = 10
        modifier = {
            trigger = { treasury > 2000 }
            add = 20
        }
    }
}

```

### 案例3：动态事件链

```pdx
# 事件1：改革开始
qing_reform.1 = {
    type = country_event
    title = qing_reform.1.t
    desc = qing_reform.1.d

    immediate = {
        set_variable = {
            name = reform_progress
            value = 0
        }
    }

    option = {
        name = qing_reform.1.a

        # 开始改革
        add_treasury = -200
        change_variable = {
            name = reform_progress
            add = 20
        }

        # 触发下一步
        trigger_event = {
            id = qing_reform.2
            days = 180
        }
    }
}

# 事件2：改革进展
qing_reform.2 = {
    type = country_event
    title = qing_reform.2.t
    desc = qing_reform.2.d

    trigger = {
        var:reform_progress >= 20
    }

    immediate = {
        change_variable = {
            name = reform_progress
            add = 20
        }
    }

    option = {
        name = qing_reform.2.a

        # 继续投资
        add_treasury = -200

        # 根据进度给予不同奖励
        if = {
            limit = {
                var:reform_progress >= 60
            }
            add_technology = steel
        }

        # 触发下一步或结束
        if = {
            limit = {
                var:reform_progress >= 100
            }
            trigger_event = qing_reform.3    # 完成事件
        }
        else = {
            trigger_event = {
                id = qing_reform.2
                days = 180
            }
        }
    }

    option = {
        name = qing_reform.2.b

        # 停止改革
        remove_variable = reform_progress
        add_radicals_in_country = {
            value = 0.03
        }
    }
}

# 事件3：改革完成
qing_reform.3 = {
    type = country_event
    title = qing_reform.3.t
    desc = qing_reform.3.d

    immediate = {
        remove_variable = reform_progress
    }

    option = {
        name = qing_reform.3.a

        add_prestige = 500
        add_modifier = {
            name = successful_reform
            months = 60
        }
    }
}

```

---

## 7.11 常见错误与最佳实践

### 7.11.1 常见错误

#### 错误1：在错误作用域使用效果

❌ **错误**：

```pdx
state = {
    add_treasury = 1000     # 错误！州没有国库
}

```

✅ **正确**：

```pdx
country = {
    add_treasury = 1000
}

```

#### 错误2：效果参数错误

❌ **错误**：

```pdx
add_modifier = my_modifier      # 错误！缺少参数

```

✅ **正确**：

```pdx
add_modifier = {
    name = my_modifier
    months = 12
}

```

#### 错误3：变量未定义就使用

❌ **错误**：

```pdx
effect = {
    change_variable = {         # 错误！变量未设置
        name = my_var
        add = 10
    }
}

```

✅ **正确**：

```pdx
immediate = {
    set_variable = {
        name = my_var
        value = 0               # 先初始化
    }
}

effect = {
    change_variable = {
        name = my_var
        add = 10
    }
}

```

#### 错误4：触发事件循环

❌ **错误**：

```pdx
# 事件A触发事件B，事件B又触发事件A（无限循环）
qing_reform.1 = {
    option = {
        trigger_event = qing_reform.2
    }
}

qing_reform.2 = {
    option = {
        trigger_event = qing_reform.1  # 错误！循环
    }
}

```

✅ **正确**：

```pdx
# 使用变量确保只触发一次
qing_reform.1 = {
    trigger = {
        NOT = { has_variable = reform_started }
    }
    immediate = {
        set_variable = reform_started
    }
    option = {
        trigger_event = qing_reform.2
    }
}

```

### 7.11.2 最佳实践

#### 1. 使用注释说明复杂逻辑

```pdx
effect = {
    # 阶段1：扣除成本
    add_treasury = -500

    # 阶段2：给予奖励
    add_prestige = 100
    add_technology = railroad

    # 阶段3：设置标记防止重复
    set_variable = {
        name = event_completed
        value = 1
    }
}

```

#### 2. 检查前置条件

```pdx
option = {
    name = my_event.1.a

    trigger = {
        # 检查是否有足够资金
        treasury >= 500
    }

    # 再次检查，确保执行时仍有资金
    if = {
        limit = { treasury >= 500 }
        add_treasury = -500
    }
}

```

#### 3. 使用有意义的变量名

```pdx
# 好
set_variable = qing_reform_progress
set_variable = industrialization_level

# 不好
set_variable = var1
set_variable = temp

```

#### 4. 测试极端情况

```pdx
# 测试：国库为0时
effect = {
    add_treasury = -500     # 会变成负数吗？
}

# 测试：人口为0的州
effect = {
    add_radicals = {
        pop_type = laborers
        value = 1000
    }
}

```

---

## 本章小结

- **效果**是实际改变游戏状态的命令，与只检查状态的触发器不同
- **国家效果**：资金、威望、科技、法律、外交、战争、修正器
- **州效果**：建筑、人口、州属性
- **人群效果**：人口规模、类型、文化、宗教
- **角色效果**：特质、职位、关系
- **变量系统**：set_variable、change_variable、remove_variable
- **条件效果**：if/else/elseif 实现条件执行
- **创建对象**：create_country、create_character、trigger_event
- **最佳实践**：使用注释、检查条件、合理命名、测试极端情况

---

## 常见问题

**Q：效果和触发器有什么区别？**

A：
- **触发器（Trigger）**：检查条件，返回真/假，不改变游戏状态
- **效果（Effect）**：执行操作，实际改变游戏状态

**Q：我可以在触发器中使用效果吗？**

A：不可以。触发器只能检查状态。要执行效果，使用`immediate`、`option`、`when_taken`等效果块。

**Q：为什么我的效果没有生效？**

A：检查以下几点：
1. 是否在正确的作用域中？
2. 效果语法是否正确？
3. 是否有足够的资源（如资金）？
4. 查看`error.log`文件

**Q：变量可以存储什么类型的数据？**

A：变量可以存储数字（整数或小数）。要存储作用域，使用`save_scope_as`。

**Q：如何确保事件只触发一次？**

A：使用变量标记：

```pdx
trigger = {
    NOT = { has_variable = event_fired }
}

immediate = {
    set_variable = event_fired
}

```

**Q：效果执行失败会报错吗？**

A：大多数效果失败会静默失败（不报错），但会在`error.log`中记录警告。建议开启调试模式查看详细信息。

---

## 练习建议

1. **基础练习**：编写一个简单事件，要求：
   - 给国家添加1000资金
   - 在首都添加一个建筑
   - 设置一个变量标记

2. **条件练习**：使用if/else编写效果：
   - 如果是列强，添加500威望
   - 如果是次强，添加250威望
   - 否则添加100威望

3. **事件链练习**：创建一个3步事件链：
   - 事件1：开始项目，扣除资金
   - 事件2（30天后）：项目进展，选择继续或放弃
   - 事件3（60天后）：项目完成，给予奖励

4. **综合练习**：创建一个"工业化冲刺"决策：
   - 需要：列强、铁路科技、2000资金
   - 效果：研究钢铁科技、在所有有铁矿的州建钢厂、添加工业化修正器
   - 限制：只能使用一次

---

> 📖 **下一章预告**：在下一章，我们将学习**变量系统（Variable）**——存储和操作数据的进阶技巧。

---

## 参考

- [Victoria 3 Wiki - Effect](https://vic3.paradoxwikis.com/Effect)
- [Victoria 3 Wiki - Variable](https://vic3.paradoxwikis.com/Variable)
- 附录C - 效果命令大全
