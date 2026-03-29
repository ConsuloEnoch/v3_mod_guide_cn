# 第22章：文化与宗教（Culture & Religion）——定义新文化/宗教

> 本章将讲解如何定义新的文化和宗教，包括文化特征、歧视特质和宗教属性。通过学习本章，你将能够创建多样化的文化和宗教系统。

## 本章目标

完成本章学习后，你将能够：
- 理解文化和宗教的定义方式
- 创建新的文化及其特征
- 设置文化间的歧视关系
- 定义新的宗教及其属性
- 实战创建"客家人"新文化

---

## 22.1 文化基础

### 22.1.1 文件位置

```pdx
my_mod/common/cultures/               # 文化定义
my_mod/common/religions/              # 宗教定义

```

### 22.1.2 文化的作用

文化影响：
- 人群的政治倾向
- 可接受的人口类型
- 国家的主要民族认同
- 歧视和同化机制

---

## 22.2 文化定义

### 22.2.1 基本结构

```pdx
# common/cultures/my_mod_cultures.txt

culture_example = {
    # 颜色（地图显示）
    color = rgb{ 200 150 100 }

    # 宗教（默认）
    religion = protestant

    # 特征（用于歧视判断）
    traits = {
        european_heritage
        german_speaking
    }

    # 男性名字列表
    male_names = {
        John James William "Alexander" "Frederick"
    }

    # 女性名字列表
    female_names = {
        Mary Elizabeth Catherine "Victoria" "Alexandra"
    }

    # 姓氏列表
    family_names = {
        Smith Johnson Williams "Brown" "Jones"
    }

    # 文化母国（用于分离主义）
    homeland = STATE_EXAMPLE
}

```

### 22.2.2 文化特征

文化特征用于定义歧视关系：

```pdx
# common/culture_traits.txt

european_heritage = {
    # 欧洲文化遗产
    graphic = "european"
}

east_asian_heritage = {
    graphic = "asian"
}

chinese_speaking = {
    # 汉语系
}

german_speaking = {
    # 德语系
}

```

---

## 22.3 歧视系统

### 22.3.1 歧视特质

定义哪些特征会导致歧视：

```pdx
# common/discrimination_traits.txt

discrimination_trait_example = {
    # 被歧视的特征
    trait = non_european

    # 歧视者
    discriminator = european_heritage

    # 描述
    desc = "Discriminated against by Europeans"
}

```

### 22.3.2 文化间关系

```pdx
# 在文化定义中

culture_han = {
    # ...

    traits = {
        east_asian_heritage
        chinese_speaking
    }

    # 不会被这些文化歧视
    not_discriminated_by = {
        manchu
        mongol
    }
}

```

---

## 22.4🎯 **实战**：创建"客家人"文化

### 22.4.1 设计思路

客家人（Hakka）是中国汉族的重要支系：
- 语言：客家话（与官话不同）
- 分布：广东、福建、江西、台湾
- 特点：重视教育、商业头脑、凝聚力强
- 历史：太平天国运动领袖多为客家人

### 22.4.2 文化定义

**文件**：`common/cultures/hakka_culture.txt`

```pdx
culture_hakka = {
    # 颜色：使用独特的褐色
    color = rgb{ 139 90 43 }

    # 宗教：与汉族相同
    religion = mahayana

    # 特征
    traits = {
        east_asian_heritage
        chinese_speaking
        hakka_speaking        # 新增特征
    }

    # 男性名字（传统客家名）
    male_names = {
        "Yuan" "Tai" "Cheng" "Fa" "Wing"
        "Ming" "Ho" "Kin" "Man" "Wai"
        "Chung" "Shing" "Lok" "Hong" "Woon"
    }

    # 女性名字
    female_names = {
        "Mei" "Ling" "Fong" "Ying" "Lan"
        "Yuk" "Hing" "Mui" "Sim" "Fun"
        "Wah" "Sau" "Lai" "King" "Chun"
    }

    # 姓氏（典型客家姓）
    family_names = {
        "Chen" "Lin" "Huang" "Zhang" "Li"
        "Wang" "Liu" "Yang" "Zhao" "Wu"
        "Xu" "Sun" "Ma" "Zhu" "Hu"
        "Guo" "He" "Gao" "Luo" "Zheng"
        "Liang" "Xie" "Song" "Tang" "Xu"
        "Deng" "Feng" "Han" "Cao" "Zeng"
        "Peng" "Xiao" "Cai" "Pan" "Tian"
        "Dong" "Yuan" "Yu" "Ye" "Jiang"
        "Du" "Su" "Wei" "Cheng" "Lu"
        "Shen" "Fu" "Liao" "Jian" "Wei"
    }

    # 文化母国
    homeland = STATE_GUANGDONG
    homeland = STATE_FUJIAN
    homeland = STATE_JIANGXI
    homeland = STATE_TAIWAN
}

```

