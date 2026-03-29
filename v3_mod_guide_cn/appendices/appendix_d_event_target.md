# Appendix D: Complete Event Target Reference

Comprehensive reference for event targets, data targets, and value targets in Victoria 3 scripting.

---

## Data Targets

Data targets access specific game objects and scopes.

### Country Data Targets

| Target   | Description    | Example  |
| -------- | -------------- | -------- |
| `c:`     | Country by tag | `c:FRA`  |
| `c:ROOT` | Root country   | `c:ROOT` |
| `c:FROM` | From country   | `c:FROM` |
| `c:THIS` | This country   | `c:THIS` |

### State Data Targets

| Target      | Description   | Example          |
| ----------- | ------------- | ---------------- |
| `s:`        | State by key  | `s:STATE_LONDON` |
| `s:capital` | Capital state | `c:FRA.capital`  |

### Character Data Targets

| Target       | Description            | Example               |
| ------------ | ---------------------- | --------------------- |
| `cu:`        | Character from country | `cu:c:FRA`            |
| `character:` | Character by ID        | `character:char_name` |

### Interest Group Data Targets

| Target     | Description            | Example                                             |
| ---------- | ---------------------- | --------------------------------------------------- |
| `ig:`      | Interest group by type | `ig:ig_industrialists`                              |
| `ig:c:FRA` | IG in country          | `ig:ig_industrialists = { ig_in_government = yes }` |

### Pop Type Data Targets

| Target      | Description     | Example                      |
| ----------- | --------------- | ---------------------------- |
| `pop_type:` | Pop type by key | `pop_type:pop_type_laborers` |

### Culture Data Targets

| Target | Description    | Example      |
| ------ | -------------- | ------------ |
| `cu:`  | Culture by key | `cu:british` |

### Religion Data Targets

| Target | Description     | Example          |
| ------ | --------------- | ---------------- |
| `rel:` | Religion by key | `rel:protestant` |

### Goods Data Targets

| Target   | Description  | Example             |
| -------- | ------------ | ------------------- |
| `goods:` | Goods by key | `goods:goods_steel` |

### Building Type Data Targets

| Target           | Description     | Example                              |
| ---------------- | --------------- | ------------------------------------ |
| `building_type:` | Building by key | `building_type:building_steel_mills` |

### Law Type Data Targets

| Target      | Description | Example                       |
| ----------- | ----------- | ----------------------------- |
| `law_type:` | Law by key  | `law_type:law_slavery_banned` |

### Technology Data Targets

| Target        | Description | Example                       |
| ------------- | ----------- | ----------------------------- |
| `technology:` | Tech by key | `technology:tech_nationalism` |

### Diplomatic Pact Data Targets

| Target             | Description | Example                    |
| ------------------ | ----------- | -------------------------- |
| `diplomatic_pact:` | Pact type   | `diplomatic_pact:alliance` |

### Party Data Targets

| Target   | Description  | Example               |
| -------- | ------------ | --------------------- |
| `party:` | Party by key | `party:party_liberal` |

---

## Value Targets

Value targets return numeric or string values for use in comparisons and calculations.

### Country Value Targets

| Target               | Returns            | Example                      |
| -------------------- | ------------------ | ---------------------------- |
| `gdp`                | Total GDP          | `gdp > 1000000`              |
| `gdp_per_capita`     | GDP per capita     | `gdp_per_capita > 20`        |
| `treasury`           | Treasury amount    | `treasury > 50000`           |
| `income`             | Weekly income      | `income > 1000`              |
| `expenses`           | Weekly expenses    | `expenses < 800`             |
| `prestige`           | Prestige value     | `prestige > 100`             |
| `infamy`             | Infamy value       | `infamy < 25`                |
| `army_size`          | Army size          | `army_size > 50`             |
| `navy_size`          | Navy size          | `navy_size > 20`             |
| `manpower`           | Available manpower | `manpower > 100000`          |
| `num_states`         | Number of states   | `num_states > 10`            |
| `num_buildings`      | Total buildings    | `num_buildings > 100`        |
| `total_population`   | Total population   | `total_population > 1000000` |
| `literacy_rate`      | Literacy %         | `literacy_rate > 0.5`        |
| `standard_of_living` | Average SoL        | `standard_of_living > 15`    |
| `war_exhaustion`     | War exhaustion     | `war_exhaustion > 50`        |
| `num_generals`       | General count      | `num_generals > 5`           |
| `num_admirals`       | Admiral count      | `num_admirals > 3`           |
| `num_battalions`     | Battalion count    | `num_battalions > 100`       |
| `num_ships`          | Ship count         | `num_ships > 50`             |

### State Value Targets

| Target                 | Returns            | Example                     |
| ---------------------- | ------------------ | --------------------------- |
| `state_population`     | State population   | `state_population > 100000` |
| `state_gdp`            | State GDP          | `state_gdp > 50000`         |
| `state_gdp_per_capita` | GDP per capita     | `state_gdp_per_capita > 15` |
| `state_literacy`       | Literacy rate      | `state_literacy > 0.4`      |
| `state_sol`            | Standard of living | `state_sol > 10`            |
| `state_infrastructure` | Infrastructure     | `state_infrastructure > 50` |
| `state_radicalism`     | Radicalism level   | `state_radicalism < 0.3`    |
| `state_loyalism`       | Loyalism level     | `state_loyalism > 0.2`      |
| `num_buildings`        | Building count     | `num_buildings > 10`        |
| `arable_land`          | Arable land        | `arable_land > 100`         |
| `arable_land_used`     | Used farmland      | `arable_land_used > 50`     |

### Pop Value Targets

