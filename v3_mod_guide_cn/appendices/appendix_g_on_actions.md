# Appendix G: On Actions Reference

Complete list of all On Actions in Victoria 3 with descriptions and scope contexts.

---

## Monthly On Actions

| On Action                    | Scope          | Description                       |
| ---------------------------- | -------------- | --------------------------------- |
| `on_monthly_pulse_country`   | Country        | Fires monthly for every country   |
| `on_monthly_pulse_state`     | State          | Fires monthly for every state     |
| `on_monthly_pulse_building`  | Building       | Fires monthly for every building  |
| `on_monthly_pulse_character` | Character      | Fires monthly for every character |
| `on_monthly_pulse_pop`       | Pop            | Fires monthly for every pop       |
| `on_monthly_pulse_ig`        | Interest Group | Fires monthly for every IG        |

---

## Yearly On Actions

| On Action                   | Scope     | Description                      |
| --------------------------- | --------- | -------------------------------- |
| `on_yearly_pulse_country`   | Country   | Fires yearly for every country   |
| `on_yearly_pulse_state`     | State     | Fires yearly for every state     |
| `on_yearly_pulse_character` | Character | Fires yearly for every character |
| `on_yearly_pulse_pop`       | Pop       | Fires yearly for every pop       |

---

## Game Lifecycle

| On Action               | Scope   | Description                  |
| ----------------------- | ------- | ---------------------------- |
| `on_game_start`         | Global  | Fires once when game starts  |
| `on_game_start_country` | Country | Per-country game start setup |
| `on_game_start_state`   | State   | Per-state game start setup   |
| `on_daily_tick`         | Global  | Fires every game day         |

---

## War & Peace

| On Action                   | Scope           | Description                |
| --------------------------- | --------------- | -------------------------- |
| `on_war_started`            | War             | When war begins            |
| `on_war_ended`              | War             | When war ends              |
| `on_battle_started`         | Battle          | When battle begins         |
| `on_battle_ended`           | Battle          | When battle ends           |
| `on_peace_agreement_signed` | Diplomatic Pact | When peace deal signed     |
| `on_wargoal_enforced`       | War Goal        | When war goal enforced     |
| `on_war_goal_added`         | War Goal        | When war goal added to war |

---

## Diplomatic Actions

| On Action                    | Scope           | Description           |
| ---------------------------- | --------------- | --------------------- |
| `on_diplomatic_pact_created` | Diplomatic Pact | When pact created     |
| `on_diplomatic_pact_broken`  | Diplomatic Pact | When pact broken      |
| `on_rivalry_started`         | Country         | When rivalry begins   |
| `on_rivalry_ended`           | Country         | When rivalry ends     |
| `on_alliance_formed`         | Diplomatic Pact | When alliance created |
| `on_alliance_broken`         | Diplomatic Pact | When alliance ends    |
| `on_subject_released`        | Country         | When subject released |
| `on_subject_annexed`         | Country         | When subject annexed  |

---

## Country Formation

| On Action                 | Scope   | Description               |
| ------------------------- | ------- | ------------------------- |
| `on_country_formed`       | Country | When new country formed   |
| `on_unification_complete` | Country | When unification finished |
| `on_revolution_started`   | Country | When revolution begins    |
| `on_revolution_ended`     | Country | When revolution ends      |
| `on_revolution_begins`    | Country | Revolution starts         |
| `on_revolution_won`       | Country | Revolutionaries win       |
| `on_revolution_lost`      | Country | Revolutionaries lose      |

---

## Laws & Politics

| On Action                    | Scope   | Description                 |
| ---------------------------- | ------- | --------------------------- |
| `on_law_activated`           | Country | When law activated          |
| `on_law_deactivated`         | Country | When law deactivated        |
| `on_enactment_started`       | Country | When enactment begins       |
| `on_enactment_ended`         | Country | When enactment ends         |
| `on_enactment_phase_changed` | Country | When phase changes          |
| `on_election_started`        | Country | When election begins        |
| `on_election_ended`          | Country | When election ends          |
| `on_government_formed`       | Country | When government changes     |
| `on_ideology_gained`         | Country | When country gains ideology |
| `on_ideology_lost`           | Country | When country loses ideology |

---

## Interest Groups

| On Action                       | Scope          | Description               |
| ------------------------------- | -------------- | ------------------------- |
| `on_ig_created`                 | Interest Group | When IG created           |
| `on_ig_destroyed`               | Interest Group | When IG destroyed         |
| `on_ig_added_to_government`     | Interest Group | When IG joins government  |
| `on_ig_removed_from_government` | Interest Group | When IG leaves government |
| `on_ig_leader_changed`          | Interest Group | When IG gets new leader   |
| `on_ig_becomes_radical`         | Interest Group | When IG becomes radical   |
| `on_ig_becomes_marginal`        | Interest Group | When IG becomes marginal  |
| `on_ig_becomes_powerful`        | Interest Group | When IG becomes powerful  |
| `on_ig_approval_changed`        | Interest Group | When approval changes     |

---

## Characters

| On Action                         | Scope     | Description             |
| --------------------------------- | --------- | ----------------------- |
| `on_character_created`            | Character | When character created  |
| `on_character_death`              | Character | When character dies     |
| `on_ruler_changed`                | Country   | When ruler changes      |
| `on_heir_changed`                 | Country   | When heir changes       |
| `on_character_exiled`             | Character | When character exiled   |
| `on_character_returns_from_exile` | Character | When returns from exile |
| `on_character_marriage`           | Character | When character marries  |
| `on_character_divorce`            | Character | When character divorces |
| `on_trait_gained`                 | Character | When trait added        |
| `on_trait_lost`                   | Character | When trait removed      |
| `on_character_promoted`           | Character | When promoted           |
| `on_character_demoted`            | Character | When demoted            |

