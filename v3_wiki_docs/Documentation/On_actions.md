# On action

From Victoria 3 Wiki

(Redirected from On actions)

This article has been verified for the current version (1.12) of the game.

**On actions** are effects called by specific circumstances. Common examples are pulses which happen on a regular period, such as monthly or yearly. Other examples include various game occurrences such as starting or ending a war, gaining a new ruler, or a character dying.

## Contents

- [1 On action structure](#on-action-structure)
  - [1.1 Modding on actions](#modding-on-actions)
- [2 List of on actions](#list-of-on-actions)
- [3 References](#references)

## On action structure

On actions have the following structure with several optional blocks. Most on actions have a specified root scope, some have additional scopes as well.

```
on_action_name = {
    trigger = {			# On_actions can have triggers. If an on_action fires and its trigger returns false, nothing happens
        trigger_conditions = yes
    }

    weight_multiplier = {	# Used to manipulate the weight of this on_action if it is a candidate in a random_on_actions list
        base = 1
        modifier = {
            add = 1
            trigger_conditions = yes
        }
    }

    events = {		# Events listed in "events" brackets will always fire as long as their trigger evaluates to true
        event_id.1
        delay = { days = 365 }
        event_id.2
        delay = { months = { 6 12 } }
        event_id.3
    }
    
    random_events = {	# A single event will be picked to fire
        
        chance_to_happen = 25

        chance_of_no_event = {
            value = 0
            if = {
                limit = { trigger_conditions = yes }
                add = 10
            }
        }

        100 = event_id.1
        200 = event_id.2
        100 = 0
    }

    first_valid = {		# Pick the first event for which the trigger returns true
        event_id.1
        event_id.2
        fallback_event_without_trigger
    }

    on_actions = {	# An on_action can fire other on_actions
        on_action_1
        on_action_2
        on_action_3
    }

    random_on_actions = {	# Same as with events
        100 = on_action_1
        200 = on_action_2
        100 = 0
    }

    first_valid_on_action = {
        on_action_1
        on_action_2
    }

    effect = {	# An on_action can run effects
        effects = yes
    }

    fallback = another_on_action
}
```

**On action parameters**

| Block | Description |
|-------|-------------|
| trigger | Triggers that determine if the on action can fire when called |
| events | List of events that are called when the on action fires |
| random_event | A single valid event is called from the list, selected by weighted random |
| first_valid | The first valid event is called from the list |
| on_actions | List of on actions that are called when the on action fires |
| random_on_actions | A single valid on action is called from the list, selected by weighted random |
| first_valid_on_action | The first valid on action is called from the list |
| effect | Effects that are fired with the on action |
| weight_multiplier | A MTTH block that modifies the weight of the on action |
| fallback | A single on action that is called if no effects, events, or on actions are fired |

On actions can also be called with the effect `trigger_event`:

```
trigger_event = {
    on_action = on_action_name
    days/months/years = X
}
```

### Modding on actions

On actions can easily modded by calling a new scripted on action from a hardcoded on action. Only a new `on_actions` block can be added to existing on actions.

Example:

```
on_monthly_pulse_country = {
    on_actions = {
        new_on_action
    }
}
new_on_action = {
    effect = {
        newly added effects
    }
}
```

## List of on actions

The given scope is root unless otherwise indicated

| Name | Given scope | Description / Notes |
|------|-------------|---------------------|
| on_acquired_technology | Root = Country, scope:technology = Technology | If called by effect, call from `country` scope |
| on_battle_ended | Root = attacker or defender country, scope:enemy_country, scope:battle, scope:attacker, scope:defender, scope:state | |
| on_become_independent | Root = newly independent country, scope:overlord = former overlord | |
| on_become_subject | Root = newly subject country, scope:overlord = new overlord | |
| on_building_built | building | |
| on_capitulation | Root = Capitulating country, scope:diplomatic_play | |
| on_character_death | character | |
| on_civil_war_won | country | |
| on_country_formed | country | |
| on_decade_pulse_country | country | If called by effect, call from `country` scope |
| on_diplo_play_start | Root = diplomatic_play, scope:actor = initiator | |
| on_diplo_play_war_start | Root = diplomatic_play, scope:actor, scope:target | |
| on_five_year_pulse_country | country | If called by effect, call from `country` scope |
| on_game_started | none | Immediately after history, but before country selection |
| on_government_reformed | country | |
| on_half_yearly_pulse_country | country | If called by effect, call from `country` scope |
| on_journal_entry_completed | journal_entry | |
| on_law_enactment_pass | country | |
| on_monthly_pulse | none | |
| on_monthly_pulse_country | country | If called by effect, call from `country` scope |
| on_new_ruler | Root = character, scope:previous = previous ruler | |
| on_revolution_end | Root = Country, scope:target = Uprising country | |
| on_revolution_start | Root = Country, scope:target = Uprising country | |
| on_war_end | Root = Diplomatic Play, scope:actor, scope:target | |
| on_yearly_pulse | none | |
| on_yearly_pulse_country | country | If called by effect, call from `country` scope |

## References

- [1.12](/Category:1.12 "Category:1.12")
- [Modding](/Category:Modding "Category:Modding")