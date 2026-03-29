# 第3章：Mod文件结构详解

> 理解Mod文件结构是成为熟练Mod开发者的关键。本章将详细讲解Mod的目录结构、文件加载顺序，以及如何正确组织你的Mod文件。

## 本章目标

完成本章学习后，你将能够：
- 理解Mod文件夹的标准结构
- 掌握各文件夹的用途和命名规范
- 理解文件加载顺序和覆盖机制
- 正确组织大型Mod的文件结构

---

## 3.1 Mod文件夹总览

### 3.1.1 基本结构

一个标准的Mod文件夹结构如下：

```pdx
my_mod/
├── .metadata/              # Mod元数据
│   ├── metadata.json       # Mod配置信息
│   └── thumbnail.png       # Mod缩略图（可选）
│
├── common/                 # 核心游戏数据
│   ├── buildings/          # 建筑定义
│   ├── countries/          # 国家定义
│   ├── cultures/           # 文化定义
│   ├── decisions/          # 决策定义
│   ├── goods/              # 商品定义
│   ├── history/            # 历史设置
│   │   ├── buildings/      # 开局建筑
│   │   ├── countries/      # 开局国家设置
│   │   ├── pops/           # 开局人口
│   │   └── states/         # 开局州设置
│   ├── institutions/       # 机构定义
│   ├── interest_groups/    # 利益集团
│   ├── laws/               # 法律定义
│   ├── modifiers/          # 修正器
│   ├── on_actions/         # 动作事件
│   ├── production_methods/ # 生产方式
│   ├── religions/          # 宗教定义
│   ├── script_values/      # 脚本数值
│   ├── technologies/       # 科技定义
│   └── ...                 # 其他类型定义
│
├── events/                 # 事件文件
│   ├── my_mod_events.txt   # 你的事件
│   └── ...                 # 可创建子文件夹组织
│
├── localization/           # 本地化文本
│   ├── english/            # 英文
│   ├── simp_chinese/       # 简体中文
│   └── ...                 # 其他语言
│
├── gfx/                    # 图形资源
│   ├── flags/              # 旗帜
│   ├── interface/          # 界面图标
│   ├── portraits/          # 肖像
│   └── ...
│
├── map_data/               # 地图数据（谨慎修改）
│   ├── state_regions/      # 州区域定义
│   └── ...
│
└── gui/                    # 界面脚本
    └── ...

```

### 3.1.2 与游戏本体的对应关系

Mod文件夹结构必须与游戏本体的`game/`文件夹对应：

```pdx
游戏本体:  Victoria 3/game/common/buildings/
Mod对应:   my_mod/common/buildings/

```

**关键原则**：路径必须完全一致，游戏才能正确识别和加载Mod文件。

---

## 3.2 核心文件夹详解

### 3.2.1 .metadata/ - 元数据

这是Mod的"身份证"，告诉启动器Mod的基本信息。

**必需文件**：
- `metadata.json` - Mod配置（参见第2章）

**可选文件**：
- `thumbnail.png` - Mod缩略图，显示在启动器中
  - 推荐尺寸：1920×1080像素
  - 格式：PNG

### 3.2.2 common/ - 核心定义

这是Mod最重要的文件夹，包含所有游戏对象定义。

#### 常用子文件夹：

| 文件夹                | 用途         | 示例文件                  |
| --------------------- | ------------ | ------------------------- |
| `buildings/`          | 建筑类型定义 | `my_mod_buildings.txt`    |
| `countries/`          | 国家定义     | `my_mod_countries.txt`    |
| `cultures/`           | 文化定义     | `my_mod_cultures.txt`     |
| `decisions/`          | 决策定义     | `my_mod_decisions.txt`    |
| `goods/`              | 商品定义     | `my_mod_goods.txt`        |
| `institutions/`       | 机构定义     | `my_mod_institutions.txt` |
| `interest_groups/`    | 利益集团     | `my_mod_igs.txt`          |
| `laws/`               | 法律定义     | `my_mod_laws.txt`         |
| `modifiers/`          | 修正器定义   | `my_mod_modifiers.txt`    |
| `on_actions/`         | 动作事件     | `my_mod_on_actions.txt`   |
| `production_methods/` | 生产方式     | `my_mod_pm.txt`           |
| `religions/`          | 宗教定义     | `my_mod_religions.txt`    |
| `script_values/`      | 脚本数值     | `my_mod_values.txt`       |
| `technologies/`       | 科技定义     | `my_mod_tech.txt`         |

