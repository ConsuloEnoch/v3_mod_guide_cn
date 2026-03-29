# Appendix K: Common Errors and Solutions

Quick reference for common Victoria 3 modding errors and their solutions.

---

## Syntax Errors

### Missing Braces

| Error          | Example                           | Solution                              |
| -------------- | --------------------------------- | ------------------------------------- |
| `Expected =`   | `trigger { is_at_war yes }`       | Add `=` → `is_at_war = yes`          |
| `Unexpected }` | `trigger = { is_at_war = yes } }` | Remove extra `}`                      |
| `Missing {`    | `trigger = is_at_war = yes`       | Wrap in braces: `{ is_at_war = yes }` |

**Correct Format:**

```pdx
trigger = {
    is_at_war = yes
}

```

### Invalid Characters

| Error                  | Cause                    | Solution                       |
| ---------------------- | ------------------------ | ------------------------------ |
| `Invalid token`        | Using special characters | Remove `#`, `@`, `$` from keys |
| `Unexpected character` | Unicode issues           | Use ASCII only                 |
| `String not closed`    | Missing quote            | Add closing `"`                |

---

## Scope Errors

### Invalid Scope

| Error                       | Cause                          | Solution                            |
| --------------------------- | ------------------------------ | ----------------------------------- |
| `Invalid scope for trigger` | Wrong scope context            | Check scope type (country vs state) |
| `Expected country scope`    | Using country trigger in state | Move to country scope               |
| `Expected state scope`      | Using state trigger in country | Use `any_state` iterator            |

**Example Fix:**

```pdx
# Wrong - state trigger in country scope
country_event = {
    trigger = {
        is_capital = yes  # ERROR: Expected state scope
    }
}

# Correct - use iterator
trigger = {
    capital = {
        is_coastal = yes  # Now in state scope
    }
}

```

### Undefined Scope

| Error                 | Cause          | Solution                             |
| --------------------- | -------------- | ------------------------------------ |
| `Scope not found`     | Typo in target | Check spelling of country/state tags |
| `Invalid country tag` | Wrong tag      | Use debug mode to verify tags        |
| `Invalid state key`   | Wrong state    | Check state region files             |

---

## Reference Errors

### Undefined Keys

| Error                   | Cause                  | Solution                      |
| ----------------------- | ---------------------- | ----------------------------- |
| `Unknown modifier`      | Modifier doesn't exist | Create modifier or check name |
| `Unknown event`         | Event ID wrong         | Check event file exists       |
| `Unknown law type`      | Wrong law key          | Check law definitions         |
| `Unknown technology`    | Wrong tech key         | Check tech files              |
| `Unknown building type` | Wrong building         | Check building types          |
| `Unknown goods`         | Wrong goods key        | Check goods definitions       |

**Fix Example:**

```pdx
# Wrong - typo
trigger_event = my_evemt.1  # 'evemt' typo

# Correct
trigger_event = my_event.1

```

### File Path Errors

| Error                    | Cause                          | Solution                       |
| ------------------------ | ------------------------------ | ------------------------------ |
| `File not found`         | Wrong path in descriptor.mod   | Check folder structure         |
| `Missing descriptor.mod` | No mod metadata                | Create descriptor.mod          |
| `Invalid path`           | Backslashes vs forward slashes | Use `/` not `\`                |
| `File encoding`          | Wrong encoding                 | Use UTF-8 BOM for localization |

---

## Logic Errors

### Trigger Always False

| Symptom            | Cause                 | Solution                         |
| ------------------ | --------------------- | -------------------------------- |
| Event never fires  | Impossible conditions | Use debug mode to check triggers |
| Decision invisible | Requirements not met  | Test with yesmen/nocb            |
| JE never starts    | Wrong scope           | Verify ROOT scope                |

**Debug Approach:**

```pdx
# Add temporary debug trigger
trigger = {
    always = yes  # Force true for testing
    # ... real triggers
}

```

### Effect Not Working

| Symptom              | Cause        | Solution                    |
| -------------------- | ------------ | --------------------------- |
| Nothing happens      | Wrong scope  | Check effect scope          |
| Modifier not applied | Syntax error | Verify modifier exists      |
| Variable not set     | Wrong syntax | Use correct variable syntax |

---

## Localization Errors

### Missing Strings

| Error                  | Cause             | Solution                 |
| ---------------------- | ----------------- | ------------------------ |
| `LOC_ERROR`            | Key not defined   | Add to localization file |
| `Missing localization` | Wrong file format | Use UTF-8 BOM            |
| `String starts with #` | Comment in value  | Escape or remove         |
| `Invalid format`       | Wrong YAML syntax | Check colon and quotes   |

