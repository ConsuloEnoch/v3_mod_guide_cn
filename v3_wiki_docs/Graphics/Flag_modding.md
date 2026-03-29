# Flag modding

From Victoria 3 Wiki

[Country flags](/List_of_flags "List of flags") in Victoria 3 are selected by [triggers](/Triggers "Triggers") from scripted *coats of arms* which are made up of one or more graphical elements.

## Contents

- [1 Flag definition](#flag-definition)
  - [1.1 Trigger scope rules](#trigger-scope-rules)
- [2 Coat of arms](#coat-of-arms)
  - [2.1 Pattern](#pattern)
  - [2.2 Emblem](#emblem)
  - [2.3 Sub](#sub)
  - [2.4 Overwriting coats of arms](#overwriting-coats-of-arms)
- [3 Power bloc emblems](#power-bloc-emblems)
- [4 Coat of arm templates](#coat-of-arm-templates)
- [5 Script terms](#script-terms)
- [6 Coat of arms colors and unit model colors](#coat-of-arms-colors-and-unit-model-colors)
- [7 References](#references)

## Flag definition

Country flag selection is scripted in /common/flag_definitions/. Each country with one or more defined flags should have its TAG listed as a block with a `flag_definition` block for each possible flag. The following example is taken from /Victoria 3/game/common/flag_definitions/00_flag_definitions.txt.

```
# FLAG_DEFINITION_LIST = {		# countries search for a list with the same name as their tag, the DEFAULT list is always included, if no flag definition is applicable for a country then its tag is used a COA_KEY
#	includes = ANOTHER_LIST		# includes another list in this list, can be repeated
#
#	flag_definition = {			# the flag definitions that make up this list, can be repeated
#		coa = [list] COA_KEY	# main flag, optional list keyword denotes a coa template
#		allow_overlord_canton = yes				# default no
#		coa_with_overlord_canton = <[list] coa>	# flag where a canton can be placed, optional list keyword same as above, defaults to coa
#		overlord_canton_offset = { x y }		# canton placement offset, default { 0 0 }
#		overlord_canton_scale = { x y }			# canton placement scale, default { 0.5 0.5 }
#		subject_canton = [list] COA_KEY	# canton applied to subjects by this country, optional list keyword same as above
#
#		priority = value		# valid flag definition with the highest priority applies
#		trigger = {}			# a trigger that determines if this flag definition is valid, see below for scope
#       allow_revolutionary_indicator = no      # Default = yes. If yes, a temporary revolutionary indicator will appear while the country is revolutionary
#       revolutionary_canton = [list] COA_KEY   # Optional. Default = default_revolutionary_canton. Defines which flag should be used as canton while this country is revolutionary
#	}
# }
```

The following is an example from the base game file with added commentary.

```
ALD = { # Algeria
	flag_definition = {
		coa = ALD
		subject_canton = ALD					#If the game rule for modifying subject flags is on, this COA is added to the canton of this country's subjects, it does not need to match the main flag
		allow_overlord_canton = yes				#If the game rule for modifying subject flags is on, can another country's canton be added to this flag set
		coa_with_overlord_canton = ALD_subject	#If the game rule for modifying subject flags is on, alternate COA for adding the overlords canton, e.g. to move central emblems to one side
		priority = 1							#Highest, i.e. largest priority definition which passes its triggers is used
	}
	flag_definition = {
		coa = ALD_republic
		subject_canton = ALD_republic
		priority = 10
		trigger = { 
			coa_def_republic_flag_trigger = yes	#Scripted triggers can be used, but note scope rules must still be respected
		}
	}
	flag_definition = {
		coa = ALD_subject_FRA
		priority = 30
		trigger = { 
			coa_def_french_ensign_trigger = yes
		}
	}	
}
```

If a country doesn't have a scripted flag definition list, it will search for a coat of arms with its tag as the key term, and failing that the game generates a flag from scripted random elements.

### Trigger scope rules

Flag definition triggers have three possible states and a number of key terms.

| | Existing country | Releasing a country | Forming a country |
|---|---|---|---|
| Root | Definition | Definition | Definition |
| Target | Country | N/A | N/A |
| Initiator | N/A | Player | Player |
| Actor | Country | Player | Player |
| Overlord | Country's direct overlord, if any | Player | Player's direct overlord, if any |

## Coat of arms

*You can find most in-game flags on this wiki at [List of flags](/List_of_flags "List of flags"); that page does not include countries with only one defined flag.*

Coats of arms (CoA) are the actual flags, which are referenced in the flag definition files. A CoA is scripted a named block with a list of graphical elements, namely *patterns*, *colored emblems*, *textured emblems*, and *subs*. The CoAs are defined in /common/coat_of_arms/coat_of_arms/. These elements typically have an inherent dimension of 768 × 512 pixels, though some are 256×256. Except for subs, which are references to other CoAs, these are image files which can be found in game/gfx/coat_of_arms/colored_emblems, game/gfx/coat_of_arms/patterns and game/gfx/coat_of_arms/textured_emblems.

### Pattern

Each CoA starts with a pattern as its base. Patterns are found in /Victoria 3/game/gfx/coat_of_arms/patterns. Each pattern image acts as a mask, with its red color being replaced by color1, and its yellow color – if present – by color2, and a few patterns have a third white color replaced by color3. In addition to setting the flag's base colors, the pattern can mask elements of a colored emblem, hiding the emblem where the pattern and emblem intersect.

Patterns are added to a CoA with `pattern = "pattern_name"` including the file extension in pattern_name.

It is possible to assign named colors to `color<#>` which are not used by the pattern, these can be used in colored emblem elements. Similarly, it is possible to define two different `color<#>` to have the same named color.

Patterns always are the lowest layer of the coat of arms

### Emblem

Emblems are more detailed designs that are layered on top of patterns and each other. They are layered from first to last definition, as well as colored emblem to textured emblem, such that the earliest defined emblem is overlaid by the rest and only the finally defined emblem is fully visible if there is any overlap, while textured emblems will always be above colored emblems. There are two types of emblems: colored emblems and textured emblems.

Colored emblems are similar to patterns, with the emblem image acting as a mask for the defined colors. Colored emblems use the blue color channel for brightness. By default an area is defined as color1, adding green defines color 2 while adding red defines color 3. So an example for a color1 pixel's rgb values would be R0 G0 B128, while color2 would be R0 G255 B128 and color3 would be R255 G0 B128. In this case the blue value is roughly the middle of the spectrum, this results in the area in question being depicted as the exact color defined in flag script, while increasing the blue value makes it lighter and decreasing makes it darker, with a blue value of 0 corresponding to black and one of 255 corresponding to white.

Textured emblems are premade images, which are added to the CoA as is. These are useful for adding emblems to a flag, which contain more than 3 different colors or do not need to allow for easy recoloring, such as elaborate seals or heraldry.

Emblems are added to a CoA by adding a block with the type of emblem, either colored_emblem or textured_emblem, then defining the emblem with `texture = "emblem_name"` including the file extension like with patterns. Colored emblems need a number of colors equal to amount used in the emblem image. Both types of emblems can be modified by including one or more `instance` blocks. Each instance block adds the emblem to the flag once and allows for manipulating its scale, position, and rotation.

Scale modifies the size of the emblem as a percentage, independently in the x and y axes; position moves the emblem so its center point is positioned relative to the top left of the flag, and rotation rotates the emblem clockwise by that number of degrees.

Emblems are layered in order, with the first defined emblem just above the pattern, the next above that, and so forth.

### Sub

Sub treats another CoA like a textured emblem, with the main difference being that the CoA is called with `parent = "CoA_Name"` and a CoA with a sub as part of its definition can't be used as a sub in another CoA (no nesting or recursion). Sub can still use instance, to duplicate and/or modify the incorporated CoA.

Subs are also layered in order, but they always go above any emblems, even if the sub is defined before the emblem.

### Overwriting coats of arms

*See also: [Mod files load order](/Mod_files_load_order "Mod files load order")*

base game coats of arms can be overwritten by defining a new version of that coat of arms in a mod file with a name that comes after the base game file in ASCII sorting. For example, a definition `SWE` in a file named `zz_mod_coats_of_arms.txt` would overwrite the base game definition `SWE` which is in `02_countries.txt`. This allows better integration of modded flags with base game flags as base game files do not need to be modified.

## Power bloc emblems

Power bloc emblems are scripted in the same way as flag coats of arms. The primary difference being a square width-to-height ratio (1:1) rather than rectangular one that flags have (3:2)

The base game definition is:

```
template_power_bloc_1 = {
    pattern = "pattern_solid.tga"
    color1 = { 0.0 0.0 0.0 0.0 }

    # If we ever change the order of layers here, remember to also update them
    # in NGraphics::NPowerBlocCoa::PIECE_LAYERS_ORDER.

    colored_emblem = {
        texture = list "power_bloc_shield"
        color1 = list "power_bloc_colors"
        color2 = list "power_bloc_colors"
        instance = { scale = { 0.72 0.72 } position = { 0.49 0.6 } }
    }

    textured_emblem = {
        texture = list "power_bloc_top"
        instance = { scale = { 0.7 0.7 } position = { 0.5 0.19 } }
    }

    textured_emblem = {
        texture = list "power_bloc_frame"
        instance = { scale = { 0.9 0.9 } position = { 0.5 0.6 } }
    }

    colored_emblem = {
        texture = list "power_bloc_center"
        color1 = list "power_bloc_colors"
        instance = { scale = { 0.45 0.45 } position = { 0.49 0.54 } }
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { 0.65 0.65 } position = { 0.155 0.55 } }
    }

    textured_emblem = {
        texture = list "power_bloc_side"
        instance = { scale = { -0.65 0.65 } position = { 0.82 0.55 } }
    }
}
```

The lists are defined in /Victoria 3/game/common/coat_of_arms/template_lists. As the comments note, these values are also referred to in the [defines](/Defines "Defines").

Power bloc *shields* (346×346px) and *centers* (220×220px) are colored emblems in the same folder as flag colored emblems, though with a file prefix of `pb_`, rather than `ce_`. Similarly, the tops (346×346px), frames (432×432px), and sides (360×360px) are textured emblems. Note the second (right) side is flipped horizontally by inverting its X scaling factor.

Players with the Sphere of Influence DLC enabled can customize their power bloc emblem from the available elements, while players without can only use randomized or prescripted emblems.

Prescripted power bloc emblems are created scripting the emblem as above, then assigned by giving a very high weight to that scripted emblem in the list of random power bloc emblems in /Victoria 3/game/common/coat_of_arms/template_lists/coa_templates.txt, as is done for the base game starting power blocs.

## Coat of arm templates

*See also: [Category:Generated flags](/Category:Generated_flags "Category:Generated flags")*

Templates are a method of generating "randomized" coats of arms. This is used to generate flags for most revolutions and secessions as well as most communist and anarchist flags.

Templates are defined in a `template = { }` with each template given its own script name, such as `template_charge` or `template_centered_coa`. These templates generally use lists from /Victoria 3/game/common/coat_of_arms/template_lists to randomly select colors, patterns, and emblems. The templates are themselves gather in lists in /Victoria 3/game/common/coat_of_arms/template_lists/coa_templates.txt for use in flag definitions.

Lists of coat of arm templates can be given script names to refer to in flag definitions. And a default list `all` is used as the default fallback if no valid flag definition can be found for a country.

## Script terms

The following table is a list of script terms used in defining coats of arms.

| Term | Function | Example | Used in |
|------|----------|---------|---------|
| pattern | Calls a pattern file | `pattern = "pattern_solid.tga"` | Base |
| color<#> | Defines a color for a pattern or colored emblem | `color1 = "red"` | Base, CE |
| colored_emblem | Begins a colored emblem block | `colored_emblem = { … }` | Base |
| textured_emblem | Begins a textured emblem block | `textured_emblem = { … }` | Base |
| list | A modifier to pattern, color, or texture | `color1 = list "normal_colors"` | Base, CE |
| sub | Begins a sub block | `sub = { … }` | Base |
| texture | Calls an emblem file | `emblem = "ce_solid.dds"` | CE, TE |
| parent | Calls a CoA definition | `parent = "sub_SWE_union_mark"` | Sub |
| instance | Begins an instance block | `instance = { … }` | CE, TE, Sub |
| mask | Selects which part of the pattern shows the emblem or sub | `mask = { 1 }` | CE, TE, Sub |

The following are terms used inside of an *instance* block:

| Term | Function | Example |
|------|----------|---------|
| scale | Scales the instance as a percentage | `scale = { 0.5 0.25 }` |
| position | Moves the center of the instance | `position = { 0.25 0.75 }` |
| rotation | Rotates the instance clockwise | `rotation = { 45 }` |

## Coat of arms colors and unit model colors

Unit models in game draw their colors from either the country's defined unit colors or from the currently used coat of arms' colors.

Unit model colors can be defined in a country's definition as:

```
primary_unit_color = { 20 20 120 }
secondary_unit_color  = { 150 190 210 }
tertiary_unit_color = { 5 5 90 }
```

Otherwise, the first three base/pattern colors defined for a coat of arms determine the unit model colors, even if those colors don't appear on the flag. Colors defined for emblems are never considered.

## References

- Victoria 3 Wiki - https://vic3.paradoxwikis.com/Flag_modding