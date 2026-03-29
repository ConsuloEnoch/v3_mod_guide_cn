# Appendix C: Complete Effect Reference

Comprehensive reference for all effect commands in Victoria 3, organized by category.

---

## Scope Effects

### Scope Change

| Effect                   | Description       | Example                                              |
| ------------------------ | ----------------- | ---------------------------------------------------- |
| `set_global_variable`    | Set global var    | `set_global_variable = { name = my_var value = 1 }`  |
| `change_global_variable` | Modify global var | `change_global_variable = { name = my_var add = 5 }` |
| `remove_global_variable` | Delete global var | `remove_global_variable = my_var`                    |

### Event Effects

| Effect          | Description       | Example                                          |
| --------------- | ----------------- | ------------------------------------------------ |
| `trigger_event` | Fire event        | `trigger_event = { id = my_event.1 days = 7 }`   |
| `random_events` | Random event pool | `random_events = { 100 = event.1 50 = event.2 }` |

---

## Country Effects

### Government & Politics

| Effect                   | Description      | Example                                            |
| ------------------------ | ---------------- | -------------------------------------------------- |
| `activate_law`           | Activate law     | `activate_law = law_type:law_slavery_banned`       |
| `deactivate_law`         | Deactivate law   | `deactivate_law = law_type:law_slavery_allowed`    |
| `start_enactment`        | Start law change | `start_enactment = law_type:law_slavery_banned`    |
| `add_ideology`           | Add ideology     | `add_ideology = ideology:ideology_liberal`         |
| `remove_ideology`        | Remove ideology  | `remove_ideology = ideology:ideology_conservative` |
| `add_ruler`              | Add ruler        | `add_ruler = { character = character_name }`       |
| `remove_ruler`           | Remove ruler     | `remove_ruler = yes`                               |
| `add_heir`               | Add heir         | `add_heir = { character = character_name }`        |
| `remove_heir`            | Remove heir      | `remove_heir = yes`                                |
| `add_to_power_bloc`      | Join power bloc  | `add_to_power_bloc = c:GBR`                        |
| `remove_from_power_bloc` | Leave power bloc | `remove_from_power_bloc = yes`                     |
| `create_power_bloc`      | Create bloc      | `create_power_bloc = { name = my_bloc }`           |
| `add_claim`              | Add claim        | `add_claim = s:STATE_ALSACE`                       |
| `remove_claim`           | Remove claim     | `remove_claim = s:STATE_ALSACE`                    |

### Economy

| Effect               | Description   | Example                                           |
| -------------------- | ------------- | ------------------------------------------------- |
| `add_treasury`       | Add money     | `add_treasury = 10000`                            |
| `add_tax`            | Modify tax    | `add_tax = { tax_type = income_tax add = 0.05 }`  |
| `set_tax`            | Set tax rate  | `set_tax = { tax_type = income_tax value = 0.1 }` |
| `add_gold_reserves`  | Add reserves  | `add_gold_reserves = 5000`                        |
| `add_market_capital` | Add to market | `add_market_capital = 1000`                       |

### Military

| Effect                | Description    | Example                                                      |
| --------------------- | -------------- | ------------------------------------------------------------ |
| `add_war_goal`        | Add war goal   | `add_war_goal = { type = conquer_state target = c:FRA }`     |
| `white_peace`         | White peace    | `white_peace = c:FRA`                                        |
| `annex`               | Annex country  | `annex = c:MEX`                                              |
| `transfer_state`      | Transfer state | `transfer_state = { target = c:FRA state = s:STATE_ALSACE }` |
| `release_country`     | Release nation | `release_country = c:POL`                                    |
| `puppet`              | Create puppet  | `puppet = c:BRA`                                             |
| `add_manpower`        | Add manpower   | `add_manpower = 10000`                                       |
| `add_army_experience` | Army XP        | `add_army_experience = 100`                                  |
| `add_navy_experience` | Navy XP        | `add_navy_experience = 100`                                  |
| `mobilize`            | Mobilize army  | `mobilize = yes`                                             |
| `demobilize`          | Demobilize     | `demobilize = yes`                                           |

### Diplomacy

