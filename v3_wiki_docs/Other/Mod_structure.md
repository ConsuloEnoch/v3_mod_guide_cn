# Mod structure

From Victoria 3 Wiki

This article is [timeless](/Category:Timeless "Category:Timeless") and should be accurate for any version of the game.

Understanding the structure of a mod folder is critical to begin modding Victoria 3.

## Contents

- [1 Mod folder location](#Mod_folder_location)
- [2 Metadata](#Metadata)
- [3 Mod folder structure](#Mod_folder_structure)
    - [3.1 Additional files](#Additional_files)
    - [3.2 File naming](#File_naming)
- [4 Mod folder template](#Mod_folder_template)
- [5 References](#References)

## Mod folder location

By default, the folder for local mods is located at:

- Users/[username]/Documents/Paradox Interactive/Victoria 3/mod on Windows and MacOS
- home/[username]/.local/share/Paradox Interactive/Victoria 3/mod on Linux

Note that Victoria 3 cannot load any mods whose file path includes non-ASCII characters. For example, if your username includes characters with accents or from a different alphabet. You can change the location of local mods by editing Steam/steamapps/common/Victoria 3/launcher/launcher-settings.json, at the line `"gameDataPath": "%USER_DOCUMENTS%/Paradox Interactive/Victoria 3",`. For example, if you change that line to `"gameDataPath": "C:/Paradox Interactive/Victoria 3",`, then the local mod folder would be at C:/Paradox Interactive/Victoria 3/mod instead of its default location.

Mods downloaded from the Steam workshop are located in Steam/steamapps/workshop/content/529340

Note that there is the general mod folder which contains all local mods, and a specific "mod folder" for each mod. The "mod folder" should have a clear, unique name, and it is the counterpart to the game folder of base Victoria 3.

## Metadata

Mods require a metadata.json file within a .metadata folder to provide additional information for the launcher.

The basic structure for the metadata file looks like this:

```json
  {
    "name" : "Mymod",                     /* Name of your mod as it should be displayed to players */
    "id" : "com.github.mymod",            /* Id of the mod, as chosen by the modder. This must be unique - we suggest using a reverse domain name 
                                             notation, but any string sufficiently unique will do. It is used when *other* mods refer to yours in relationships.
                                             Please note that the ID needs to be consistent over time. Do not include version numbers or change if you rename your
                                             mod, since that would wreck any relationships. Do not use the example ID given here! */
    "version" : "1.1",                    /* Version of your mod. The launcher will typically understand semantic versioning, others are hit-and-miss */
    "game_id" : "victoria3",              /* Game for which the mod is created. Should always be "victoria3", unless something is seriously off. Safety catch to 
                                             avoid games trying to load mods that are made for other games and violently crashing */
    "supported_game_version" : "1.0.4",   /* Version of the game for which your mod has been made. This works with "*" as a wildcard and "+" to indicate "or higher" */
    "short_description" : "Best mod!",    /* A description of your mod to be shown in popups or other places where longer texts or descriptions with 
                                             decorations won't fit */
    "tags" : ["province", "fix"],         /* Tags defines in what categories your mod will be listed under locally. To prevent tag spamming, a maximum of 5 are allowed.
                                             Please note that this does not guarantee that any mods backend list the mod correctly (make sure to specify tags during upload) */
    "relationships" : [                   /* Descriptions on how your mod relates to other mods. Naturally, an empty list means "no relationships" */
        {
            "rel_type" : "dependency",    /* The type of relationship that this item describes. Supported types are "dependency", "incompatible_with", 
                                             "load_before", "load_after" - The latter three are being tested in launcher version 2023.10-rc */
            "id" : "com.github.othermod", /* The "id" of the mod the relationship concerns. This does not relate to a mod's workshop ID/number string. */
            "display_name" : "Othermod",  /* Display name of the other mod if that mod is *not* present on disk - If you have it installed, we'll use 
                                             the "name" from its own descriptor file */
            "resource_type" : "mod",      /* What type of item you depend on. Currently we only support "mod", but "dlc" is being considered as well */
            "version" : "1.2.*"           /* If this version of your mod depends on a certain version of the other mod, you can put it here. If you don't 
                                             care, just use "*". Same globbing as for "supported_game_version" */
        }
    ],                 
    "game_custom_data" : {                /* Victoria 3-specific information that the game engine needs to know */
      "multiplayer_synchronized" : true   /*  */
    }
  }
```

The .metadata folder may also contain a *thumbnail.png* file that serves as the thumbnail in the launcher.

## Mod folder structure

The specific mod folder is the counter part of base Victoria 3's game folder. Thus, the structure within that folder must be maintained for the mod to function correctly. For example, starting from the mod folder, the structure to modify decisions should be:

- mod/[mod-name-folder]/common/decisions/[mod decision files]
- Common errors are adding or removing a level, the following would not work as the game cannot read the files correctly:
    - mod/[mod-name-folder]/game/common/decisions/[mod decision files]
    - mod/[mod-name-folder]/common/[mod decision files]
    - mod/[mod-name-folder]/decisions/[mod decision files]

Also be aware of typos. Misspelled folders are not read correctly. Also note that most folders are given in plural form when that works in English grammar; the main exception is common/technology.

Certain folders, namely common/history and events, can have any number of subfolders, which can be arbitrarily named. This is mainly useful for organization, to keep related files closer together.

### Additional files

The game engine generally loads full folders and not specifically named files. So for most mods, it is better to define their content in files which are [loaded after the base game](/Mod_files_load_order "Mod files load order"). For example, a new file into the common/buildings folder named `my_modded_buildings.txt` will load just as well as one that is named identically to a base game file.

### File naming

Mod files should be given a reasonably unique name. A common practice is to use a mod "prefix" such as an acronym or abbreviation of the mod's name. Most game files do not require certain name, but are named for clarity. Files with required names should be indicated in their related article on this wiki.

Also note that file names are very important for the [load order](/Load_order "Load order"), which determines which mod file is used when two or more mods modify the same game element.

## Mod folder template

[This repository](https://github.com/Victoria-3-Modding-Co-op/Mod-Template) from the Victoria 3 Modding Co-op has a basic mod folder setup along with other helpful resources for starting mod development from scratch.

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

Scripted types

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • [Religion](/Religion_modding "Religion modding") • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • [Technology](/Technology_modding "Technology modding") • [Treaties](/Treaty_modding "Treaty modding") • [War goals](/War_goal_modding "War goal modding")

Map

[Map](/Map_modding "Map modding") • [Geographic regions](/Geographic_region_modding "Geographic region modding") • [States](/State_modding "State modding")

Graphics

[3D Models](/Model_modding "Model modding") • [Interface](/Interface_modding "Interface modding") • [Graphical Assets](/Graphical_asset_modding "Graphical asset modding") • [Fonts](/index.php?title=Font_modding&action=edit&redlink=1 "Font modding (page does not exist)") • [Flags](/Flag_modding "Flag modding")

Audio

[Music](/index.php?title=Music_modding&action=edit&redlink=1 "Music modding (page does not exist)") • [Sound](/Sound_modding "Sound modding")

Other

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • Mod structure • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=Mod_structure&oldid=34733](https://vic3.paradoxwikis.com/index.php?title=Mod_structure&oldid=34733)"

Categories:
- Timeless
- Modding

This page was last edited on 27 March 2026, at 05:09.
Content is available under Attribution-ShareAlike 3.0 unless otherwise noted.