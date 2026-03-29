# 第二十六章：地图编辑

## 本章目标

学习本章后，你将能够：
- 使用地图编辑器修改地图
- 理解高度图和省份系统
- 修改州的边界和资源分布
- 创建和编辑河流
- 了解地图修改的限制和注意事项

---

## 概念讲解：地图是什么？

### 比喻：地图是一张分层的蛋糕

维多利亚3的地图就像一张多层的蛋糕：

- **高度图层** = 蛋糕的底座（决定地形高低）
- **省份层** = 奶油夹层（最小的地图单元）
- **州层** = 蛋糕切片（由多个省份组成）
- **河流层** = 巧克力酱（蜿蜒穿过各层）
- **资源层** = 糖霜装饰（可耕地、矿产等）

每一层都有其特定功能，共同构成完整的地图。

### 为什么要修改地图？

1. **历史修正**：修正错误的州界或资源分布
2. **架空历史**：创建完全虚构的世界地图
3. **性能优化**：简化复杂地区以提高性能
4. **新内容**：添加新的可玩区域

---

## 26.1 地图编辑器

### 26.1.1 启动地图编辑器

**方法一：启动选项**

1. 在Steam中右键点击维多利亚3
2. 选择"属性"
3. 在"启动选项"中输入：`-mapeditor`
4. 启动游戏

**方法二：控制台命令**

1. 以调试模式启动游戏
2. 按`~`键打开控制台
3. 输入：`map_editor`

**方法三：桌面快捷方式**

1. 找到游戏目录下的`victoria3.exe`
2. 创建快捷方式
3. 在目标后添加：`-mapeditor`
4. 使用此快捷方式启动

### 26.1.2 编辑器界面

地图编辑器主要工具栏：

| 工具       | 图标   | 功能         |
| ---------- | ------ | ------------ |
| 高度图工具 | 山峰   | 修改地形高度 |
| 省份工具   | 网格   | 编辑省份边界 |
| 州工具     | 地图   | 编辑州边界   |
| 河流工具   | 波浪   | 编辑河流     |
| 资源工具   | 矿石   | 修改资源分布 |
| 样条线工具 | 蜘蛛网 | 编辑交通路径 |

---

## 26.2 高度图（Heightmap）

### 26.2.1 什么是高度图？

高度图是一张灰度图像，定义了地形的起伏：
- **黑色** = 最低点（深海）
- **白色** = 最高点（高山）
- **灰色** = 过渡高度

💡 **比喻**：就像一张浮雕地图，越亮的地方越高。

### 26.2.2 高度图文件

文件位置：`map_data/heightmap.png`

**技术要求**：
- 格式：PNG
- 位深：16位灰度
- 尺寸：必须与原图一致（原版是8192x3616）

**相关文件**：

```pdx
map_data/
├── heightmap.png              # 主高度图
├── indirection_heightmap.png  # 自动生成
└── packed_heightmap.png       # 自动生成

```

⚠️ **注意**：后两个文件由编辑器自动生成，不要手动修改。

### 26.2.3 使用外部工具编辑

**推荐工具**：
- Photoshop（专业）
- GIMP（免费）
- World Machine（地形生成）
- Gaea（地形生成）

**编辑步骤**：

1. 打开原版`heightmap.png`
2. 编辑地形（注意保持整体高度比例）
3. 保存为16位灰度PNG
4. 放入Mod的`map_data/`文件夹
5. 在编辑器中重新打包（Repack）

### 26.2.4 常见问题

**地图出现空洞或海洋异常**：

原因：高度图分辨率问题

解决：
1. 在编辑器中选择"Heightmap Resolution"工具
2. 选择受影响的区域
3. 点击"Resolution +"增加分辨率

**新高度图显示不正确**：

检查：
1. 是否为16位灰度
2. 尺寸是否正确
3. 是否已在编辑器中重新打包

---

## 26.3 省份（Province）

### 26.3.1 什么是省份？

省份是维多利亚3地图的最小单元：
- 每个州由多个省份组成
- 省份决定了建筑物的位置
- 人口和贸易在省份级别计算

### 26.3.2 省份地图

文件位置：`map_data/provinces.png`

**特点**：
- 每个省份有唯一的RGB颜色
- 颜色用于识别省份ID
- 省份必须是连续的像素区域

**省份定义文件**：

```pdx
common/provinces/
└── 00_provinces.txt

```

示例：

```pdx
# 省份定义
province = {
    id = 1
    color = { 255 0 0 }      # 红色
    state = x                # 所属州
    coastal = yes            # 是否沿海
    terrain = plains         # 地形类型
    city = 1                 # 城市位置（枢纽）
    port = 1                 # 港口位置
    farm = 2                 # 农场位置
    mine = 3                 # 矿场位置
    wood = 4                 # 伐木场位置
}

```

