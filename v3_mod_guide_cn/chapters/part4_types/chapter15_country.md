# 第15章：国家（Country）——定义新国家

> 本章将详细讲解如何定义和修改国家，包括国家类型、等级、文化、宗教等属性。通过学习本章，你将能够创建全新的国家或修改现有国家的设定。

## 本章目标

完成本章学习后，你将能够：
- 理解国家定义文件的结构
- 掌握国家类型和等级的区别
- 设置国家的首都、文化和宗教
- 配置国家的初始科技和法律
- 创建全新的国家定义

---

## 15.1 国家定义基础

### 15.1.1 文件位置

国家定义文件存放在：

```pdx
my_mod/common/country_definitions/    # 国家基本定义
my_mod/common/history/countries/      # 开局历史设置
my_mod/common/country_formation/      # 国家形成条件

```

### 15.1.2 基本结构

```pdx
# common/country_definitions/my_mod_countries.txt

# 国家代码（必须3个字母）
TAG = {
    color = { 147 130 110 }           # 地图颜色（RGB）
    country_type = recognized         # 国家类型
    tier = empire                     # 国家等级
    cultures = { north_german }       # 主要文化
    capital = STATE_BRANDENBURG       # 首都州
    religion = protestant             # 国教（可选）
}

```

### 15.1.3 最小国家定义

最简单的完整国家定义：

```pdx
# 江南共和国
JNP = {
    color = { 100 149 237 }           # 天蓝色
    country_type = recognized
    tier = kingdom
    cultures = { han }
    capital = STATE_JIANGSU
}

```

---

## 15.2 国家属性详解

### 15.2.1 国家代码（TAG）

**TAG**是国家的唯一标识符：
- 必须**3个字母**
- 必须**大写**
- 必须**唯一**

```pdx
✅ 正确：CHI、GBR、FRA、JNP
❌ 错误：china、CHINA、C、TOOLONG

```

**常用国家TAG**：
| 国家 | TAG | 国家   | TAG |
| ---- | --- | ------ | --- |
| 大清 | CHI | 英国   | GBR |
| 法国 | FRA | 俄国   | RUS |
| 美国 | USA | 普鲁士 | PRU |
| 日本 | JAP | 奥地利 | AUS |

### 15.2.2 地图颜色（color）

定义国家在大地图上的颜色：

```pdx
# RGB格式（0-255）
color = { 147 130 110 }

# HSV格式（0.0-1.0）
color = hsv{ 0.5 0.7 0.8 }

# HSV360格式（色相0-360，饱和度0-100，明度0-100）
color = hsv360{ 200 70 80 }

```

**颜色选择建议**：
- 避免与邻国颜色过于相似
- 使用符合历史或文化特征的颜色
- 确保颜色在游戏地图上清晰可见

### 15.2.3 国家类型（country_type）

决定国家的外交地位：

| 类型            | 说明                   | 示例                   |
| --------------- | ---------------------- | ---------------------- |
| `recognized`    | 被认可国家（完全主权） | 英国、法国、大清       |
| `unrecognized`  | 未认可国家（有限主权） | 波斯、暹罗、埃塞俄比亚 |
| `decentralized` | 分散国家（部落联盟）   | 非洲部落、美洲原住民   |
| `colonial`      | 殖民地（特殊类型）     | -                      |

```pdx
# 被认可大国
country_type = recognized

# 未认可国家（游戏初期会被列强欺负）
country_type = unrecognized

# 分散部落
country_type = decentralized

```

### 15.2.4 国家等级（tier）

决定国家的声望等级：

| 等级           | 说明   | 示例               |
| -------------- | ------ | ------------------ |
| `empire`       | 帝国   | 大清、英国、俄国   |
| `kingdom`      | 王国   | 普鲁士、西班牙     |
| `duchy`        | 公国   | 巴伐利亚、萨克森   |
| `principality` | 亲王国 | 摩纳哥、列支敦士登 |
| `city_state`   | 城邦   | 威尼斯、汉堡       |

```pdx
# 帝国
tier = empire

# 王国
tier = kingdom

# 公国
tier = duchy

```

### 15.2.5 主要文化（cultures）

定义国家的主体民族：

```pdx
# 单一文化
cultures = { han }

# 多文化国家
cultures = { north_german south_german }

# 奥匈帝国式多文化
cultures = { austrian hungarian czech }

```

### 15.2.6 首都（capital）

定义国家的默认首都：

```pdx
# 使用州区域代码
capital = STATE_BEIJING
capital = STATE_LONDON
capital = STATE_PARIS

```

