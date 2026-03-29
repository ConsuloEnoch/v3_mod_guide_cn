# Data types

From Victoria 3 Wiki

(Redirected from GUI script)

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
| AIAttitude | AI attitude data |
| AIStrategy | AI strategy data |
| AcceptanceStatus | Acceptance status |
| AcceptanceStatusSegment | Acceptance status segment |
| Battle | Battle data |
| Building | Building data |
| BuildingType | Building type |
| CFixedPoint | Number stored with 6 digits of precision |
| Character | Character data |
| Country | Country data |
| CountryDefinition | Country definition |
| Culture | Culture data |
| Goods | Goods data |
| InterestGroup | Interest group data |
| Law | Law data |
| LawType | Law type |
| Market | Market data |
| MarketGoods | Market goods data |
| Party | Party data |
| Pop | Pop data |
| PopType | Pop type |
| PoliticalMovement | Political movement data |
| Religion | Religion data |
| Scope | Scope data |
| State | State data |
| StateRegion | State region data |
| Technology | Technology data |
| Unit | Unit data |
| War | War data |

**Core Data Types:**

| Type | Description |
|------|-------------|
| CVector2f | Type containing two float numbers |
| CVector2i | Type containing two integer numbers |
| CVector3f | Type containing three float numbers |
| CVector3i | Type containing three integer numbers |
| CVector4f | Type containing four float numbers |
| CVector4i | Type containing four integer numbers |
| CPdxFloatRect | Rectangle within a 2D float space |
| CPdxIntRect | Rectangle within a 2D integer space |
| CString | String type |
| CUTF8String | UTF-8 String type |

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
| GetNameNoFormatting | Returns name without formatting | Country, Character |
| GetAdjective | Returns a country's adjective | Country |
| GetAdjectiveNoFormatting | Returns adjective without formatting | Country |
| GetFullName | Returns a character's full name | Character |
| GetFullNameNoFormatting | Returns full name without formatting | Character |
| GetFirstName | Returns a character's first name | Character |
| GetFirstNameNoFormatting | Returns first name without formatting | Character |
| GetLastName | Returns a character's last name | Character |
| GetLastNameNoFormatting | Returns last name without formatting | Character |
| GetSheHe | Returns 'she' or 'he' | Character |
| GetHerHis | Returns 'her' or 'his' | Character |
| GetHerselfHimself | Returns 'herself' or 'himself' | Character |
| GetCustom | Returns custom localization | Various |
| ScriptValue | Returns the calculated value of a named script value | Various |
| GetPopType | Returns pop type | Pop |
| GetGoods | Returns goods | Goods |
| GetCulture | Returns culture | Culture |
| GetReligion | Returns religion | Religion |
| GetState | Returns state | State |
| GetCountry | Returns country | Country |

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
| GetTechnology | Various | Technology | Gets the technology scope |

**Scope Navigation:**

| Promote | Description |
|---------|-------------|
| Self | Returns the same scope |
| Root | Returns the root scope |
| Prev | Returns the previous scope |
| From | Returns the from scope |

## Data functions

Data functions can be formatted in the same way as regular localization strings, but they also have special formatting.

**Format codes:**

| Code | Function |
|------|----------|
| `*` | Converts values into K, M, or B format at thresholds of 1,000, 1,000,000, and 1,000,000,000 |
| `K` | Converts values into K format, fixed 2 decimal places |
| `=` | Adds "+" to positive values and "-" to negative values |
| `+` | Colors positive values green and negative values red |
| `-` | Colors positive values red and negative values green |
| `:` | Colors positive values gold and negative values blue |
| `;` | Colors positive values blue and negative values gold |
| `U` | First letter is made uppercase |
| `l` | First letter is made lowercase |
| `L` | Underlines text |
| `%` | Converts value to percent (multiply by 100, add percent sign) |
| `1-5` | Determines how many decimal places are shown, max 3 with `*` |

## References

- [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
- [1.10](/Category:1.10 "Category:1.10")
- [Modding](/Category:Modding "Category:Modding")