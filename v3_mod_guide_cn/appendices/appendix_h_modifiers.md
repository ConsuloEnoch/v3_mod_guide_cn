# Appendix H: Modifiers Reference

Complete reference for modifier types and categories in Victoria 3.

---

## Country Modifiers

### Economy Modifiers

| Modifier                                     | Effect                | Example Value   |
| -------------------------------------------- | --------------------- | --------------- |
| `country_gdp_growth_add`                     | GDP growth rate       | `0.05` = +5%    |
| `country_gdp_growth_mult`                    | GDP growth multiplier | `0.1` = +10%    |
| `country_treasury_growth_add`                | Treasury growth       | `0.1` = +10%    |
| `country_income_tax_rate_add`                | Income tax rate       | `0.05` = +5%    |
| `country_consumption_tax_rate_add`           | Consumption tax       | `0.05` = +5%    |
| `country_tariff_rate_add`                    | Tariff rate           | `0.1` = +10%    |
| `country_building_cost_mult`                 | Building cost         | `-0.1` = -10%   |
| `country_building_throughput_add`            | Throughput            | `0.05` = +5%    |
| `country_building_throughput_mult`           | Throughput multiplier | `0.1` = +10%    |
| `country_laborers_mortality_mult`            | Laborer mortality     | `0.1` = +10%    |
| `country_infrastructure_add`                 | Infrastructure        | `10` = +10      |
| `country_infrastructure_from_population_add` | Infra from pop        | `0.001` = +0.1% |

### Political Modifiers

| Modifier                                    | Effect                | Example Value |
| ------------------------------------------- | --------------------- | ------------- |
| `country_political_strength_add`            | Political strength    | `0.1` = +10%  |
| `country_legitimacy_add`                    | Legitimacy            | `10` = +10    |
| `country_legitimacy_headofstate_add`        | Legitimacy from ruler | `5` = +5      |
| `country_ideology_gov_ig_change_speed_mult` | Ideology change speed | `0.2` = +20%  |
| `country_law_enactment_success_add`         | Enactment success     | `0.1` = +10%  |
| `country_law_enactment_time_mult`           | Enactment time        | `-0.2` = -20% |
| `country_law_enactment_radicals_mult`       | Enactment radicals    | `-0.1` = -10% |
| `country_law_enactment_approval_add`        | Enactment approval    | `5` = +5      |
| `country_election_campaign_cost_mult`       | Campaign cost         | `-0.1` = -10% |
| `country_party_pol_str_mult`                | Party strength        | `0.1` = +10%  |

### Military Modifiers

| Modifier                                  | Effect             | Example Value |
| ----------------------------------------- | ------------------ | ------------- |
| `country_military_wages_mult`             | Military wages     | `0.1` = +10%  |
| `country_morale_recovery_mult`            | Morale recovery    | `0.2` = +20%  |
| `country_morale_loss_mult`                | Morale loss        | `-0.1` = -10% |
| `country_offense_add`                     | Offense            | `10` = +10    |
| `country_defense_add`                     | Defense            | `10` = +10    |
| `country_mobilization_speed_mult`         | Mobilization speed | `0.2` = +20%  |
| `country_mobilization_cost_mult`          | Mobilization cost  | `-0.1` = -10% |
| `country_war_exhaustion_mult`             | War exhaustion     | `-0.1` = -10% |
| `country_army_maintenance_mult`           | Army maintenance   | `-0.1` = -10% |
| `country_navy_maintenance_mult`           | Navy maintenance   | `-0.1` = -10% |
| `country_manpower_recovery_mult`          | Manpower recovery  | `0.1` = +10%  |
| `country_battle_defense_own_capital_mult` | Capital defense    | `0.2` = +20%  |

### Diplomatic Modifiers