> ⚠️ **注意**：首都必须是`common/strategic_regions/`中定义的州区域。

### 15.2.7 国教（religion）

可选，默认使用第一个主要文化的宗教：

```pdx
# 明确指定国教
religion = protestant
religion = catholic
religion = buddhist
religion = muslim

```

---

## 15.3 国家历史设置

### 15.3.1 开局设置文件

国家开局设置在`common/history/countries/`：

```pdx
# common/history/countries/my_mod_country_setup.txt

TAG = {
    # 初始资金
    add_treasury = 1000

    # 初始科技
    effect = {
        set_technology = {
            railroad = 1
            steel = 1
        }
    }

    # 初始法律
    activate_law = law_type:law_monarchy
    activate_law = law_type:law_autocracy
    activate_law = law_type:law_serfdom

    # 初始关系
    set_relations = { country = c:GBR value = 50 }

    # 初始利益集团势力
    ig:ig_landowners = { set_ig_bolstering = yes }
    ig:ig_industrialists = { set_ig_bolstering = yes }
}

```

### 15.3.2 完整历史设置示例

```pdx
# 江南共和国开局设置
JNP = {
    # 1836年开局
    add_treasury = 800
    add_prestige = 100

    # 科技
    effect = {
        set_technology = { railroad = 1 }
        set_technology = { steel = 1 }
    }

    # 法律
    activate_law = law_type:law_monarchy
    activate_law = law_type:law_oligarchy
    activate_law = law_type:law_mercantilism
    activate_law = law_type:law_serfdom

    # 初始建筑
    effect = {
        every_scope_state = {
            add_building = building_iron_mine
            add_building = building_textile_mills
        }
    }
}

```

---

## 15.4 国家形成

### 15.4.1 国家形成定义

定义哪些州可以形成某个国家：

```pdx
# common/country_formation/my_mod_formations.txt

JNP = {
    # 使用文化母国自动确定州
    use_culture_states = yes

    # 或者手动指定州
    states = {
        STATE_JIANGSU
        STATE_ZHEJIANG
        STATE_ANHUI
    }

    # 需要的州比例（默认0.75）
    required_states_fraction = 0.6

    # 额外条件
    possible = {
        country_rank >= rank_value:minor_power
        is_subject = no
    }

    # AI形成意愿
    ai_will_do = { always = yes }
}

```

### 15.4.2 可形成国家类型

| 类型     | 说明           | 示例               |
| -------- | -------------- | ------------------ |
| 文化统一 | 同文化国家统一 | 德国、意大利       |
| 区域统一 | 特定区域统一   | 巴尔干联邦         |
| 帝国重建 | 重建历史帝国   | 罗马帝国、蒙古帝国 |

---

## 15.5🎯 **实战**：创建"江南共和国"

### 15.5.1 设计思路

假设历史分歧点：太平天国运动后，江南地区脱离清朝独立。

**国家设定**：
- TAG：JNP（Jiangnan Republic）
- 领土：江苏、浙江、安徽
- 首都：南京（STATE_JIANGSU）
- 文化：汉族
- 类型：被认可国家
- 等级：王国

### 15.5.2 国家定义

**文件**：`common/country_definitions/jiangnan_republic.txt`

```pdx
# 江南共和国
JNP = {
    # 地图颜色：天蓝色（代表江南水乡）
    color = { 100 149 237 }

    # 被认可国家
    country_type = recognized

    # 王国等级
    tier = kingdom

    # 汉族为主
    cultures = { han }

    # 首都在江苏（南京）
    capital = STATE_JIANGSU
}

```

### 15.5.3 开局历史设置

**文件**：`common/history/countries/jiangnan_republic_setup.txt`

```pdx
JNP = {
    # 初始资源
    add_treasury = 800
    add_prestige = 150

    # 科技水平（比大清略先进）
    effect = {
        set_technology = { railroad = 1 }
        set_technology = { steel = 1 }
        set_technology = { pump_extraction = 1 }
    }

    # 政治制度（君主立宪倾向）
    activate_law = law_type:law_monarchy
    activate_law = law_type:law_landed_voting
    activate_law = law_type:law_freedom_of_conscience
    activate_law = law_type:law_mercantilism
    activate_law = law_type:law_interventionism
    activate_law = law_type:law_censorship

    # 初始外交关系
    set_relations = { country = c:CHI value = -50 }
    set_relations = { country = c:GBR value = 30 }
    set_relations = { country = c:FRA value = 20 }

    # 初始修正器
    add_modifier = {
        name = newly_independent
        months = 24
    }

    # 初始利益集团
    effect = {
        ig:ig_industrialists = {
            set_ig_bolstering = yes
        }
        ig:ig_landowners = {
            set_ig_suppression = yes
        }
    }
}

```

