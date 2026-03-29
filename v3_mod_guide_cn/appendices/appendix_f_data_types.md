# Appendix F: Data Types Reference

Complete reference for all data types used in Victoria 3 scripting.

---

## Primitive Data Types

### Integer

Whole numbers without decimals.

| Format   | Example       | Range                           |
| -------- | ------------- | ------------------------------- |
| Standard | `value = 100` | -2,147,483,648 to 2,147,483,647 |
| Positive | `value = 50`  | 0 to 2,147,483,647              |
| Negative | `value = -25` | Use for penalties               |

**Usage Examples:**

```pdx
add_prestige = 100
num_buildings_of_type = { type = building_steel_mills value > 5 }
year > 1850

```

### Float (Decimal)

Numbers with decimal points.

| Format     | Example        | Notes                      |
| ---------- | -------------- | -------------------------- |
| Standard   | `value = 0.5`  | 0.0 to 1.0 for percentages |
| Percentage | `value = 0.75` | 75% as 0.75                |
| Large      | `value = 2.5`  | Multipliers                |

**Usage Examples:**

```pdx
literacy_rate > 0.5  # More than 50%
add_radicals = { value = 0.1 }  # 10% radicals
modifier = { multiply = 1.5 }

```

### Boolean

True/false values.

| Value | Meaning        | Example             |
| ----- | -------------- | ------------------- |
| `yes` | True/Enabled   | `is_at_war = yes`   |
| `no`  | False/Disabled | `is_democracy = no` |

**Usage Examples:**

```pdx
is_at_war = yes
has_modifier = my_modifier  # Implicit yes
is_subsidized = no

```

---

## String Data Types

### Name/Key Strings

Used for identifiers and localization keys.

| Type          | Format         | Example                |
| ------------- | -------------- | ---------------------- |
| Country Tag   | `XXX`          | `c:FRA`, `c:GER`       |
| State Key     | `STATE_XXX`    | `s:STATE_LONDON`       |
| Building Type | `building_xxx` | `building_steel_mills` |
| Law Type      | `law_xxx`      | `law_slavery_banned`   |
| Technology    | `tech_xxx`     | `tech_nationalism`     |
| Modifier      | `xxx`          | `my_modifier`          |
| Event ID      | `xxx.n`        | `my_event.1`           |

**Usage Examples:**

```pdx
c:FRA
s:STATE_LONDON
has_law = law_type:law_slavery_banned
trigger_event = my_event.1

```

### Localization Strings

Keys that map to display text.

| Type        | Format        | Example             |
| ----------- | ------------- | ------------------- |
| Event Title | `xxx.t`       | `my_event.1.t`      |
| Event Desc  | `xxx.d`       | `my_event.1.d`      |
| Option      | `xxx.a`       | `my_event.1.a`      |
| Modifier    | `xxx`         | `my_modifier`       |
| Concept     | `concept_xxx` | `concept_democracy` |

---

## Complex Data Types

### Color

RGB or RGBA color values.

| Format | Example                   | Usage               |
| ------ | ------------------------- | ------------------- |
| RGB    | `color = { 255 0 0 }`     | Red                 |
| RGBA   | `color = { 255 0 0 255 }` | Red with full alpha |
| Hex    | `color = hex { 00FF00 }`  | Green               |

**Usage Examples:**

```pdx
# In country definition
color = { 0 85 164 }  # France blue

# In scripted GUI
textcolor = { 255 255 255 }  # White

```

### Date

Game dates in year-month-day format.

| Format    | Example               | Notes            |
| --------- | --------------------- | ---------------- |
| Full      | `1850.1.1`            | January 1, 1850  |
| Year only | `year = 1850`         | Any time in year |
| Range     | `1850.6.1 - 1860.6.1` | Date range       |

**Usage Examples:**

```pdx
# In history
1850.1.1 = {
    activate_law = law_type:law_slavery_banned
}

# In triggers
year > 1850

```

### Scope References

References to game scopes.

| Type           | Syntax              | Example                              |
| -------------- | ------------------- | ------------------------------------ |
| Country        | `c:XXX`             | `c:FRA`                              |
| State          | `s:XXX`             | `s:STATE_LONDON`                     |
| Character      | `character:xxx`     | `character:napoleon`                 |
| Interest Group | `ig:xxx`            | `ig:ig_industrialists`               |
| Pop Type       | `pop_type:xxx`      | `pop_type:pop_type_laborers`         |
| Culture        | `cu:xxx`            | `cu:british`                         |
| Religion       | `rel:xxx`           | `rel:protestant`                     |
| Goods          | `goods:xxx`         | `goods:goods_steel`                  |
| Building Type  | `building_type:xxx` | `building_type:building_steel_mills` |
| Law Type       | `law_type:xxx`      | `law_type:law_slavery_banned`        |
| Technology     | `technology:xxx`    | `technology:tech_nationalism`        |
| Party          | `party:xxx`         | `party:party_liberal`                |