### 26.3.3 修改省份

**添加新省份**：

1. 在`provinces.png`中绘制新区域
2. 选择一个唯一的RGB颜色
3. 在`00_provinces.txt`中添加定义
4. 分配到相应的州

**修改省份边界**：

1. 在图像编辑器中修改`provinces.png`
2. 确保边界清晰（像素级）
3. 在地图编辑器中重新加载
4. 重新生成路径网络（见下文）

⚠️ **警告**：修改省份是重大改动，会影响存档兼容性！

---

## 26.4 州（State）

### 26.4.1 州的定义

州由多个省份组成，是游戏的核心地理单元。

**州定义文件**：

```pdx
common/history/states/
└── 00_states.txt          # 历史设置

map_data/state_regions/
└── 00_state_regions.txt   # 地理定义

```

### 26.4.2 创建新州

**步骤1：定义州区域**

```pdx
# 文件：map_data/state_regions/00_my_states.txt

STATE_JIANGNAN = {
    id = 1001                              # 唯一ID
    subsistence_building = building_subsistence_farms

    provinces = { 1 2 3 4 5 }             # 包含的省份ID

    traits = {
        state_trait_rich_farmland
        state_trait_natural_harbors
    }

    city = 1                               # 城市枢纽
    port = 2                               # 港口枢纽
    farm = 3
    mine = 4
    wood = 5
}

```

**步骤2：设置历史状态**

```pdx
# 文件：common/history/states/00_my_states.txt

s:STATE_JIANGNAN = {
    create_state = {
        country = c:QNG                   # 初始所有者
        owned_provinces = { 1 2 3 4 5 }
    }

    # 初始建筑
    add_building = {
        type = building_urban_center
        level = 10
    }

    add_building = {
        type = building_textile_mills
        level = 5
    }

    # 初始资源
    add_resource = {
        type = silk
        amount = 20
    }
}

```

**步骤3：本地化**

```yaml
# 文件：localization/english/map/states_l_english.yml

STATE_JIANGNAN: "江南"

```

**步骤4：枢纽名称**

```yaml
# 文件：localization/english/hub_names_l_english.yml

STATE_JIANGNAN_city: "南京"
STATE_JIANGNAN_port: "上海"
STATE_JIANGNAN_mine: "马鞍山"
STATE_JIANGNAN_farm: "苏州"
STATE_JIANGNAN_wood: "杭州"

```

### 26.4.3 路径网络（Spline Network）

创建新州后，必须设置路径网络，这样军队和贸易才能正常运作。

**步骤**：

1. **生成枢纽位置**：
   - 在调试模式下启动游戏
   - 错误日志会提示"map object locator incomplete"
   - 复制`Documents/Victoria 3/generated/`中的位置文件
   - 粘贴到`gfx/map/map_object_data/`

2. **创建锚点（Anchors）**：
   - 打开地图编辑器
   - 切换到"Spline Network Strip Tool"
   - 选择新州
   - 点击"Automatically Place All Hub Anchors"
   - 保存（只勾选"Spline Network"）

3. **连接路径**：
   - 使用"Create a Strip Between Two Anchors"工具
   - 创建连接到邻近州的"state_road"路径
   - 如果是沿海州，创建"coastal_naval_route"连接海港

4. **测试**：
   - 重启游戏
   - 检查错误日志
   - 确保没有"Strip between locators..."错误

---

## 26.5 河流系统

### 26.5.1 河流地图

文件位置：`map_data/rivers.png`

**技术要求**：
- 格式：8位索引RGB
- 必须使用特定颜色调色板
- 尺寸：与省份图相同

### 26.5.2 河流颜色

**参考颜色**（不用于渲染）：
- `#ffffff`（白色）= 陆地
- `#7a7a7a`（灰色）= 水域

**渐变颜色**（河流宽度）：
从浅蓝到深绿共13个等级，表示从窄到宽的河流。

| 颜色      | 宽度 |
| --------- | ---- |
| `#00e5ff` | 最窄 |
| `#00cbff` |      |
| `#0096ff` |      |
| `#005fff` |      |
| `#1500ff` |      |
| `#1100e9` |      |
| `#0e00cf` |      |
| `#08009b` |      |
| `#030068` |      |
| `#005800` |      |
| `#008100` |      |
| `#00a300` |      |
| `#00d400` | 最宽 |

**特殊颜色**：
- `#00ff00`（绿色）= 河流源头
- `#ff0000`（红色）= 支流汇入点
- `#ffc000`（黄色）= 河流分叉点

### 26.5.3 绘制河流规则

**基本原则**：
1. 每条河流系统只能有一个源头（绿色）
2. 源头必须位于主河流起点
3. 支流用红色连接到主河流
4. 分叉用黄色标记
5. 所有像素必须正交连接（不能对角线）
6. 每个像素最多连接两个其他像素

