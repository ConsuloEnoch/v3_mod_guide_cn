# Appendix B: Complete Trigger Reference

Comprehensive reference for all trigger conditions in Victoria 3, organized by category.

---

## Comparison Triggers

| Trigger | Description      | Example                                       |
| ------- | ---------------- | --------------------------------------------- |
| `>`     | Greater than     | `gdp > 1000000`                               |
| `<`     | Less than        | `prestige < 100`                              |
| `>=`    | Greater or equal | `army_size >= 50`                             |
| `<=`    | Less or equal    | `infamy <= 25`                                |
| `=`     | Equal to         | `government_ideology = ideology_conservative` |
| `!=`    | Not equal to     | `government_ideology != ideology_radical`     |

---

## Boolean Triggers

| Trigger  | Description            | Example                          |
| -------- | ---------------------- | -------------------------------- |
| `exists` | Scope/target exists    | `exists = c:FRA`                 |
| `NOT`    | Logical NOT            | `NOT = { is_at_war = yes }`      |
| `AND`    | Logical AND (default)  | `AND = { trigger_a trigger_b }`  |
| `OR`     | Logical OR             | `OR = { trigger_a trigger_b }`   |
| `NOR`    | Neither condition true | `NOR = { trigger_a trigger_b }`  |
| `NAND`   | Not both true          | `NAND = { trigger_a trigger_b }` |

---

## Country Triggers

### Government & Politics

| Trigger               | Description                 | Example                                             |
| --------------------- | --------------------------- | --------------------------------------------------- |
| `government_ideology` | Current government ideology | `government_ideology = ideology_conservative`       |
| `is_democracy`        | Has democratic government   | `is_democracy = yes`                                |
| `is_monarchy`         | Is monarchy                 | `is_monarchy = yes`                                 |
| `has_law`             | Has specific law            | `has_law = law_type:law_slavery_banned`             |
| `is_enacting_law`     | Currently changing law      | `is_enacting_law = law_type:law_slavery_banned`     |
| `has_ideology`        | Country has ideology        | `has_ideology = ideology:ideology_liberal`          |
| `has_interest_group`  | IG in government            | `has_interest_group = ig:ig_landowners`             |
| `ig_in_government`    | Specific IG ruling          | `ig:ig_industrialists = { ig_in_government = yes }` |
| `has_party`           | Has political party         | `has_party = party:party_liberal`                   |
| `is_election_active`  | Election ongoing            | `is_election_active = yes`                          |
| `has_election_type`   | Specific election type      | `has_election_type = election_type:universal`       |
| `ruler`               | Access ruler scope          | `ruler = { age > 40 }`                              |
| `heir`                | Access heir scope           | `heir = { has_trait = charismatic }`                |

### Economy

| Trigger                 | Description             | Example                                                              |
| ----------------------- | ----------------------- | -------------------------------------------------------------------- |
| `gdp`                   | Gross domestic product  | `gdp > 5000000`                                                      |
| `gdp_per_capita`        | GDP per capita          | `gdp_per_capita > 20`                                                |
| `treasury`              | Current treasury        | `treasury > 100000`                                                  |
| `income_trend`          | Income trend value      | `income_trend > 0`                                                   |
| `num_buildings`         | Total buildings         | `num_buildings > 100`                                                |
| `num_buildings_of_type` | Buildings of type       | `num_buildings_of_type = { type = building_steel_mills value > 10 }` |
| `num_goods_produced`    | Goods produced          | `num_goods_produced = { goods = goods_steel value > 100 }`           |
| `num_goods_consumed`    | Goods consumed          | `num_goods_consumed = { goods = goods_wheat value < 50 }`            |
| `in_debt`               | Currently in debt       | `in_debt = yes`                                                      |
| `in_default`            | In default              | `in_default = yes`                                                   |
| `is_bankrupt`           | Bankrupt                | `is_bankrupt = yes`                                                  |
| `market_price`          | Price of good in market | `market_price = { target = goods_steel value > 30 }`                 |
| `market_price_change`   | Price trend             | `market_price_change = { target = goods_steel value > 0.1 }`         |
| `is_exporting`          | Exporting good          | `is_exporting = goods_steel`                                         |
| `is_importing`          | Importing good          | `is_importing = goods_wheat`                                         |

### Military

