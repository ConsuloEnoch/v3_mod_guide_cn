# Script value

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.10.

*See also: Macro*

**Script values** are mathematical calculations that allow creating dynamic values based on game values during gameplay.

Script values can be used in most scripts that accept numeric values, namely effects, triggers, and variables, as well as for many AI behavior calculations.

A script value is calculated every time it is used. This is generally useful; however, in cases where the value might be invoked frequently – such as in localization or a GUI, it is often better to save the value to a variable and display or use that, updating the variable only as needed.

Script values can be defined immediately in an effect or trigger, or they can be defined as an easily reusable named script value.

## Contents

- [1 Named values and inline values](#named-values-and-inline-values)
  - [1.1 Static values](#static-values)
- [2 Formulae and operators](#formulae-and-operators)
  - [2.1 Examples](#examples)
- [3 Script values and scope](#script-values-and-scope)
- [4 Conditionals](#conditionals)
- [5 Iterators](#iterators)
- [6 Localization](#localization)
- [7 Temporary Values](#temporary-values)
- [8 List of example script values](#list-of-example-script-values)
- [9 @ values](#-values)
- [10 References](#references)

## Named values and inline values

Named values are defined in .txt files contained in common/script_values/. Inline values are defined directly at their use with an effect, trigger, or other use.

Script values cannot use more than 5 decimal places. The largest possible value is 92233720368547.75807, while the smallest possible value is -92233720368547.75808.

Be careful of value loops. A value should never depend on itself directly.

### Static values

The simplest script value is just a literal value. A static script value is simply a script name with a literal number value following, such as `construction_cost_medium = 400`.

## Formulae and operators

Most script values are a formula, made up of one or more operators. Operators are evaluated in linear order, left-to-right, top-to-bottom; there is no order of operations such as PEMDAS/BEDMAS.

| Operator | Description |
|----------|-------------|
| value | Sets script value to this (overwrites any previous value) |
| add | Adds this value to script value |
| subtract | Subtracts this value from the script value |
| multiply | Multiplies the script value by this value |
| divide | Divides the script value by this value |
| modulo | Gets the remainder after dividing the script value by this value |
| max | Sets the script value to this if the script value is larger |
| min | Sets the script value to this if the script value is smaller |
| round | Rounds script value to an integer |
| ceiling | Rounds script value up to an integer |
| floor | Rounds script value down to an integer |
| round_to | Rounds script value to nearest multiple of this value |
| fixed_range | Sets script value to a random fixed-point value within range |
| integer_range | Sets script value to a random integer value within range |
| pow | Raises the value to the specified exponent |

### Examples

```
example_value = {
  add = 5
  multiply = 4
  max = 10
  subtract = 3
  value = 13
}
```

## Script values and scope

Script values are typically calculated in the scope where they are called.

Two ways of setting a specific scope for a script value:
1. Dot scoping with event targets: `c:FRA = { add_treasury = c:GBR.half_expenses }`
2. Scoping values in the formula: `c:GBR.expenses`

## Conditionals

Using the conditionals `if`, `else_if`, and `else` allows formulas to vary in controlled ways depending on game state.

```
tech_scaled_income = {
  value = income
  if = {
    limit = { has_technology_researched = currency_standards }
    multiply = 1.05
  }
  if = {
    limit = { has_technology_researched = banking }
    multiply = 1.05
  }
}
```

## Iterators

Iterators, or lists, can be used within formulas to run the same set of operators multiple times.

```
total_infrastructure = {
  every_scope_state = {
    add = infrastructure
  }
}
```

## Localization

Script values can be displayed in localization with the function `ScriptValue('named_script_value')`.

When a `desc` is available, the value itself can be given custom formatting by using `format = loc_key`.

## Temporary Values

A temporary value can be saved using `save_temporary_value_as`. This can be used to save values that will be used frequently within the same script.

```
coal_synergy = {
    every_scope_building = {
        limit = { is_building_type = building_steel_mills }
        add = level
    }
    save_temporary_value_as = number_of_steel_mills
    
    value = 0
    
    every_scope_building = {
        limit = { is_building_type = building_coal_mine }
        add = level
    }
    save_temporary_value_as = number_of_coal_mines
}
```

## List of example script values

*Main article: List of example script values*

## @ values

An **@ value** (or at value) is a more limited version of a script value. An @ value can only be used within the same file and can only be defined in a pure mathematical formula or a literal string, without reference to gamestate.

Example @ value definitions:

```
@pi = 3.1416
@third = @[1/3]
@sub_YUC_hoist_scale = @[third*2]
@canton_scale_cross_x = @[ ( 333 / 768 ) + 0.001 ]
@this_is_you = "this_is_you.dds"
```

An @ formula is always wrapped in `@[ ]` and follows PEMDAS/BEDMAS order of operations.

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Modding](/Category:Modding "Category:Modding")