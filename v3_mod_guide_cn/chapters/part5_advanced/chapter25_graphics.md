# 第二十五章：图形资源

## 本章目标

学习本章后，你将能够：
- 理解DDS图像格式和导出方法
- 创建和修改国家旗帜
- 了解3D模型的基本结构
- 为Mod添加自定义图形资源
- 掌握图形资源的最佳实践

---

## 概念讲解：图形资源是什么？

### 比喻：游戏是一张巨大的拼图

想象一下，维多利亚3就像一张巨大的拼图：
- **旗帜** = 每块拼图的独特标识
- **建筑模型** = 拼图上的立体建筑
- **界面元素** = 拼图的边框和背景
- **事件图片** = 拼图上的精美插画

图形资源就是制作这些拼图块的"原材料"。

### 为什么需要图形资源？

1. **视觉识别**：旗帜让玩家一眼认出国家
2. **沉浸感**：精美的模型和图片增强游戏体验
3. **信息传递**：图标和符号快速传达信息
4. **个性化**：自定义资源让Mod独具特色

---

## 25.1 DDS图像格式

### 25.1.1 什么是DDS？

DDS（DirectDraw Surface）是维多利亚3主要的图像格式。它是一种压缩图像格式，专为游戏优化设计。

💡 **比喻**：DDS就像是专门为游戏引擎设计的"压缩包"，既能保持图像质量，又能快速加载。

### 25.1.2 为什么要用DDS？

| 格式    | 文件大小 | 加载速度 | 游戏兼容性 |
| ------- | -------- | -------- | ---------- |
| PNG     | 大       | 慢       | 差         |
| JPG     | 中       | 中       | 差         |
| **DDS** | **小**   | **快**   | **好**     |

### 25.1.3 图像尺寸要求

⚠️ **重要**：使用DDS格式时，图像尺寸必须满足以下要求：

1. **压缩图像**：分辨率必须是**4的倍数**（如256x256、512x512、1024x1024）
2. **非压缩图像**：可以是任意尺寸
3. **旗帜标准尺寸**：768x512像素（3:2比例）

如果尺寸不符合要求，游戏会显示错误，图像可能出现显示问题。

---

## 25.2 导出DDS图像

### 25.2.1 使用Paint.NET（推荐新手）

Paint.NET是一个免费、易用的图像编辑工具，非常适合DDS导出。

**下载地址**：https://www.getpaint.net/

**安装DDS插件**：
1. 下载DDS插件（.dll文件）
2. 将插件放入Paint.NET的`Effects`文件夹
3. 重启Paint.NET

**导出压缩图像**：

1. 编辑完图像后，选择"文件"→"另存为"
2. 选择格式：DDS
3. 设置选项：
   - **格式**：BC7 (sRGB, DX 11+)
   - **生成Mip Maps**：勾选 ✓
   - **插值算法**：Bicubic（默认）

**导出非压缩图像**：

1. 格式选择：**B8G8R8A8 (Linear, A8R8G8B8)**
2. 同样勾选"生成Mip Maps"

💡 **提示**：Mip Maps是图像的多分辨率版本，让游戏在不同距离显示合适的清晰度。

### 25.2.2 使用GIMP（功能更强大）

GIMP是一个专业级免费图像编辑软件。

**下载地址**：https://www.gimp.org/

**导出设置**：

1. 编辑完成后，选择"文件"→"导出为"
2. 文件名后缀改为`.dds`
3. 导出选项：
   - **压缩**：BC3 / DXT5
   - **生成Mip Maps**：勾选（事件图片除外）
   - **Mip Map滤镜**：Kaiser（推荐）

### 25.2.3 常用工具对比

| 工具      | 优点           | 缺点         | 推荐人群 |
| --------- | -------------- | ------------ | -------- |
| Paint.NET | 简单易用，免费 | 功能较少     | 新手     |
| GIMP      | 功能强大，免费 | 学习曲线陡峭 | 有经验者 |
| Photoshop | 最专业         | 付费         | 专业人士 |

---

## 25.3 旗帜系统

### 25.3.1 旗帜是什么？

在维多利亚3中，旗帜（Coat of Arms，简称CoA）是由多个图形元素组合而成的国家标识。它由以下部分组成：

1. **底纹（Pattern）**：旗帜的背景图案
2. **徽章（Emblem）**：叠加在底纹上的图案
3. **子旗帜（Sub）**：嵌套的其他旗帜

### 25.3.2 旗帜文件位置

```pdx
my_mod/
├── gfx/
│   └── coat_of_arms/
│       ├── patterns/           # 底纹图案
│       ├── colored_emblems/    # 彩色徽章
│       └── textured_emblems/   # 纹理徽章
├── common/
│   └── coat_of_arms/
│       └── coat_of_arms/       # 旗帜定义
└── common/
    └── flag_definitions/       # 旗帜分配规则

```