---

## Buildings & Economy

| On Action                  | Scope    | Description                 |
| -------------------------- | -------- | --------------------------- |
| `on_building_created`      | Building | When building created       |
| `on_building_destroyed`    | Building | When building destroyed     |
| `on_building_expanded`     | Building | When building expanded      |
| `on_building_downsized`    | Building | When building downsized     |
| `on_building_bankrupt`     | Building | When building goes bankrupt |
| `on_building_sold`         | Building | When building sold          |
| `on_building_nationalized` | Building | When building nationalized  |
| `on_building_privatized`   | Building | When building privatized    |
| `on_subsidy_started`       | Building | When subsidy begins         |
| `on_subsidy_ended`         | Building | When subsidy ends           |

---

## States

| On Action                   | Scope   | Description               |
| --------------------------- | ------- | ------------------------- |
| `on_state_created`          | State   | When state created        |
| `on_state_transfer`         | State   | When state changes hands  |
| `on_state_claim_added`      | State   | When claim added          |
| `on_state_claim_removed`    | State   | When claim removed        |
| `on_state_homeland_added`   | State   | When homeland added       |
| `on_state_homeland_removed` | State   | When homeland removed     |
| `on_state_incorporated`     | State   | When state incorporated   |
| `on_state_unincorporated`   | State   | When state unincorporated |
| `on_capital_moved`          | Country | When capital changes      |

---

## Pops

| On Action                 | Scope | Description               |
| ------------------------- | ----- | ------------------------- |
| `on_pop_created`          | Pop   | When pop created          |
| `on_pop_merged`           | Pop   | When pops merge           |
| `on_pop_split`            | Pop   | When pop splits           |
| `on_pop_type_changed`     | Pop   | When pop type changes     |
| `on_pop_culture_changed`  | Pop   | When pop culture changes  |
| `on_pop_religion_changed` | Pop   | When pop religion changes |
| `on_pop_moved`            | Pop   | When pop moves states     |
| `on_pop_emigrated`        | Pop   | When pop emigrates        |
| `on_pop_immigrated`       | Pop   | When pop immigrates       |

---

## Technology

| On Action                  | Scope   | Description             |
| -------------------------- | ------- | ----------------------- |
| `on_technology_researched` | Country | When tech researched    |
| `on_technology_unlocked`   | Country | When tech unlocked      |
| `on_research_started`      | Country | When research begins    |
| `on_research_cancelled`    | Country | When research cancelled |

---

## Market

| On Action                   | Scope       | Description                 |
| --------------------------- | ----------- | --------------------------- |
| `on_market_created`         | Market      | When market created         |
| `on_market_joined`          | Country     | When joins market           |
| `on_market_left`            | Country     | When leaves market          |
| `on_market_capital_changed` | Market      | When market capital changes |
| `on_trade_route_created`    | Trade Route | When trade route created    |
| `on_trade_route_destroyed`  | Trade Route | When trade route destroyed  |

---

## Journal Entries

| On Action                   | Scope         | Description              |
| --------------------------- | ------------- | ------------------------ |
| `on_journal_entry_started`  | Journal Entry | When JE created          |
| `on_journal_entry_ended`    | Journal Entry | When JE completed/failed |
| `on_journal_entry_progress` | Journal Entry | When progress changes    |
| `on_journal_entry_timeout`  | Journal Entry | When JE times out        |

---

## Power Blocs

| On Action                      | Scope      | Description             |
| ------------------------------ | ---------- | ----------------------- |
| `on_power_bloc_created`        | Power Bloc | When bloc created       |
| `on_power_bloc_disbanded`      | Power Bloc | When bloc disbanded     |
| `on_power_bloc_member_added`   | Country    | When joins bloc         |
| `on_power_bloc_member_removed` | Country    | When leaves bloc        |
| `on_power_bloc_leader_changed` | Power Bloc | When leadership changes |

---

## Decisions

| On Action                       | Scope    | Description         |
| ------------------------------- | -------- | ------------------- |
| `on_decision_taken`             | Decision | When decision taken |
| `on_decision_cooldown_complete` | Decision | When cooldown ends  |

---

## Player Actions

| On Action                    | Scope   | Description                 |
| ---------------------------- | ------- | --------------------------- |
| `on_player_country_selected` | Country | When player selects country |
| `on_spectator_mode_entered`  | Global  | When entering spectator     |
| `on_spectator_mode_exited`   | Global  | When exiting spectator      |

---

## Scope Quick Reference

| On Action Prefix | Scope Type      |
| ---------------- | --------------- |
| `on_*_country`   | Country         |
| `on_*_state`     | State           |
| `on_*_character` | Character       |
| `on_*_pop`       | Pop             |
| `on_*_building`  | Building        |
| `on_*_ig`        | Interest Group  |
| `on_*_war`       | War             |
| `on_*_pact`      | Diplomatic Pact |
| `on_*_market`    | Market          |

---

## Usage Example

```pdx
# In on_actions file
on_actions = {
    on_monthly_pulse_country = {
        effect = {
            if = {
                limit = {
                    is_at_war = yes
                    NOT = { has_variable = war_months }
                }
                set_variable = { name = war_months value = 0 }
            }
            if = {
                limit = { is_at_war = yes }
                change_variable = { name = war_months add = 1 }
            }
        }
    }

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

## Cross-References

- See **Appendix A** for scope types
- See **Appendix C** for effect usage
- See **Appendix I** for file paths
- See **Appendix K** for on_action errors