### 22.4.3 文化特征定义

**文件**：`common/culture_traits/hakka_traits.txt`

```pdx
hakka_speaking = {
    graphic = "asian"

    # 描述
    desc = "Hakka speaking culture"
}

```

### 22.4.4 歧视特质

**文件**：`common/discrimination_traits/hakka_discrimination.txt`

```pdx
# 客家人可能被其他汉语群体轻微歧视
# （实际上在现实中歧视较少，但语言差异存在）

hakka_minority = {
    trait = hakka_speaking

    discriminator = chinese_speaking

    desc = "Language barrier with other Chinese groups"

    # 轻度歧视
    severity = minor
}

```

### 22.4.5 本地化

**文件**：`localization/simp_chinese/hakka_culture_l_simp_chinese.yml`

```yaml
l_simp_chinese:
 culture_hakka:0 "客家人"
 culture_hakka_adj:0 "客家"
 culture_hakka_collective_noun:0 "客家人"
 culture_hakka_desc:0 "客家人是汉族的重要支系，以其独特的语言、重视教育和强烈的族群认同而闻名。历史上，客家人在太平天国运动中发挥了重要作用。"

 hakka_speaking:0 "客家语系"

 hakka_minority:0 "客家少数群体"
 hakka_minority_desc:0 "由于语言和文化差异，客家人在某些地区可能面临轻微的文化隔阂。"

```

### 22.4.6 州设置

**文件**：`common/history/pops/hakka_population.txt`

```pdx
POPS = {
    # 广东客家人
    s:STATE_GUANGDONG = {
        pop = {
            culture = hakka
            religion = mahayana
            size = 5000000            # 广东有500万客家人

            pop_type = farmers
            proportion = 0.6
        }

        pop = {
            culture = hakka
            size = 2000000

            pop_type = shopkeepers    # 客家人善于经商
            proportion = 0.15
        }
    }

    # 福建客家人
    s:STATE_FUJIAN = {
        pop = {
            culture = hakka
            religion = mahayana
            size = 3000000

            pop_type = farmers
            proportion = 0.7
        }
    }

    # 江西客家人
    s:STATE_JIANGXI = {
        pop = {
            culture = hakka
            religion = mahayana
            size = 4000000

            pop_type = farmers
            proportion = 0.8
        }
    }

    # 台湾客家人
    s:STATE_TAIWAN = {
        pop = {
            culture = hakka
            religion = mahayana
            size = 800000

            pop_type = farmers
            proportion = 0.5
        }

        pop = {
            culture = hakka
            size = 200000

            pop_type = laborers
            proportion = 0.2
        }
    }
}

```

---

## 22.5 宗教定义

### 22.5.1 基本结构

```pdx
# common/religions/my_mod_religions.txt

religion_example = {
    # 纹理
    texture = "gfx/interface/icons/religion_icons/example.dds"

    # 颜色
    color = { 200 100 50 }

    # 特征
    traits = {
        christian
        monotheist
    }

    # 不受哪些宗教歧视
    not_discriminated_by = {
        catholic
        protestant
    }
}

```

### 22.5.2🎯 **实战**：定义"道教"宗教

**文件**：`common/religions/taoism.txt`

```pdx
religion_taoism = {
    texture = "gfx/interface/icons/religion_icons/taoism.dds"

    color = { 0 128 128 }        # 青色（道教颜色）

    traits = {
        eastern
        animist
    }

    # 不受佛教和儒教歧视
    not_discriminated_by = {
        buddhist
        confucian
    }
}

```

### 22.5.3 本地化

```yaml
l_simp_chinese:
 religion_taoism:0 "道教"
 religion_taoism_desc:0 "中国传统宗教，强调天人合一、道法自然。"

```

---

## 22.6 文化与国家

### 22.6.1 多文化国家

```pdx
# 在country_definitions中
JNP = {
    # 江南共和国接受多种文化
    cultures = { han hakka yue }

    # 或者指定主要文化
    primary_culture = han
    accepted_cultures = { hakka yue }
}

```

### 22.6.2 文化同化

```pdx
effect = {
    # 同化人群
    every_scope_pop = {
        limit = { culture = hakka }
        change_culture = han
    }
}

```

---

## 本章小结

- **文化定义**：在`common/cultures/`，包含颜色、宗教、特征、名字
- **文化特征**：用于定义歧视关系
- **歧视系统**：定义哪些特征会被歧视
- **宗教定义**：在`common/religions/`，简单直接
- **实战案例**：完整的"客家人"文化系统

---

## 参考

- [Victoria 3 Wiki - Culture modding](https://vic3.paradoxwikis.com/Culture_modding)
- [Victoria 3 Wiki - Religion modding](https://vic3.paradoxwikis.com/Religion_modding)
