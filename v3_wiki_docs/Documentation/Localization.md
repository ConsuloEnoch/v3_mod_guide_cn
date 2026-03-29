# Localization

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.10.

Localization files must be `.yml` format encoded in UTF-8-BOM. Otherwise, the game simply ignores the file. Further, the filename must end with `_l_<language>`; any file name can be used as long as this format is respected. For example: `MODNAME_USAGE_decisions_l_english.yml`.

The localization files are processed in reverse alphabetical order (from Z to A), adding `a` or `0` at the beginning of your localization file will make sure it applied last. When replacing vanilla localization, a better practice is to use a folder `replace` as in `/english/replace/overwriting_l_english.yml`.

**NOTE:** All text presented to the player ***must*** be done through localization keys.

## Contents

- [1 Languages](#languages)
- [2 Basic example](#basic-example)
  - [2.1 Localization reuse](#localization-reuse)
- [3 Formatting](#formatting)
  - [3.1 Colouring characters](#colouring-characters)
  - [3.2 Other custom formatting](#other-custom-formatting)
  - [3.3 Text icons](#text-icons)
- [4 Data functions](#data-functions)
  - [4.1 Function formatting](#function-formatting)
- [5 Concepts](#concepts)
  - [5.1 Alternate concept text](#alternate-concept-text)
- [6 Custom tooltips](#custom-tooltips)
- [7 Saved scopes](#saved-scopes)
  - [7.1 Country as saved scope](#country-as-saved-scope)
  - [7.2 Character as saved scope](#character-as-saved-scope)
- [8 Customizable Localization](#customizable-localization)
  - [8.1 Example](#example)
  - [8.2 Usage](#usage)
  - [8.3 Supported types](#supported-types)
- [9 References](#references)

## Languages

| Language | Internal name |
|----------|---------------|
| English | english |
| Brazilian Portuguese | braz_por |
| French | french |
| German | german |
| Polish | polish |
| Russian | russian |
| Spanish | spanish |
| Japanese | japanese |
| Simplified Chinese | simp_chinese |
| Korean | korean |
| Turkish | turkish |

## Basic example

Each localization entry should appear as follows:

```
l_<lang>:
 key: "Localized text"
```

Comments can be added with `#` outside quotation marks.

### Localization reuse

Localization keys can be used within each other by added `$key$` to the localized string.

```
key1: "example"
key2: "This is an $key1$"
```

## Formatting

All custom formatting begins with a `#` followed by the formatting key. To end formatting, a `#!` is necessary.

### Colouring characters

| Key | Colour |
|-----|--------|
| #! | Ends the current formatting rule |
| #r | Red |
| #green | Green |
| #light_green | Light Green |
| #blue | Blue |
| #white | White |
| #darker_white | Darker White |
| #yellow | Yellow |
| #gold | Gold |
| #black | Black |
| #gray | Gray |

### Other custom formatting

| Key | Effect |
|-----|--------|
| #b | Bolds text |
| #italic | Italicizes text |
| #lore | Lightens text |
| #shadow | Adds drop shadow to text |
| #l/#L | Underlines text |

### Text icons

All text icons start with `@` followed by the icon's key and `!` following the key.

| Key | Icon |
|-----|------|
| @information! | Information |
| @warning! | Warning |
| @money! | Money |
| @green_checkmark! | Yes/Check |
| @red_cross! | No/Cross |
| @construction! | Construction |
| @bur! | Bureaucracy |
| @aut! | Authority |
| @inf! | Influence |
| @innovation! | Innovation |
| @officers! | Officers |
| @capitalists! | Capitalists |
| @clergymen! | Clergymen |
| @engineers! | Engineers |
| @devout! | Devout |

## Data functions

Data functions allow for dynamic text to be included in a localization string. Functions are always enclosed in square brackets.

**Example data functions:**

| Function name | Description |
|---------------|-------------|
| GetName | Returns the name as a tooltipped string |
| GetNameNoFlag | Returns a country's name without the flag |
| GetAdjective | Returns a country's adjective |
| GetPrimaryRoleTitle | Returns a character's primary role |
| GetGoods(' ') | Returns the input goods as an object |
| ScriptValue(' ') | Returns the calculated value of the input named script value |
| GetCurrentBarValue( ) | Returns the value of a progress bar |

### Function formatting

| Code | Function | Incompatible with |
|------|----------|-------------------|
| `*` | Converts values into K, M, or B format | `K` |
| `K` | Converts values into K format | `*`, decimals |
| `=` | Adds "+" to positive, "-" to negative | |
| `+` | Colors positive green, negative red | `- : ;` |
| `-` | Colors positive red, negative green | `+ : ;` |
| `:` | Colors positive gold, negative blue | `- + ;` |
| `;` | Colors positive blue, negative gold | `- + :` |
| `U` | First letter uppercase | `l` |
| `l` | First letter lowercase | `U` |
| `L` | Underlines text | |
| `%` | Converts to percent | |
| `1-5` | Decimal places | `K` |

## Concepts

Concepts are built-in info guides, which provide the player info through a tooltip. To add a concept tooltip to a localization string, use `[<concept_name>]`.

### Alternate concept text

Concepts can also be used with alternate text: `[Concept('concept_construction', 'State Construction Efficiency')]`

## Custom tooltips

Localization strings can be defined with custom tooltips:
- `#tooltippable;tooltip:<tooltip_loc_key> <tooltip_text>#!`
- `#tooltippable #tooltip:<tooltip_loc_key> <tooltip_text>#!#!`

## Saved scopes

Saved scopes can be included in localization through a localization function. These always start with `[SCOPE`, followed by the particular type of scope.

### Country as saved scope

```
immediate = {
    c:USA = {
        save_scope_as = usa_nation_scope
    }
}
```

Usage: `[SCOPE.sCountry('usa_nation_scope').GetName]`

### Character as saved scope

```
immediate = {
    ruler = {
        save_scope_as = pru_leader
    }
}
```

Usage: `[SCOPE.sCharacter('pru_leader').GetFullName]`

## Customizable Localization

Custom localization can be called with `GetCustom('custom_localization_name')` in local scope or `[Localize('custom_localization_name')]` in global scope.

### Example

```
ruler_residence = {
    type = country
    random_valid = yes
    
    text = {
        trigger = {
            has_law = law_type:law_monarchy
        }
        localization_key = custom_royal_palace
    }

    text = {
        trigger = {
            has_law = law_type:law_presidential_republic
        }
        localization_key = custom_presidential_palace
    }

    text = {
        trigger = {
            always = no
        }
        fallback = yes
        localization_key = custom_palace
    }
}
```

### Usage

```
ruler_killed_event.1.d: "Our ruler was killed yesterday, while at the [ROOT.GetCountry.GetCustom('ruler_residence')]."
```

### Supported types

Custom localizations can use any of the following types:

- Battle, Building, BuildingType, CanalType, Character, CivilWar, CombatUnit, CommanderOrder, CommanderOrderType, Country, CountryCreation, CountryDefinition, CountryFormation, Culture, Decree, DiplomaticAction, DiplomaticPact, DiplomaticPlay, DiplomaticRelations, Front, Hq, Ideology, Institution, InstitutionType, Interest, InterestGroup, InterestGroupTrait, JournalEntry, Law, LawType, Market, MarketGoods, Objective, Party, PoliticalMovement, Pop, PopType, Province, Religion, ShippingLane, State, StateRegion, StateTrait, StrategicRegion, Technology, Theater, TradeRoute, War

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Expand](/Category:Expand "Category:Expand")
- [Modding](/Category:Modding "Category:Modding")