| Modifier                                 | Effect               | Example Value |
| ---------------------------------------- | -------------------- | ------------- |
| `country_prestige_add`                   | Prestige             | `100` = +100  |
| `country_prestige_mult`                  | Prestige multiplier  | `0.1` = +10%  |
| `country_infamy_decay_mult`              | Infamy decay         | `0.2` = +20%  |
| `country_infamy_generation_mult`         | Infamy generation    | `-0.1` = -10% |
| `country_diplomatic_play_maneuvers_add`  | Diplomatic maneuvers | `10` = +10    |
| `country_diplomatic_play_maneuvers_mult` | Maneuvers multiplier | `0.1` = +10%  |
| `country_diplomatic_acceptance_add`      | Diplo acceptance     | `10` = +10    |
| `country_relations_decay_mult`           | Relations decay      | `0.1` = +10%  |
| `country_power_bloc_strength_add`        | Power bloc strength  | `0.1` = +10%  |

### Technology Modifiers

| Modifier                                      | Effect          | Example Value |
| --------------------------------------------- | --------------- | ------------- |
| `country_research_speed_mult`                 | Research speed  | `0.1` = +10%  |
| `country_tech_spread_mult`                    | Tech spread     | `0.1` = +10%  |
| `country_production_tech_research_speed_mult` | Production tech | `0.15` = +15% |
| `country_military_tech_research_speed_mult`   | Military tech   | `0.15` = +15% |
| `country_society_tech_research_speed_mult`    | Society tech    | `0.15` = +15% |

### Population Modifiers

| Modifier                         | Effect             | Example Value    |
| -------------------------------- | ------------------ | ---------------- |
| `country_pop_growth_add`         | Population growth  | `0.001` = +0.1%  |
| `country_birth_rate_add`         | Birth rate         | `0.001` = +0.1%  |
| `country_mortality_add`          | Mortality          | `-0.001` = -0.1% |
| `country_literacy_growth_add`    | Literacy growth    | `0.05` = +5%     |
| `country_sol_growth_add`         | SoL growth         | `0.05` = +5%     |
| `country_standard_of_living_add` | Standard of living | `1` = +1         |
| `country_expected_sol_add`       | Expected SoL       | `1` = +1         |

### Culture & Religion

| Modifier                             | Effect             | Example Value |
| ------------------------------------ | ------------------ | ------------- |
| `country_conversion_speed_add`       | Conversion speed   | `0.1` = +10%  |
| `country_assimilation_speed_add`     | Assimilation speed | `0.1` = +10%  |
| `country_promotion_speed_add`        | Promotion speed    | `0.1` = +10%  |
| `country_demotion_speed_add`         | Demotion speed     | `-0.1` = -10% |
| `country_acceptance_status_gain_add` | Acceptance gain    | `0.1` = +10%  |

---

## State Modifiers

### Economy

| Modifier                                                 | Effect             | Example Value   |
| -------------------------------------------------------- | ------------------ | --------------- |
| `state_construction_mult`                                | Construction speed | `0.1` = +10%    |
| `state_infrastructure_add`                               | Infrastructure     | `10` = +10      |
| `state_infrastructure_from_buildings_add`                | Building infra     | `0.1` = +10%    |
| `state_building_barracks_max_level_add`                  | Barracks cap       | `5` = +5 levels |
| `state_building_port_max_level_add`                      | Port cap           | `2` = +2 levels |
| `state_building_university_max_level_add`                | University cap     | `2` = +2 levels |
| `state_building_government_administration_max_level_add` | Admin cap          | `5` = +5        |
| `state_arable_land_add`                                  | Arable land        | `20` = +20      |
| `state_arable_land_mult`                                 | Arable land mult   | `0.1` = +10%    |

### Resources

