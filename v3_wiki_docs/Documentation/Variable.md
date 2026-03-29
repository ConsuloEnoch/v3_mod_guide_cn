# Variable

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.11.

**Variables** are scriptable event targets that can hold values or scopes. Many effects and triggers can use variables as a target in place of a directly scripted object or value. Variables can also be used as scopes.

## Contents

- [1 Variable types](#variable-types)
  - [1.1 Variable usage](#variable-usage)
  - [1.2 Flag and variables](#flag-and-variables)
- [2 Variable lists](#variable-lists)
- [3 Variable effects](#variable-effects)
- [4 Variable triggers](#variable-triggers)
- [5 References](#references)

## Variable types

There are three types of variables: "regular", global, and local.

| Variable type | Scoped | Persistent | Event target |
|---------------|--------|------------|--------------|
| "regular" | Yes | Yes | var: |
| global | No | Yes | global_var: |
| local | No | No | local_var: |

Outside variable specific effects and triggers, variables must be referenced with the event target prefix of their type.

### Variable usage

Once a variable has been set, its value can be used in many effects and triggers. Any script term where a scope or script value can be used can generally accept a variable as well.

Variables can hold a numerical or Boolean value, a game object as a scope, or a localization key.

Regular variables are set in the currently scoped game object and can only be referenced from that object's scope. Global and local variables are set in no scope and can be referenced from anywhere.

Local variables are temporary and are automatically removed at the end of the effect or event chain that created them. Regular and global variables are persistent.

### Flag and variables

Variables can hold localization keys by setting the value with `flag:loc_key`. This is useful for interface modding and localization.

```
foo: "bar"

set_variable = {
  name = test
  value = flag:foo
}
```

The GUI script function `[Var('test').GetFlagName]` returns the string "bar".

## Variable lists

Variable lists are custom iterator lists, whose elements are all specifically added and removed by effect.

## Variable effects

| Effect | Description |
|--------|-------------|
| add_to_global_variable_list | Adds the event target to a global variable list |
| add_to_local_variable_list | Adds the event target to a local variable list |
| add_to_variable_list | Adds the event target to a variable list |
| change_global_variable | Changes the value of a numeric global variable |
| change_local_variable | Changes the value of a numeric local variable |
| change_variable | Changes the value of a numeric variable |
| clamp_global_variable | Clamps a global variable to specified max and min |
| clamp_local_variable | Clamps a local variable to specified max and min |
| clamp_variable | Clamps a variable to specified max and min |
| clear_global_variable_list | Empties the list |
| clear_local_variable_list | Empties the list |
| clear_variable_list | Empties the list |
| every_in_global_list | Iterate through all items in global list |
| remove_global_variable | Removes a global variable |
| remove_list_global_variable | Removes the target from a global variable list |
| remove_list_local_variable | Removes the target from a local variable list |
| remove_list_variable | Removes the target from a variable list |
| remove_variable | Removes a variable |
| round_global_variable | Rounds a global variable to the nearest specified value |
| round_local_variable | Rounds a local variable to the nearest specified value |
| round_variable | Rounds a variable to the nearest specified value |
| set_global_variable | Sets a global variable |
| set_local_variable | Sets a local variable |
| set_variable | Sets a variable |
| sort_global_variable_list | Sorts a global variable list |
| sort_local_variable_list | Sorts a local variable list |
| sort_variable_list | Sorts a variable list |

## Variable triggers

| Trigger | Description |
|---------|-------------|
| add_to_temporary_list | Saves a temporary target for use during the trigger execution |
| any_in_global_list | Iterate through all items in global list |
| any_in_list | Iterate through all items in list |
| any_in_local_list | Iterate through all items in local list |
| global_variable_list_size | Checks the size of a global variable list |
| has_global_variable | Checks whether the current scope has the specified global variable set |
| has_global_variable_list | Checks whether the current scope has the specified global variable list set |
| has_local_variable | Checks whether the current scope has the specified local variable set |
| has_local_variable_list | Checks whether the current scope has the specified local variable list set |
| has_variable | Checks whether the current scope has the specified variable set |
| has_variable_list | Checks whether the current scope has the specified variable list set |
| is_in_list | Checks if a target is in a list |
| is_target_in_global_variable_list | Checks if a target is in a global variable list |
| is_target_in_local_variable_list | Checks if a target is in a local variable list |
| is_target_in_variable_list | Checks if a target is in a variable list |
| list_size | Checks the size of a list |
| local_variable_list_size | Checks the size of a local variable list |
| variable_list_size | Checks the size of a variable list |

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.11](/Category:1.11 "Category:1.11")
- [Modding](/Category:Modding "Category:Modding")