### Arrays

Lists of values or scopes.

| Type         | Format              | Example                                       |
| ------------ | ------------------- | --------------------------------------------- |
| String Array | `[ value1 value2 ]` | `valid_states = [ STATE_LONDON STATE_PARIS ]` |
| Scope Array  | `[ c:FRA c:GER ]`   | `major_powers = [ c:FRA c:GBR c:RUS ]`        |

**Usage Examples:**

```pdx
# In script values
valid_buildings = [ building_steel_mills building_munition_plants ]

# In triggers
any_scope_state = {
    limit = { is_in_list = valid_states }
}

```

---

## Special Data Types

### Weights

Used for randomization and AI decisions.

| Type       | Format         | Range          |
| ---------- | -------------- | -------------- |
| Weight     | `base = 100`   | 0 to infinity  |
| Modifier   | `add = 50`     | Adjusts weight |
| Multiplier | `multiply = 2` | Scales weight  |

**Usage Examples:**

```pdx
# In AI strategy
ai_chance = {
    base = 50
    modifier = {
        add = 25
        has_technology = tech_nationalism
    }
}

# In random events
random_events = {
    100 = my_event.1
    50 = my_event.2
}

```

### Triggers

Boolean conditions returning yes/no.

| Format  | Example                            |
| ------- | ---------------------------------- |
| Simple  | `is_at_war = yes`                  |
| Complex | `AND = { trigger_a trigger_b }`    |
| Scope   | `any_state = { is_coastal = yes }` |

**Usage Examples:**

```pdx
limit = {
    is_at_war = no
    infamy < 25
}

```

### Effects

Actions that modify game state.

| Format      | Example                                |
| ----------- | -------------------------------------- |
| Simple      | `add_prestige = 100`                   |
| Complex     | `every_state = { add_modifier = ... }` |
| Conditional | `if = { limit = { ... } effect }`      |

**Usage Examples:**

```pdx
immediate = {
    add_prestige = 50
    every_state = {
        add_modifier = {
            name = celebration
            months = 6
        }
    }
}

```

### Script Values

Named calculations.

| Format    | Example                            |
| --------- | ---------------------------------- |
| Simple    | `value = 10`                       |
| Complex   | `value = { multiply = 2 add = 5 }` |
| Reference | `value = my_script_value`          |

**Usage Examples:**

```pdx
# In modifier
my_modifier = {
    country_prestige_add = my_prestige_value
}

# In effect
add_prestige = { value = my_calculated_value }

```

---

## Type Conversion

### Implicit Conversions

| From    | To      | Example                   |
| ------- | ------- | ------------------------- |
| Integer | Float   | `value = 10` → `10.0`    |
| Boolean | Integer | `yes` → `1`, `no` → `0` |
| Scope   | Boolean | Exists check              |

### Explicit Conversion

```pdx
# Convert float to int via rounding
set_variable = {
    name = rounded_value
    value = {
        value = 10.7
        round = yes
    }
}

# Convert scope to tag
set_variable = {
    name = enemy_tag
    value = c:GER
}

```

---

## Type Safety Best Practices

### Common Type Mismatches

| Error                   | Cause                          | Solution          |
| ----------------------- | ------------------------------ | ----------------- |
| Expected int, got float | Passing 1.5 where int expected | Round or use int  |
| Invalid scope           | Wrong scope type               | Check context     |
| Unknown key             | Typo in string                 | Verify key exists |
| Color wrong size        | RGB vs RGBA mismatch           | Check format      |

### Validation Tips

1. **Use correct decimal format** - `0.5` not `.5`
2. **Check scope types** - Country vs State scopes differ
3. **Verify keys exist** - Test in game or check files
4. **Use proper arrays** - Bracket format for lists

---

## Type Quick Reference Table

| Context          | Expected Type | Example                       |
| ---------------- | ------------- | ----------------------------- |
| `add_prestige`   | Integer       | `add_prestige = 100`          |
| `literacy_rate`  | Float (0-1)   | `literacy_rate > 0.5`         |
| `is_at_war`      | Boolean       | `is_at_war = yes`             |
| `c:`             | Country Tag   | `c:FRA`                       |
| `has_law`        | Law Type      | `law_type:law_slavery_banned` |
| `color`          | Color         | `color = { 255 0 0 }`         |
| `year`           | Integer       | `year > 1850`                 |
| `trigger_event`  | Event ID      | `my_event.1`                  |
| `value` (script) | Script Value  | `value = country_gdp`         |

---

## Cross-References

- See **Appendix A** for scope types
- See **Appendix D** for event targets
- See **Appendix E** for variables
- See **Appendix K** for type-related errors