#### history/ 子文件夹

`common/history/`存放开局历史设置：

```pdx
common/history/
├── buildings/      # 开局建筑（建筑类型和等级）
├── countries/      # 开局国家状态（资金、科技、法律等）
├── construction/   # 开局正在建造的项目
├── diplomacy/      # 开局外交关系
├── interests/      # 开局利益范围
├── leaders/        # 开局领导人
├── pops/           # 开局人口分布
├── strategic_regions/  # 开局战略区域设置
└── states/         # 开局州设置（资源、人口等）

```

### 3.2.3 events/ - 事件文件

存放所有事件定义。与`common/`不同，`events/`文件夹**可以创建任意子文件夹**来组织文件。

**推荐组织方式**：

```pdx
events/
├── my_mod/
│   ├── qing_events.txt        # 大清相关事件
│   ├── economy_events.txt     # 经济事件
│   └── war_events.txt         # 战争事件
└── _readme.txt                # 文件夹说明（可选）

```

### 3.2.4 localization/ - 本地化

存放所有显示文本，按语言分子文件夹。

**文件夹命名**：
- `english/` - 英文
- `simp_chinese/` - 简体中文
- `spanish/` - 西班牙语
- `french/` - 法语
- 等等...

**文件命名规范**：

```pdx
[mod_prefix]_[content]_l_[language].yml

```

**示例**：

```pdx
my_mod_events_l_english.yml      # 英文事件文本
my_mod_events_l_simp_chinese.yml # 中文事件文本
my_mod_buildings_l_english.yml   # 英文建筑文本

```

> ⚠️ **重要**：本地化文件必须使用**UTF-8 BOM编码**！

### 3.2.5 gfx/ - 图形资源

存放贴图、图标、旗帜等图像资源。

**常用子文件夹**：

```pdx
gfx/
├── flags/              # 国家旗帜
│   ├── large/          # 大地图旗帜
│   ├── medium/         # 中等大小旗帜
│   ├── small/          # 小地图旗帜
│   └── flat/           # 扁平化旗帜
├── interface/          # 界面图标
│   ├── icons/          # 各种图标
│   └── portraits/      # 角色肖像
├── portraits/          # 角色肖像资源
└── models/             # 3D模型（高级）

```

**图像格式**：
- DDS（主要格式）
- PNG（部分界面元素）
- TGA（较少使用）

### 3.2.6 gui/ - 界面脚本

修改或创建游戏界面。

```pdx
gui/
├── my_mod_interface.gui    # 自定义界面
└── ...

```

### 3.2.7 map_data/ - 地图数据

修改地图相关内容。⚠️ **谨慎修改**！

```pdx
map_data/
├── state_regions/      # 州区域定义
├── strategic_regions/  # 战略区域
└── ...

```

---

## 3.3 文件加载顺序

### 3.3.1 基本加载规则

游戏加载Mod文件遵循以下顺序：

```pdx
1. 游戏本体文件
2. Mod文件（按字母顺序）
3. 同名文件：后加载的覆盖先加载的

```

### 3.3.2 文件夹加载顺序

游戏按以下顺序加载文件夹：

```pdx
1. 游戏本体 game/ 文件夹
2. 所有启用的Mod文件夹（按Mod名称字母顺序）
3. 同一Mod内，文件按字母顺序加载

```

