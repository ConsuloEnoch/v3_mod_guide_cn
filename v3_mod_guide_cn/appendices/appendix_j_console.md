# Appendix J: Console Commands Reference

Complete reference for Victoria 3 console commands and debugging tools.

---

## Opening the Console

| Key                | Description                       |
| ------------------ | --------------------------------- |
| `` ` `` (Backtick) | Open/close console                |
| `~` (Tilde)        | Alternative on some keyboards     |
| `^`                | Alternative on European keyboards |

---

## Essential Commands

### Game Control

| Command      | Syntax                     | Description               |
| ------------ | -------------------------- | ------------------------- |
| `help`       | `help` or `help [command]` | List commands or get help |
| `debug_mode` | `debug_mode`               | Show debug info           |
| `observe`    | `observe`                  | Switch to observer mode   |
| `tag`        | `tag [country_tag]`        | Switch to country         |
| `money`      | `money [amount]`           | Add money to player       |
| `prestige`   | `prestige [amount]`        | Add prestige              |
| `infamy`     | `infamy [amount]`          | Set infamy                |
| `yesmen`     | `yesmen`                   | AI accepts all proposals  |
| `nocb`       | `nocb`                     | No casus belli needed     |
| `fow`        | `fow`                      | Toggle fog of war         |
| `ti`         | `ti`                       | Toggle terrain info       |

### Time Control

| Command    | Syntax              | Description    |
| ---------- | ------------------- | -------------- |
| `date`     | `date [YYYY.MM.DD]` | Set game date  |
| `speed`    | `speed [1-5]`       | Set game speed |
| `pause`    | `pause`             | Pause game     |
| ` unpause` | `unpause`           | Unpause game   |
| `tick`     | `tick [number]`     | Advance days   |

---

## Country Commands

### Nation Management

| Command                | Syntax                                     | Description         |
| ---------------------- | ------------------------------------------ | ------------------- |
| `annex`                | `annex [country_tag]`                      | Annex country       |
| `release`              | `release [country_tag]`                    | Release country     |
| `change_tag`           | `change_tag [country_tag]`                 | Change your country |
| `transfer_state`       | `transfer_state [state_key] [country_tag]` | Give state          |
| `add_claim`            | `add_claim [state_key]`                    | Add claim           |
| `add_accepted_culture` | `add_accepted_culture [culture]`           | Accept culture      |
| `add_primary_culture`  | `add_primary_culture [culture]`            | Add primary culture |
| `research`             | `research [tech_key]`                      | Research technology |
| `instant_wargoal`      | `instant_wargoal [type] [country_tag]`     | Add war goal        |

### Politics

| Command           | Syntax                           | Description        |
| ----------------- | -------------------------------- | ------------------ |
| `election`        | `election`                       | Force election     |
| `enact`           | `enact [law_key]`                | Enact law          |
| `activate_law`    | `activate_law [law_key]`         | Activate law       |
| `add_ideology`    | `add_ideology [ideology_key]`    | Add ideology       |
| `remove_ideology` | `remove_ideology [ideology_key]` | Remove ideology    |
| `kill_ruler`      | `kill_ruler`                     | Kill current ruler |
| `kill_heir`       | `kill_heir`                      | Kill heir          |
| `set_ruler`       | `set_ruler [character_key]`      | Set ruler          |
| `add_trait`       | `add_trait [trait_key]`          | Add ruler trait    |

### Economy

| Command            | Syntax                                        | Description        |
| ------------------ | --------------------------------------------- | ------------------ |
| `build`            | `build [building_key] [state_key] [level]`    | Build instantly    |
| `destroy_building` | `destroy_building [building_key] [state_key]` | Destroy building   |
| `goods`            | `goods [goods_key] [amount]`                  | Add goods          |
| `market_price`     | `market_price [goods_key] [price]`            | Set price          |
| `infrastructure`   | `infrastructure [state_key] [amount]`         | Add infrastructure |
| `treasury`         | `treasury [amount]`                           | Set treasury       |

---

## Military Commands

### Warfare

| Command           | Syntax                     | Description    |
| ----------------- | -------------------------- | -------------- |
| `whitepeace`      | `whitepeace [country_tag]` | White peace    |
| `war`             | `war [country_tag]`        | Declare war    |
| `truce`           | `truce [country_tag]`      | Force truce    |
| `mobilize`        | `mobilize`                 | Mobilize army  |
| `demobilize`      | `demobilize`               | Demobilize     |
| `manpower`        | `manpower [amount]`        | Add manpower   |
| `army_experience` | `army_experience [amount]` | Add army XP    |
| `navy_experience` | `navy_experience [amount]` | Add navy XP    |
| `general`         | `general [name]`           | Create general |
| `admiral`         | `admiral [name]`           | Create admiral |

### Units

| Command      | Syntax                          | Description    |
| ------------ | ------------------------------- | -------------- |
| `spawn_army` | `spawn_army [state_key] [size]` | Spawn army     |
| `spawn_navy` | `spawn_navy [state_key] [size]` | Spawn navy     |
| `kill_units` | `kill_units [country_tag]`      | Kill all units |
| `supply`     | `supply [state_key]`            | Set supply     |

---

## State Commands

### State Management

| Command               | Syntax                                       | Description       |
| --------------------- | -------------------------------------------- | ----------------- |
| `incorporate_state`   | `incorporate_state [state_key]`              | Incorporate state |
| `unincorporate_state` | `unincorporate_state [state_key]`            | Unincorporate     |
| `set_state_owner`     | `set_state_owner [state_key] [country_tag]`  | Change owner      |
| `set_state_type`      | `set_state_type [state_key] [type]`          | Set type          |
| `add_state_trait`     | `add_state_trait [state_key] [trait_key]`    | Add trait         |
| `remove_state_trait`  | `remove_state_trait [state_key] [trait_key]` | Remove trait      |
| `set_capital`         | `set_capital [state_key]`                    | Move capital      |

### Population

| Command      | Syntax                                        | Description      |
| ------------ | --------------------------------------------- | ---------------- |
| `pop`        | `pop [pop_type] [culture] [size] [state_key]` | Add pops         |
| `kill_pop`   | `kill_pop [state_key] [amount]`               | Kill population  |
| `literacy`   | `literacy [state_key] [amount]`               | Set literacy     |
| `assimilate` | `assimilate [state_key] [culture]`            | Assimilate       |
| `convert`    | `convert [state_key] [religion]`              | Convert religion |

---

## Event Commands

### Event Control

| Command           | Syntax             | Description       |
| ----------------- | ------------------ | ----------------- |
| `event`           | `event [event_id]` | Trigger event     |
| `clear_events`    | `clear_events`     | Clear event queue |
| `kill_all_events` | `kill_all_events`  | Kill all events   |

### Journal Entries

| Command                | Syntax                           | Description  |
| ---------------------- | -------------------------------- | ------------ |
| `create_journal_entry` | `create_journal_entry [je_key]`  | Create JE    |
| `end_journal_entry`    | `end_journal_entry [je_key]`     | End JE       |
| `set_progress`         | `set_progress [je_key] [amount]` | Set progress |

---

## Debug Commands

### Information Display

| Command           | Syntax               | Description          |
| ----------------- | -------------------- | -------------------- |
| `debug_mode`      | `debug_mode`         | Toggle debug overlay |
| `debug_tooltip`   | `debug_tooltip`      | Detailed tooltips    |
| `province_info`   | `province_info`      | Show province info   |
| `show_errors`     | `show_errors`        | Show script errors   |
| `reload`          | `reload [file_type]` | Reload files         |
| `reload_gfx`      | `reload_gfx`         | Reload graphics      |
| `reload_textures` | `reload_textures`    | Reload textures      |
| `gui_editor`      | `gui_editor`         | Open GUI editor      |

### Logging

| Command     | Syntax       | Description    |
| ----------- | ------------ | -------------- |
| `log`       | `log [text]` | Write to log   |
| `clear_log` | `clear_log`  | Clear log file |
| `dump_data` | `dump_data`  | Export data    |

---

## Cheat Commands

| Command               | Syntax                | Description          |
| --------------------- | --------------------- | -------------------- |
| `god`                 | `god`                 | God mode             |
| `instant_build`       | `instant_build`       | Instant construction |
| `instant_research`    | `instant_research`    | Instant research     |
| `instant_diplomacy`   | `instant_diplomacy`   | Instant diplomacy    |
| `ignore_limits`       | `ignore_limits`       | Ignore constraints   |
| `win_wars`            | `win_wars`            | Auto-win wars        |
| `always_accept_deals` | `always_accept_deals` | AI accepts deals     |
| `ai`                  | `ai`                  | Toggle AI            |
| `human_ai`            | `human_ai`            | AI controls player   |

---

## Testing Commands

| Command           | Syntax                        | Description    |
| ----------------- | ----------------------------- | -------------- |
| `test`            | `test [test_name]`            | Run test       |
| `test_all`        | `test_all`                    | Run all tests  |
| `assert`          | `assert [condition]`          | Test assertion |
| `set_variable`    | `set_variable [name] [value]` | Set debug var  |
| `print_variables` | `print_variables`             | Show variables |

---

## Common Tags

### Major Powers

| Tag   | Country       | Tag   | Country        |
| ----- | ------------- | ----- | -------------- |
| `GBR` | Great Britain | `FRA` | France         |
| `GER` | Germany       | `RUS` | Russia         |
| `USA` | United States | `AUS` | Austria        |
| `ITA` | Italy         | `TUR` | Ottoman Empire |
| `PRU` | Prussia       | `JAP` | Japan          |
| `CHI` | China         | `RAJ` | British Raj    |
| `BRA` | Brazil        | `MEX` | Mexico         |
| `CAN` | Canada        | `AUS` | Australia      |

### Finding Tags

```pdx
# Use debug_mode to see country tags in tooltips
# Hover over country flags or state names

```

---

## Quick Command Reference

### Development Workflow

```pdx
# Enable debug mode
debug_mode

# Quick testing setup
money 100000
prestige 500
infamy 0
instant_build
nocb

# Switch to test country
tag FRA

# Trigger test event
event my_event.1

# Check for errors
show_errors

```

### Testing Modifiers

```pdx
# Add test modifier
add_modifier my_test_modifier

# Check effects in tooltip
debug_tooltip

```

---

## Cross-References

- See **Appendix K** for troubleshooting with console
- See **Appendix L** for test snippets