### 25.3.3 创建旗帜定义

旗帜定义在`common/coat_of_arms/coat_of_arms/`文件夹中。

**基本旗帜结构**：

```pdx
# 文件：common/coat_of_arms/coat_of_arms/00_my_flags.txt

# 江南共和国旗帜
jiangnan_coa = {
    # 底纹 - 使用纯色背景
    pattern = "pattern_solid.tga"
    color1 = "blue"              # 蓝色背景

    # 彩色徽章 - 黄色五角星
    colored_emblem = {
        texture = "ce_star_05.dds"
        color1 = "yellow"

        instance = {
            scale = { 0.5 0.5 }      # 缩放50%
            position = { 0.5 0.4 }   # 中心偏上位置
        }
    }

    # 第二个徽章 - 下方的波浪纹
    colored_emblem = {
        texture = "ce_waves_01.dds"
        color1 = "white"

        instance = {
            scale = { 0.8 0.3 }
            position = { 0.5 0.75 }
        }
    }
}

```

### 25.3.4 底纹（Pattern）详解

底纹是旗帜的基础层，所有其他元素都叠加在它上面。

**底纹特点**：
- 使用`.tga`格式
- 红色通道 → color1
- 黄色通道 → color2
- 白色通道（部分图案）→ color3
- 作为遮罩（mask），控制徽章显示区域

**常用底纹文件**（在游戏`gfx/coat_of_arms/patterns/`中）：

| 文件名                            | 描述   | 颜色数 |
| --------------------------------- | ------ | ------ |
| pattern_solid.tga                 | 纯色   | 1      |
| pattern_horizontal_stripes_01.tga | 横条纹 | 2      |
| pattern_vertical_stripes_01.tga   | 竖条纹 | 2      |
| pattern_quarters_01.tga           | 四分格 | 2      |
| pattern_diagonal_01.tga           | 对角线 | 2      |

### 25.3.5 徽章（Emblem）详解

徽章是叠加在底纹上的图案，分为两类：

**彩色徽章（Colored Emblem）**：
- 可使用颜色遮罩
- 文件前缀：`ce_`
- 可使用color1、color2、color3

**纹理徽章（Textured Emblem）**：
- 直接使用图片
- 文件前缀：`te_`
- 适合复杂图案（如国徽、印章）

**徽章实例（Instance）属性**：

| 属性     | 说明                 | 示例                     |
| -------- | -------------------- | ------------------------ |
| scale    | 缩放比例             | `scale = { 0.5 0.5 }`    |
| position | 位置（相对于左上角） | `position = { 0.5 0.5 }` |
| rotation | 旋转角度（度）       | `rotation = 45`          |

### 25.3.6 子旗帜（Sub）

子旗帜允许在一个旗帜中嵌入另一个旗帜：

```pdx
complex_coa = {
    pattern = "pattern_solid.tga"
    color1 = "red"

    # 嵌入另一个旗帜
    sub = {
        parent = "jiangnan_coa"      # 引用其他旗帜

        instance = {
            scale = { 0.3 0.3 }
            position = { 0.2 0.2 }
        }
    }
}

```

⚠️ **注意**：子旗帜不能再嵌套子旗帜（禁止递归）。

### 25.3.7 旗帜分配规则

在`common/flag_definitions/`中定义国家使用哪个旗帜：

```pdx
# 文件：common/flag_definitions/00_my_flags.txt

# 江南共和国的旗帜规则
JNG = {
    # 默认旗帜
    flag_definition = {
        coa = jiangnan_coa
        priority = 1
    }

    # 共和制旗帜（优先级更高）
    flag_definition = {
        coa = jiangnan_coa_republic
        priority = 10

        trigger = {
            coa_def_republic_flag_trigger = yes
        }
    }

    # 革命旗帜
    flag_definition = {
        coa = jiangnan_coa_revolutionary
        priority = 100

        trigger = {
            is_revolutionary = yes
        }
    }
}

```

**关键参数**：

| 参数                  | 说明                     |
| --------------------- | ------------------------ |
| coa                   | 使用的旗帜定义           |
| priority              | 优先级（数字越大越优先） |
| trigger               | 触发条件                 |
| allow_overlord_canton | 允许宗主国徽章           |
| subject_canton        | 对附庸国显示的徽章       |

---

## 25.4🎯 **实战**：为江南共和国设计旗帜

### 25.4.1 设计理念

江南共和国旗帜设计思路：
- 主色调：蓝色（代表江南的水乡）
- 中心元素：金色五角星（代表统一和希望）
- 底部元素：白色波浪（代表长江和江南的水系）

### 25.4.2 旗帜定义代码