| Modifier                              | Effect            | Example Value |
| ------------------------------------- | ----------------- | ------------- |
| `state_resources_tech_production_add` | Resource output   | `0.1` = +10%  |
| `state_coal_mine_throughput_add`      | Coal throughput   | `0.1` = +10%  |
| `state_iron_mine_throughput_add`      | Iron throughput   | `0.1` = +10%  |
| `state_lead_mine_throughput_add`      | Lead throughput   | `0.1` = +10%  |
| `state_sulfur_mine_throughput_add`    | Sulfur throughput | `0.1` = +10%  |
| `state_gold_mine_throughput_add`      | Gold throughput   | `0.1` = +10%  |
| `state_oil_rig_throughput_add`        | Oil throughput    | `0.1` = +10%  |
| `state_rubber_lodge_throughput_add`   | Rubber throughput | `0.1` = +10%  |

### Population

| Modifier                               | Effect              | Example Value   |
| -------------------------------------- | ------------------- | --------------- |
| `state_pop_growth_add`                 | Population growth   | `0.001` = +0.1% |
| `state_migration_pull_add`             | Migration pull      | `50` = +50      |
| `state_migration_pull_mult`            | Migration pull mult | `0.2` = +20%    |
| `state_migration_push_mult`            | Migration push      | `-0.2` = -20%   |
| `state_radicals_from_sol_change_mult`  | Radicals from SoL   | `-0.1` = -10%   |
| `state_loyalists_from_sol_change_mult` | Loyalists from SoL  | `0.1` = +10%    |
| `state_turmoil_effects_mult`           | Turmoil effects     | `-0.1` = -10%   |

### Political

| Modifier                           | Effect              | Example Value |
| ---------------------------------- | ------------------- | ------------- |
| `state_radicals_in_government_add` | Radicals in gov     | `-0.1` = -10% |
| `state_revolution_progress_mult`   | Revolution progress | `0.2` = +20%  |
| `state_tax_collection_mult`        | Tax collection      | `0.1` = +10%  |

---

## Building Modifiers

### Production

| Modifier                                       | Effect          | Example Value    |
| ---------------------------------------------- | --------------- | ---------------- |
| `building_throughput_add`                      | Throughput      | `0.1` = +10%     |
| `building_throughput_mult`                     | Throughput mult | `0.1` = +10%     |
| `building_output_mult`                         | Output          | `0.1` = +10%     |
| `building_input_mult`                          | Input           | `-0.05` = -5%    |
| `building_employment_mult`                     | Employment      | `0.1` = +10%     |
| `building_workforce_scaled_mortality_risk_add` | Mortality       | `-0.001` = -0.1% |

### Specific Building Types

| Modifier                                            | Effect         | Example Value |
| --------------------------------------------------- | -------------- | ------------- |
| `building_group_bg_agriculture_throughput_add`      | Agriculture    | `0.1` = +10%  |
| `building_group_bg_ranching_throughput_add`         | Ranching       | `0.1` = +10%  |
| `building_group_bg_plantations_throughput_add`      | Plantations    | `0.1` = +10%  |
| `building_group_bg_mining_throughput_add`           | Mining         | `0.1` = +10%  |
| `building_group_bg_manufacturing_throughput_add`    | Manufacturing  | `0.1` = +10%  |
| `building_group_bg_urban_facilities_throughput_add` | Urban          | `0.1` = +10%  |
| `building_group_bg_infrastructure_throughput_add`   | Infrastructure | `0.1` = +10%  |
| `building_group_bg_government_throughput_add`       | Government     | `0.1` = +10%  |
| `building_group_bg_military_throughput_add`         | Military       | `0.1` = +10%  |

### Military Buildings

| Modifier                                | Effect          | Example Value |
| --------------------------------------- | --------------- | ------------- |
| `building_group_bg_army_throughput_add` | Army throughput | `0.1` = +10%  |
| `building_group_bg_navy_throughput_add` | Navy throughput | `0.1` = +10%  |
| `building_unit_type_army_offense_add`   | Army offense    | `10` = +10    |
| `building_unit_type_army_defense_add`   | Army defense    | `10` = +10    |
| `building_unit_type_navy_offense_add`   | Navy offense    | `10` = +10    |
| `building_unit_type_navy_defense_add`   | Navy defense    | `10` = +10    |

---

## Pop Modifiers

