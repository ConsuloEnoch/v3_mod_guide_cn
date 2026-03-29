# Appendix I: File Paths Quick Reference

Complete quick reference for all Victoria 3 mod file paths and locations.

---

## Common Folder Structure

```pdx
YourMod/
├── common/
│   ├── achievements/
│   ├── ai_strategies/
│   ├── battle_conditions/
│   ├── buildings/
│   ├── canal_types/
│   ├── character_interactions/
│   ├── character_templates/
│   ├── cultures/
│   ├── decisions/
│   ├── defines/
│   ├── diplomatic_actions/
│   ├── diplomatic_plays/
│   ├── eras/
│   ├── event_categories/
│   ├── flag_definitions/
│   ├── game_concepts/
│   ├── gamerules/
│   ├── genes/
│   ├── goods/
│   ├── history/
│   │   ├── buildings/
│   │   ├── characters/
│   │   ├── countries/
│   │   ├── diplomacy/
│   │   ├── pops/
│   │   ├── states/
│   │   └── trade_routes/
│   ├── ideologies/
│   ├── interest_groups/
│   ├── journal_entries/
│   ├── laws/
│   ├── map/
│   ├── modifiers/
│   ├── on_actions/
│   ├── parties/
│   ├── pop_needs/
│   ├── pop_types/
│   ├── production_methods/
│   ├── religions/
│   ├── scripted_effects/
│   ├── scripted_triggers/
│   ├── state_traits/
│   ├── strategic_regions/
│   ├── subject_types/
│   ├── technologies/
│   └── ...
├── events/
│   ├── country_events/
│   ├── state_events/
│   ├── character_events/
│   ├── diplomatic_events/
│   └── ...
├── gfx/
│   ├── interface/
│   ├── portraits/
│   ├── flags/
│   ├── map/
│   └── ...
├── gui/
│   ├── scripted_guis/
│   └── ...
├── localization/
│   ├── english/
│   ├── french/
│   ├── german/
│   └── ...
├── map_data/
│   ├── state_regions/
│   ├── strategic_regions/
│   ├── adjacencies.csv
│   ├── continents.txt
│   └── ...
├── music/
├── thumbnail.png
└── descriptor.mod

```

---

## Common Folders - Detailed

### common/ Folder

| Subfolder             | Purpose                 | Key Files           |
| --------------------- | ----------------------- | ------------------- |
| `achievements/`       | Achievement definitions | `*.txt`             |
| `ai_strategies/`      | AI behavior strategies  | `*.txt`             |
| `buildings/`          | Building definitions    | `*.txt`             |
| `cultures/`           | Culture definitions     | `*.txt`             |
| `decisions/`          | Decision definitions    | `*.txt`             |
| `diplomatic_actions/` | Diplo actions           | `*.txt`             |
| `diplomatic_plays/`   | Diplo play types        | `*.txt`             |
| `game_concepts/`      | Tutorial tooltips       | `*.txt`             |
| `genes/`              | Portrait genes          | `*.txt`             |
| `goods/`              | Trade good types        | `*.txt`             |
| `history/`            | Starting game state     | Multiple subfolders |
| `ideologies/`         | Ideology definitions    | `*.txt`             |
| `interest_groups/`    | IG definitions          | `*.txt`             |
| `journal_entries/`    | Journal entries         | `*.txt`             |
| `laws/`               | Law types               | `*.txt`             |
| `modifiers/`          | Modifier definitions    | `*.txt`             |
| `on_actions/`         | On action scripts       | `*.txt`             |
| `parties/`            | Political parties       | `*.txt`             |
| `pop_types/`          | Pop type definitions    | `*.txt`             |
| `production_methods/` | PM definitions          | `*.txt`             |
| `religions/`          | Religion definitions    | `*.txt`             |
| `scripted_effects/`   | Reusable effects        | `*.txt`             |
| `scripted_triggers/`  | Reusable triggers       | `*.txt`             |
| `state_traits/`       | State trait definitions | `*.txt`             |
| `strategic_regions/`  | Strategic regions       | `*.txt`             |
| `technologies/`       | Technology definitions  | `*.txt`             |

---

## History Subfolders

| Path                           | Contains            | File Format |
| ------------------------------ | ------------------- | ----------- |
| `common/history/buildings/`    | Starting buildings  | `*.txt`     |
| `common/history/characters/`   | Starting characters | `*.txt`     |
| `common/history/countries/`    | Country setup       | `*.txt`     |
| `common/history/diplomacy/`    | Starting relations  | `*.txt`     |
| `common/history/pops/`         | Population setup    | `*.txt`     |
| `common/history/states/`       | State ownership     | `*.txt`     |
| `common/history/trade_routes/` | Starting trade      | `*.txt`     |

---

## Events Folders

