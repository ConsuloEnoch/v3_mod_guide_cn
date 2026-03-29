# Technology modding

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.11.

[Technologies](/Technologies "Technologies") represent material, social, and political inventions. Each technology can unlock various other mechanics, provide direct [modifier](/Modifier_types "Modifier types") effects, or a mixture of both.

## Contents

-   [1 Example technology](#Example_technology)
-   [2 Technology eras](#Technology_eras)
-   [3 Technology item](#Technology_item)
-   [4 Walkthrough guide](#Walkthrough_guide)
    -   [4.1 Define eras](#Define_eras)
    -   [4.2 Define a technology](#Define_a_technology)
-   [5 References](#References)

## Example technology

Technology definitions always include an era, a category, a texture, and an AI weight. Most technologies also include a list of prerequisite unlocking technologies and may include a list of modifiers.

nitroglycerin = {
	# Unlocks Nitroglycerin PM in Coal, Iron, Lead, Sulfur Mines
	# Unlocks Ammonia-Soda Process PM in Chemical Industries
	# Countries get a +25% chance of discovering new resources
	
	era = era\_2
	texture = "gfx/interface/icons/invention\_icons/nitroglycerin.dds"
	category = production
	
	modifier = {
		country\_resource\_discovery\_chance\_mult = 0.25
	}
	
	unlocking\_technologies = {	
		intensive\_agriculture
		prospecting
	}
	
	ai\_weight = {
		value = 1
	}
}

## Technology eras

Technology eras define the base cost of each technology. Technology eras are defined in /Victoria 3/game/common/technology/eras. Each era is a simple listing of a unique script name as a block and a technology cost. The cost is how many points of innovation are required to research the technology with no modifiers to the cost.

era\_1 = { #Pre-1836
	technology\_cost = 7500 # for progress bonuses, use an approximate third: 2500
}

Era script names are also used with the effect `add_era_researched` which unlocks all technologies of that era.

## Technology item

Technologies are defined in /Victoria 3/game/common/technology/technologies. Each technology is defined as a block with a unique script name, which also acts a [localization](/Localization "Localization") key, within that block, the technology must have a defined era, texture, category, and AI weight. Technologies may also have a modifier block and a list of unlocking technologies – prerequisites that must be researched before this technology can be researched. Technologies that unlock buildings, laws, or other such things do not include those unlocks in their definition, but instead are listed in the definition of the item or mechanic they unlock. Technologies can also be hidden from the technology screen by adding `can_research = no`, which makes the technology obtainable only by effect and shown only when researched.

Element

Values

Required

`era`

era script names

Yes

`texture`

path to image file

Yes

`category`

`production`, `military`, or `society`

Yes

`ai_weight = { }`

[script value](/Script_value "Script value")

Yes

`modifier = { }`

list of [modifier types](/Modifier_types "Modifier types")

No

`unlocking_technologies = { }`

list of technologies

No

`can_research`

`yes` or `no`

No

## Walkthrough guide

### Define eras

Within your /<mod>/common/technology/eras folder, create a .txt file of any name, e.g. "01\_my\_eras.txt"

Within "01\_my\_eras.txt", create a new era block with its technology cost:

cool\_era = { #Post-1936
	technology\_cost = 20000 # for progress bonuses, use an approximate third: 7000
}

Eras are read in by the game based on their order and the containing files' order. So 01\_my\_eras.txt would come after the vanilla 00\_eras.txt and thus the new era is added after the vanilla eras as "era 6" or "VI" in game. The technology\_cost does not need to increase linearly and can be set at any desired amount.

If you are sticking to the vanilla eras, you can ignore this step, but remember to add the correct era to any technologies you add.

### Define a technology

In the /<mod>/common/technology/technologies folder, make a new .txt file of any name, e.g. "40\_my\_techs.txt"

If you want to modify any vanilla technology, copy its entry to your new file and make any changes. If your file comes after the vanilla files in ASCII sorting, your modified entry will overwrite the vanilla entry. This makes compatibility with other mods easier as well as makes updating for new patch easier as your changes are limited to only technologies you modify.

To create a new technology, simply add a new entry to your file, remember that technologies that unlock other features, such as production methods, have to be added to those features. Remember that the technology's era should be equal to or later than all prerequisite technologies, otherwise it can cause issue with technology costs.

technicolor = {
	era = cool\_era
	texture = "gfx/interface/icons/invention\_icons/<new icon>.dds"
	category = society
	
	modifier = {
		country\_prestige\_mult = 0.1 #color film is awesome!
	}
    
	unlocking\_technologies = {	
		mass\_propaganda
	}
	
	ai\_weight = {
		value = 1
	}
}

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

Scripted types

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • [Religion](/Religion_modding "Religion modding") • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • Technology • [Treaties](/Treaty_modding "Treaty modding") • [War goals](/War_goal_modding "War goal modding")

Map

[Map](/Map_modding "Map modding") • [Geographic regions](/Geographic_region_modding "Geographic region modding") • [States](/State_modding "State modding")

Graphics

[3D Models](/Model_modding "Model modding") • [Interface](/Interface_modding "Interface modding") • [Graphical Assets](/Graphical_asset_modding "Graphical asset modding") • [Fonts](/index.php?title=Font_modding&action=edit&redlink=1 "Font modding (page does not exist)") • [Flags](/Flag_modding "Flag modding")

Audio

[Music](/index.php?title=Music_modding&action=edit&redlink=1 "Music modding (page does not exist)") • [Sound](/Sound_modding "Sound modding")

Other

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "https://vic3.paradoxwikis.com/index.php?title=Technology\_modding&oldid=32106"

Source: https://vic3.paradoxwikis.com/Technology_modding