### Economic

| Modifier                  | Effect         | Example Value |
| ------------------------- | -------------- | ------------- |
| `pop_income_mult`         | Income         | `0.1` = +10%  |
| `pop_tax_capacity_add`    | Tax capacity   | `10` = +10    |
| `pop_qualifications_mult` | Qualifications | `0.1` = +10%  |
| `pop_workforce_add`       | Workforce      | `100` = +100  |

### Political

| Modifier                          | Effect             | Example Value |
| --------------------------------- | ------------------ | ------------- |
| `pop_political_strength_mult`     | Political strength | `0.1` = +10%  |
| `pop_approval_add`                | Approval           | `5` = +5      |
| `pop_interest_group_approval_add` | IG approval        | `5` = +5      |

### Needs

| Modifier               | Effect       | Example Value |
| ---------------------- | ------------ | ------------- |
| `pop_basic_needs_add`  | Basic needs  | `-0.1` = -10% |
| `pop_luxury_needs_add` | Luxury needs | `-0.1` = -10% |
| `pop_expected_sol_add` | Expected SoL | `1` = +1      |

---

## Interest Group Modifiers

| Modifier                             | Effect             | Example Value |
| ------------------------------------ | ------------------ | ------------- |
| `interest_group_pol_str_mult`        | Political strength | `0.1` = +10%  |
| `interest_group_pop_attraction_mult` | Pop attraction     | `0.1` = +10%  |
| `interest_group_approval_add`        | Approval           | `5` = +5      |
| `interest_group_approval_mult`       | Approval mult      | `0.1` = +10%  |

---

## Character Modifiers

| Modifier                      | Effect        | Example Value       |
| ----------------------------- | ------------- | ------------------- |
| `character_popularity_add`    | Popularity    | `10` = +10          |
| `character_command_limit_add` | Command limit | `5` = +5 battalions |
| `character_morale_cap_add`    | Morale cap    | `10` = +10          |
| `character_death_chance_mult` | Death chance  | `-0.1` = -10%       |
| `character_health_add`        | Health        | `0.1` = +10%        |

---

## Market Modifiers

| Modifier                                  | Effect                | Example Value |
| ----------------------------------------- | --------------------- | ------------- |
| `market_price_deviation_from_base_add`    | Price deviation       | `0.1` = +10%  |
| `market_price_deviation_from_base_mult`   | Price deviation mult  | `0.1` = +10%  |
| `market_trade_route_competitiveness_mult` | Trade competitiveness | `0.1` = +10%  |

---

## Modifier Categories

| Category         | Description         | Common Use                  |
| ---------------- | ------------------- | --------------------------- |
| `country`        | Nation-wide effects | Laws, tech, events          |
| `state`          | State-level effects | Local conditions, resources |
| `building`       | Building-specific   | Industry, military          |
| `building_group` | Building categories | Sector bonuses              |
| `pop`            | Population effects  | Class bonuses               |
| `pop_type`       | Specific pop types  | Laborer bonuses             |
| `interest_group` | IG effects          | Political favor             |
| `character`      | Character effects   | Leader bonuses              |
| `market`         | Market effects      | Trade, prices               |
| `goods`          | Goods-specific      | Production bonuses          |

---

## Modifier Example

```pdx
# In common/modifiers/my_modifiers.txt
my_custom_modifier = {
    icon = "gfx/interface/icons/modifiers/my_icon.dds"

    country_prestige_add = 50
    country_research_speed_mult = 0.1
    state_construction_mult = 0.1
    building_throughput_add = 0.05

    # Duration can be set when adding
    # add_modifier = { name = my_custom_modifier months = 12 }
}

# For temporary modifiers with decay
temporary_boost = {
    country_prestige_add = 100
    decay = yes  # Modifier decays over time
}

```

---

## Cross-References

- See **Appendix C** for add_modifier effect
- See **Appendix I** for modifier file paths
- See **Appendix L** for modifier code snippets