| Trigger                 | Description                  | Example                       |
| ----------------------- | ---------------------------- | ----------------------------- |
| `army_size`             | Total army size              | `army_size > 50`              |
| `navy_size`             | Total navy size              | `navy_size > 20`              |
| `num_generals`          | Number of generals           | `num_generals > 5`            |
| `num_admirals`          | Number of admirals           | `num_admirals > 3`            |
| `num_battalions`        | Battalion count              | `num_battalions > 100`        |
| `num_ships`             | Ship count                   | `num_ships > 50`              |
| `is_at_war`             | At war                       | `is_at_war = yes`             |
| `is_at_war_with`        | At war with specific country | `is_at_war_with = c:GER`      |
| `war_exhaustion`        | War exhaustion level         | `war_exhaustion > 50`         |
| `manpower`              | Available manpower           | `manpower > 100000`           |
| `has_war_goal`          | Has war goal                 | `has_war_goal = yes`          |
| `is_defender_in_war`    | Defender in war              | `is_defender_in_war = yes`    |
| `is_attacker_in_war`    | Attacker in war              | `is_attacker_in_war = yes`    |
| `has_mobilized`         | Mobilized for war            | `has_mobilized = yes`         |
| `mobilization_progress` | Mobilization %               | `mobilization_progress > 0.5` |

### Diplomacy

| Trigger                    | Description            | Example                                                    |
| -------------------------- | ---------------------- | ---------------------------------------------------------- |
| `prestige`                 | Prestige rank/value    | `prestige > 100`                                           |
| `infamy`                   | Infamy level           | `infamy < 25`                                              |
| `relations`                | Relations with country | `relations = { target = c:GER value > 0 }`                 |
| `has_diplomatic_pact`      | Has pact type          | `has_diplomatic_pact = { type = alliance target = c:GBR }` |
| `is_ally`                  | Is allied              | `is_ally = c:GBR`                                          |
| `is_rival`                 | Is rival               | `is_rival = c:FRA`                                         |
| `is_subject`               | Is subject nation      | `is_subject = yes`                                         |
| `is_subject_of`            | Subject of specific    | `is_subject_of = c:GBR`                                    |
| `has_subject`              | Has subject            | `has_subject = c:IND`                                      |
| `is_independent`           | Fully independent      | `is_independent = yes`                                     |
| `is_unrecognized`          | Unrecognized power     | `is_unrecognized = yes`                                    |
| `is_unification_candidate` | Can unify              | `is_unification_candidate = yes`                           |
| `is_power_bloc_leader`     | Leads power bloc       | `is_power_bloc_leader = yes`                               |
| `is_in_power_bloc`         | In power bloc          | `is_in_power_bloc = yes`                                   |
| `has_power_bloc`           | Has created bloc       | `has_power_bloc = yes`                                     |

### Demographics

| Trigger                      | Description            | Example                          |
| ---------------------------- | ---------------------- | -------------------------------- |
| `total_population`           | Total pops             | `total_population > 5000000`     |
| `literacy_rate`              | Literacy %             | `literacy_rate > 0.5`            |
| `standard_of_living`         | Average SoL            | `standard_of_living > 15`        |
| `pop_growth`                 | Growth rate            | `pop_growth > 0`                 |
| `num_accepted_cultures`      | Accepted cultures      | `num_accepted_cultures > 3`      |
| `num_discriminated_cultures` | Discriminated cultures | `num_discriminated_cultures < 5` |
| `has_culture`                | Has culture            | `has_culture = cu:british`       |
| `primary_culture`            | Primary culture        | `primary_culture = cu:british`   |
| `has_religion`               | Has religion           | `has_religion = rel:protestant`  |
| `state_religion`             | State religion         | `state_religion = rel:catholic`  |

### Technology

| Trigger                       | Description         | Example                                                         |
| ----------------------------- | ------------------- | --------------------------------------------------------------- |
| `has_technology`              | Has tech researched | `has_technology = tech_nationalism`                             |
| `tech_progress`               | Tech progress       | `tech_progress = { technology = tech_nationalism value > 0.5 }` |
| `num_technologies_researched` | Total techs         | `num_technologies_researched > 50`                              |
| `is_researching`              | Researching tech    | `is_researching = tech_nationalism`                             |

### Geography

| Trigger                     | Description          | Example                                           |
| --------------------------- | -------------------- | ------------------------------------------------- |
| `num_states`                | Number of states     | `num_states > 20`                                 |
| `num_homelands`             | Homeland states      | `num_homelands > 5`                               |
| `num_colonial_states`       | Colonial states      | `num_colonial_states > 3`                         |
| `capital`                   | Access capital state | `capital = { is_coastal = yes }`                  |
| `owns_state`                | Owns state           | `owns_state = s:STATE_LONDON`                     |
| `has_state_in_state_region` | Has state in region  | `has_state_in_state_region = state_region_iberia` |
| `has_claim`                 | Has claim on state   | `has_claim = s:STATE_ALSACE`                      |