| Target         | Returns            | Example             |
| -------------- | ------------------ | ------------------- |
| `pop_size`     | Pop size           | `pop_size > 10000`  |
| `pop_income`   | Weekly income      | `pop_income > 5`    |
| `pop_savings`  | Savings amount     | `pop_savings > 100` |
| `pop_sol`      | Standard of living | `pop_sol > 15`      |
| `pop_approval` | Approval level     | `pop_approval > 0`  |

### Character Value Targets

| Target       | Returns          | Example            |
| ------------ | ---------------- | ------------------ |
| `age`        | Character age    | `age > 30`         |
| `num_traits` | Number of traits | `num_traits > 2`   |
| `ig_support` | IG support       | `ig_support > 0.3` |

### Building Value Targets

| Target                | Returns        | Example                     |
| --------------------- | -------------- | --------------------------- |
| `building_level`      | Building level | `building_level > 5`        |
| `building_employment` | Employment %   | `building_employment > 0.8` |
| `building_throughput` | Throughput     | `building_throughput > 1.0` |
| `building_profit`     | Weekly profit  | `building_profit > 100`     |
| `building_wage`       | Wage level     | `building_wage > 10`        |
| `building_workforce`  | Workforce size | `building_workforce > 1000` |

### Interest Group Value Targets

| Target        | Returns         | Example                                                             |
| ------------- | --------------- | ------------------------------------------------------------------- |
| `ig_clout`    | Political clout | `ig_clout > 0.2`                                                    |
| `ig_approval` | Approval level  | `ig_approval > 0`                                                   |
| `ig_strength` | State strength  | `state_ig_strength = { target = ig:ig_industrialists value > 0.3 }` |

### Diplomatic Value Targets

| Target                | Returns        | Example                                                      |
| --------------------- | -------------- | ------------------------------------------------------------ |
| `relations`           | Relation value | `relations = { target = c:GER value > 0 }`                   |
| `market_price`        | Price of goods | `market_price = { target = goods_steel value > 30 }`         |
| `market_price_change` | Price change   | `market_price_change = { target = goods_steel value > 0.1 }` |

### Date Value Targets

| Target  | Returns       | Example       |
| ------- | ------------- | ------------- |
| `year`  | Current year  | `year > 1850` |
| `month` | Current month | `month > 6`   |
| `day`   | Current day   | `day > 15`    |

---

## Subscope Access

Access nested scopes using dot notation.

### Country Subscopes

| Access              | Returns          | Example                    |
| ------------------- | ---------------- | -------------------------- |
| `.capital`          | Capital state    | `c:FRA.capital`            |
| `.ruler`            | Ruler character  | `c:FRA.ruler`              |
| `.heir`             | Heir character   | `c:FRA.heir`               |
| `.overlord`         | Overlord country | `c:IND.overlord`           |
| `.market`           | Market scope     | `c:USA.market`             |
| `.state[STATE_KEY]` | Specific state   | `c:GBR.state:STATE_LONDON` |
| `.interest_groups`  | All IGs          | `c:FRA.interest_groups`    |
| `.states`           | All states       | `c:FRA.states`             |

### State Subscopes

| Access       | Returns           | Example                    |
| ------------ | ----------------- | -------------------------- |
| `.owner`     | Owning country    | `s:STATE_LONDON.owner`     |
| `.country`   | Claimant country  | `s:STATE_LONDON.country`   |
| `.market`    | State's market    | `s:STATE_LONDON.market`    |
| `.buildings` | All buildings     | `s:STATE_LONDON.buildings` |
| `.homelands` | Homeland cultures | `s:STATE_LONDON.homelands` |

### Character Subscopes

| Access            | Returns             | Example                    |
| ----------------- | ------------------- | -------------------------- |
| `.country`        | Character's country | `character.country`        |
| `.interest_group` | Character's IG      | `character.interest_group` |
| `.party`          | Character's party   | `character.party`          |

### Pop Subscopes

| Access            | Returns            | Example              |
| ----------------- | ------------------ | -------------------- |
| `.country`        | Pop's country      | `pop.country`        |
| `.state`          | Pop's state        | `pop.state`          |
| `.workplace`      | Workplace building | `pop.workplace`      |
| `.interest_group` | Pop's IG           | `pop.interest_group` |

### Building Subscopes

| Access       | Returns          | Example              |
| ------------ | ---------------- | -------------------- |
| `.state`     | Building's state | `building.state`     |
| `.owner`     | Building owner   | `building.owner`     |
| `.employees` | Worker pops      | `building.employees` |

### Interest Group Subscopes

| Access     | Returns      | Example      |
| ---------- | ------------ | ------------ |
| `.country` | IG's country | `ig.country` |
| `.leader`  | IG leader    | `ig.leader`  |
| `.party`   | IG's party   | `ig.party`   |

---

## Comparison Examples

### Using Value Targets

```pdx
# Compare GDP
c:FRA = {
    gdp > 1000000
}

# Compare relations
relations = {
    target = c:GER
    value > 20
}

# Complex comparison
ROOT = {
    gdp > c:GBR.gdp
}

```

### Using Data Targets

```pdx
# Check if country exists
exists = c:FRA

# Check law
has_law = law_type:law_slavery_banned

# Check technology
has_technology = technology:tech_nationalism

```

### Using Subscopes

```pdx
# Access capital state
c:FRA = {
    capital = {
        is_coastal = yes
    }
}

# Access ruler character
c:FRA = {
    ruler = {
        has_trait = charismatic
    }
}

# Compare states
s:STATE_LONDON.owner = c:GBR

```

---

## Cross-References

- See **Appendix A** for iterator usage with targets
- See **Appendix B** for triggers using value targets
- See **Appendix C** for effects applying to targets
- See **Appendix F** for data type definitions
