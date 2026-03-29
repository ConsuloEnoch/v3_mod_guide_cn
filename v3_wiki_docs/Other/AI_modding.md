# AI modding

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.9.

AI modding involves changing AI behavior through various files.

## Contents

- [1 AI defines](#AI_defines)
- [2 AI strategies](#AI_strategies)
    - [2.1 Basic Blocks](#Basic_Blocks)
    - [2.2 Diplomatic Blocks](#Diplomatic_Blocks)
        - [2.2.1 Diplomatic Play Support](#Diplomatic_Play_Support)
        - [2.2.2 Wargoal Scores](#Wargoal_Scores)
        - [2.2.3 Wargoal Weights](#Wargoal_Weights)
        - [2.2.4 Secret Goals](#Secret_Goals)
        - [2.2.5 Secret Goals Weights](#Secret_Goals_Weights)
        - [2.2.6 Treaties](#Treaties)
        - [2.2.7 Other Diplomatic Play Blocks](#Other_Diplomatic_Play_Blocks)
    - [2.3 Building Blocks](#Building_Blocks)
        - [2.3.1 Building Group Weights](#Building_Group_Weights)
        - [2.3.2 Subsidies and War Subsidies](#Subsidies_and_War_Subsidies)
        - [2.3.3 Goods](#Goods)
    - [2.4 Wanted Blocks](#Wanted_Blocks)
    - [2.5 Military Blocks](#Military_Blocks)
        - [2.5.1 Combat Unit Groups](#Combat_Unit_Groups)
        - [2.5.2 Conscript Ratio](#Conscript_Ratio)
    - [2.6 Other Blocks](#Other_Blocks)
        - [2.6.1 Institution Scores](#Institution_Scores)
        - [2.6.2 State Value](#State_Value)
        - [2.6.3 Treaty Port Value](#Treaty_Port_Value)
        - [2.6.4 Subject Value](#Subject_Value)
- [3 AI values](#AI_values)
- [4 References](#References)

## AI defines

*Main article: [AI defines](/Defines#00_ai "Defines")*

The AI defines control much of the AI's behavior by setting static values for many mechanics.

## AI strategies

AI strategies determine much of how AI behaves in game. They are located in `common/ai_strategies/`. AI strategies are reselected periodically; the new strategies are selected weighted-randomly, based on the weights of all valid strategies.

There are three types of AI strategy, administrative, diplomatic and political. There is a subset of diplomatic for subjects, defined in a different file.

Each country can only have one of each type of strategy.

### Basic Blocks

Below are the blocks inside AI strategies. 'Default' in this case means in the default strategy, in `00_default_strategy`, and 'Use in Other Strategy' describes what would happen if you would use it in any strategy.

| Block | Default | Use in Other Strategy | Description |
|-------|---------|----------------------|-------------|
| `icon` | `gfx/interface/icons/ai_strategy_icons/placate_population.dds` | override | icon |
| `will_form_power_bloc` | | | If this trigger evaluates true for ANY of the strategies, it will form a power bloc. Empty trigger counts as false in this case |
| `desired_tax_level` | `medium` | | These are the tax levels the AI will try and stay in, though it can go above max level if in an emergency |
| `max_tax_level` | `high` | | |
| `min_tax_level` | `low` | | |
| `ideological_opinion_effect_mult` | `1.0` | | How much is the AI's diplomatic acceptance, etc affected by government ideological differences |
| `revolution_aversion` | `5` (with exceptions for ottoman during sick man and july monarchy) | | Chance each day that the AI will stop enacting a law that is going to cause a civil war (1 aversion should translate into ~25%) |
| `min_law_chance_to_pass` | `50` | | Base chance required for AI to enact a law |
| `max_progressiveness` | `25` | | Max progressiveness AI will consider when enacting laws |
| `max_regressiveness` | `25` | | Max regressiveness AI will consider when enacting laws |
| `colonial_interest_ratio` | `0.0`-`0.3` (depends on navy size) | | How many of its interests should the AI dedicate to regions with unrecognized and decentralized powers |
| `change_law_chance` | `1` | additive | Chance each update that the AI is willing to start changing a law (1 = 1%) |
| `pro_interest_groups` | | | Which interest groups the AI will try and put/avoid in power |
| `anti_interest_groups` | | | |
| `pro_movements` | | | Which movements the AI will try and support/supress |
| `anti_movements` | | | |
| `obligation_value` | depends on rank, army comparison, and attitude | | How much value does the AI place on an obligation from another country |
| `nationalization_desire` | `0.0``100` for command economy | | AI desire to nationalize/privatize buildings, uses `NATIONALIZATION_DESIRE_NATIONALIZE_THRESHOLD` & `NATIONALIZATION_DESIRE_PRIVATIZE_THRESHOLD` defines to compare. |
| `strategic_region_scores` | depends on the region | | This block has accepts smaller strategic region blocks inside of it |
| `possible` | `always = no` | per strategy | Whether this strategy can be assigned to a country |
| `weight` | `0` | | Chance that this strategy will be randomly allocated to a country |

### Diplomatic Blocks

#### Diplomatic Play Support

The diplomatic_play_support block is added to a country's support for another in a diplomatic play. It evaluates support for the target and initiator only.

It has the following scopes available:

- `root` (supporting country doing the evaluation)
- `country` (country AI is evaluating support for)
- `enemy_country` (the opposing country)
- `diplomatic_play_type` (the type of diplomatic play)
- `is_initiator` (if the country AI is evaluating support for is the initiator)

You can also add descriptions when adding values which will be displayed in the tooltip.

#### Wargoal Scores

The `wargoal_scores` determines how much an AI values a wargoal. It is an additive block.

It has the following scopes available:

- `root` (country doing the evaluation)
- `target_country` (wargoal target)
- `target_state` (wargoal target state, if any)

It has the following wargoals available:

- `conquer_state`
- `return_state`
- `transfer_subject`
- `make_protectorate`
- `make_tributary`
- `increase_autonomy`
- `reduce_autonomy`
- `humiliation`
- `join_power_bloc`
- `regime_change`
- `force_nationalization`
- `foreign_investment_rights`
- `open_market`
- `revoke_claim`
- `contain_threat`
- `annex_country`
- `colonization_rights`
- `unification`
- `unification_leadership`
- `liberate_subject`
- `liberate_country`
- `leave_power_bloc`
- `independence`
- `secession`

#### Wargoal Weights

The `wargoal_weights` block is a multiplier for wargoal values. It is multiplicative.

#### Secret Goals

The secret_goal_scores block determines how likely should the AI be to have a particular strategic desire towards another country. It is an additive block. It has the following scopes available:

- `root` (country doing the evaluation)
- `target_country` (target country)

The secret goals include:

- `none`
- `befriend`
- `reconcile`
- `protect`
- `antagonize`
- `conquer`
- `dominate`

#### Secret Goals Weights

The `secret_goal_weights` block is a multiplier for wargoal values. It is multiplicative.

#### Treaties

The `treaty_category_scores` block has these categories available:

- `economy` (default 4)
- `trade` (default 5)
- `military` (default 3)
- `military_defense` (default 4)
- `ideology` (default 0)
- `expansion` (default 4)
- `power_bloc` (default 1)
- `other` (default 1)
- `none` (default 0)

#### Other Diplomatic Play Blocks

| Block | Default | Use in Other Strategy | Description |
|-------|---------|----------------------|-------------|
| `undesirable_infamy_level` | `50` | override | AI will avoid this much infamy unless its a wargoal it really wants |
| `unacceptable_infamy_level` | `100` | | AI will never deliberately add wargoals that will bring its infamy this high |
| `diplomatic_play_neutrality` | `50` (with an exception for ottomans during sick man) | additive | Added to base neutrality in diplomatic plays (note: I don't think you can subtract values) |
| `diplomatic_play_boldness` | `50` (too many cases to list here) | | How confident a country is |
| `wargoal_maneuvers_fraction` | `0.35` (with exceptions for syria, manifest destiny, and french natural borders) | | How many maneuvers is the AI okay with using in the initial phase to add more wargoals. Values below 0 and above 1 have no further effect |
| `recklessness` | `1` (double against pariahs, overlords and other case specific ones) | | Multiplier for the AI's estimation of its own strength. The AI wants to have at least parity in what it believes its own forces to be and what the enemy forces |
| `aggression` | `0.5` | | How likely is the AI to start a diplomatic play against another country if their attitude allows for it |

### Building Blocks

#### Building Group Weights

The `building_group_weights` is a multiplier to the score AI assigns to building groups (default 1). The use in other strategy for this is multiplicative, meaning it can result in several multiplications.

This block takes building groups, for example:

```
building_group_weights = {
    bg_agriculture = 1.25
}
```

#### Subsidies and War Subsidies

The `subsidies` and `war_subsidies` blocks control which buildings the AI will subsidise. Use in other strategies will override.

These blocks take building types, and have these values in order of increasing priority (as described by MONEY_SPENDING_* in defines/00_ai.txt):

- `nice_to_have`
- `wants_to_have`
- `should_have`
- `must_have` (always on)

Default subsidies are `must_have` for `building_power_plant`, `building_railway`, and `building_port`.

#### Goods

The `goods_stances` block determines how much supply the AI wants of a certain good. Use in other strategies will override.

The format for these follows this:

```
<good> = {
    stance = <stance>
    trigger = { <trigger> }
}
```

where the stance can be:

- `wants_high_supply`
- `wants_export`
- `does_not_want`

### Wanted Blocks

| Block | Default | Use in Other Strategy | Description |
|-------|---------|----------------------|-------------|
| `wanted_construction_output` | depends on investment pool, income, population and rank | additive | How much construction output should the AI aim for |
| `wanted_army_size` | depends on income (every 2.5k), population, overseas population, tech, strategies, with a special case for British countries having a `0.75` multiplier | | How many levels of barracks should the AI have |
| `wanted_navy_size` | depends on coastal and overseas population, income (every 5k), tech, strategies, with a special case for British countries having an extra `50` | | How many levels of naval base should the AI have |

### Military Blocks

#### Combat Unit Groups

The `combat_unit_group_weights` sets the weight for each combat unit group, and so determines the ratio the AI aims to have of each. It is an additive block. It has the following scopes available:

- `root` (country doing the evaluation)
- `military_formation` (military formation)

Vanilla has the following groups:

- `combat_unit_group_infantry`
- `combat_unit_group_artillery`
- `combat_unit_group_cavalry`
- `combat_unit_group_light_ship`
- `combat_unit_group_capital_ship`
- `combat_unit_group_support_ship`

#### Conscript Ratio

The conscript_battalion_ratio block sets how many conscript battalions the AI should have for each regular battalion in a formation. It is an additive block. It has the following scopes available:

- `root` (country doing the evaluation)
- `military_formation` (military formation)

By default, it relies on army law and tech.

### Other Blocks

#### Institution Scores

The `institution_scores` block controls which institutions the AI prefers to invest in. These include the following for vanilla:

- `institution_colonial_affairs`
- `institution_social_security`
- `institution_workplace_safety`
- `institution_schools`
- `institution_police`
- `institution_health_system`
- `institution_home_affairs`

By default, they are all set to `10`.

#### State Value

The `state_value` block is additive, and controls how much the AI values a state.

It has the following scopes available:

- `root` (country doing the evaluation)
- `target_state` (state)
- `target_country` (state owner)

The default is mainly based on population and GDP, has a lot of cases, including a lot of journal entries and not taking Chinese states unless another power has already done so.

By default, it has a max of `1000` for owned states and `200` for not owned states.

#### Treaty Port Value

The treaty_port_value block is additive, and controls how much the AI values a treaty port. It has the following scopes available:

- `root` (country doing the evaluation)
- `target_state` (state)
- `target_country` (state owner)

The default is mainly based on population and GDP, with some extra for Opium wars and carving up China.

By default, it has a max of `100`.

#### Subject Value

There are two related blocks, `subject_value` and `become_subject_value`.

`subject_value` has the following scopes:

- `root` (country doing the evaluation)
- `target_country` (prospective subject)

`become_subject_value` has the following scopes:

- `root` (country doing the evaluation)
- `overlord` (prospective overlord)

The default is mainly based on GDP, with prestige also being a factor for already owned subjects.

## AI values

AI values determine how likely an AI is to take a certain action. These include ai_chance, ai_weight, ai_value, ai_will_do, and several others. The precise implementation and effect varies based on the content or type it is used in. For more details on how these work, see the pages on modding scripted content and types.

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

AI • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=AI_modding&oldid=31326](https://vic3.paradoxwikis.com/index.php?title=AI_modding&oldid=31326)"

Categories:
- Pages with syntax highlighting errors
- Potentially outdated
- 1.9
- Modding

This page was last edited on 4 October 2025, at 00:08.
Content is available under Attribution-ShareAlike 3.0 unless otherwise noted.