### 15.5.4 州设置

**文件**：`common/history/states/jiangnan_states.txt`

```pdx
# 设置江南共和国的州

STATES = {
    s:STATE_JIANGSU = {
        create_country = {
            country = c:JNP
            owned_states = {
                STATE_JIANGSU
                STATE_ZHEJIANG
                STATE_ANHUI
            }
        }

        # 人口
        set_population = {
            culture = han
            size = 25000000
        }

        # 初始建筑
        create_building = {
            building = building_textile_mills
            level = 5
        }
        create_building = {
            building = building_steel_mills
            level = 3
        }
        create_building = {
            building = building_port
            level = 2
        }
    }

    s:STATE_ZHEJIANG = {
        set_population = {
            culture = han
            size = 15000000
        }

        create_building = {
            building = building_textile_mills
            level = 3
        }
        create_building = {
            building = building_port
            level = 2
        }
    }

    s:STATE_ANHUI = {
        set_population = {
            culture = han
            size = 12000000
        }

        create_building = {
            building = building_agriculture
            level = 4
        }
    }
}

```

### 15.5.5 本地化文件

**文件**：`localization/simp_chinese/jiangnan_republic_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 # 国家名称
 JNP:0 "江南共和国"
 JNP_ADJ:0 "江南"

 # 国家描述（选择国家时显示）
 je_making_jiangnan_republic_desc:0 "在太平天国运动后，江南地区宣布独立，建立了一个以工商立国的现代化政权。"

 # 国家形成
 form_jiangnan_republic:0 "成立江南共和国"
 form_jiangnan_republic_desc:0 "统一江南地区，建立一个现代化的工商国家。"

 # 修正器
 newly_independent:0 "新近独立"
 newly_independent_desc:0 "这个国家刚刚获得独立，人民充满热情，但也面临许多挑战。"

```

### 15.5.6 创建事件链

**文件**：`events/jiangnan_independence.txt`

```pdx
namespace = jiangnan_independence

# 独立宣言事件
jiangnan_independence.1 = {
    type = country_event

    title = jiangnan_independence.1.t
    desc = jiangnan_independence.1.d

    trigger = {
        this = c:JNP
        year = 1836
        month = 1
    }

    fire_only_once = yes

    immediate = {
        set_variable = jiangnan_independent
    }

    option = {
        name = jiangnan_independence.1.a

        add_prestige = 100
        add_modifier = {
            name = newly_independent
            months = 24
        }

        # 与大清关系恶化
        c:CHI = {
            change_relations = {
                target = root
                value = -50
            }
        }
    }
}

```

---

## 15.6 国家修改技巧

### 15.6.1 修改现有国家

```pdx
# 修改大清开局设置
CHI = {
    # 增加初始资金
    add_treasury = 500

    # 增加初始科技
    effect = {
        set_technology = { railroad = 1 }
    }

    # 修改法律
    activate_law = law_type:law_monarchy
}

```

### 15.6.2 创建历史替代国家

```pdx
# 假设太平天国成功
TAIP = {
    color = { 200 50 50 }
    country_type = recognized
    tier = empire
    cultures = { han }
    capital = STATE_JIANGSU
}

```

---

## 本章小结

- **国家定义**：在`common/country_definitions/`中设置基本属性
- **必要属性**：TAG、color、country_type、tier、cultures、capital
- **可选属性**：religion、is_named_from_capital等
- **历史设置**：在`common/history/countries/`中设置开局状态
- **国家形成**：在`common/country_formation/`中定义统一条件
- **实战案例**：完整创建了"江南共和国"Mod

---

## 常见问题

**Q：国家代码必须是3个字母吗？**

A：是的，必须是3个大写字母。

**Q：如何找到州区域代码？**

A：查看`common/strategic_regions/`文件夹中的文件。

**Q：可以修改游戏原有国家吗？**

A：可以，在Mod中重新定义或使用history文件修改开局设置。

**Q：国家颜色可以游戏中更改吗？**

A：可以通过脚本修改，但会在重新加载时重置为定义值。

---

## 参考

- [Victoria 3 Wiki - Country modding](https://vic3.paradoxwikis.com/Country_modding)