**Correct Format:**

```yaml
l_english:
 my_event.1.t:0 "Event Title"
 my_event.1.d:0 "Event description here."
 my_event.1.a:0 "Option A"

```

### Encoding Issues

| Symptom              | Cause          | Solution                     |
| -------------------- | -------------- | ---------------------------- |
| Garbled text         | Wrong encoding | Save as UTF-8 BOM            |
| Missing characters   | ASCII only     | Include encoding declaration |
| Special chars broken | BOM missing    | Add BOM header               |

---

## Performance Errors

### CTD (Crash to Desktop)

| Cause             | Solution                         |
| ----------------- | -------------------------------- |
| Recursive trigger | Remove self-referencing triggers |
| Infinite loop     | Add limits to events/JEs         |
| Memory leak       | Clean up variables               |
| Invalid graphics  | Check DDS format                 |
| Missing file      | Verify all file paths            |

### Lag/Freezes

| Cause               | Solution              |
| ------------------- | --------------------- |
| Too many on_actions | Reduce frequency      |
| Complex triggers    | Simplify conditions   |
| Large iterators     | Add limits            |
| Memory usage        | Optimize scope chains |

---

## Crash Logs

### Reading Error Logs

**Location:**

```pdx
Documents/Paradox Interactive/Victoria 3/logs/
├── error.log       # Script errors
├── system.log      # System errors
└── game.log        # Game events

```

### Common Crash Messages

| Message            | Meaning            | Solution              |
| ------------------ | ------------------ | --------------------- |
| `Access violation` | Memory error       | Check for null scopes |
| `Null pointer`     | Missing object     | Verify exists checks  |
| `Stack overflow`   | Infinite recursion | Add iteration limits  |
| `Out of memory`    | Too much data      | Optimize mod          |
| `Division by zero` | Math error         | Check denominators    |

---

## Debug Mode

### Enabling Debug

```pdx
# In console
debug_mode

# Or launch with:
-debug_mode

```

### Debug Features

| Feature           | How to Access        | Use               |
| ----------------- | -------------------- | ----------------- |
| Tag display       | Hover over country   | See country tags  |
| State keys        | Hover over state     | See state regions |
| Error overlay     | Enable debug_mode    | See script errors |
| Detailed tooltips | Enable debug_tooltip | See full values   |

---

## Testing Checklist

### Before Release

- [ ] No errors in error.log
- [ ] All events fire correctly
- [ ] Localization displays properly
- [ ] No CTDs during normal play
- [ ] Performance acceptable
- [ ] Save/Load works
- [ ] Multiplayer compatible (if applicable)

### Validation Steps

1. **Start new game** - No immediate CTD
2. **Check error log** - Should be empty
3. **Test events** - Trigger manually
4. **Check localization** - All strings display
5. **Verify scopes** - Check with debug mode
6. **Test edge cases** - Empty scopes, limits

---

## Quick Fixes

### Event Not Firing

```pdx
# Add debug trigger
trigger = {
    always = yes  # Temporary
}

# Check with console
event my_event.1

```

### Localization Not Showing

```yaml
# Check file encoding (UTF-8 BOM)
# Check key matches exactly
# Verify file in correct localization folder

```

### Modifier Not Working

```pdx
# Verify modifier exists
# Check scope (country vs state)
# Confirm syntax in defines

```

### Variable Issues

```pdx
# Always check if exists first
if = {
    limit = { has_variable = my_var }
    # use variable
}

# Or initialize
if = {
    limit = { NOT = { has_variable = my_var } }
    set_variable = { name = my_var value = 0 }
}

```

---

## Error Prevention

### Best Practices

1. **Always use exists checks** before accessing scopes
2. **Initialize variables** before using them
3. **Test incrementally** - don't write huge files at once
4. **Check error.log frequently** during development
5. **Use version control** to track changes
6. **Validate files** with PDX script tools if available

### Code Style

```pdx
# Good: Explicit and safe
if = {
    limit = {
        exists = c:FRA
        c:FRA = { is_at_war = yes }
    }
    c:FRA = { add_prestige = 100 }
}

# Bad: Assumes scope exists
c:FRA = { add_prestige = 100 }

```

---

## Cross-References

- See **Appendix J** for console commands
- See **Appendix I** for file path conventions
- See **Appendix L** for code snippets with error handling