---

## State Triggers

### Basic State Info

| Trigger          | Description       | Example                   |
| ---------------- | ----------------- | ------------------------- |
| `is_capital`     | Is capital state  | `is_capital = yes`        |
| `is_coastal`     | Has coastline     | `is_coastal = yes`        |
| `is_homeland`    | Is homeland       | `is_homeland = cu:french` |
| `is_colonial`    | Is colonial state | `is_colonial = yes`       |
| `is_front`       | Is frontline      | `is_front = yes`          |
| `is_under_siege` | Being sieged      | `is_under_siege = yes`    |

### Population

| Trigger                   | Description         | Example                       |
| ------------------------- | ------------------- | ----------------------------- |
| `state_population`        | Total population    | `state_population > 100000`   |
| `state_population_change` | Growth rate         | `state_population_change > 0` |
| `state_literacy`          | Literacy rate       | `state_literacy > 0.4`        |
| `state_sol`               | Standard of living  | `state_sol > 10`              |
| `state_radicalism`        | Radicalism level    | `state_radicalism < 0.3`      |
| `state_loyalism`          | Loyalism level      | `state_loyalism > 0.2`        |
| `state_radicals`          | Number of radicals  | `state_radicals > 10000`      |
| `state_loyalists`         | Number of loyalists | `state_loyalists > 5000`      |

### Economy

| Trigger                   | Description         | Example                                                       |
| ------------------------- | ------------------- | ------------------------------------------------------------- |
| `has_building`            | Has building type   | `has_building = building_steel_mills`                         |
| `num_buildings`           | Building count      | `num_buildings > 10`                                          |
| `num_buildings_of_type`   | Specific type count | `num_buildings_of_type = { type = building_farms value > 5 }` |
| `has_building_level`      | Building level      | `has_building_level = { type = building_farms level > 3 }`    |
| `state_gdp`               | State GDP           | `state_gdp > 100000`                                          |
| `state_gdp_per_capita`    | GDP per capita      | `state_gdp_per_capita > 15`                                   |
| `state_infrastructure`    | Infrastructure      | `state_infrastructure > 50`                                   |
| `has_free_arable_land`    | Free farmland       | `has_free_arable_land = yes`                                  |
| `arable_land`             | Arable land amount  | `arable_land > 100`                                           |
| `arable_land_used`        | Used farmland       | `arable_land_used > 50`                                       |
| `has_trade_route`         | Has trade route     | `has_trade_route = yes`                                       |
| `is_trade_route_exporter` | Exports in route    | `is_trade_route_exporter = yes`                               |
| `is_trade_route_importer` | Imports in route    | `is_trade_route_importer = yes`                               |
| `market_price`            | Local price         | `market_price = { target = goods_steel value > 25 }`          |

### Resources

| Trigger               | Description         | Example                                                         |
| --------------------- | ------------------- | --------------------------------------------------------------- |
| `has_resource`        | Has resource        | `has_resource = resource_iron`                                  |
| `has_resource_amount` | Resource amount     | `has_resource_amount = { resource = resource_iron value > 10 }` |
| `resource_amount`     | Get resource amount | `resource_amount = { resource = resource_coal } > 20`           |

### Political

| Trigger             | Description          | Example                                                             |
| ------------------- | -------------------- | ------------------------------------------------------------------- |
| `has_law`           | Law applies in state | `has_law = law_type:law_slavery_banned`                             |
| `state_has_ig`      | IG has presence      | `state_has_ig = ig:ig_industrialists`                               |
| `state_ig_strength` | IG strength          | `state_ig_strength = { target = ig:ig_industrialists value > 0.3 }` |
| `has_revolution`    | State in revolution  | `has_revolution = yes`                                              |

---

## Pop Triggers

### Demographics

| Trigger             | Description      | Example                             |
| ------------------- | ---------------- | ----------------------------------- |
| `pop_size`          | Population size  | `pop_size > 10000`                  |
| `pop_growth`        | Growth rate      | `pop_growth > 0`                    |
| `pop_type`          | Type of pop      | `pop_type = pop_type_laborers`      |
| `pop_has_culture`   | Culture          | `pop_has_culture = cu:british`      |
| `pop_has_religion`  | Religion         | `pop_has_religion = rel:protestant` |
| `pop_accepted`      | Is accepted      | `pop_accepted = yes`                |
| `pop_discriminated` | Is discriminated | `pop_discriminated = yes`           |

### Economics

