# Appendix E: Variables and Script Values

Complete reference for variable operations and script values in Victoria 3.

---

## Variable Types

### Scope Variables

Stored in specific scopes and accessible only within that scope chain.

| Type                 | Storage         | Scope              |
| -------------------- | --------------- | ------------------ |
| `variable`           | Country scope   | Country-specific   |
| `state_variable`     | State scope     | State-specific     |
| `pop_variable`       | Pop scope       | Pop-specific       |
| `character_variable` | Character scope | Character-specific |
| `building_variable`  | Building scope  | Building-specific  |

### Global Variables

Stored globally and accessible everywhere.

| Type         | Storage                 | Access             |
| ------------ | ----------------------- | ------------------ |
| `global_var` | Global scope            | Any script         |
| `temp`       | Temporary (event-local) | Current event only |

---

## Variable Operations

### Setting Variables

| Operation      | Syntax         | Example                                            |
| -------------- | -------------- | -------------------------------------------------- |
| Set            | `set_variable` | `set_variable = { name = my_var value = 10 }`      |
| Set from value | `set_variable` | `set_variable = { name = gdp_val value = gdp }`    |
| Set to scope   | `set_variable` | `set_variable = { name = enemy target = c:GER }`   |
| Copy variable  | `set_variable` | `set_variable = { name = new_var copy = old_var }` |

### Modifying Variables

| Operation | Syntax               | Example                                                    |
| --------- | -------------------- | ---------------------------------------------------------- |
| Add       | `change_variable`    | `change_variable = { name = my_var add = 5 }`              |
| Subtract  | `change_variable`    | `change_variable = { name = my_var subtract = 3 }`         |
| Multiply  | `change_variable`    | `change_variable = { name = my_var multiply = 2 }`         |
| Divide    | `change_variable`    | `change_variable = { name = my_var divide = 2 }`           |
| Modulo    | `change_variable`    | `change_variable = { name = my_var modulo = 3 }`           |
| Random    | `randomize_variable` | `randomize_variable = { name = my_var min = 1 max = 100 }` |

### Removing Variables

| Operation | Syntax            | Example                    |
| --------- | ----------------- | -------------------------- |
| Remove    | `remove_variable` | `remove_variable = my_var` |
| Clear all | `clear_variables` | `clear_variables = yes`    |

### Global Variables

| Operation     | Syntax                   | Example                                                   |
| ------------- | ------------------------ | --------------------------------------------------------- |
| Set global    | `set_global_variable`    | `set_global_variable = { name = global_var value = 100 }` |
| Change global | `change_global_variable` | `change_global_variable = { name = global_var add = 10 }` |
| Remove global | `remove_global_variable` | `remove_global_variable = global_var`                     |

---

## Variable Triggers

### Checking Variables

| Trigger               | Description    | Example                                         |
| --------------------- | -------------- | ----------------------------------------------- |
| `variable_value`      | Check value    | `variable_value = { name = my_var value > 10 }` |
| `has_variable`        | Has variable   | `has_variable = my_var`                         |
| `has_global_variable` | Has global var | `has_global_variable = global_var`              |

### Comparison

| Operator | Description   | Example                                          |
| -------- | ------------- | ------------------------------------------------ |
| `=`      | Equal         | `variable_value = { name = my_var value = 5 }`   |
| `>`      | Greater than  | `variable_value = { name = my_var value > 5 }`   |
| `<`      | Less than     | `variable_value = { name = my_var value < 10 }`  |
| `>=`     | Greater/equal | `variable_value = { name = my_var value >= 5 }`  |
| `<=`     | Less/equal    | `variable_value = { name = my_var value <= 10 }` |

---

## Variable Usage

### In Triggers

```pdx
# Check if variable exists
has_variable = my_var

# Check variable value
variable_value = { name = my_var value > 50 }

# Compare with value
ROOT = {
    variable_value = {
        name = enemy_strength
        value < army_size
    }
}

```

### In Effects

```pdx
# Set variable
set_variable = { name = war_count value = 0 }

# Modify variable
change_variable = { name = war_count add = 1 }

# Use variable in effect
add_prestige = { value = var:my_prestige_value }

```

### In Localization

```yaml
# Access variable
[ROOT.GetVariable('my_var')]
[Scope.GetVariable('war_count')]

# In script with formatting
value = var:my_var

```

---

## Script Values

Script values are predefined calculations used in modifiers and triggers.

### Value Types

| Type       | Description    | Example        |
| ---------- | -------------- | -------------- |
| `value`    | Fixed number   | `value = 10`   |
| `add`      | Addition       | `add = 5`      |
| `multiply` | Multiplication | `multiply = 2` |
| `divide`   | Division       | `divide = 2`   |

### Country Script Values