| Effect                   | Description      | Example                                                       |
| ------------------------ | ---------------- | ------------------------------------------------------------- |
| `add_prestige`           | Add prestige     | `add_prestige = 100`                                          |
| `add_infamy`             | Add infamy       | `add_infamy = 10`                                             |
| `add_relations`          | Modify relations | `add_relations = { target = c:FRA value = 20 }`               |
| `set_relations`          | Set relations    | `set_relations = { target = c:FRA value = 50 }`               |
| `create_diplomatic_pact` | Create pact      | `create_diplomatic_pact = { type = alliance target = c:GBR }` |
| `break_diplomatic_pact`  | End pact         | `break_diplomatic_pact = { type = alliance target = c:GBR }`  |
| `add_rivalry`            | Add rival        | `add_rivalry = c:FRA`                                         |
| `remove_rivalry`         | Remove rival     | `remove_rivalry = c:FRA`                                      |
| `set_ally`               | Set alliance     | `set_ally = c:GBR`                                            |

### Technology

| Effect                    | Description  | Example                                                          |
| ------------------------- | ------------ | ---------------------------------------------------------------- |
| `add_research`            | Add progress | `add_research = { technology = tech_nationalism progress = 50 }` |
| `unlock_technology`       | Unlock tech  | `unlock_technology = tech_nationalism`                           |
| `set_research_technology` | Set research | `set_research_technology = tech_nationalism`                     |

### Demographics

| Effect                    | Description      | Example                               |
| ------------------------- | ---------------- | ------------------------------------- |
| `add_primary_culture`     | Add culture      | `add_primary_culture = cu:irish`      |
| `remove_primary_culture`  | Remove culture   | `remove_primary_culture = cu:irish`   |
| `add_accepted_culture`    | Accept culture   | `add_accepted_culture = cu:polish`    |
| `remove_accepted_culture` | Unaccept culture | `remove_accepted_culture = cu:polish` |
| `set_state_religion`      | Change religion  | `set_state_religion = rel:catholic`   |

---

## State Effects

### Ownership

| Effect              | Description    | Example                         |
| ------------------- | -------------- | ------------------------------- |
| `transfer_state_to` | Transfer state | `transfer_state_to = c:FRA`     |
| `set_state_owner`   | Set owner      | `set_state_owner = c:FRA`       |
| `set_state_type`    | State type     | `set_state_type = incorporated` |

### Economy

| Effect                     | Description      | Example                                                                  |
| -------------------------- | ---------------- | ------------------------------------------------------------------------ |
| `create_building`          | Create building  | `create_building = { building = building_steel_mills level = 5 }`        |
| `destroy_building`         | Destroy building | `destroy_building = building_steel_mills`                                |
| `add_building_level`       | Add levels       | `add_building_level = { type = building_farms levels = 2 }`              |
| `set_building_subsidized`  | Subsidize        | `set_building_subsidized = { type = building_steel_mills status = yes }` |
| `add_state_infrastructure` | Add infra        | `add_state_infrastructure = 10`                                          |
| `add_arable_land`          | Add farmland     | `add_arable_land = 20`                                                   |

### Population

| Effect                  | Description     | Example                                                              |
| ----------------------- | --------------- | -------------------------------------------------------------------- |
| `add_pop`               | Add population  | `add_pop = { pop_type = laborers culture = cu:british size = 1000 }` |
| `remove_pop`            | Remove pops     | `remove_pop = { pop_type = laborers size = 500 }`                    |
| `convert_pop_type`      | Convert pops    | `convert_pop_type = { from = peasants to = laborers }`               |
| `set_state_homeland`    | Set homeland    | `set_state_homeland = cu:french`                                     |
| `remove_state_homeland` | Remove homeland | `remove_state_homeland = cu:french`                                  |

### Political

| Effect               | Description    | Example                             |
| -------------------- | -------------- | ----------------------------------- |
| `add_radicals`       | Add radicals   | `add_radicals = { value = 0.1 }`    |
| `add_loyalists`      | Add loyalists  | `add_loyalists = { value = 0.1 }`   |
| `set_state_religion` | State religion | `set_state_religion = rel:catholic` |

---

## Pop Effects

### Demographics

| Effect             | Description     | Example                               |
| ------------------ | --------------- | ------------------------------------- |
| `change_pop_type`  | Change type     | `change_pop_type = pop_type_laborers` |
| `set_pop_culture`  | Change culture  | `set_pop_culture = cu:german`         |
| `set_pop_religion` | Change religion | `set_pop_religion = rel:catholic`     |
| `add_pop_size`     | Change size     | `add_pop_size = 100`                  |
| `kill_pop`         | Kill population | `kill_pop = { value = 0.1 }`          |