| Trigger          | Description        | Example                        |
| ---------------- | ------------------ | ------------------------------ |
| `pop_income`     | Weekly income      | `pop_income > 5`               |
| `pop_savings`    | Savings amount     | `pop_savings > 100`            |
| `pop_sol`        | Standard of living | `pop_sol > 15`                 |
| `pop_paid_taxes` | Tax amount         | `pop_paid_taxes > 0`           |
| `is_employed`    | Has job            | `is_employed = yes`            |
| `is_unemployed`  | No job             | `is_unemployed = yes`          |
| `workplace`      | Has workplace      | `workplace = { exists = yes }` |
| `is_peasant`     | Is peasant         | `is_peasant = yes`             |

### Politics

| Trigger              | Description    | Example                                      |
| -------------------- | -------------- | -------------------------------------------- |
| `pop_is_radical`     | Is radical     | `pop_is_radical = yes`                       |
| `pop_is_loyalist`    | Is loyalist    | `pop_is_loyalist = yes`                      |
| `pop_interest_group` | In IG          | `pop_interest_group = ig:ig_industrialists`  |
| `pop_party`          | In party       | `pop_party = party:party_liberal`            |
| `pop_supports_law`   | Supports law   | `pop_supports_law = law_type:law_free_trade` |
| `pop_approval`       | Approval level | `pop_approval > 0`                           |

---

## Character Triggers

### Basic Info

| Trigger         | Description      | Example                   |
| --------------- | ---------------- | ------------------------- |
| `age`           | Character age    | `age > 30`                |
| `is_ruler`      | Is ruler         | `is_ruler = yes`          |
| `is_heir`       | Is heir          | `is_heir = yes`           |
| `is_general`    | Is general       | `is_general = yes`        |
| `is_admiral`    | Is admiral       | `is_admiral = yes`        |
| `is_politician` | Is politician    | `is_politician = yes`     |
| `has_trait`     | Has trait        | `has_trait = charismatic` |
| `num_traits`    | Number of traits | `num_traits > 2`          |

### Politics

| Trigger                | Description       | Example                                              |
| ---------------------- | ----------------- | ---------------------------------------------------- |
| `is_in_government`     | In government     | `is_in_government = yes`                             |
| `is_ig_leader`         | IG leader         | `is_ig_leader = yes`                                 |
| `is_party_leader`      | Party leader      | `is_party_leader = yes`                              |
| `ig_support`           | IG support level  | `ig_support > 0.3`                                   |
| `is_interested_in_law` | Interested in law | `is_interested_in_law = law_type:law_slavery_banned` |

---

## Building Triggers

| Trigger                 | Description       | Example                                |
| ----------------------- | ----------------- | -------------------------------------- |
| `building_type`         | Type of building  | `building_type = building_steel_mills` |
| `building_level`        | Level of building | `building_level > 5`                   |
| `building_employment`   | Employment rate   | `building_employment > 0.8`            |
| `building_throughput`   | Throughput %      | `building_throughput > 1.0`            |
| `building_profit`       | Weekly profit     | `building_profit > 100`                |
| `building_wage`         | Wage level        | `building_wage > 10`                   |
| `building_workforce`    | Workforce size    | `building_workforce > 1000`            |
| `is_subsidized`         | Is subsidized     | `is_subsidized = yes`                  |
| `is_government_owned`   | Government owned  | `is_government_owned = yes`            |
| `is_under_construction` | Being built       | `is_under_construction = yes`          |

---

## Interest Group Triggers

| Trigger            | Description     | Example                       |
| ------------------ | --------------- | ----------------------------- |
| `ig_type`          | IG type         | `ig_type = ig_industrialists` |
| `ig_clout`         | Political clout | `ig_clout > 0.2`              |
| `ig_approval`      | Approval level  | `ig_approval > 0`             |
| `ig_in_government` | In ruling gov   | `ig_in_government = yes`      |
| `ig_is_radical`    | Is radical      | `ig_is_radical = yes`         |
| `ig_is_marginal`   | Is marginal     | `ig_is_marginal = yes`        |
| `ig_is_powerful`   | Is powerful     | `ig_is_powerful = yes`        |
| `ig_leader`        | Access leader   | `ig_leader = { age > 40 }`    |

---

## Date & Time Triggers

| Trigger         | Description   | Example                              |
| --------------- | ------------- | ------------------------------------ |
| `year`          | Current year  | `year > 1850`                        |
| `month`         | Current month | `month > 6`                          |
| `day`           | Current day   | `day > 15`                           |
| `has_game_rule` | Game rule set | `has_game_rule = rule_historical_ai` |

---

## Cross-References

- See **Appendix A** for scope types
- See **Appendix C** for effects that work with these triggers
- See **Appendix D** for event target values
- See **Appendix K** for common trigger errors
