# Appendix L: Code Snippet Library

Reusable code templates and patterns for Victoria 3 modding.

---

## Event Templates

### Basic Country Event

```pdx
# In events/my_mod_events.txt

namespace = my_mod

country_event = {
    id = my_mod.1
    title = my_mod.1.t
    desc = my_mod.1.d
    flavor = my_mod.1.f

    picture = gfx/event_pictures/my_picture.dds

    event_type = country_event

    trigger = {
        # Event trigger conditions
        is_at_war = no
        year > 1850
    }

    immediate = {
        # Effects when event fires
        set_variable = { name = event_fired value = yes }
    }

    option = {
        name = my_mod.1.a
        trigger = {
            # Option availability
            prestige > 100
        }
        highlight = yes

        add_prestige = 50
        add_modifier = {
            name = my_modifier
            months = 12
        }
    }

    option = {
        name = my_mod.1.b
        default_option = yes

        add_prestige = 10
    }
}

```

### State Event Template

```pdx
state_event = {
    id = my_mod.2
    title = my_mod.2.t
    desc = my_mod.2.d

    trigger = {
        owner = {
            is_at_war = no
        }
        state_population > 100000
    }

    immediate = {
        owner = {
            set_variable = { name = state_event_count add = 1 }
        }
    }

    option = {
        name = my_mod.2.a
        add_radicals = { value = 0.05 }
    }
}

```

### Character Event Template

```pdx
character_event = {
    id = my_mod.3
    title = my_mod.3.t
    desc = my_mod.3.d

    trigger = {
        age > 30
        is_ruler = yes
    }

    option = {
        name = my_mod.3.a
        add_trait = charismatic
    }
}

```

---

## Journal Entry Templates

### Basic Journal Entry

```pdx
# In common/journal_entries/my_journal_entries.txt

my_journal_entry = {
    icon = "gfx/interface/icons/event_icons/my_icon.dds"

    is_shown_when_inactive = {
        exists = c:FRA
        c:FRA = { is_player = yes }
    }

    possible = {
        c:FRA = {
            is_at_war = no
            prestige > 100
        }
    }

    complete = {
        c:FRA = {
            num_buildings_of_type = {
                type = building_steel_mills
                value >= 10
            }
        }
    }

    on_complete = {
        c:FRA = {
            add_prestige = 100
            trigger_event = { id = my_mod.10 }
        }
    }

    fail = {
        c:FRA = {
            is_bankrupt = yes
        }
    }

    on_fail = {
        c:FRA = {
            add_radicals = { value = 0.1 }
        }
    }

    timeout = 1825  # Days

    on_timeout = {
        c:FRA = {
            add_prestige = -50
        }
    }

    weight = 100

    should_be_pinned_by_default = yes
}

```

### Progressive Journal Entry

```pdx
my_progressive_je = {
    icon = "gfx/interface/icons/event_icons/my_icon.dds"

    complete = {
        custom_tooltip = {
            text = je_completion_tooltip
            variable = {
                name = je_progress
                value >= 100
            }
        }
    }

    on_monthly_pulse = {
        effects = {
            if = {
                limit = {
                    num_buildings_of_type = {
                        type = building_steel_mills
                        value > 0
                    }
                }
                change_variable = {
                    name = je_progress
                    add = 5
                }
            }
        }
    }

    current_value = {
        value = variable:je_progress
    }

    goal_add_value = {
        add = 100
    }
}

```

---

## Decision Templates

### Basic Decision

```pdx
# In common/decisions/my_decisions.txt

my_decision = {
    is_shown = {
        exists = c:ROOT
        is_player = yes
    }

    possible = {
        is_at_war = no
        infamy < 25
        has_technology = tech_nationalism
    }

    when_taken = {
        add_prestige = 50
        add_modifier = {
            name = national_pride
            months = 12
        }
    }

    ai_chance = {
        base = 100

        modifier = {
            add = 50
            has_technology = tech_nationalism
        }

        modifier = {
            factor = 0
            infamy > 50
        }
    }
}

```

---

## Modifier Templates

### Country Modifier

```pdx
# In common/modifiers/my_modifiers.txt

my_country_modifier = {
    icon = "gfx/interface/icons/modifiers/my_icon.dds"

    country_prestige_add = 50
    country_research_speed_mult = 0.1
    country_building_cost_mult = -0.1

    state_construction_mult = 0.1
}

```

### State Modifier

```pdx
my_state_modifier = {
    icon = "gfx/interface/icons/modifiers/my_icon.dds"

    state_population_growth_add = 0.001
    state_infrastructure_add = 10
    state_building_group_bg_manufacturing_throughput_add = 0.1
}

```

### Temporary Modifier

```pdx
my_temporary_modifier = {
    icon = "gfx/interface/icons/modifiers/my_icon.dds"

    decay = yes  # Modifier decays over time

    country_prestige_add = 100
}

```

---

## Scripted Effect Templates

### Reusable Effect

```pdx
# In common/scripted_effects/my_effects.txt

my_scripted_effect = {
    if = {
        limit = { exists = yes }

        add_prestige = 50

        every_state = {
            limit = { is_capital = yes }
            add_modifier = {
                name = capital_bonus
                months = 6
            }
        }
    }
}

```