### Economics

| Effect          | Description   | Example                                |
| --------------- | ------------- | -------------------------------------- |
| `add_savings`   | Add savings   | `add_savings = 100`                    |
| `add_income`    | Add income    | `add_income = 5`                       |
| `set_workplace` | Set workplace | `set_workplace = building_steel_mills` |

### Politics

| Effect                   | Description    | Example                                         |
| ------------------------ | -------------- | ----------------------------------------------- |
| `set_pop_interest_group` | Set IG         | `set_pop_interest_group = ig:ig_industrialists` |
| `add_radicalism`         | Add radicalism | `add_radicalism = 0.1`                          |
| `add_loyalism`           | Add loyalism   | `add_loyalism = 0.1`                            |

---

## Character Effects

### Basic

| Effect               | Description    | Example                        |
| -------------------- | -------------- | ------------------------------ |
| `add_trait`          | Add trait      | `add_trait = charismatic`      |
| `remove_trait`       | Remove trait   | `remove_trait = arrogant`      |
| `set_character_role` | Set role       | `set_character_role = general` |
| `kill_character`     | Kill character | `kill_character = yes`         |
| `retire_character`   | Retire         | `retire_character = yes`       |

### Political

| Effect                | Description | Example                                     |
| --------------------- | ----------- | ------------------------------------------- |
| `set_character_ig`    | Set IG      | `set_character_ig = ig:ig_industrialists`   |
| `set_character_party` | Set party   | `set_character_party = party:party_liberal` |
| `make_ruler`          | Make ruler  | `make_ruler = yes`                          |
| `make_heir`           | Make heir   | `make_heir = yes`                           |

---

## Building Effects

| Effect                 | Description    | Example                      |
| ---------------------- | -------------- | ---------------------------- |
| `set_building_level`   | Set level      | `set_building_level = 10`    |
| `add_building_level`   | Add levels     | `add_building_level = 2`     |
| `destroy_building`     | Destroy        | `destroy_building = yes`     |
| `set_subsidized`       | Set subsidized | `set_subsidized = yes`       |
| `set_government_owned` | Set ownership  | `set_government_owned = yes` |
| `set_workforce`        | Set workforce  | `set_workforce = 1000`       |
| `add_workforce`        | Add workers    | `add_workforce = 100`        |

---

## Interest Group Effects

| Effect                   | Description     | Example                          |
| ------------------------ | --------------- | -------------------------------- |
| `add_ig_clout`           | Add clout       | `add_ig_clout = 0.1`             |
| `set_ig_clout`           | Set clout       | `set_ig_clout = 0.3`             |
| `add_ig_approval`        | Add approval    | `add_ig_approval = 10`           |
| `set_ig_approval`        | Set approval    | `set_ig_approval = 5`            |
| `set_ig_leader`          | Set leader      | `set_ig_leader = character_name` |
| `add_to_government`      | Add to gov      | `add_to_government = yes`        |
| `remove_from_government` | Remove from gov | `remove_from_government = yes`   |

---

## Modifier Effects

| Effect                 | Description      | Example                                                      |
| ---------------------- | ---------------- | ------------------------------------------------------------ |
| `add_modifier`         | Add modifier     | `add_modifier = { name = my_modifier months = 12 }`          |
| `remove_modifier`      | Remove modifier  | `remove_modifier = my_modifier`                              |
| `add_country_modifier` | Country modifier | `add_country_modifier = { name = modifier_name months = 6 }` |
| `add_state_modifier`   | State modifier   | `add_state_modifier = { name = modifier_name months = 6 }`   |

---

## Journal Entry Effects

| Effect                       | Description  | Example                                              |
| ---------------------------- | ------------ | ---------------------------------------------------- |
| `create_journal_entry`       | Create JE    | `create_journal_entry = { type = my_journal_entry }` |
| `end_journal_entry`          | End JE       | `end_journal_entry = my_journal_entry`               |
| `set_journal_entry_progress` | Set progress | `set_journal_entry_progress = 50`                    |
| `add_journal_entry_progress` | Add progress | `add_journal_entry_progress = 10`                    |

---

## Cross-References

- See **Appendix A** for scope contexts
- See **Appendix B** for trigger conditions
- See **Appendix H** for modifier definitions
- See **Appendix K** for common effect errors