| Value                    | Description        | Example                          |
| ------------------------ | ------------------ | -------------------------------- |
| `country_gdp`            | GDP value          | `value = country_gdp`            |
| `country_gdp_per_capita` | GDP per capita     | `value = country_gdp_per_capita` |
| `country_prestige`       | Prestige           | `value = country_prestige`       |
| `country_infamy`         | Infamy             | `value = country_infamy`         |
| `country_army_size`      | Army size          | `value = country_army_size`      |
| `country_navy_size`      | Navy size          | `value = country_navy_size`      |
| `country_population`     | Population         | `value = country_population`     |
| `country_literacy`       | Literacy rate      | `value = country_literacy`       |
| `country_sol`            | Standard of living | `value = country_sol`            |

### State Script Values

| Value                  | Description        | Example                        |
| ---------------------- | ------------------ | ------------------------------ |
| `state_population`     | Population         | `value = state_population`     |
| `state_gdp`            | GDP                | `value = state_gdp`            |
| `state_sol`            | Standard of living | `value = state_sol`            |
| `state_literacy`       | Literacy           | `value = state_literacy`       |
| `state_infrastructure` | Infrastructure     | `value = state_infrastructure` |
| `state_radicalism`     | Radicalism         | `value = state_radicalism`     |

### Pop Script Values

| Value          | Description        | Example                |
| -------------- | ------------------ | ---------------------- |
| `pop_size`     | Pop size           | `value = pop_size`     |
| `pop_income`   | Income             | `value = pop_income`   |
| `pop_sol`      | Standard of living | `value = pop_sol`      |
| `pop_approval` | Approval           | `value = pop_approval` |

### Military Script Values

| Value            | Description    | Example                  |
| ---------------- | -------------- | ------------------------ |
| `army_size`      | Army size      | `value = army_size`      |
| `navy_size`      | Navy size      | `value = navy_size`      |
| `num_battalions` | Battalions     | `value = num_battalions` |
| `num_ships`      | Ships          | `value = num_ships`      |
| `manpower`       | Manpower       | `value = manpower`       |
| `war_exhaustion` | War exhaustion | `value = war_exhaustion` |

---

## Complex Script Value Examples

### Calculated Values

```pdx
# In modifiers or script values files
my_calculated_value = {
    value = country_gdp
    divide = 1000
    multiply = {
        value = country_literacy
        add = 0.5
    }
}

# Using add/multiply
prestige_from_gdp = {
    value = country_gdp
    divide = 1000000
    add = 10
}

```

### Conditional Values

```pdx
my_value = {
    if = {
        limit = { is_at_war = yes }
        value = 2.0
    }
    else_if = {
        limit = { infamy > 50 }
        value = 1.5
    }
    else = {
        value = 1.0
    }
}

```

### Modifier Usage

```pdx
# In modifier definition
my_modifier = {
    country_prestige_add = {
        value = my_script_value
        multiply = 1.5
    }
}

```

---

## Variable Examples

### Event Counter

```pdx
# Initialize
trigger_event = {
    id = my_event.1
    days = 30
}

# In event
country_event = {
    id = my_event.1

    immediate = {
        if = {
            limit = { NOT = { has_variable = event_counter } }
            set_variable = { name = event_counter value = 0 }
        }
        change_variable = { name = event_counter add = 1 }
    }

    option = {
        name = my_event.1.a
        trigger = {
            variable_value = { name = event_counter value < 5 }
        }
        trigger_event = {
            id = my_event.1
            days = 30
        }
    }
}

```

### Dynamic Relations

```pdx
# Set dynamic relation value
c:FRA = {
    set_variable = {
        name = relation_with_germany
        value = {
            value = relations
            target = c:GER
        }
    }
}

# Use in trigger
c:FRA = {
    variable_value = {
        name = relation_with_germany
        value < 0
    }
}

```

### Global Event Tracking

```pdx
# Set global variable on first occurrence
if = {
    limit = { NOT = { has_global_variable = world_war_started } }
    set_global_variable = { name = world_war_started value = yes }
    set_global_variable = { name = world_war_year value = year }
}

# Check later
has_global_variable = world_war_started

```

---

## Common Patterns

### Temporary Calculation

```pdx
# Store calculation in temp variable
set_temp_variable = {
    name = temp_calc
    value = {
        value = gdp
        divide = 1000000
    }
}

# Use in effect
add_prestige = { value = temp:temp_calc }

```

### Scope Variable Access

```pdx
# Accessing from different scope
PREV = {
    variable_value = { name = my_var value > 10 }
}

# Accessing with var: syntax
gdp > var:min_gdp_threshold

```

---

## Cross-References

- See **Appendix B** for variable triggers
- See **Appendix C** for variable effects
- See **Appendix H** for script values in modifiers
- See **Appendix L** for code snippets using variables
