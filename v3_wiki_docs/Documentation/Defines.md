# Defines

From Victoria 3 Wiki

**Defines** are variables used by the engine. They regulate basic game behaviors and settings that are not opened to scripting (IG approval thresholds, camera field-of-view, etc.).

Defines are static and global: they apply to the whole game and cannot be changed dynamically.

Vanilla values are configured in the folder /Victoria 3/game/common/defines, primarily in `00_defines.txt`.

Each of the lists on this represents a section of the defines; in the defines files, these sections are all prefixed with `N`, for example `NCountry`.

## Contents

- [1 Define modding](#define-modding)
- [2 00_defines](#00_defines)
  - [2.1 Game](#game)
  - [2.2 JominiMap](#jominimap)
  - [2.3 Country](#country)
  - [2.4 Politics](#politics)
  - [2.5 Economy](#economy)
  - [2.6 Military](#military)
  - [2.7 Diplomacy](#diplomacy)
  - [2.8 PowerBlocs](#powerblocs)
  - [2.9 Pops](#pops)
  - [2.10 Events](#events)
  - [2.11 Technology](#technology)
  - [2.12 Characters](#characters)
  - [2.13 Battle](#battle)
  - [2.14 War](#war)
  - [2.15 TravelNetwork](#travelnetwork)
  - [2.16 HarvestConditions](#harvestconditions)
  - [2.17 Text](#text)
  - [2.18 Debug](#debug)
- [3 00_ai](#00_ai)
- [4 00_audio](#00_audio)
- [5 00_graphics](#00_graphics)
- [6 00_interfaces](#00_interfaces)
- [7 00_shaders](#00_shaders)
- [8 References](#references)

## Define modding

Defines can be modified individually or in batches without overwriting an entire defines file. This better preserves compatibility and makes it easier to keep up with changes in future patches.

To modify a define, create a new file in <mod>/common/defines/ that loads after the base game files such as `01_mod_defines.txt`. In that file, add a block for each set of defines to be modified and include the modified defines in those blocks, for example:

```
NCountry = {
	INCORPORATION_TIME_NO_MATCH = 100	# Base game 20 years; Years if the state's Homeland cultures have nothing in common with the country's primary cultures
}

NDiplomacy = {
	COUNTRY_TIER_HEGEMONY_PRESTIGE = 150	# Base game 50
}
```

In the case of multiple mods modifying the same define, the mod with the last loaded filename determines the final value of the define.

## 00_defines

### Game

| Define | Default Value | Dev Comment |
|--------|---------------|-------------|
| START_DATE | "1836.1.1" | |
| END_DATE | "1936.1.1" | |
| SAVE_VERSION | 0 | |
| MP_LAG_TICKS_BOUNDS | 28 | # Host will advance up to a week ahead of players ( 7 * 4 ) |
| DEAD_OBJ_UNDESTROYED_DAYS | 22 | # number of days "killed"/removed objects will persist in memory before ultimately destroyed as they are referenced by events etc |
| MAX_NUMBER_OF_AUTOSAVES | 5 | # The game will only keep the MAX_NUMBER_OF_AUTOSAVES latest autosaves. |

### JominiMap

| Define | Default Value | Dev Comment |
|--------|---------------|-------------|
| WORLD_EXTENTS_X | 8192 | |
| WORLD_EXTENTS_Y | 24 | #This determines the max height of the world. Original settings = 25.5 |
| WORLD_EXTENTS_Z | 3615 | |
| WATERLEVEL | 1.74 | #Original Settings 3.7 |

### Country

| Define | Default Value | Dev Comment |
|--------|---------------|-------------|
| DEFAULT_COUNTRY_TYPE | "recognized" | |
| COMPANY_COUNTRY_TYPE | "company" | |
| DEFAULT_MAX_NUM_COUNTRY_FORMATION_CANDIDATES | 3 | # If nothing is specified in the country formation, this is used |
| COUNTRY_FORMATION_CANDIDATE_MIN_RANK | 6 | # countries with a lower rank value than this cannot be formation candidates |
| MOVE_CAPITAL_COOLDOWN_YEARS | 5 | |
| MOVE_MARKET_CAPITAL_COOLDOWN_YEARS | 5 | |
| MAX_POWER_EFFECT | 1.0 | # The max by which a power excess/deficiency modifier can scale |
| GREAT_POWER_RANK_KEY | "great_power" | |
| MAJOR_POWER_RANK_KEY | "major_power" | |
| MINOR_POWER_RANK_KEY | "minor_power" | |
| SPLIT_STATE_DOMINANT_LAND_SHARE_THRESHOLD | 0.5 | # States with more land share than this can use the region's name |
| SPLIT_STATE_PRIME_LAND_WEIGHT | 5.0 | |
| CAPITAL_CULTURE_CORE_WEIGHT | 10 | |
| CAPITAL_NON_INCORPORATED_WEIGHT | 0.001 | |
| DEFAULT_SUBSISTENCE_BUILDING | "building_subsistence_farm" | |
| CONSTRUCTION_CAMP_BUILDING | "building_construction_sector" | |
| BARRACKS_BUILDING | "building_barrack" | |
| NAVAL_BASE_BUILDING | "building_naval_base" | |
| PORT_BUILDING | "building_port" | |
| URBAN_CENTER_BUILDING | "building_urban_center" | |
| CONSCRIPTION_CENTER_BUILDING | "building_conscription_center" | |
| CONSCRIPTION_CENTER_LEVEL_POPULATION_DIVISOR | 1000 | # Civilian population is divded by this amount to calculate maximum conscription center level [>=1] |
| TRADE_CENTER_BUILDING | "building_trade_center" | |
| MANOR_HOUSE_BUILDING | "building_manor_house" | |
| FINANCIAL_DISTRICT_BUILDING | "building_financial_district" | |
| RAILWAY_BUILDING | "building_railway" | |
| POWER_BLOC_STATUE_BUILDING | "building_power_bloc_statue" | |
| COMPANY_HEADQUARTER_BUILDING | "building_company_headquarter" | |
| COMPANY_REGIONAL_HEADQUARTER_BUILDING | "building_company_regional_headquarter" | |
| CONSTRUCTION_QUEUE_INCREMENT_SHIFT | 5 | # Increment/Decrement used for buildings construction queue when holding down Shift |
| CONSTRUCTION_QUEUE_INCREMENT_CONTROL | 10 | # Increment/Decrement used for buildings construction queue when holding down Ctrl |
| WEEKS_TO_STORE_LOYALIST_RADICAL_STATISTICS | 52 | # Number of weeks of statistics for loyalists/radicals that is stored and shown |
| INCORPORATION_TIME_SAME_CULTURE | 2 | # Years if the state is a Homeland of one of the country's primary cultures |
| INCORPORATION_TIME_SAME_HERITAGE_AND_LANGUAGE | 5 | # Years if the state is a Homeland of a culture that matches of one of the country's primary cultures' Heritage and Language traits |
| INCORPORATION_TIME_SAME_HERITAGE_OR_LANGUAGE | 10 | # Years if the state is a Homeland of a culture that matches of one of the country's primary cultures' Heritage traits |
| INCORPORATION_TIME_SAME_TRAIT_GROUP | 15 | # Years if the state is a Homeland of a culture with any trait in common with a country's primary cultures |
| INCORPORATION_TIME_NO_MATCH | 25 | # Years if the state's Homeland cultures have nothing in common with the country's primary cultures |
| INCORPORATION_TIME_MIN_MULTIPLIER | 0.1 | # Incorporation speed cannot be reduced below this by modifiers |
| JOURNAL_ENTRY_UPDATE_ACTIVE | 4 | # Number of ticks between each update of Active (Possible) Journal Entries, can be overriden on journal entry type |
| JOURNAL_ENTRY_UPDATE_INACTIVE | 14 | # Number of ticks between each update of Inactive Journal Entries, can be overriden on journal entry type |
| MAX_TRADITION_TRAITS_PER_CULTURE | 4 | # How many tradition traits a culture is allowed to have at most |

*[Content continues with all the define tables...]*

## References

- Victoria 3 Wiki - https://vic3.paradoxwikis.com/Defines