### 3.3.3 同名文件覆盖

**关键概念**：同名文件会相互覆盖，后加载的生效。

**示例场景**：

Mod A：`my_mod/buildings.txt`
Mod B：`another_mod/buildings.txt`

如果两个文件都修改了同一个建筑，**字母顺序靠后的Mod生效**。

**避免冲突的方法**：

1. **使用唯一文件名**：

   ```pdx
   my_mod_a_buildings.txt
   my_mod_b_buildings.txt

   ```

2. **使用覆盖而非修改**：
   如果要修改游戏原有内容，使用`replace`或`overwrite`机制

3. **使用Mod依赖**：
   在`metadata.json`中声明依赖关系

### 3.3.4 代码级别的覆盖

在游戏中，你可以显式覆盖已有定义：

```pdx
# 覆盖已有建筑
dwd_building_gold_mine = {
    replace = building_gold_mine  # 替换原有金矿

    # 新定义...
}

```

或者在effects中使用`overwrite`：

```pdx
effect = {
    overwrite = yes  # 覆盖现有效果
    # 新效果...
}

```

---

## 3.4 命名规范

### 3.4.1 文件命名

**推荐格式**：

```pdx
[mod_prefix]_[content]_[type].txt

```

**示例**：

```pdx
my_mod_qing_reform_events.txt     # 好
qing_events.txt                    # 可接受但可能冲突
events.txt                         # 差（太通用）
my-mod-qing-events.txt             # 差（不要用连字符）

```

### 3.4.2 ID命名

游戏中所有对象都有唯一ID，命名规范：

```pdx
[mod_prefix]_[name]

```

**示例**：

```pdx
my_mod_qing_reform = {      # 事件ID
    # ...
}

my_mod_great_reform_decision = {   # 决策ID
    # ...
}

```

### 3.4.3 本地化Key命名

```pdx
[mod_prefix]_[id]_[type]

```

**示例**：

```yaml
my_mod_qing_reform_title:0 "洋务运动"
my_mod_qing_reform_desc:0 "清朝开始进行现代化改革..."
my_mod_qing_reform_option_1:0 "开始改革"

```

---

## 3.5 大型Mod的组织策略

### 3.5.1 按功能模块组织

```pdx
my_large_mod/
├── core/                   # 核心修改
│   └── common/
│       └── countries/
├── features/               # 功能模块
│   ├── economy/
│   │   ├── common/
│   │   ├── events/
│   │   └── localization/
│   ├── military/
│   └── politics/
└── shared/                 # 共享资源
    └── localization/

```

> ⚠️ **注意**：这种结构在单个Mod中不直接支持，需要通过良好的文件命名来实现类似效果。

### 3.5.2 文件注释头

在每个文件开头添加注释，说明文件内容：

```pdx
# ============================================================================
# 文件名: my_mod_qing_reform_events.txt
# 作者: [你的名字]
# 版本: 1.0
# 描述: 清朝洋务运动相关事件
# 更新日期: 2026-03-29
# ============================================================================

namespace = my_mod_qing

my_mod_qing_reform_start = {
    # ...
}

```

### 3.5.3 README文件

在Mod根目录创建`README.txt`说明Mod：

```pdx
我的大型Mod
版本: 1.0
作者: [你的名字]

功能列表:
- 修改了清朝开局
- 添加了洋务运动事件链
- 新增建筑和科技

安装说明:
1. 解压到mod文件夹
2. 在启动器中启用
3. 开始游戏

兼容性:
- 支持游戏版本 1.8.x
- 与其他Mod可能有冲突

联系方式:
- Steam: [你的SteamID]
- Discord: [你的Discord]

```

---

## 3.6 调试技巧

### 3.6.1 查看加载的Mod

在游戏控制台中输入：

```pdx
debug_mode

```

可以看到游戏加载了哪些Mod，以及加载顺序。

