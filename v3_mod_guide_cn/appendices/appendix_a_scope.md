# Appendix A: Complete Scope Reference

Comprehensive reference for all scope types and iterators in Victoria 3 scripting.

---

## Base Scope Types

| Scope  | Description                                 | Access Example |
| ------ | ------------------------------------------- | -------------- |
| `ROOT` | The initial scope where the script started  | `ROOT`         |
| `THIS` | The current scope                           | `THIS`         |
| `PREV` | The previous scope in the chain             | `PREV`         |
| `FROM` | The scope that triggered the event/decision | `FROM`         |

---

## Country Scopes

| Scope                       | Description                     | Example Usage    |
| --------------------------- | ------------------------------- | ---------------- |
| `c:`                        | Country data target             | `c:FRA` (France) |
| `cu:`                       | Country scope from character    | `cu:character`   |
| `THIS` (in country context) | The current country             | `THIS.capital`   |
| `ROOT` (country event)      | The country receiving the event | `ROOT = c:FRA`   |

### Country Subscopes

| Subscope    | Accesses         | Example                    |
| ----------- | ---------------- | -------------------------- |
| `.capital`  | Capital state    | `c:FRA.capital`            |
| `.heir`     | Heir character   | `c:ENG.heir`               |
| `.ruler`    | Ruler character  | `c:RUS.ruler`              |
| `.overlord` | Overlord country | `vassal.overlord`          |
| `.market`   | Market scope     | `c:USA.market`             |
| `.state`    | Specific state   | `c:GBR.state:STATE_LONDON` |

---

## State Scopes

| Scope                     | Description         | Example          |
| ------------------------- | ------------------- | ---------------- |
| `s:`                      | State data target   | `s:STATE_LONDON` |
| `THIS` (in state context) | The current state   | `THIS.owner`     |
| State from building       | Building's location | `building.state` |
| State from pop            | Pop's location      | `pop.state`      |

### State Subscopes

| Subscope     | Accesses            | Example                |
| ------------ | ------------------- | ---------------------- |
| `.owner`     | Owning country      | `s:STATE_LONDON.owner` |
| `.capital`   | Capital building    | `state.capital`        |
| `.homelands` | Homeland countries  | `state.homelands`      |
| `.country`   | Country with claims | `state.country`        |

---

## Pop Scopes

| Scope             | Description         | Example               |
| ----------------- | ------------------- | --------------------- |
| Pop in context    | Current pop scope   | `THIS` (in pop event) |
| Pop from building | Workers in building | `building.employees`  |
| Pop from state    | Pops in state       | `state.pop_types`     |

### Pop Subscopes

| Subscope          | Accesses           | Example              |
| ----------------- | ------------------ | -------------------- |
| `.country`        | Pop's country      | `pop.country`        |
| `.state`          | Pop's state        | `pop.state`          |
| `.workplace`      | Workplace building | `pop.workplace`      |
| `.interest_group` | IG affiliation     | `pop.interest_group` |

---

## Character Scopes

| Scope                | Description        | Example                     |
| -------------------- | ------------------ | --------------------------- |
| Character in context | Current character  | `THIS` (in character event) |
| `cu:`                | From country scope | `c:FRA.ruler`               |
| Character from IG    | IG leader          | `ig.leader`                 |
| Character from party | Party leader       | `party.leader`              |

### Character Subscopes

| Subscope          | Accesses            | Example                    |
| ----------------- | ------------------- | -------------------------- |
| `.country`        | Character's country | `character.country`        |
| `.interest_group` | Character's IG      | `character.interest_group` |
| `.party`          | Character's party   | `character.party`          |

---

## Building Scopes

| Scope               | Description        | Example                      |
| ------------------- | ------------------ | ---------------------------- |
| Building in context | Current building   | `THIS` (in building trigger) |
| Building from state | Buildings in state | `state.buildings`            |
| Building from pop   | Workplace          | `pop.workplace`              |

### Building Subscopes

| Subscope     | Accesses         | Example              |
| ------------ | ---------------- | -------------------- |
| `.state`     | Building's state | `building.state`     |
| `.owner`     | Building owner   | `building.owner`     |
| `.employees` | Worker pops      | `building.employees` |

---

## Market Scopes

| Scope               | Description      | Example                    |
| ------------------- | ---------------- | -------------------------- |
| Market in context   | Current market   | `THIS` (in market context) |
| Market from country | Country's market | `c:USA.market`             |
| Market from state   | State's market   | `state.market`             |

---

## Interest Group Scopes

| Scope             | Description    | Example                    |
| ----------------- | -------------- | -------------------------- |
| IG in context     | Current IG     | `THIS` (in IG context)     |
| IG from country   | Country's IGs  | `country.interest_groups`  |
| IG from pop       | Pop's IG       | `pop.interest_group`       |
| IG from character | Character's IG | `character.interest_group` |

### IG Subscopes

