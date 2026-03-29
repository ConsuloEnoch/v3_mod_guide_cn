# Modifier modding

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.10.

*See also: [Modifier types](/Modifier_types "Modifier types")*

**Modifiers** are containers of values that affect gameplay. Modifiers use [modifier types](/Modifier_types "Modifier types") to define their effects. Modifiers can be defined as *static modifiers*, sometimes called *event modifiers*, or in various scripted types, such as [technologies](/Technology_modding "Technology modding"), [laws](/Law_modding "Law modding"), and more.

## Contents

-   [1 Static modifiers](#Static_modifiers)
    -   [1.1 Static modifier effects and triggers](#Static_modifier_effects_and_triggers)
-   [2 Modifier blocks](#Modifier_blocks)
-   [3 References](#References)

## Static modifiers

Static modifiers are defined in /common/static_modifiers, for example:

```
splendid_coastal_state = { # This is the static modifier
    icon = gfx/interface/icons/timed_modifier_icons/modifier_gear_positive.dds # This is an icon, and it is optional
    state_infrastructure_add = 20 # This is a modifier type
    character_popularity_add = 100 # You can add whatever modifier types you want, but be mindful of the scope
}
```

Any number of [modifier types](/Modifier_types "Modifier types") can be used in a static modifier, but note the *flow* of each modifier type, as they may have no effect if the static modifier is applied to the wrong scope.

### Static modifier effects and triggers

To apply a static modifier, use the [effect](/Effect "Effect") `add_modifier`:

```
add_modifier = { # Applies a modifier to the current scope
    name = splendid_coastal_state # the static modifier you want
    multiplier = -3 # Optional, multiply modifier type values by a number, script value, or math block
    is_decaying = no # Optional, if yes, it will decay over its lifetime, default is no
    months = 3 # Optional, if it is not set or negative, the modifier is permanent. Can also use days, weeks, or years instead.
}
```

The multiplier value adjusts the base values of the static modifier. This allows inverting or scaling a static modifier's effects.

A short form, `add_modifier = static_modifier_name`, can be used as well, which is the equivalent of

```
add_modifier = {
    name = static_modifier_name
    multiplier = 1 #i.e., no multiplier
    is_decaying = no
    months = -1 #i.e., permanent
}
```

The effect `remove_modifier = static_modifier_name` removes the specified static modifier from the current scope.

List of modifier effects

| Effect | Description | Example | Scopes | Targets |
|--------|-------------|---------|--------|---------|
| add_culture_acceptance_modifier | Apply a cultural acceptance modifier in the scoped country for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_culture_acceptance_modifier = {<br>  culture = culture_scope<br>  days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent<br>  multiplier = value (optional) #multiplies the values of the static modifier<br>  is_decaying = yes (optional) #sets modifier to decay in strength over its duration<br>} | country | |
| add_culture_standard_of_living_modifier | Apply a standard of living modifier in the scoped state for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_culture_standard_of_living_modifier = {<br>  culture = culture_scope<br>  days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent<br>  multiplier = value (optional) #multiplies the values of the static modifier<br>  is_decaying = yes (optional) #sets modifier to decay in strength over its duration<br>} | state | |
| add_enactment_modifier | Adds an enactment-related timed modifier effect to object in scope | add_enactment_modifier = {<br>  name = modifier_key<br>} | country | |
| add_fervor_target_modifier | Apply a fervor target modifier in the scoped country for the given culture. Other than the required culture argument, this effect has the same syntax as add_modifier. | add_fervor_target_modifier = {<br>  culture = culture_scope<br>  days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent<br>  multiplier = value (optional) #multiplies the values of the static modifier<br>  is_decaying = yes (optional) #sets modifier to decay in strength over its duration<br>} | country | |
| add_modifier | Adds a timed modifier effect to object in scope | add_modifier = {<br>  name = static_modifier_name<br>  days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent<br>  multiplier = value (optional) #multiplies the values of the static modifier<br>  is_decaying = yes (optional) #sets modifier to decay in strength over its duration<br>}<br>add_modifier = static_modifier_name #set as permanent modifier with no multiplier or decay | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state | |
| add_religion_standard_of_living_modifier | Apply a standard of living modifier in the scoped state for the given religion. Other than the required religion argument, this effect has the same syntax as add_modifier. | add_religion_standard_of_living_modifier = {<br>  religion = religion_scope<br>  days/weeks/months/years = value (optional) #can use scripted values, negative values are permanent<br>  multiplier = value (optional) #multiplies the values of the static modifier<br>  is_decaying = yes (optional) #sets modifier to decay in strength over its duration<br>} | state | |
| clear_enactment_modifier | Clears all current law enactment modifiers of scope country. | | country | |
| remove_enactment_modifier | Removes an enactment-related timed modifier effect to object in scope | | country | |
| remove_modifier | Removes a timed modifier effect to object in scope | remove_modifier = static_modifier_name | building, character, country, institution, interest_group, journal_entry, political_movement, power_bloc, state | |

The [trigger](/Trigger "Trigger") `has_modifier = static_modifier_name` checks for the presence of the specified static modifier in the current scope.

The scripted values that the game uses are defined in /Victoria 3/game/common/script_values/event_values.txt

## Modifier blocks

Many scripted types may contain one or more modifier blocks. These are typically defined as a block `modifier = { }` or similar. These work identically to static modifiers, except that they apply automatically to a certain scope, rather than being added by effect.

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • Modifiers • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

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

Retrieved from "[https://vic3.paradoxwikis.com/Modifier_modding](https://vic3.paradoxwikis.com/Modifier_modding)"

Categories:
-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [1.10](/Category:1.10 "Category:1.10")
-   [Modding](/Category:Modding "Category:Modding")