### 3.6.2 检查文件覆盖

在`error.log`中搜索：

```pdx
Overwriting
Duplicate

```

可以看到哪些文件被覆盖了。

### 3.6.3 测试加载顺序

创建测试文件检查加载顺序：

```pdx
# 在多个Mod中创建同名文件
# 文件内容：
my_mod_test = {
    set_global_variable = {
        name = loaded_mod
        value = 1  # 每个Mod用不同数字
    }
}

```

然后检查哪个值被设置，就知道哪个Mod最后加载。

---

## 3.7 常见错误

### 错误1：文件夹层级错误

❌ 错误：

```pdx
my_mod/
└── game/
    └── common/
        └── buildings.txt

```

✅ 正确：

```pdx
my_mod/
└── common/
    └── buildings.txt

```

### 错误2：文件扩展名错误

❌ 错误：

```pdx
my_mod_events.txt.txt  # 重复扩展名
my_mod_events.pdx      # 错误扩展名

```

✅ 正确：

```pdx
my_mod_events.txt

```

### 错误3：本地化编码错误

❌ 错误：UTF-8（无BOM）

✅ 正确：UTF-8 BOM

### 错误4：YAML格式错误

❌ 错误：

```yaml
l_simp_chinese:
my_mod_name:0 "名称"  # 缺少缩进

```

✅ 正确：

```yaml
l_simp_chinese:
 my_mod_name:0 "名称"  # 注意缩进

```

---

## 本章小结

- Mod文件夹结构必须与游戏本体的`game/`文件夹对应
- `common/`存放核心定义，`events/`存放事件，`localization/`存放文本
- 文件按字母顺序加载，同名文件后加载的覆盖先加载的
- 使用Mod前缀避免命名冲突
- 本地化文件必须使用UTF-8 BOM编码
- 良好的文件组织和注释对大型Mod至关重要

---

## 常见问题

**Q：我可以在Mod中创建自己的文件夹吗？**

A：大部分文件夹必须遵循游戏结构，但`events/`和`common/history/`可以创建任意子文件夹用于组织。

**Q：两个Mod修改了同一个文件会怎样？**

A：按Mod名称字母顺序加载，后加载的覆盖先加载的。建议：
1. 使用不同文件名
2. 在metadata.json中声明加载顺序
3. 合并兼容性补丁

**Q：如何知道某个功能对应哪个文件夹？**

A：查看游戏本体的`game/`文件夹，找到对应功能的官方文件，然后在Mod中创建相同路径。

**Q：我可以删除游戏原有内容吗？**

A：不能直接删除，但可以通过覆盖使其无效。例如，给一个建筑设置`building_group = none`可以禁用它。

**Q：Mod有大小限制吗？**

A：没有硬性限制，但过大的Mod（几百MB以上）可能影响加载时间和性能。

---

## 练习建议

1. **浏览游戏文件**：打开`Victoria 3/game/`文件夹，熟悉官方文件的组织结构

2. **创建完整结构**：为你的Mod创建一个完整的文件夹结构，包括所有可能的子文件夹

3. **练习文件命名**：为以下Mod内容创建合适的文件名：
   - 清朝改革事件
   - 新建筑"江南制造局"
   - 新科技"近代海军"
   - 相关的中文本地化文件

4. **测试加载顺序**：创建两个简单Mod，测试加载顺序对最终效果的影响

5. **组织你的Mod**：规划一个大型Mod的文件结构，考虑如何组织多个事件链、建筑和科技

---

> 📖 **下一章预告**：在下一章，我们将学习维多利亚3脚本语言的基础语法，包括缩进、括号、等号等核心概念。

---

## 参考

- [Victoria 3 Wiki - Mod Structure](https://vic3.paradoxwikis.com/Mod_structure)
- [Victoria 3 Wiki - Load Order](https://vic3.paradoxwikis.com/Mod_files_load_order)
