# Culture modding

From Victoria 3 Wiki

*See also: [Religion modding](/Religion_modding "Religion modding")*

[Culture](/Culture "Culture") in Victoria 3 represents the abstracted ethnicity and traditions of pops and countries.

## Contents

- [1 Culture definition](#culture-definition)
- [2 Discrimination traits](#discrimination-traits)
  - [2.1 Trait groups](#trait-groups)
- [3 Modifier Definitions](#modifier-definitions)
- [4 Base game cultures](#base-game-cultures)
- [5 References](#references)

## Culture definition

Cultures are defined in /Victoria 3/game/common/cultures/. The definition is a script name, color, religion, traits, list of names, ethnicities, and graphics. For example:

```
mazanderani ={	#Script name can be anything, but best to match desired in-game localization unless it overlaps some other script term
    color= rgb{ 158 68 137 }	#either rgb (255) or hsv (decimal)

    religion = shiite	#Any defined religion; default religion for pops and countries of this culture
    heritage = heritage_iranian
    language = language_tabari
    traditions = { tradition_persianate }

    male_common_first_names={	#space or line-separated list of names, each is a localization key, and so must have no spaces
        [names]
    }
    female_common_first_names = {
	[names]
    }
    common_last_names={
	[names]
    }

    ethnicities = {	#weighted list of ethnicities, affects appearance of pop and character models
	1 = arab
    }
    graphics = arabic	#Graphical culture used for pops and countries with this culture
}
```

The script name is used as a localization key as well as for triggers and effects.

The color can be either RGB or HSV format: RGB uses 0-255 values while HSV uses decimal values.

Heritage is a single heritage trait, language a single language trait, and tradition any number of tradition traits.

Name lists are used for generating characters of that culture and should include at least `male_common_first_names`, `female_common_first_names`, and `common_last_names`. Additional lists can use `noble` and `regal` in place of `common`, e.g. `male_noble_first_names` or `regal_last_names`.

Ethnicities are a weighted list of defined ethnicities in /Victoria 3/game/common/ethnicities/. Unmodified cultures typically have one ethnicity, with a few that have two or more.

Graphics are defined in /Victoria 3/game/common/culture_graphics/, just as a simple defined block, `arabic = {}`. This is referenced in cultures and in various graphics files.

Each culture may also have an `obsessions` block, listing one or more consumable goods that the culture starts obsessed with. Do not define more than the `MAX_NUM_OBSESSIONS` goods as starting obsessions.

Similarly, each culture may also have a `taboos` block, listing one or more consumable goods that the culture has as a taboo. It is not clear if there is a maximum number of taboos. Culture taboos override religion taboos

## Discrimination traits

Cultures and [religions](/Religion_modding "Religion modding") both use discrimination traits defined in /Victoria 3/game/common/discrimination_traits/. Each trait is defined as by a unique script name and block. Each trait has a `type` which can be `heritage`, `language`, or `tradition`. The script name is also a localization key.

For example:

```
language_germanophone = { # a language trait
	type = language
	trait_group = language_group_germanic
}

heritage_abyssinian = { # a heritage trait
	type = heritage
	trait_group = heritage_group_african
}

tradition_rumelian = {
	type = tradition
}
```

The prefixes are only for easy reference and categorization.

Nothing distinguishes a cultural trait from a religious trait besides its use in culture and religion definitions. Religions only use heritage traits, not language or tradition traits.

Heritage and language traits also have a trait group, representing a collection of similar traits.

### Trait groups

Discrimination trait groups are defined in /Victoria 3/game/common/discrimination_trait_groups/. Trait groups are identical to traits except that they cannot be a tradition type, nor do they have a further group.

For example

```
language_group_germanic = { # a language trait group
	type = language
}

heritage_group_african = { # a heritage trait group
	type = heritage
}
```

## Modifier Definitions

*See also: [Modifier types](/Modifier_types "Modifier types"), [Modifier modding](/Modifier_modding "Modifier modding")*

When creating a culture, you must also create two sets of [static modifiers](/Modifier_modding "Modifier modding"), `(culture name)_standard_of_living_modifier_positive` and `(culture name)_standard_of_living_modifier_negative` and `(culture name)_cultural_acceptance_modifier_positive` and `(culture name)_cultural_acceptance_modifier_negative`. You must also create [modifier types](/Modifier_types "Modifier types") named `state_(culture name)_standard_of_living_add`, which is used by the [effect](/Effect "Effect") add_culture_standard_of_living_modifier and `country_(culture name)_cultural_acceptance_add` which is used with add_culture_acceptance_modifier. Examples of these definitions for vanilla cultures can be found at /Victoria 3/game/common/static_modifiers/07_culture_standard_of_living.txt and /Victoria 3/game/common/modifier_type_definitions/99_todo_sort_into_other_files.txt

For example:

```
#in static_modifiers
scottish_standard_of_living_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_standard_of_living_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	state_scottish_standard_of_living_add = 1
}

scottish_cultural_acceptance_modifier_positive = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds"
	country_scottish_cultural_acceptance_add = 1
}

scottish_cultural_acceptance_modifier_negative = {
	icon = "gfx/interface/icons/timed_modifier_icons/modifier_flag_negative.dds"
	country_scottish_cultural_acceptance_add = 1
}

#############################
#in modifier_types
state_scottish_standard_of_living_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}

country_scottish_cultural_acceptance_add = {
	decimals=1
	color=good
	game_data = {
		ai_value=0
	}
}
```

## Base game cultures

*See also: [List of cultures](/List_of_cultures "List of cultures")*

Most base game cultures use the same script name as the English localized name, except all in lowercase, and with spaces or hyphens replaced by underscores and replacing all non-ASCII characters with their closest equivalent.

The following cultures differ from this pattern and use a non-obvious script name. Some are slight respellings, others use alternate names for the culture.

| Culture | Script name |
|---------|-------------|
| Franco-Provençal | francoprovencal |
| English | british |
| Sephardim | sephardic |
| Amazigh | berber |
| Kazakh | kazak |
| Kyrgyz | kirgiz |
| Oria | oriya |
| Punjabi | panjabi |
| Telugu | telegu |
| Aboriginal | aborigine |
| O'odham | oodham |
| Fluvial Bantu | fluvian_bantu |
| Chitrali | kho |
| Szekler | szekely |

## References

- Victoria 3 Wiki - https://vic3.paradoxwikis.com/Culture_modding