### Parameterized Effect

```pdx
my_parameterized_effect = {
    # Usage: my_parameterized_effect = { AMOUNT = 100 }

    add_prestige = $AMOUNT$

    every_state = {
        limit = { is_capital = yes }
        add_state_infrastructure = $AMOUNT$
    }
}

```

---

## Scripted Trigger Templates

### Reusable Trigger

```pdx
# In common/scripted_triggers/my_triggers.txt

is_major_power = {
    prestige > 100
    num_states > 10
    OR = {
        army_size > 50
        navy_size > 30
    }
}

```

### Complex Trigger

```pdx
has_strong_economy = {
    gdp > 1000000
    gdp_per_capita > 20
    in_debt = no
    num_buildings > 50

    any_scope_state = {
        percent > 0.5
        state_sol > 15
    }
}

```

---

## On Action Templates

### Monthly Pulse

```pdx
# In common/on_actions/my_on_actions.txt

on_actions = {
    on_monthly_pulse_country = {
        effect = {
            if = {
                limit = {
                    has_variable = my_var
                    variable_value = { name = my_var value < 100 }
                }
                change_variable = { name = my_var add = 1 }
            }
        }
    }
}

```

### Event Triggering

```pdx
on_actions = {
    on_war_started = {
        effect = {
            ROOT = {
                set_variable = { name = war_start_year value = year }
                trigger_event = { id = war_events.1 days = 1 }
            }
        }
    }
}

```

---

## Variable Patterns

### Counter Pattern

```pdx
# Initialize if not exists
if = {
    limit = { NOT = { has_variable = my_counter } }
    set_variable = { name = my_counter value = 0 }
}

# Increment
change_variable = { name = my_counter add = 1 }

# Check and reset
if = {
    limit = { variable_value = { name = my_counter value >= 10 } }
    trigger_event = { id = my_mod.100 }
    set_variable = { name = my_counter value = 0 }
}

```

### State Tracking

```pdx
# Set state
set_variable = { name = current_phase value = 1 }

# Switch statement
if = {
    limit = { variable_value = { name = current_phase value = 1 } }
    # Phase 1 effects
    set_variable = { name = current_phase value = 2 }
}
else_if = {
    limit = { variable_value = { name = current_phase value = 2 } }
    # Phase 2 effects
    set_variable = { name = current_phase value = 3 }
}

```

---

## Iterator Patterns

### Find Best State

```pdx
# Find state with highest GDP
ordered_state = {
    order_by = state_gdp
    max = 1
    position = 0

    add_modifier = {
        name = economic_leader
        months = 12
    }
}

```

### Apply to Multiple

```pdx
# Apply to top 5 industrial states
ordered_state = {
    order_by = num_buildings
    max = 5
    position = 0

    add_modifier = {
        name = industrial_hub
        months = 6
    }
}

```

### Random Selection

```pdx
# Pick random coastal state
random_state = {
    limit = { is_coastal = yes }

    add_modifier = {
        name = port_bonus
        months = 6
    }
}

```

---

## Localization Template

```yaml
# In localization/english/my_mod_l_english.yml

l_english:
 # Event
 my_mod.1.t:0 "Event Title"
 my_mod.1.d:0 "Event description text here."
 my_mod.1.f:0 "Flavor text for atmosphere."
 my_mod.1.a:0 "Option A: First choice"
 my_mod.1.b:0 "Option B: Alternative"

 # Journal Entry
 my_journal_entry:0 "Journal Entry Title"
 my_journal_entry_desc:0 "Description of the journal entry."
 my_journal_entry_reason:0 "Why this appeared."
 je_completion_tooltip:0 "Complete this by reaching 100 progress."

 # Decision
 my_decision:0 "Decision Name"
 my_decision_desc:0 "Description of what this decision does."
 my_decision_reason:0 "Why you can take this."

 # Modifier
 my_modifier:0 "Modifier Name"
 my_modifier_desc:0 "This modifier provides bonuses."

 # Scripted GUI
 my_button:0 "Click Me"
 my_button_desc:0 "This button does something."

 # Concepts
 concept_my_concept:0 "My Concept"
 concept_my_concept_desc:0 "Explanation of this concept."

```

---

## descriptor.mod Template

```pdx
version="1.0"
tags={
    "Alternative History"
    "Gameplay"
    "Balance"
}
name="My Mod"
supported_version="1.5.*"
path="mod/my_mod"
remote_file_id="1234567890"

# Optional: Replace base game folders
replace_path="common/buildings"
replace_path="common/history/buildings"

```

---

## Building Template

```pdx
# In common/buildings/my_buildings.txt

my_custom_building = {
    building_group = bg_manufacturing

    texture = "gfx/interface/icons/building_icons/my_building.dds"

    required_construction = construction_cost_medium

    production_methods = {
        pm_default
        pm_advanced_production
    }

    economy_of_scale = yes

    should_auto_expand = {
        default_auto_expand_rule = yes
        state_building_levels_market_navy = yes
    }
}

```

---

## Cross-References

- See **Appendix A** for scope details
- See **Appendix B** for triggers
- See **Appendix C** for effects
- See **Appendix H** for modifiers
- See **Appendix I** for file paths
