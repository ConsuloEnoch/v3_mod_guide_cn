# State modding guide

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") unknown.

*See also: [State modding](/State_modding "State modding"), [Map modding#State Modding](/Map_modding#State_Modding "Map modding")*

## Contents

-   [1 Creating a new state region](#Creating_a_new_state_region)
    -   [1.1 Get the province IDs](#Get_the_province_IDs)
    -   [1.2 Define the state region](#Define_the_state_region)
        -   [1.2.1 Strategic region](#Strategic_region)
        -   [1.2.2 Localization](#Localization)
    -   [1.3 Map elements](#Map_elements)
    -   [1.4 State history](#State_history)
-   [2 Overwriting existing states](#Overwriting_existing_states)
    -   [2.1 Defining the state](#Defining_the_state)
    -   [2.2 Adding pops](#Adding_pops)
    -   [2.3 Adding buildings](#Adding_buildings)
    -   [2.4 Annexing the state properly](#Annexing_the_state_properly)
-   [3 References](#References)

## Creating a new state region\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=1 "Edit section: Creating a new state region") | [edit source](/index.php?title=State_modding_guide&action=edit&section=1 "Edit section: Creating a new state region")\]

This guide covers how to create a new state region without editing the province map.

Important starting notes:

-   It's recommended to do text editing with a better editor than plain Notepad. My recommendations are Notepad++ (which is what this guide will use), Visual Studio Code and Sublime.
-   All .txt files in the game must have the encoding `UTF8-BOM`. They may not work properly if they don't have that. If you don't know how to set the encoding, just copy an existing file and change its contents.
-   Everything after a `#` in a text file is "commented out", meaning the game ignores what's written after the #.
-   This guide is done in the context of a mod that is already set up and working properly, so make sure you've got that important step done first.

### Get the province IDs\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=2 "Edit section: Get the province IDs") | [edit source](/index.php?title=State_modding_guide&action=edit&section=2 "Edit section: Get the province IDs")\]

First of all, you need to know the IDs of the provinces that will be taken from the old state and being the part of the new state. One way you can do this is to go in game with debug mode and hover on a land, you will find "Province ID". Take note all of them. Alternatively, open /Victoria 3/game/map\_data/provinces.png and note the hexcode color of provinces in that image.

In this guide, we will take Singapore province and form Singapore as its own state. The province ID of Singapore is `xC00130`. You may take note of multiple province IDs.

### Define the state region\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=3 "Edit section: Define the state region") | [edit source](/index.php?title=State_modding_guide&action=edit&section=3 "Edit section: Define the state region")\]

On this part, we will define the map data of the newly created Singapore state. You mod file will be here:

/<mod>/map\_data/state\_regions/<filename>.txt

You can find the corresponding file here

/Victoria 3/game/map\_data/state\_regions/<anyfile>.txt

From there, copy the related states' script and paste in the new mod file. Remove any provinces from the old states and move them to the new state, including the hubs (city, port, farm, etc). Also, on the new state, only use the included province IDs for those hubs.

Each state region needs a unique script name and state ID. Here, we'll use `STATE_SINGAPORE` as the script name, and `800` as the state ID.

In our Singapore example, the script will look like this:

STATE\_MALAYA \= {
    id \= 540
    subsistence\_building \= "building\_subsistence\_rice\_paddies"
    provinces \= { "x0080B0" "x08673B" "x23578B" "x374A68" "x660411" "x66170B" "x6CFA94" "x76546D" "x78EF92" "x8080B0" "x80C0B0" "x8E3305" "xAA2287" "xAF3737" "xB6B53D" "xC84C4C" "xCAB9F2" "xCF3E8D" "xD8E596" "xE87C53" "xF9F87A" "xFCBAFC" }
    city \= "x8E3305"
    port \= "x8E3305"
    farm \= "x76546D"
    mine \= "x08673B"
    wood \= "xCAB9F2"
    arable\_land \= 35
    arable\_resources \= { "bg\_rice\_farms" "bg\_livestock\_ranches" "bg\_coffee\_plantations" "bg\_tea\_plantations" "bg\_sugar\_plantations" "bg\_banana\_plantations" }
    capped\_resources \= {
        bg\_coal\_mining \= 32
        bg\_lead\_mining \= 24
        bg\_logging \= 17
        bg\_fishing \= 10
    }
    resource \= {
        type \= "bg\_rubber"
        undiscovered\_amount \= 40
    }
    naval\_exit\_id \= 3052
}
STATE\_SINGAPORE \= {
    id \= 800
    subsistence\_building \= "building\_subsistence\_rice\_paddies"
    provinces \= { "xC00130" }
    city \= "xC00130"
    port \= "xC00130"
    farm \= "xC00130"
    mine \= "xC00130"
    wood \= "xC00130"
    arable\_land \= 4
    arable\_resources \= { "bg\_rice\_farms" "bg\_livestock\_ranches" "bg\_coffee\_plantations" "bg\_tea\_plantations" "bg\_sugar\_plantations" "bg\_banana\_plantations" }
    capped\_resources \= {
        bg\_logging \= 1
        bg\_fishing \= 12
    }
    naval\_exit\_id \= 3052
}

#### Strategic region\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=4 "Edit section: Strategic region") | [edit source](/index.php?title=State_modding_guide&action=edit&section=4 "Edit section: Strategic region")\]

To include the new state in a strategic region, you need to define the mod file on this path:

/<mod>/common/strategic\_regions/<filename>.txt

And the corresponding file will be here:

/Victoria 3/game/common/strategic\_regions/<any file>.txt

Next, you need to find the desired regions script name and redefine that on the new file. In our Singapore example, the region is Indochina. So, the new file will look like this:

region\_indochina \= {
	graphical\_culture \= "asian"
	capital\_province \= x5C3070
	map\_color \= { 0.9 0.1 0.1 }
	states \= { STATE\_CAMBODIA STATE\_MEKONG STATE\_TONKIN STATE\_ANNAM STATE\_LAOS STATE\_CHIANG\_MAI STATE\_NAKHON\_RATCHASIMA STATE\_MALAYA STATE\_TENASSERIM STATE\_BANGKOK STATE\_KACHIN STATE\_SHAN\_STATES STATE\_BURMA STATE\_PEGU STATE\_SINGAPORE}
}

Notice that we add `STATE_SINGAPORE` there.

#### Localization\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=5 "Edit section: Localization") | [edit source](/index.php?title=State_modding_guide&action=edit&section=5 "Edit section: Localization")\]

To give the state region an in-game name, create a file on this path.

<mod>/localization/english/map/<filename>\_l\_english.yml

Remember, add "`_l_english`" at the end of the file name. It's a lower case "L", not an uppercase "i" or a 1.

The mod file will look like this.

l\_english:
 STATE\_SINGAPORE:0 "Singapore"

### Map elements\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=6 "Edit section: Map elements") | [edit source](/index.php?title=State_modding_guide&action=edit&section=6 "Edit section: Map elements")\]

*Main article: [Map\_modding#State\_Modding](/Map_modding#State_Modding "Map modding")*

There are a number of map elements, which are required for good function of new state regions

### State history\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=7 "Edit section: State history") | [edit source](/index.php?title=State_modding_guide&action=edit&section=7 "Edit section: State history")\]

To define the new state's history, see the following guide.

## Overwriting existing states\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=8 "Edit section: Overwriting existing states") | [edit source](/index.php?title=State_modding_guide&action=edit&section=8 "Edit section: Overwriting existing states")\]

*See also: [Mod files load order](/Mod_files_load_order "Mod files load order")*

The examples below are for new countries but this also works for existing countries.[\[1\]](#cite_note-1) This guide only mentions relevant history files. All other history files work normally and do not need anything special. This whole process is needed so the games pop and building calculation is correct. If you annex the full state in /<mod>/common/history/states, the buildings and pops will not be fully integrated and buildings will have no workers at game start.

None of these files should overwrite base game files.

### Defining the state\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=9 "Edit section: Defining the state") | [edit source](/index.php?title=State_modding_guide&action=edit&section=9 "Edit section: Defining the state")\]

/<mod>/common/history/states

The first thing we do is create a new file. In this file, we add all provinces except one province per country that already owns the state. This creates a new split state that is totally empty, and it does not annex any existing states.

Here is an example where I gave Guatemala to `GOK`:

STATES \= {
    s:STATE\_GUATEMALA \= {
        create\_state \= {
            country \= c:GOK
            owned\_provinces \= {
                x02073E x7D333F x464F6A x0F5049
                xBD8628 xA9090A x78C465 xD9BEFE
                xD030C0 x42124E xB2E11E x50B040
                x2D4EB6 x5449D0 x6D71DA x702CD9
                x65C19A x30E01C x50B0C0 xC67219
                xD176F3 xFA4B41 x011E0F
            }
        }
    }
}

If you are creating a new state region or split state instead of overwriting a state, only add the relevant provinces.

### Adding pops\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=10 "Edit section: Adding pops") | [edit source](/index.php?title=State_modding_guide&action=edit&section=10 "Edit section: Adding pops")\]

/<mod>/common/history/pops

When adding pops we need to remove existing ones from the original state owner, so when we later annex it properly we do not get their population. The removal and recreation leads to proper integration of pop workplaces.

**NOTE**: This needs to be done even if you plan to keep the same pops. In that case you will need to copy the pops from the base game.

In this example we kill the whole population of Guatemala first, and then add our own. We need to do it for UCA and GBR since it is a split state:

POPS \= {
    s:STATE\_GUATEMALA \= {
        region\_state:UCA \= {
            kill\_population\_percent\_in\_state \= {
                percent \= 1 \# 100%
            }
        }
        region\_state:GBR \= {
            kill\_population\_percent\_in\_state \= {
                percent \= 1 \# 100%
            }
        }
        region\_state:GOK \= {
            create\_pop \= {
                culture \= orcish
                size \= 200000
            }
            create\_pop \= {
                pop\_type \= slaves
                culture \= central\_american
                size \= 164404
            }
            create\_pop \= {
                pop\_type \= slaves
                culture \= mayan
                size \= 312000
            }
        }
    }
}

If you are creating a new state region or split state instead of overwriting a state, you only need to kill pops if you are redefining how many pops are in the original states.

### Adding buildings\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=11 "Edit section: Adding buildings") | [edit source](/index.php?title=State_modding_guide&action=edit&section=11 "Edit section: Adding buildings")\]

/<mod>/common/history/buildings

When adding buildings we need to remove existing ones from the original state owner, so when we later annex it properly we do not get their buildings without workforces. The removal and recreation leads to proper integration of pop workplaces. To find which buildings to remove see the base game history files.

**NOTE**: This needs to be done even if you plan to keep the same buildings. In that case you will need to copy the buildings from the base game.

In this example, we remove all buildings of Guatemala first and then add our own. We need to do it for UCA and GBR since it is a split state:

BUILDINGS \= {
    s:STATE\_GUATEMALA \= {
        region\_state:UCA \= {
            \# Clean up base game buildings
            remove\_building \= building\_government\_administration
            remove\_building \= building\_maize\_farm
            remove\_building \= building\_livestock\_ranch
            remove\_building \= building\_barracks
        }
        region\_state:GBR \= {
            \# Clean up base game buildings
            remove\_building \= building\_port
        }
        region\_state:GOK \= {
            create\_building \= {
                building \= "building\_port"
                add\_ownership \= {
                    country \= {
                        country \= "c:GOK"
                        levels \= 2
                    }
                }
                reserves \= 1
                activate\_production\_methods \= { "pm\_anchorage" }
            }
            \# More buildings could be here
        }
    }
}

If you are creating a new state region or split state instead of overwriting a state, you only need to remove buildings if you are redefining how many are in the original states.

### Annexing the state properly\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=12 "Edit section: Annexing the state properly") | [edit source](/index.php?title=State_modding_guide&action=edit&section=12 "Edit section: Annexing the state properly")\]

/<mod>/common/on\_actions

Finally, we need to annex the now empty states by stealing the last provinces. This needs to be done from the `on_game_started` [on action](/On_actions "On actions"). Be sure to create a new on actions file with a custom on action for compatibility.

This is an example where we steal the last two provinces (GBR and UCA) for Guatemala:

on\_game\_started \= {
    on\_actions \= {
        mod\_history\_setup\_on\_action
    }
}

mod\_history\_setup\_on\_action \= {
    effect \= {
        s:STATE\_GUATEMALA \= {
            set\_owner\_of\_provinces \= {
                country \= c:GOK
                provinces \= {
                    xDEC8D3
                    xD0B040
                }
            }
        }
    }
}

Of course, skip this step if not overwriting the original states.

## References\[[edit](/index.php?title=State_modding_guide&veaction=edit&section=13 "Edit section: References") | [edit source](/index.php?title=State_modding_guide&action=edit&section=13 "Edit section: References")\]

1.  [↑](#cite_ref-1) Adapted from [Bahmut | Chris's guide](https://discord.com/channels/827163966551621662/1346877562143510622) on the [Victoria 3 Mod Co-op Discord](https://discord.com/invite/uUbuMTQjA7)

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

Scripted types

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • [Religion](/Religion_modding "Religion modding") • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • [Technology](/Technology_modding "Technology modding") • [Treaties](/Treaty_modding "Treaty modding") • [War goals](/War_goal_modding "War goal modding")

Map

[Map](/Map_modding "Map modding") • [Geographic regions](/Geographic_region_modding "Geographic region modding") • [States](/State_modding "State modding")

Graphics

[3D Models](/Model_modding "Model modding") • [Interface](/Interface_modding "Interface modding") • [Graphical Assets](/Graphical_asset_modding "Graphical asset modding") • [Fonts](/index.php?title=Font_modding&action=edit&redlink=1 "Font modding (page does not exist)") • [Flags](/Flag_modding "Flag modding")

Audio

[Music](/index.php?title=Music_modding&action=edit&redlink=1 "Music modding (page does not exist)") • [Sound](/Sound_modding "Sound modding")

Other

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • State modding guide

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=State\_modding\_guide&oldid=32432](https://vic3.paradoxwikis.com/index.php?title=State_modding_guide&oldid=32432)"

[Categories](/Special:Categories "Special:Categories"):

-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [Unknown version](/Category:Unknown_version "Category:Unknown version")
-   [Modding](/Category:Modding "Category:Modding")

-   This page was last edited on 12 November 2025, at 17:50.
-   Content is available under [Attribution-ShareAlike 3.0](https://central.paradoxwikis.com/Central:Copyrights "central:Central:Copyrights") unless otherwise noted.

-   [Privacy policy](/Victoria_3_Wiki:Privacy_policy)
-   [About Victoria 3 Wiki](/Victoria_3_Wiki:About)
-   [Disclaimers](/Victoria_3_Wiki:General_disclaimer)
-   [Mobile view](https://vic3.paradoxwikis.com/index.php?title=State_modding_guide&mobileaction=toggle_view_mobile)

-   [![Attribution-ShareAlike 3.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/3.0/)
-   [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)