```pdx
# 文件：common/coat_of_arms/coat_of_arms/00_jiangnan.txt

# 基础版江南共和国旗帜
jiangnan_republic_coa = {
    pattern = "pattern_solid.tga"
    color1 = "dark_blue"

    # 中央大星
    colored_emblem = {
        texture = "ce_star_05.dds"
        color1 = "gold"

        instance = {
            scale = { 0.6 0.6 }
            position = { 0.5 0.35 }
        }
    }

    # 四颗小星
    colored_emblem = {
        texture = "ce_star_04.dds"
        color1 = "gold"

        instance = { scale = { 0.15 0.15 } position = { 0.35 0.55 } }
        instance = { scale = { 0.15 0.15 } position = { 0.42 0.60 } }
        instance = { scale = { 0.15 0.15 } position = { 0.58 0.60 } }
        instance = { scale = { 0.15 0.15 } position = { 0.65 0.55 } }
    }

    # 底部波浪
    colored_emblem = {
        texture = "ce_waves_02.dds"
        color1 = "white"

        instance = {
            scale = { 1.0 0.25 }
            position = { 0.5 0.85 }
        }
    }
}

# 共和制特别版
jiangnan_republic_coa_republic = {
    pattern = "pattern_solid.tga"
    color1 = "light_blue"

    colored_emblem = {
        texture = "ce_star_05.dds"
        color1 = "gold"

        instance = {
            scale = { 0.5 0.5 }
            position = { 0.5 0.4 }
        }
    }

    colored_emblem = {
        texture = "ce_wreath.dds"
        color1 = "green"
        color2 = "gold"

        instance = {
            scale = { 0.7 0.5 }
            position = { 0.5 0.75 }
        }
    }
}

# 革命版
jiangnan_republic_coa_revolutionary = {
    pattern = "pattern_diagonal_01.tga"
    color1 = "red"
    color2 = "black"

    colored_emblem = {
        texture = "ce_fist.dds"
        color1 = "gold"

        instance = {
            scale = { 0.4 0.4 }
            position = { 0.5 0.5 }
        }
    }
}

```

### 25.4.3 分配规则

```pdx
# 文件：common/flag_definitions/00_jiangnan_flags.txt

JNG = {
    # 默认旗帜
    flag_definition = {
        coa = jiangnan_republic_coa
        subject_canton = jiangnan_republic_coa
        allow_overlord_canton = yes
        priority = 1
    }

    # 共和制
    flag_definition = {
        coa = jiangnan_republic_coa_republic
        subject_canton = jiangnan_republic_coa_republic
        priority = 10

        trigger = {
            coa_def_republic_flag_trigger = yes
        }
    }

    # 革命状态
    flag_definition = {
        coa = jiangnan_republic_coa_revolutionary
        priority = 100

        trigger = {
            is_revolutionary = yes
        }
    }

    # 君主制（如果未来添加）
    flag_definition = {
        coa = jiangnan_republic_coa_monarchy
        priority = 20

        trigger = {
            coa_def_monarchy_flag_trigger = yes
        }
    }
}

```

### 25.4.4 颜色定义

如果使用的是自定义颜色，需要在`common/named_colors/`中定义：

```pdx
# 文件：common/named_colors/00_jiangnan_colors.txt

colors = {
    dark_blue = { 0.1 0.2 0.5 }      # 深蓝
    light_blue = { 0.3 0.5 0.8 }     # 浅蓝
    gold = { 0.9 0.7 0.1 }           # 金色
}

```

---

## 25.5 3D模型基础

### 25.5.1 模型文件结构

维多利亚3的3D模型使用Clauswitz引擎格式，主要文件：

| 文件类型 | 扩展名 | 说明               |
| -------- | ------ | ------------------ |
| 网格文件 | .mesh  | 3D模型几何数据     |
| 材质文件 | .asset | 模型配置和材质引用 |
| 纹理文件 | .dds   | 模型贴图           |
| 骨骼文件 | .anim  | 动画数据（如有）   |

### 25.5.2 模型层级（LOD）

游戏使用LOD（Level of Detail，细节层级）系统优化性能：

| LOD   | 距离 | 用途     |
| ----- | ---- | -------- |
| LOD_0 | 很近 | 最高细节 |
| LOD_1 | 中等 | 中等细节 |
| LOD_2 | 较远 | 较低细节 |
| LOD_3 | 很远 | 最低细节 |

💡 **比喻**：就像看远处的山，太远时只能看到轮廓，走近了才能看清树木和石头。

### 25.5.3 建筑模型结构

典型的建筑模型包含三个部分：

1. **mesh_mesh**：主要3D模型
2. **decal_decal**：地面贴花（如石板路）
3. **worlddecal_worlddecal**：城市地面纹理

### 25.5.4 修改现有模型

**基本步骤**：