| Subscope   | Accesses     | Example      |
| ---------- | ------------ | ------------ |
| `.country` | IG's country | `ig.country` |
| `.leader`  | IG leader    | `ig.leader`  |
| `.party`   | IG's party   | `ig.party`   |

---

## Diplomatic Scopes

| Scope           | Description                      | Example                       |
| --------------- | -------------------------------- | ----------------------------- |
| `rel:`          | Relation scope between countries | `rel:c:FRA.c:GER`             |
| Diplomatic pact | Current pact                     | `THIS` (in diplomatic events) |

---

## Iterator Types

### Any_ Iterators (True if ANY match)

| Iterator              | Iterates Over       | Returns |
| --------------------- | ------------------- | ------- |
| `any_country`         | All countries       | Boolean |
| `any_state`           | States in scope     | Boolean |
| `any_pop`             | Pops in scope       | Boolean |
| `any_building`        | Buildings in scope  | Boolean |
| `any_character`       | Characters in scope | Boolean |
| `any_interest_group`  | IGs in scope        | Boolean |
| `any_diplomatic_pact` | Pacts in scope      | Boolean |
| `any_scope_state`     | States in array     | Boolean |
| `any_scope_building`  | Buildings in array  | Boolean |
| `any_scope_pop`       | Pops in array       | Boolean |

### Every_ Iterators (Apply to ALL)

| Iterator               | Iterates Over       | Returns                 |
| ---------------------- | ------------------- | ----------------------- |
| `every_country`        | All countries       | Effects applied to each |
| `every_state`          | States in scope     | Effects applied to each |
| `every_pop`            | Pops in scope       | Effects applied to each |
| `every_building`       | Buildings in scope  | Effects applied to each |
| `every_character`      | Characters in scope | Effects applied to each |
| `every_interest_group` | IGs in scope        | Effects applied to each |
| `every_scope_state`    | States in array     | Effects applied to each |
| `every_scope_building` | Buildings in array  | Effects applied to each |

### Random_ Iterators (Pick ONE randomly)

| Iterator                | Iterates Over       | Returns              |
| ----------------------- | ------------------- | -------------------- |
| `random_country`        | All countries       | One random country   |
| `random_state`          | States in scope     | One random state     |
| `random_pop`            | Pops in scope       | One random pop       |
| `random_building`       | Buildings in scope  | One random building  |
| `random_character`      | Characters in scope | One random character |
| `random_interest_group` | IGs in scope        | One random IG        |
| `random_scope_state`    | States in array     | One random state     |

### Ordered_ Iterators (Pick by ordering)

| Iterator            | Iterates Over       | Ordered By      |
| ------------------- | ------------------- | --------------- |
| `ordered_country`   | All countries       | Specified value |
| `ordered_state`     | States in scope     | Specified value |
| `ordered_pop`       | Pops in scope       | Specified value |
| `ordered_building`  | Buildings in scope  | Specified value |
| `ordered_character` | Characters in scope | Specified value |

**Ordered Iterator Options:**
- `order_by = <value>` - What to order by
- `max = <number>` - Maximum to pick
- `position = 0` - Position in order (0 = first/highest)

---

## Iterator Examples

### Any_ Iterator

```pdx
c:FRA = {
    any_state = {
        is_capital = yes
        has_building = building_arms_factory
    }
}
# Returns true if France has ANY state that is capital AND has arms factory

```

### Every_ Iterator

```pdx
c:FRA = {
    every_state = {
        add_modifier = {
            name = industrial_bonus
            months = 12
        }
    }
}
# Adds modifier to EVERY state in France

```

### Random_ Iterator

```pdx
c:FRA = {
    random_state = {
        limit = {
            has_building = building_steel_mills
        }
        add_modifier = {
            name = steel_boom
            months = 6
        }
    }
}
# Picks ONE random state with steel mills and adds modifier

```

### Ordered_ Iterator

```pdx
c:FRA = {
    ordered_state = {
        order_by = state_gdp
        max = 3
        position = 0
        add_modifier = {
            name = top_economic_state
            months = 12
        }
    }
}
# Applies to the top 3 states by GDP

```

---

## Scope Limitations

| Context           | Available Scopes       | Notes                   |
| ----------------- | ---------------------- | ----------------------- |
| Country Events    | ROOT = country         | FROM may vary           |
| State Events      | ROOT = state           | Use .owner for country  |
| Pop Events        | ROOT = pop             | Use .country, .state    |
| Character Events  | ROOT = character       | Use .country            |
| Diplomatic Events | ROOT = diplomatic_pact | Use FROM for initiator  |
| Journal Entries   | ROOT = country         | Use scope for subscopes |
| Decisions         | ROOT = country         | FROM = decision target  |
| On Actions        | Varies                 | See Appendix G          |

---

## Cross-References

- See **Appendix B** for triggers used within scopes
- See **Appendix C** for effects applied to scopes
- See **Appendix D** for event target syntax
- See **Appendix G** for on-action scope contexts
