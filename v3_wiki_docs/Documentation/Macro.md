# Macro

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.10.

*See also: Effects, Triggers*

**Macros** are blocks of script that can be reused. There are two main types of macros: **scripted effects** and **scripted triggers**. A macro is usually equivalent to copying the script from where it is defined to where it is used. They are useful for maintaining commonly used effects, as only one script block needs to be updated to update the effect across multiple triggers or effects.

## Contents

- [1 Definition](#definition)
  - [1.1 Localization](#localization)
- [2 Use](#use)
- [3 Parameters](#parameters)
  - [3.1 Parameter use](#parameter-use)
    - [3.1.1 Unpaired parameter use](#unpaired-parameter-use)
    - [3.1.2 Partial script replacement](#partial-script-replacement)
- [4 Other macros](#other-macros)
  - [4.1 GUI function macros](#gui-function-macros)
  - [4.2 Scripted lists](#scripted-lists)
  - [4.3 Script values](#script-values)
  - [4.4 @ values](#-values)
- [5 References](#references)

## Definition

Scripted effects and triggers are defined in their respective folders: /common/scripted_effects/ and /common/scripted_triggers/

A scripted effect or trigger is defined as a script name and a block of script, for example:

```
unification_claims_effect = {
    if = {
        limit = {
            any_state_region = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
        }
        every_state_region = {
            limit = {
                any_scope_state = {
                    is_homeland_of_country_cultures = ROOT
                    NOT = { owner = ROOT }
                    NOT = { has_claim_by = ROOT }
                }
            }
            add_claim = ROOT
        }
    }
    else = {
        add_loyalists = {
            value = 0.05
        }
    }
}
```

This particular scripted effect is used for several country formation events.

A scripted effect is a regular effect block and can use any effect scripting as required. Similarly, a scripted trigger is a regular trigger block and can use any trigger scripting as required. This includes the use of scripted effects and triggers within other scripted effects and triggers.

### Localization

*See also: Localization*

By default, using a scripted effect or trigger generates the same tooltip as if it were scripted in place. Thus, it is often convenient to wrap the macro script in a `hidden_effect/hidden_trigger = { }`, `custom_tooltip = { }`, or `custom_description = { }` block. These script blocks function similarly, by hiding the auto-generated tooltip. The first, `hidden_effect/hidden_trigger = { }`, simply prevents any contained script from generating tooltips. The second, `custom_tooltip = { }`, prevents auto tooltips and instead displays a specified localization string. The last, `custom_description = { }`, sets up a full effect or trigger localization set, defined in common/effect_localization/ or common/trigger_localization/, respectively.

## Use

Simple scripted effects are called with `scripted_effect_name = yes`. Simple scripted triggers can are called with `scripted_trigger_name = yes/no`. `scripted_trigger_name = no` is equivalent to `NOT = { scripted_trigger_name = yes }`, that is, it returns true if the scripted trigger returns false.

## Parameters

Scripted effects and triggers can also make use of *parameters*, which are literal script replacements. This allows for customization of the macro when it is called.

Example definition:

```
transfer_state = { # Changes ownership of any state within a STATE region
    if = {
        limit = {
            exists = $GIVER$
            exists = $TAKER$
            $TAKER$ != $GIVER$
            $STATE$ = {
                any_scope_state = {
                    $GIVER$ = owner
                }
            }
        }
        $STATE$ = {
            every_scope_state = {
                limit = {
                    owner = $GIVER$
                }
                set_state_owner = $TAKER$
            }
        }
    }
}
```

This scripted effect has three parameters, indicated as the strings starting and ending with `$`: `$GIVER$`, `$TAKER$`, and `$STATE$`.

### Parameter use

When calling a scripted effect or trigger with parameters, the format is like the following:

```
transfer_state = {
    STATE = s:STATE_MONTENEGRO
    GIVER = c:TUR
    TAKER = root
}
```

The parameters are passed as literal text replacement.

#### Unpaired parameter use

Most examples of parameters in the base game are paired with an effect or trigger, but it also possible to use unpaired parameters, where the entire trigger or effect is passed through when the macro is used.

#### Partial script replacement

Further, because this is literal script text replacement, parameters can even be used to replace part of a script term.

## Other macros

Beside scripted effects and triggers, there are a few other macro or macro-like script elements.

### GUI function macros

*See also: Interface modding, Data types*

GUI function macros are defined in /data_binding/. These macros can be used in GUI and localization functions. Like scripted effects and triggers, these are direct text replacement and can use parameters.

### Scripted lists

*See also: Scope § Iterators*

Scripted lists are defined in /common/scripted_lists/. These are customized iterator lists with a built in trigger.

### Script values

*Main article: Script value*

Script values, defined in /common/script_values/, are similar to macros, particularly static script values.

### @ values

*Main article: Script value § @ values*

@ values are intra-file macros. They must be defined in the file where they are used, and can be used in place of most number values.

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Modding](/Category:Modding "Category:Modding")