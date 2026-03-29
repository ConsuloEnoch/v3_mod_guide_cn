# Decision modding

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.10.

[Decisions](/Decision "Decision") are scripted effects that can be taken in certain circumstances. Decisions are defined in /Victoria 3/game/common/decisions.

## Contents

-   [1 Example decision](#Example_decision)
    -   [1.1 Decision elements](#Decision_elements)
-   [2 Localization](#Localization)
-   [3 References](#References)

## Example decision

Decisions have two scripted [trigger](/Trigger "Trigger") blocks, a scripted [effect](/Effect "Effect") block, and an AI chance script value block.

Example:

```
#Internal reference name of the decision
example_decision = {

	#Trigger block that determines whether the decision is shown to the player as a potential option
	is_shown = {
		this = c:ABC
		
		#A variable is often used to make sure the decision is not repeatable
		NOT = { has_variable = example_decision_taken }
	}

	#Trigger block that determines when a shown decision can actually be selected
	possible = {
		has_technology_researched = organized_sports
	}
	
	#The effects that are executed once the decision is taken
	when_taken = {
		trigger_event = {
			id = example_events.1
			popup = yes
		}
		
		#The variable referenced in the is_shown trigger/section
		set_variable = {
			name = example_decision_taken
		} 	
	}	
	
	#The chance/weight that the ai will take the decision, defaults to 1 if not specified. If chance is 0, the AI will not use the decision
	ai_chance = {
		value = 100
		<script_value>
	}
}
```

### Decision elements

| Element | Description | Scope |
|---------|-------------|-------|
| decision script name | The internal script name/identifier for the decision, must be unique | N/A |
| `is_shown = { }` | A [trigger](/Trigger "Trigger") block that determines whether a decision appears in the list of potential decisions for a country | Country |
| `possible = { }` | A [trigger](/Trigger "Trigger") block that determines when shown decisions can be used | Country |
| `when_taken = { }` | An [effect](/Effect "Effect") block that is fired when the decision is clicked | Country |
| `ai_chance = { }` | A [script value](/Script_value "Script value") block that gives a weight for this decision to AI countries using this decision when available | Country |

## Localization

Decisions have the following [localization](/Localization "Localization") keys:

-   <decision_script_name>: The name/title of the decision
-   <decision_script_name>_desc: The description/flavor of the decision
-   <decision_script_name>_tooltip: A tooltip header for the decision; by default the tooltip includes the `possible` triggers and `when_taken` effects of the decision; this localization key adds a header to those parts.

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

Decisions • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

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

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

---

Retrieved from "[https://vic3.paradoxwikis.com/Decision_modding](https://vic3.paradoxwikis.com/Decision_modding)"

Categories:
-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [1.10](/Category:1.10 "Category:1.10")
-   [Modding](/Category:Modding "Category:Modding")