| Path                        | Contains          | Example                |
| --------------------------- | ----------------- | ---------------------- |
| `events/country_events/`    | Country events    | `my_mod_events.txt`    |
| `events/state_events/`      | State events      | `state_events.txt`     |
| `events/character_events/`  | Character events  | `character_events.txt` |
| `events/diplomatic_events/` | Diplomatic events | `diplo_events.txt`     |

---

## Graphics Folders

| Path             | Contains         | Formats         |
| ---------------- | ---------------- | --------------- |
| `gfx/interface/` | UI icons/buttons | `.dds`, `.png`  |
| `gfx/flags/`     | Country flags    | `.dds`, `.tga`  |
| `gfx/portraits/` | Portrait assets  | `.dds`, `.png`  |
| `gfx/map/`       | Map markers      | `.dds`, `.png`  |
| `gfx/models/`    | 3D models        | `.mesh`, `.dds` |

---

## GUI Folders

| Path                 | Contains            | Format  |
| -------------------- | ------------------- | ------- |
| `gui/`               | GUI layouts         | `*.gui` |
| `gui/scripted_guis/` | Scripted interfaces | `*.txt` |
| `gfx/fonts/`         | Font files          | `.ttf`  |

---

## Localization Structure

| Path                         | Contains             | Format  |
| ---------------------------- | -------------------- | ------- |
| `localization/english/`      | English strings      | `*.yml` |
| `localization/french/`       | French strings       | `*.yml` |
| `localization/german/`       | German strings       | `*.yml` |
| `localization/japanese/`     | Japanese strings     | `*.yml` |
| `localization/korean/`       | Korean strings       | `*.yml` |
| `localization/polish/`       | Polish strings       | `*.yml` |
| `localization/russian/`      | Russian strings      | `*.yml` |
| `localization/simp_chinese/` | Chinese strings      | `*.yml` |
| `localization/spanish/`      | Spanish strings      | `*.yml` |
| `localization/braz_por/`     | Brazilian Portuguese | `*.yml` |

---

## Map Data

| Path                          | Purpose               | Format  |
| ----------------------------- | --------------------- | ------- |
| `map_data/state_regions/`     | State region data     | `*.txt` |
| `map_data/strategic_regions/` | Strategic regions     | `*.txt` |
| `map_data/adjacencies.csv`    | Map adjacencies       | `.csv`  |
| `map_data/continents.txt`     | Continent definitions | `.txt`  |
| `map_data/heightmap.png`      | Height map            | `.png`  |
| `map_data/industries.png`     | Industry map          | `.png`  |
| `map_data/provinces.png`      | Province map          | `.png`  |

---

## Key Game Files

| File                       | Path                        | Purpose           |
| -------------------------- | --------------------------- | ----------------- |
| `descriptor.mod`           | Root                        | Mod metadata      |
| `defines.txt`              | `common/defines/`           | Game constants    |
| `00_static_modifiers.txt`  | `common/modifiers/`         | Base modifiers    |
| `00_on_actions.txt`        | `common/on_actions/`        | Global on actions |
| `00_scripted_effects.txt`  | `common/scripted_effects/`  | Base effects      |
| `00_scripted_triggers.txt` | `common/scripted_triggers/` | Base triggers     |

---

## File Naming Conventions

| Type         | Naming Pattern       | Example                |
| ------------ | -------------------- | ---------------------- |
| Mod file     | `descriptor.mod`     | `descriptor.mod`       |
| Text files   | `*.txt`              | `my_events.txt`        |
| Localization | `*_l_<language>.yml` | `my_mod_l_english.yml` |
| GUI files    | `*.gui`              | `my_interface.gui`     |
| Images       | `*.dds`, `*.png`     | `my_icon.dds`          |

---

## File Override Rules

| Override Type     | Behavior              | Example                             |
| ----------------- | --------------------- | ----------------------------------- |
| `replace_path`    | Replace entire folder | `replace_path = "common/buildings"` |
| File in same path | Overrides base game   | `common/events/my_events.txt`       |
| Same file name    | Overrides base file   | `common/laws/00_slavery.txt`        |

---

## descriptor.mod Example

```pdx
version="1.0"
tags={
    "Alternative History"
    "Gameplay"
}
name="My Mod"
supported_version="1.5.*"
replace_path="common/buildings"
replace_path="common/history/buildings"

```

---

## Common File Extensions

| Extension | Type         | Use Case                |
| --------- | ------------ | ----------------------- |
| `.txt`    | PDX script   | Game logic, definitions |
| `.yml`    | Localization | Translated strings      |
| `.gui`    | GUI layout   | Interface definitions   |
| `.dds`    | Texture      | Icons, flags, maps      |
| `.png`    | Image        | Alternative to DDS      |
| `.csv`    | Data         | Map adjacencies         |
| `.mod`    | Metadata     | Mod descriptor          |

---

## Cross-References

- See **Appendix A** for scope contexts
- See **Appendix B** for triggers
- See **Appendix C** for effects
- See **Appendix K** for file path errors
