# War goal modding

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

This article has been verified for the current [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") (1.12) of the game.

*See also: [War goals](/War_goals "War goals")*

**War goals** are diplomatic demands that one country can make on another. The definitions are found in `common/war_goal_types`

## Contents

-   [1 War Goal Definition](#War_Goal_Definition)
    -   [1.1 Basic](#Basic)
    -   [1.2 Kind](#Kind)
    -   [1.3 Settings](#Settings)
        -   [1.3.1 Validation](#Validation)
        -   [1.3.2 Other](#Other)
    -   [1.4 Contestion Type](#Contestion_Type)
    -   [1.5 Target Type](#Target_Type)
    -   [1.6 Validation Triggers](#Validation_Triggers)
    -   [1.7 Infamy & Maneuvers](#Infamy_&_Maneuvers)
    -   [1.8 On Enforced](#On_Enforced)
    -   [1.9 AI](#AI)
-   [2 Example War goal](#Example_War_goal)
-   [3 References](#References)

## War Goal Definition

### Basic

Block

Description

`icon`

path to the icon

`execution_priority`

higher value gets executed first

### Kind

"Kind" here refers to pre-defined execution behaviour and pre-defined checks. All of the vanilla war goals are associated with a kind, and that's pretty much as far as it goes. For no pre-defined effects or checks, use `custom`.

The following can be used:

-   `annex_country`
-   `ban_slavery`
-   `colonization_rights`
-   `conquer_state`
-   `contain_threat`
-   `enforce_treaty_article`
-   `force_nationalization`
-   `foreign_investment_rights`
-   `humiliation`
-   `increase_autonomy`
-   `independence`
-   `join_power_bloc`
-   `leave_power_bloc`
-   `liberate_country`
-   `liberate_subject`
-   `make_dominion`
-   `make_protectorate`
-   `make_tributary`
-   `open_market`
-   `reduce_autonomy`
-   `regime_change`
-   `return_state`
-   `revoke_all_claims`
-   `revoke_claim`
-   `secession`
-   `take_treaty_port`
-   `transfer_subject`
-   `unification`
-   `unification_leadership`
-   `custom`

### Settings

#### Validation

You can set flags in your war goal settings to mark them for validation.

Setting

Description

`annexes_entire_state`

marks the wargoal with expected behaviour. used to calculate conflicts

`annexes_entire_country`

`country_creation`

`turns_into_subject`

Setting

Description

`conflicts_with_annex_state`

marks the wargoal as potentially conflicting with respective type wargoals

`conflicts_with_annex_country`

`conflicts_with_make_subject`

`conflicts_with_existing_subject`

`conflicts_with_country_creation`

You can then set your war goal to validate for certain things, or conflicts with other war goals depending on their settings.

Setting

Description

`validate_subject_relation`

checks if the resulting subject relation of this war goal is valid

`validate_formation_candidate_self`

check to make sure the goal holder is a formation candidate

`validate_formation_candidate_target`

check to make sure the goal target is a formation candidate

`validate_sole_formation_candidate`

check to make sure the goal holder is the only formation candidate

`validate_target_not_treaty_port`

check to make sure the target state is not a treaty port

`validate_join_power_bloc`

special validation for respective wargoal kind

`validate_colonization_rights`

`validate_force_nationalization`

`validate_foreign_investment_rights`

`validate_regime_change`

`validate_contain_threat`

`validate_revoke_claims`

`validate_increase_autonomy`

`validate_take_treaty_port`

`validate_independence`

`validate_conflicts_war_goals_holder`

validate conflicts with war goals of the same type from holder

`validate_conflicts_war_goals_all`

validate conflicts with war goals of the same type from all participating countries

`validate_conflicts_conquer_state`

validates conflicts with wargoal types that have the respective conflict flag

`validate_conflicts_annex_country`

`validate_conflicts_make_subject`

`validate_conflicts_existing_subject`

#### Other

These are just more settings to use.

Setting

Description

`require_target_be_part_of_war`

can't target neutral countries

`can_add_for_other_country`

allows adding the goal for other participating countries

`overlord_is_stakeholder`

if the stakeholder of the war goal should be the overlord

`can_target_decentralized`

if the war goal can target decentralized countries

`has_other_stakeholder`

if the war goal has a different stakeholder than the target

`skip_build_list`

if the war goal can be picked in the war goal menu

`targets_enemy_subject`

if the war goal should target an enemy subject specifically

`targets_enemy_claims`

if the war goal should target the claims of a country

`requires_interest`

if the war goal requires you to have an interest in the relevant strategic region

### Contestion Type

Sets what counts as "controlling" the war goal.

The following can be used:

-   `control_target_state`
-   `control_target_country_capital`
-   `control_any_target_country_state`
-   `control_any_target_incorporated_state`
-   `control_own_state`
-   `control_own_capital`
-   `control_all_own_states`
-   `control_all_target_country_claims`
-   `control_any_releasable_state`

### Target Type

Sets what type of object the war goal targets.

These can be:

-   `country` (loops over enemy countries to generate war goal alternatives)
-   `state` (loops over states belonging to enemy countries)
-   `treaty_article` (loops over article types and then enemy countries)

### Validation Triggers

These are trigger blocks which determine whether your war goal can be used. The following scopes are available:

-   `root` (holder country)
-   `creator_country`
-   `diplomatic_play`
-   `target_country`
-   `target_state`
-   `stakeholder`
-   `target_region`
-   `article_options`

Trigger

Description

`possible`

determines if the war goal is listed when selecting war goals in a diplomatic play

`valid`

determines if the war goal is valid from a script perspective

### Infamy & Maneuvers

These blocks set how much infamy and maneuvers it will take to select a war goal (before modifiers). Both take a script value.

The following scopes are available:

-   `root` (holder country)
-   `creator_country`
-   `diplomatic_play`
-   `target_country`
-   `target_state`
-   `stakeholder`
-   `target_region`
-   `article_options`

### On Enforced

The `on_enforced` block is where you put script you want the war goal to execute. This is separate from behaviour defined in the `kind` block.

The following scopes are available:

-   `root` (holder country)
-   `creator_country`
-   `diplomatic_play`
-   `target_country`
-   `target_state`
-   `stakeholder`
-   `target_region`
-   `article_options`

### AI

There is one setting in the AI block.

Setting

Values

Description

`is_significant_demand`

yes/no

I flag that determines how important AI considers this war goal to be

## Example War goal

conquer\_state = {
	icon = "gfx/interface/icons/war\_goals/conquer\_state.dds"

	kind = conquer\_state

	settings = {
		require\_target\_be\_part\_of\_war
		annexes\_entire\_state
		can\_add\_for\_other\_country
		requires\_interest

		# Validation
		validate\_target\_not\_treaty\_port
		validate\_conflicts\_conquer\_state

		conflicts\_with\_country\_creation
		conflicts\_with\_annex\_state
	}

	execution\_priority = 69

	contestion\_type = control\_target\_state

	target\_type = state

	possible = {
		# trigger to determine if a goal with its target data is listed when selecting a war goal in the diplo play panel
		# scopes: root = holder, creator\_country, diplomatic\_play, target\_country, target\_state, stakeholder, target\_region, article\_options
	}

	valid = {
		# trigger in addition to some basic validation code-side
		# scopes: root = holder, creator\_country, diplomatic\_play, target\_country, target\_state, stakeholder, target\_region, article\_options
		scope:target\_state = {
			owner = scope:target\_country
			NOT = { has\_claim\_by = root }
		}
	}

	maneuvers = {
		value = 0

		add = {
			desc = "MANEUVERS\_BASE\_VALUE"
			value = 10
		}

		multiply = {
			desc = "MANEUVERS\_TARGET\_STATE\_POPULATION\_FACTOR"
			value = scope:target\_state.state\_population
			divide = define:NDiplomacy|SWAY\_OFFER\_WARGOAL\_MANEUVERS\_COST\_POPULATION\_SCALING\_FACTOR
			multiply = define:NDiplomacy|SWAY\_OFFER\_WARGOAL\_MANEUVERS\_COST\_POPULATION\_SCALING\_MULTIPLIER
			max = define:NDiplomacy|SWAY\_OFFER\_WARGOAL\_MANEUVERS\_COST\_POPULATION\_SCALING\_MULTIPLIER\_MAX\_PER\_STATE
		}
	}

	infamy = {
		value = 0

		add = {
			desc = "INFAMY\_BASE\_VALUE"
			value = 5
		}

		multiply = {
			desc = "INFAMY\_STATE\_POPULATION\_FACTOR"
			value = scope:target\_state.state\_population
			divide = define:NDiplomacy|WAR\_GOAL\_INFAMY\_POPULATION\_SCALING\_FACTOR
			multiply = define:NDiplomacy|WAR\_GOAL\_INFAMY\_POPULATION\_SCALING\_MULTIPLIER
			add = 1
			max = define:NDiplomacy|WAR\_GOAL\_INFAMY\_POPULATION\_SCALING\_MULTIPLIER\_MAX\_PER\_STATE
		}

		multiply = {
			desc = "country\_infamy\_generation\_against\_unrecognized\_mult"
			value = 1
			if = {
				limit = {
					scope:target\_country = {
						is\_country\_type = unrecognized
					}
				}
				add = modifier:country\_infamy\_generation\_against\_unrecognized\_mult
			}
		}

		multiply = {
			desc = "IG\_OTHER\_FACTORS\_HEADER"
			value = 1

			if = {
				limit = {
					scope:target\_state = {
						is\_homeland\_of\_country\_cultures = root
					}
				}
				add = define:NDiplomacy|WAR\_GOAL\_INFAMY\_HOMELAND\_FACTOR
			}

			if = {
				limit = {
					scope:target\_state = {
						is\_incorporated = no
					}
				}
				add = define:NDiplomacy|WAR\_GOAL\_INFAMY\_UNINCORPORATED\_FACTOR
			}
		}

		min = 5
	}

	on\_enforced = {
		# script effect on top of the predefined code effect
	}

	ai = {
		is\_significant\_demand = yes
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

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • [Religion](/Religion_modding "Religion modding") • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • [Technology](/Technology_modding "Technology modding") • [Treaties](/Treaty_modding "Treaty modding") • War goals

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

Retrieved from "https://vic3.paradoxwikis.com/index.php?title=War\_goal\_modding&oldid=33247"

Source: https://vic3.paradoxwikis.com/War_goal_modding