**禁止的做法**：
- ❌ 河流汇入后再分叉（支流不能再次成为主河流）
- ❌ 多个源头
- ❌ 对角线连接
- ❌ 一个像素连接三个方向

### 26.5.4 编辑河流

**使用GIMP**：

1. 打开原版`rivers.png`
2. 使用铅笔工具（1像素粗细）绘制
3. 使用吸管工具选择正确的颜色
4. 导出为8位索引PNG
5. 放入Mod的`map_data/`

⚠️ **警告**：河流错误会导致游戏崩溃或河流不显示！

---

## 26.6 资源分布

### 26.6.1 修改资源

资源在`common/history/states/`中定义：

```pdx
s:STATE_GUANGDONG = {
    add_resource = {
        type = coal
        amount = 30            # 增加30单位煤矿
    }

    add_resource = {
        type = iron
        amount = 20
    }
}

```

### 26.6.2 可用资源类型

| 资源类型 | 说明 |
| -------- | ---- |
| coal     | 煤炭 |
| iron     | 铁矿 |
| lead     | 铅矿 |
| sulfur   | 硫磺 |
| oil      | 石油 |
| gold     | 黄金 |
| rubber   | 橡胶 |
| silk     | 丝绸 |
| dye      | 染料 |
| coffee   | 咖啡 |
| opium    | 鸦片 |
| tea      | 茶叶 |
| tobacco  | 烟草 |
| sugar    | 糖   |
| wood     | 木材 |

---

## 26.7🎯 **实战**：调整江南地区

### 26.7.1 目标

将江南地区（原属于大清的江苏省部分）划分为独立的"江南州"：

1. 从江苏省划出部分省份
2. 创建新的江南州
3. 设置正确的资源分布
4. 建立路径网络

### 26.7.2 修改步骤

**步骤1：修改州定义**

```pdx
# 修改 map_data/state_regions/00_china.txt

# 原江苏州缩小
STATE_JIANGSU = {
    # 移除一些省份到新州
    provinces = { x x x }  # 剩余的省份
}

# 新建江南州
STATE_JIANGNAN = {
    id = 2001
    subsistence_building = building_subsistence_farms

    provinces = { x x x x x }  # 从江苏划出的省份

    traits = {
        state_trait_rich_farmland
        state_trait_natural_harbors
        state_trait_warm_climate
    }

    city = x
    port = x
    farm = x
    mine = x
    wood = x
}

```

**步骤2：设置历史**

```pdx
# common/history/states/00_china.txt

s:STATE_JIANGNAN = {
    create_state = {
        country = c:QNG
        owned_provinces = { x x x x x }
    }

    add_building = {
        type = building_urban_center
        level = 15
    }

    add_building = {
        type = building_textile_mills
        level = 10
    }

    add_building = {
        type = building_dye_plantation
        level = 5
    }

    add_resource = {
        type = silk
        amount = 30
    }
}

```

**步骤3：本地化**

```yaml
# localization/english/states_l_english.yml
l_english:
  STATE_JIANGNAN: "江南"

```

**步骤4：路径网络**

按照26.4.3节的步骤设置路径网络。

---

## 常见问题

**Q1：修改地图后游戏崩溃怎么办？**

排查步骤：
1. 检查error.log中的错误信息
2. 验证所有文件格式正确
3. 确保所有ID唯一
4. 检查河流是否符合规则
5. 确认路径网络完整

**Q2：如何备份原版地图文件？**

建议：
1. 不要直接修改游戏文件
2. 在Mod中创建相同的文件路径结构
3. 只复制需要修改的文件到Mod

**Q3：修改地图是否影响存档？**

是的！地图修改会：
- 使旧存档无法加载
- 改变游戏平衡
- 需要玩家开始新游戏

**Q4：可以创建完全新的世界地图吗？**

可以，但需要：
1. 替换所有地图文件
2. 重新定义所有省份和州
3. 重写所有历史设置
4. 调整所有国家定义

这是一个巨大的工程，推荐参考"Total Conversion Sandbox"Mod。

---

## 本章小结

本章学习了地图编辑的核心知识：

1. **地图编辑器**：启动方法和基本工具
2. **高度图**：16位灰度PNG，决定地形起伏
3. **省份系统**：RGB颜色识别的最小地图单元
4. **州系统**：由省份组成，需要路径网络
5. **河流系统**：严格的绘制规则和颜色编码
6. **资源分布**：在州历史中定义

💡 **提示**：地图修改是最复杂的Mod类型之一。建议从小的调整开始，逐步掌握。

---

## 练习建议

1. **练习1**：修改一个州的资源分布
2. **练习2**：尝试调整州边界（不改变省份）
3. **练习3**：修改一条河流的走向
4. **练习4**：创建一个新州（需要完整设置）

⚠️ **警告**：地图修改前务必备份！