1. **复制文件**：从游戏目录复制模型文件到Mod目录
2. **编辑模型**：使用Blender + PDX Tools编辑.mesh文件
3. **导出**：保存为.mesh格式
4. **测试**：在游戏中查看效果

⚠️ **警告**：不要直接修改游戏文件！始终复制到Mod文件夹中编辑。

### 25.5.5 所需工具

- **Blender**：免费3D建模软件（https://www.blender.org/）
- **PDX Blender Tools**：Paradox官方Blender插件
  - 支持导入/导出.mesh文件
  - 支持游戏材质系统

**安装PDX Tools**：
1. 下载插件
2. 在Blender中：编辑→偏好设置→插件→安装
3. 启用"Import-Export: Paradox Tools"

---

## 25.6 其他图形资源

### 25.6.1 事件图片

事件图片存储在`gfx/event_pictures/`：

**文件要求**：
- 格式：DDS或PNG
- 推荐尺寸：800x600或1024x768
- 不需要Mip Maps

**引用方法**：

```pdx
my_event = {
    type = country_event

    event_image = {
        video = "gfx/event_pictures/my_event_pic.dds"
    }

    # ...
}

```

### 25.6.2 商品图标

商品图标存储在`gfx/interface/icons/goods_icons/`：

- 尺寸：64x64像素
- 格式：DDS（带透明通道）
- 命名：`good_[商品名].dds`

### 25.6.3 界面图标

界面图标存储在`gfx/interface/icons/`：

常用文件夹：
- `generic_icons/`：通用图标
- `ideology_icons/`：意识形态图标
- `production_method_icons/`：生产方式图标
- `trait_icons/`：特质图标

---

## 25.7 图形资源最佳实践

### 25.7.1 文件命名规范

```pdx
✅ 推荐：
- jiangnan_flag_coa.dds
- building_arsenal_01.mesh
- event_taiping_revolution.dds

❌ 避免：
- 图片1.dds
- New Folder (2)/file.mesh
- flag FINAL FINAL v3.dds

```

### 25.7.2 性能优化

1. **合理使用Mip Maps**：
   - 需要：纹理、模型贴图
   - 不需要：事件图片、界面图标

2. **控制文件大小**：
   - 旗帜：最大768x512
   - 事件图片：最大1024x768
   - 图标：64x64或128x128

3. **使用压缩**：
   - BC7：高质量压缩（推荐旗帜）
   - BC3/DXT5：标准压缩（推荐一般纹理）

### 25.7.3 工作流程建议

```pdx
1. 设计阶段
   ↓ 使用Photoshop/GIMP设计
2. 尺寸检查
   ↓ 确保是4的倍数
3. 导出DDS
   ↓ 选择正确的压缩格式
4. 放入Mod
   ↓ 复制到正确文件夹
5. 游戏测试
   ↓ 检查显示效果
6. 调整优化
   ↓ 根据测试结果修改

```

---

## 常见问题

**Q1：我的旗帜在游戏中显示为黑色/透明怎么办？**

检查：
1. DDS格式是否正确导出
2. 文件路径是否正确
3. 图像尺寸是否为4的倍数
4. 颜色名称是否正确定义

**Q2：如何找到原版旗帜的底纹和徽章？**

原版资源位于：

```pdx
Victoria 3/game/gfx/coat_of_arms/
├── patterns/           # 底纹
├── colored_emblems/    # 彩色徽章
└── textured_emblems/   # 纹理徽章

```

**Q3：可以为同一个国家设置多个旗帜吗？**

可以！使用不同的`priority`和`trigger`，根据政体、意识形态等条件切换旗帜。

**Q4：3D模型必须使用LOD吗？**

强烈建议。虽然可以只使用LOD_0，但会影响游戏性能，特别是在大型城市。

---

## 本章小结

本章学习了图形资源的核心知识：

1. **DDS格式**：游戏专用的图像格式，需要4的倍数尺寸
2. **导出工具**：Paint.NET（简单）和GIMP（专业）
3. **旗帜系统**：底纹+徽章+子旗帜的组合系统
4. **旗帜分配**：使用flag_definitions根据条件分配旗帜
5. **3D模型基础**：.mesh格式、LOD系统、Blender工作流
6. **最佳实践**：命名规范、性能优化、工作流程

💡 **提示**：旗帜设计是Mod的门面，花些时间设计独特的旗帜能大大提升Mod品质。

---

## 练习建议

1. **练习1**：为江南共和国设计3种不同政体的旗帜
2. **练习2**：尝试修改一个原版国家的旗帜颜色
3. **练习3**：创建一个简单的事件图片
4. **练习4**：导出一张DDS图像并在游戏中测试

📖 **参考**：完整的旗帜元素列表请参阅Wiki的旗帜页面。
