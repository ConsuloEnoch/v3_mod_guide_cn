# Religion modding

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.11.

*See also: [Culture modding](/Culture_modding "Culture modding")*

**[Religion](/Religion "Religion") in Victoria 3 represents the abstracted faith of pops and countries.**

## Contents

-   [1 Religion definition](#Religion_definition)
-   [2 Discrimination traits](#Discrimination_traits)
    -   [2.1 Trait groups](#Trait_groups)
-   [3 Modifier Definitions](#Modifier_Definitions)
-   [4 References](#References)

## Religion definition

Religions are defined in /Victoria 3/game/common/religions. The definition is a script name, texture, traits, color, and optionally taboos.

For example:

hindu = {	#script name, also used as localization key
	icon = "gfx/interface/icons/religion\_icons/hindu.dds"	#image file
	heritage = heritage\_dharmic #a heritage trait
	color = { 0.8 0.2 0.3 }	#color in RGB decimal
	taboos = {	#optional list of consumable goods
		meat
	}
}

The script name is used as a localization key as well as for triggers and effects.

-   The icon is an image file.
-   The color is RGB decimal format.
-   The heritage can be any heritage trait.
-   Color is used for interface and map color marking.

Each religion may also have an `taboo` block, listing one or more consumable goods that the religion considers taboo. It is not clear if there is a maximum number of taboos.

## Discrimination traits

[Cultures](/Culture_modding "Culture modding") and religions both use discrimination traits defined in /Victoria 3/game/common/discrimination\_traits/. Each trait is defined as by a unique script name and block. Each trait has a `type` which can be `heritage`, `language`, or `tradition`. The script name is also a localization key.

For example:

language\_germanophone = { # a language trait
	type = language
	trait\_group = language\_group\_germanic
}

heritage\_abyssinian = { # a heritage trait
	type = heritage
	trait\_group = heritage\_group\_african
}

tradition\_rumelian = {
	type = tradition
}

The prefixes are only for easy reference and categorization.

Nothing distinguishes a cultural trait from a religious trait besides its use in culture and religion definitions. Religions only use heritage traits, not language or tradition traits.

Heritage and language traits also have a trait group, representing a collection of similar traits.

### Trait groups

Discrimination trait groups are defined in /Victoria 3/game/common/discrimination\_trait\_groups/. Trait groups are identical to traits except that they cannot be a tradition type, nor do they have a further group.

For example

language\_group\_germanic = { # a language trait group
	type = language
}

heritage\_group\_african = { # a heritage trait group
	type = heritage
}

## Modifier Definitions

*See also: [Modifier types](/Modifier_types "Modifier types"), [Modifier modding](/Modifier_modding "Modifier modding")*

When creating a religion, you must also create two [static modifiers](/Modifier_modding "Modifier modding"), named `(religion name)_standard_of_living_modifier_positive` and `(religion name)_standard_of_living_modifier_negative`.

You must also create a [modifier type](/Modifier_type "Modifier type") named `state_(religion name)_standard_of_living_add`, which is used by the [effect](/Effect "Effect") `add_religion_standard_of_living_modifier`. Examples of these definitions for vanilla religions can be found at /Victoria 3/game/common/static\_modifiers/08\_religion\_standard\_of\_living.txt and /Victoria 3/game/common/modifier\_type\_definitions/99\_todo\_sort\_into\_other\_files.txt

For example:

#in static\_modifiers
catholic\_standard\_of\_living\_modifier\_positive = {
	icon = "gfx/interface/icons/timed\_modifier\_icons/modifier\_flag\_positive.dds"
	state\_catholic\_standard\_of\_living\_add = 1
}

catholic\_standard\_of\_living\_modifier\_negative = {
	icon = "gfx/interface/icons/timed\_modifier\_icons/modifier\_flag\_negative.dds"
	state\_catholic\_standard\_of\_living\_add = 1
}
#############################
#in modifier\_types
state\_catholic\_standard\_of\_living\_add = {
	decimals=1
	color=good
	game\_data = {
		ai\_value=0
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

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • Religion • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • [Technology](/Technology_modding "Technology modding") • [Treaties](/Treaty_modding "Treaty modding") • [War goals](/War_goal_modding "War goal modding")

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

Retrieved from "https://vic3.paradoxwikis.com/index.php?title=Religion\_modding&oldid=34744"

Source: https://vic3.paradoxwikis.com/Religion_modding