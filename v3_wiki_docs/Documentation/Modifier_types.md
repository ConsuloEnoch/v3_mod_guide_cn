# Modifier types

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.10.

*See also: Modifier modding*

**Modifier types** are game script which modify various game statistics or allow or block certain actions. A *static modifier* may include multiple modifier types. Modifier types are also used in many other game objects, such as laws, institutions, and technologies, among others.

## Contents

- [1 Behavior of modifier types](#behavior-of-modifier-types)
  - [1.1 Modifier blocks](#modifier-blocks)
  - [1.2 Modifier type flow](#modifier-type-flow)
  - [1.3 Modifier type values in script](#modifier-type-values-in-script)
- [2 Defining modifier types](#defining-modifier-types)
  - [2.1 Localization](#localization)
- [3 List of defined modifier types](#list-of-defined-modifier-types)
- [4 Object-based modifiers](#object-based-modifiers)
- [5 Script-only modifier types](#script-only-modifier-types)
- [6 List of all defined modifier types](#list-of-all-defined-modifier-types)
- [7 References](#references)

## Behavior of modifier types

Modifier types can hold a numerical or Boolean value. Identical numerical modifier types affecting the same scope sum together to provide the final effect. Boolean modifier types can return only `yes` or `no`.

There are three categories of modifier types: hardcoded, object-based, and script-only.

- Hardcoded modifier types are defined based on game code and are only minimally moddable.
- Object-based modifier types are defined based on a mix game code and game objects, and new modifier types can be defined for new game objects.
- Script-only modifier types are defined entirely by script and do not have a direct effect on gameplay.

Modifier types have a default value of `0` for numerical types and `no` for Boolean types.

### Modifier blocks

A **modifier block** is an script element that accepts modifier types. A common example is a **static modifier** defined in common/static_modifiers.

A static modifier generally looks like this:

```
unification_prestige = {
    icon = gfx/interface/icons/timed_modifier_icons/modifier_statue_positive.dds
    country_prestige_add = 25
}
```

### Modifier type flow

Modifier types "flow" from the object where they are applied to the object type they affect.

**List of modifier type flow connections**

| From scope | Flows to | Flow Prefix | Notes |
|------------|----------|-------------|-------|
| Battle | Unit | `battle_` | Non-combat unit modifiers flow but do nothing |
| Building | Goods | `building_` | |
| Character | Battle, Unit | `character_` | Non-combat unit modifiers flow but do nothing |
| Country | Battle, Building, Goods, Interest Group, Military Formation, Political Movement, State, Tax, Unit | `country_` | |
| Goods | | `goods_` | `_add` modifier types only work in production method building modifiers |
| Interest group | | `interest_group_` | |
| Market | | `market_` | |
| Military formation | Character, Unit | `military_formation_` | |
| Political movement | | `political_movement_` | |
| Power Bloc | | `power_bloc_` | |
| State | Battle, Building, Building Group, Unit | `state_` | Non-combat unit modifiers flow but do nothing |
| Tax | | `tax_` | |
| Unit | | `unit_` | |

### Modifier type values in script

The event target `modifier` returns the summed value of the given modifier type.

## Defining modifier types

All modifier types are defined in common/modifier_type_definitions. Each modifier type is scripted as its own block and may contain a number of parameters:

| Parameter | Description |
|-----------|-------------|
| decimals | Defines how many decimals are used in displaying the modifier type's value |
| color | Defines how the value is colored: neutral, good, or bad |
| percent | If set to `yes`, displays value as a percentage |
| boolean | If set to `yes`, defines the modifier as Boolean instead of numerical |
| prefix | Determines which localization key should be prefixed when displaying the values |
| suffix | Determines which localization key should be suffixed when displaying the values |

### Localization

Each modifier type generates two localization keys, `<name>` and `<name>_desc`

## List of defined modifier types

The following modifiers are all defined in unmodified Victoria 3 in common/modifier_type_definitions.

## Object-based modifiers

Object-based modifiers can be extended for mods that add new types for each object category.

| Category | Description | Definition folder |
|----------|-------------|-------------------|
| $AcceptanceStatus$ | Acceptance status | common/acceptance_statuses |
| $BuildingGroup$ | Building group | common/building_groups |
| $BuildingType$ | Building type | common/buildings |
| $Culture$ | Culture | common/cultures |
| $Goods$ | Good type | common/goods |
| $Institution$ | Institution | common/institutions |
| $Law$ | Law | common/laws |
| $InterestGroup$ | Interest Group | common/interest_groups |
| $PoliticalMovement$ | Political movement | common/political_movements |
| $PopType$ | Profession | common/pop_types |
| $Religion$ | Religion | common/religions |
| $SocialClass$ | Social class | common/social_classes |

## Script-only modifier types

Script-only modifier types do not have a direct effect on the gamestate. Instead, they act as "hooks" for other scripting.

## List of all defined modifier types

This table contains all modifier types defined in Victoria 3 for easy searching.

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Modding](/Category:Modding "Category:Modding")