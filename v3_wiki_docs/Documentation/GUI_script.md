# GUI script

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for version 1.10.

**GUI script** is the style of scripting used in the game's GUI and localization. This is different from the script used in most other game files, though there are some corresponding objects, such as countries and variables. Similar to game script's scopes, GUI script uses data types; some of these correspond to game scopes while others are used only with GUI script.

GUI script is divided in two types: *Functions* and *Promotes*.

## Contents

- [1 Common features](#common-features)
- [2 Lists of data types](#lists-of-data-types)
  - [2.1 Data type descriptions](#data-type-descriptions)
- [3 Const vs nonconst](#const-vs-nonconst)
- [4 GUI functions](#gui-functions)
  - [4.1 List of all data type functions](#list-of-all-data-type-functions)
- [5 GUI promotes](#gui-promotes)
  - [5.1 List of all GUI promotes](#list-of-all-gui-promotes)
- [6 References](#references)

## Common features

All GUI script is written in "CamelCase", where each word in the function or promote is capitalized and no spaces are used. Each piece of GUI script is always enclosed in square brackets. Within the square brackets, the functions and promotes can be chained together with "dot chaining", for example `[State.GetJobseekersDesc]`.

Some functions and promotes take arguments which are enclosed in parentheses immediately following the function or promote, for example `[GetPopType('peasants').GetName]`.

Some functions and promotes are "global", meaning they can be used without reference to a data type.

## Lists of data types

These tables list all data types used in GUI scripting which have at least one function or promote.

**List of data types for functions**

| Type | Description |
|------|-------------|
| AIAttitude | |
| AIStrategy | |
| AcceptanceStatus | |
| Battle | |
| Building | |
| BuildingType | |
| Character | |
| Country | |
| CountryDefinition | |
| Culture | |
| Goods | |
| InterestGroup | |
| Law | |
| LawType | |
| Market | |
| MarketGoods | |
| Party | |
| Pop | |
| PopType | |
| PoliticalMovement | |
| Religion | |
| Scope | |
| State | |
| StateRegion | |
| Technology | |
| Unit | |
| War | |

## Const vs nonconst

Some data types have const and nonconst versions. A const data type cannot be used with functions or promotes that modify the data.

## GUI functions

GUI functions are used to retrieve data or perform calculations. They are always enclosed in square brackets and use CamelCase.

### List of all data type functions

**Common Functions:**

| Function | Description | Data Type |
|----------|-------------|-----------|
| GetName | Returns the name as a tooltipped string | Various |
| GetNameNoFlag | Returns a country's name without the flag | Country |
| GetAdjective | Returns a country's adjective | Country |
| GetFullName | Returns a character's full name | Character |
| GetFirstName | Returns a character's first name | Character |
| GetLastName | Returns a character's last name | Character |
| GetSheHe | Returns 'she' or 'he' | Character |
| GetHerHis | Returns 'her' or 'his' | Character |
| GetHerselfHimself | Returns 'herself' or 'himself' | Character |
| GetCustom | Returns custom localization | Various |
| ScriptValue | Returns the calculated value of a named script value | Various |

## GUI promotes

GUI promotes are used to change the scope or data type. They allow chaining from one data type to another.

### List of all GUI promotes

**Common Promotes:**

| Promote | From | To | Description |
|---------|------|-----|-------------|
| GetCountry | Various | Country | Gets the country scope |
| GetState | Various | State | Gets the state scope |
| GetMarket | Various | Market | Gets the market scope |
| GetBuilding | Various | Building | Gets the building scope |
| GetCharacter | Various | Character | Gets the character scope |
| GetInterestGroup | Various | InterestGroup | Gets the interest group scope |
| GetPop | Various | Pop | Gets the pop scope |
| GetGoods | Various | Goods | Gets the goods scope |
| GetCulture | Various | Culture | Gets the culture scope |
| GetReligion | Various | Religion | Gets the religion scope |
| GetLaw | Various | Law | Gets the law scope |

## Data functions

Data functions can be formatted in the same way as regular localization strings, but they also have special formatting.

**Format codes:**

| Code | Function |
|------|----------|
| `*` | Converts values into K, M, or B format |
| `K` | Converts values into K format |
| `=` | Adds "+" to positive values and "-" to negative values |
| `+` | Colors positive values green and negative values red |
| `-` | Colors positive values red and negative values green |
| `:` | Colors positive values gold and negative values blue |
| `;` | Colors positive values blue and negative values gold |
| `U` | First letter is made uppercase |
| `l` | First letter is made lowercase |
| `L` | Underlines text |
| `%` | Converts value to percent |
| `1-5` | Determines how many decimal places are shown |

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Modding](/Category:Modding "Category:Modding")