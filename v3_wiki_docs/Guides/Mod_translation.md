# Mod translation

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

This article is [timeless](/Category:Timeless "Category:Timeless") and should be accurate for any version of the game.

## Contents

-   [1 Translating mods using ParaTranz](#Translating_mods_using_ParaTranz)
    -   [1.1 Existing Projects](#Existing_Projects)
    -   [1.2 Link](#Link)
    -   [1.3 Setup Guide](#Setup_Guide)
-   [2 References](#References)

## Translating mods using ParaTranz\[[edit](/index.php?title=Mod_translation&veaction=edit&section=1 "Edit section: Translating mods using ParaTranz") | [edit source](/index.php?title=Mod_translation&action=edit&section=1 "Edit section: Translating mods using ParaTranz")\]

[ParaTranz](https://paratranz.cn/projects?game=vic3) is a platform for translating PDX mods into different languages. They have a lot of really nice features:

-   Offering translations from other mods that partially match
-   Exporting with updated language tags (`l_[language]` suffixes and such)
-   Doing checksum comparisons on file and localization key level when importing a new version of a localization file
-   And a lot more

### Existing Projects\[[edit](/index.php?title=Mod_translation&veaction=edit&section=2 "Edit section: Existing Projects") | [edit source](/index.php?title=Mod_translation&action=edit&section=2 "Edit section: Existing Projects")\]

There are a lot of existing projects for big mods. I have contacted an existing project for a Chinese translation of my mod and now include their translations into my mod officially and provide them with updated loc files before updates.

### Link\[[edit](/index.php?title=Mod_translation&veaction=edit&section=3 "Edit section: Link") | [edit source](/index.php?title=Mod_translation&action=edit&section=3 "Edit section: Link")\]

-   [https://paratranz.cn/projects?game=vic3](https://paratranz.cn/projects?game=vic3)

### Setup Guide\[[edit](/index.php?title=Mod_translation&veaction=edit&section=4 "Edit section: Setup Guide") | [edit source](/index.php?title=Mod_translation&action=edit&section=4 "Edit section: Setup Guide")\]

First create a project which is straight forward.

[![ParaTranz project example.webp](/images/thumb/5/5b/ParaTranz_project_example.webp/300px-ParaTranz_project_example.webp.png)](/File:ParaTranz_project_example.webp)

Go to files and click "Manage Files".

[![ParaTranz manage files.webp](/images/thumb/3/31/ParaTranz_manage_files.webp/300px-ParaTranz_manage_files.webp.png)](/File:ParaTranz_manage_files.webp)

Click "Add Files".

[![ParaTranz add files.webp](/images/thumb/1/1e/ParaTranz_add_files.webp/300px-ParaTranz_add_files.webp.png)](/File:ParaTranz_add_files.webp)

Check the "update" checkbox (for the future) and drag & drop the whole english localization folder into the marked area.

[![ParaTranz upload files.webp](/images/thumb/8/8e/ParaTranz_upload_files.webp/300px-ParaTranz_upload_files.webp.png)](/File:ParaTranz_upload_files.webp)

If you already have translations you can import those as well. The tool does checksum checks and only updates localizations keys that have changed.

[![ParaTranz import translations.webp](/images/thumb/d/d3/ParaTranz_import_translations.webp/300px-ParaTranz_import_translations.webp.png)](/File:ParaTranz_import_translations.webp)

Then to translate go to the files page (not the manage files one) and click on a loc file.

[![ParaTranz select file.webp](/images/thumb/7/73/ParaTranz_select_file.webp/300px-ParaTranz_select_file.webp.png)](/File:ParaTranz_select_file.webp)

Then it will send you to the translation view. As you can see it knows PDX formatting and even warns translators if a formatting or concept tag is missing in the translation. Also it has support for linking multiple machine translators like DeepL, Google Translate, Deepseek and so on.

[![ParaTranz translation view.webp](/images/thumb/c/c9/ParaTranz_translation_view.webp/300px-ParaTranz_translation_view.webp.png)](/File:ParaTranz_translation_view.webp)

I also recommend activating the "replace yml" settings in the export settings

[![ParaTranz export settings.webp](/images/thumb/8/8c/ParaTranz_export_settings.webp/300px-ParaTranz_export_settings.webp.png)](/File:ParaTranz_export_settings.webp)

## References\[[edit](/index.php?title=Mod_translation&veaction=edit&section=5 "Edit section: References") | [edit source](/index.php?title=Mod_translation&action=edit&section=5 "Edit section: References")\]

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

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

Mod translation • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=Mod\_translation&oldid=21797](https://vic3.paradoxwikis.com/index.php?title=Mod_translation&oldid=21797)"

[Categories](/Special:Categories "Special:Categories"):

-   [Timeless](/Category:Timeless "Category:Timeless")
-   [Modding](/Category:Modding "Category:Modding")

-   This page was last edited on 15 May 2025, at 00:52.
-   Content is available under [Attribution-ShareAlike 3.0](https://central.paradoxwikis.com/Central:Copyrights "central:Central:Copyrights") unless otherwise noted.

-   [Privacy policy](/Victoria_3_Wiki:Privacy_policy)
-   [About Victoria 3 Wiki](/Victoria_3_Wiki:About)
-   [Disclaimers](/Victoria_3_Wiki:General_disclaimer)
-   [Mobile view](https://vic3.paradoxwikis.com/index.php?title=Mod_translation&mobileaction=toggle_view_mobile)

-   [![Attribution-ShareAlike 3.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/3.0/)
-   [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)