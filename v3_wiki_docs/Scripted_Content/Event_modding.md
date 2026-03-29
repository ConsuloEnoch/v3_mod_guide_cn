# Event modding

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.11.

*See also: [events](/Events "Events")*

Events are one of the most important elements of a well-rounded mod. Events can add flavor and personality to your mod by providing for player interaction and being a vehicle for the history, mechanics, lore, etc. of your mod.

Events in Victoria 3 **never** trigger on their own; they must always be fired by another effect, such as an on action, journal entry, decision, or another event.

## Contents

-   [1 File location](#File_location)
-   [2 File structure](#File_structure)
    -   [2.1 Namespace](#Namespace)
    -   [2.2 Comments](#Comments)
-   [3 Event structure](#Event_structure)
    -   [3.1 Basic structure](#Basic_structure)
    -   [3.2 ID, type, and placement](#ID,_type,_and_placement)
    -   [3.3 Title, description, and flavor](#Title,_description,_and_flavor)
    -   [3.4 Event image](#Event_image)
    -   [3.5 Icon, sound effect, and duration](#Icon,_sound_effect,_and_duration)
    -   [3.6 Trigger and cancellation trigger](#Trigger_and_cancellation_trigger)
    -   [3.7 Immediate effects](#Immediate_effects)
    -   [3.8 Cooldown](#Cooldown)
    -   [3.9 Options](#Options)
    -   [3.10 After](#After)
    -   [3.11 Other features](#Other_features)
-   [4 Hidden events](#Hidden_events)
-   [5 Event templates](#Event_templates)
-   [6 References](#References)

## File location

Events are stored in a .txt files inside the /Victoria 3/game/events folder, for mods, this is /<mod>/events. Event files can also be organized within sub-folders such as `/events/gbr_events`.

*All event files must be in UTF-8 BOM encoding.*

## File structure

### Namespace

Every event file starts with a `namespace` entry. **You must have this in your events file or your events will not work**. From here, every event is named and numbered using this namespace. The same file can contain multiple namespaces, though each namespace should be declared before any events using it are defined.

```
namespace = example_event

example_event.1 = {
	<event_contents>
}

example_event.2 = {
	<event_contents>
}
```

### Comments

Like elsewhere in Victoria 3 scripting, anything placed after a `#` symbol on a line is ignored by the game engine. You can use this to provide comments either giving context for event scripting or to leave yourself reminders.

```
example_event.1 = {
	<event_content> # Anything you write here will be ignored by the game engine
}
```

## Event structure

### Basic structure

The overall structure of each event is fairly consistent. Here is an event template with almost every element present. These are explained in the upcoming sections.

```
example_event.1 = { # 
	type = country_event
	placement = root
	
	title = example_event.1.t
	desc = example_event.1.d
	flavor = example_event.1.f
	
	event_image = {
		video = "<media_alias>"
	}
	
	icon = "gfx/interface/icons/event_icons/event_default.dds"
	
	on_opened_soundeffect = "event:/SFX/UI/Alerts/event_appear"
	
	duration = 3
	
	trigger = { #optional, defaults to yes if empty or unused
	}
	
	cancellation_trigger = { #optional, only use if event should be cancelled by a change in gamestate
	}

	cooldown = { #optional, defines time period before event can be evaluated again
	}

	immediate = { #optional, sets effects that happen immediately when event is fired
	}
	
	option = {
		name = example_event.1.a
		default_option = yes
	}
	
	option = {
		name = example_event.1.b
	}
    	
	option = {
		name = example_event.1.c
        trigger = { } #optional, determines if option is available/visible
        
	}
	
	after = { #optional, sets effects that happen after an option is selected
	}

}
```

### ID, type, and placement

The event ID takes the form of `<namespace>.<id>` The ID can be any number, except 0, as long as there are no duplicates in any event files. For example, you could do `example_event.1` or `example_event.0001`.

`type` determines the starting scope of the event. Usually, this is `country_event`, but can also be `state_event` or `character_event`. See [Scopes](/Scopes "Scopes") for more information on how to use scopes.

Lastly, `placement` determines where the event icon is placed on the map. By default, this is scope the event triggered from, but this can also use a saved scope, i.e. `placement = scope:<your_saved_scope>`

### Title, description, and flavor

The information in these fields determines what is shown in the title bar of an event along with the upper description text box and the lower flavor text box on the right side of the event window. These all correspond to localization keys in localization files. See [Localization](/Localization "Localization") for more information on localization.

Most events use a fixed localization, but you can give events dynamic text by using `triggered_desc` For example:

```
	desc = {
		triggered_desc = {
			desc = example_event.1.d1
			trigger = {
				<your triggers here>
			}
		}
		triggered_desc = {
			desc = example_event.1.d2
			trigger = {
				<your triggers here>
			}
		}
	}
```

While the instruction is called `triggered_desc`, it works the same for the `title` and `flavor`. You have as many of these blocks as you like. If multiple `triggered_desc` blocks are valid, they are all displayed in the order they are listed in the event file; alternatively, any number of `triggered_desc` can be wrapped with a `first_valid` or `random_valid` block. These select only a single contained `triggered_desc`, either the first one to pass its triggers or a random one that passes its triggers.

### Event image

[List of event images](/Event_images "Event images")

There are two types of event images: videos and textures. Videos should be a .bk2 (Bink Video) file and textures should be a .dds (DirectDraw Surface) file.

Videos reference a `media_alias` in /Victoria 3/game/gfx/media_aliases/media_aliases.txt using this structure:

```
	event_image = {
		video = "<media_alias>"
	}
```

Textures reference a static image using this structure:

```
	event_image = {
		texture = "gfx/event_pictures/<texture_name>.dds"
	}
```

Events can also show one or two character portraits with a `gui_window` and `left_icon` and `right_icon`. The vanilla gui_windows are defined in /Victoria 3/game/gui/eventwindow.gui, in `event_window` blocks. The left_icon and right_icon are terms defined in these event_windows and can be set to characters via scopes. Events can also use `minor_left_icon` and `minor_right_icon` which can be set to country scopes for the country's flag, or character scope for a small portrait.

### Icon, sound effect, and duration

`icon` determines the texture that is shown in the outliner and on the map when the event triggers. These are found in /Victoria 3/game/gfx/interface/icons/event_icons and it should be a .dds (DirectDraw Surface) file. Other icons can be selected as well, such as technology icons

`soundeffect` determines the sound that is played when the event is clicked on and the event window opens. Typically, this is unchanged. The audio played while the event is open is defined in the `media_alias`.

`duration` affects how many months the event is present in the outliner before auto-resolving. Set this to 0 for no time limit.

### Trigger and cancellation trigger

*See [Triggers](/Triggers "Triggers") for more information on using triggers. See [On actions](/On_actions "On actions"), [Journal modding](/Journal_modding "Journal modding"), and [Decision modding](/Decision_modding "Decision modding") for more information on those elements*

Events in Victoria 3 must be triggered by an effect, which includes the common following examples:

-   `events` or `random_events` blocks in an on_action or effect block of a journal entry.
-   `when_taken` block of a decision.
-   Effect blocks in another event.

In addition to any triggers used in the triggering effect, an event can use its own set of triggers to determine whether it can fire. If the trigger block is omitted or empty, it is considered always able to fire.

Triggers are evaluated based on the event's initial scope, determined by its `type`, and are evaluated for every country/state/character. Incorrectly structured trigger blocks can cause events to fire repeatedly, fire for the wrong countries, or just not fire at all.

Here is an example of simple trigger block. The triggers first evaluates that the country USA exists. Next it evaluates if this country is USA. When all triggers are true, the event fires:

```
	trigger = {
		exists = c:USA # this checks if a country with the tag "USA" exists
		this = c:USA # this checks if a country with the tag "USA" is the current scoped country
	}
```

**Remember**: The game evaluates *every single* scope that matches the event type. In the above example, the game iterates through every country until it finds a match for the two triggers. You can limit events to single countries by adding triggers that check for exact country tags, primary cultures, state religion, etc. If you have an event firing repeatedly, consider your triggers from the perspective of other scopes. *Note: If you include an event in an on_action without any triggers specified, it fires every time that on_action is evaluated.*

Here is an example of a more complicated trigger block:

```
	trigger = {
		has_technology_researched = nationalism
		NOT = { has_technology_researched = pan-nationalism }
		is_subject = no
		is_junior_in_customs_union = no
		OR = {
			country_rank = rank_value:great_power
			country_rank = rank_value:major_power
			country_rank = rank_value:unrecognized_major_power
		}
		OR = {
			c:GRE ?= {
				has_technology_researched = nationalism
			}
			c:SER ?= {
				has_technology_researched = nationalism
			}
			c:MON ?= {
				has_technology_researched = nationalism
			}
		}
	}
```

In this case, the first few triggers are all evaluated from the `root` scope, usually the country scope. The last three triggers are evaluated from other scopes. You can make these trigger blocks as simple or complicated as you like – just remember excessive trigger blocks can impact game performance.

`cancellation_trigger` is an optional block that determines if an event should disappear without allowing the player to interact with it. For example, if you have an event you want to cancel if the player has the Oligarchy law enacted, you can use:

```
	cancellation_trigger = {
		has_law = law_type:law_oligarchy
	}
```

This is most useful for events that might be no longer valid or relevant due to changes in game state between the time the event fires and when the player or AI selects an option or the event's duration ends.

### Immediate effects

*See [Effects](/Effects "Effects") for more information regarding effects.*

Everything covered in the previous section had to do with triggers. The `immediate` block on the other hand, uses effects.

Anything in the `immediate` of an event is executed the moment the event is triggered, before the event is presented to the player. Usually, this is used to prepare for the event by setting variables, creating characters, and saving scopes, but you can put any effects in this block. A common use for the immediate block is to save scopes in order to customize the event's localization.

Here is an example:

```
	immediate = {
		ruler = {
			save_scope_as = ruler_scope
		}
		heir = {
			save_scope_as = heir_scope
		}
		ig:ig_armed_forces = {
			leader = {
				save_scope_as = ig_armed_forces_scope
			}
		}
		c:GBR = {
			save_scope_as = uk_scope
		}
		s:STATE_BAVARIA = {
			random_scope_state = {
				save_scope_as = bavaria_state_scope
			}
		}
		random_scope_character = {
			limit = {
				has_variable = example_variable
			}
			save_scope_as = example_character_scope
		}
		set_variable = example_event_happened
	}
```

As with most effect blocks, all effects are executed at the `root` scope unless otherwise specified. In this example, several scopes are saved for use either in localization or for other effects down the line. You can, for example, set up your localization to have `[SCOPE.sCharacter('<scope_key>').GetFullName]` and then scope to a character and save that character as `scope_key` in an event's immediate block to let your events be more dynamic. You can find several examples of this being done in the vanilla events. You can also set variables as a means to ensure events only fire once or to set up event chains.

For example, this would ensure an event only fires once for a given country:

```
	trigger = {
		NOT = {
			has_variable = example_variable
		}
	}
	
	immediate = {
		set_variable = example_variable
	}
```

### Cooldown

The `cooldown` is an optional block that temporarily blocks an event from firing again for a given time. This block accepts the arguments `years`, `months`, and `days`. Using this block sets a variable that prevents the event from being triggered for the specified time. Keep in mind that variables set with the `set_variable` effect can also have a duration.

```
	cooldown = {
		years = 3
	}
```

### Options

Every event must have at least one `option` and at least one of those must have a `default_option` entry (except for hidden events, see [below](#Hidden_events)). An event can have as many options as you like, but too many options can make the event window look progressively uglier and eventually unusable.

Each option has a `name` which is a localization key. While Paradox typically uses the format `event_id.1.a, event_id.1.b, etc`, these can be any localization key.

Here is a simple set of two options:

```
	option = {
		name = example_event.1.a
		default_option = yes
		add_modifier = {
			name = modifier_example
			months = normal_modifier_time
		}
	}
	
	option = {
		name = example_event.1.b
		add_radicals = {
			pop_type = academics
			value = medium_radicals
		}
	}
```

Like the `immediate` block, effects in each option are executed from the `root` scope unless otherwise specified. You can also use saved scopes from either the `immediate` effects or from previous events if this event is part of an unbroken event chain:

```
	immediate = {
		set_global_variable = example_var # global_variables are visible to all countries
		s:STATE_PELOPONNESE = { # this scopes to a specific state_region
			random_scope_state = { # this searches for a state within the state region; since there is no limit, it iterates until it finds the first state in this state_region
				save_scope_as = peloponnese_scope # we save this to use later
			}
		}
	}
	
	option = {
		name = example_event.1.a
		default_option = yes
		add_modifier = { # these can be applied to countries, states, characters, IGs, and units
			name = modifier_example # always ensure the modifier you use works in the scope you're assigning it to
			months = normal_modifier_time # this is pre-defined value provided by the game, but you can use your own amount
		}
		scope:peloponnese_scope = { # this changes the current scope to the state we saved earlier
			add_loyalists_in_state = { # this effect only works in the state scope. this is why we had to save a state scope earlier
				pop_type = academics # these are defined in \\common\\pop_types
				value = medium_radicals # this is a pre-defined value, don't be thrown off by the name "medium_radicals" it is actually referencing a fixed number in \\common\\script_values\\event_values.txt
			}
		}	
	}
```

Options can also have `trigger` blocks of their own, which can be used to add extra layers to your events. In this example, the `trigger` blocks show one option to FRA and another option to everyone else (the `!=` means "not equal to"):

```
	option = {
		name = example_event.1.a # every option needs a name
		default_option = yes # every event needs a default option or the game will print an error
		trigger = {
			c:FRA != this # != means "not equal to"
		}
		show_as_tooltip = { # this presents the effects to the player as if it will be executed, but does nothing
			c:FRA = { # changes the current scope to the country FRA
				create_diplomatic_pact = {
					country = c:TUN # Must be a country scope. If you saved a country scope, you can use that instead.
					type = protectorate
				}
			}
		}
	}
	
	option = {
		name = example_event.1.a # options can have the same name as each other
		trigger = {
			c:FRA = this # This displays this option if the current country is FRA
		}
		create_diplomatic_pact = { # This effect will be executed, unlike the above one
			country = c:TUN
			type = protectorate
		}
	}
```

Here is a more complicated option example:

```
	option = {
		name = example_event.1.a
		default_option = yes
		add_journal_entry = {
			type = je_example_journal # this adds the specified journal entry. You must use the "type =" argument or the effect will fail
		}
		scope:example_saved_scope = { # lets say you saved this in the immediate
			add_modifier = {
				name = modifier_example # this is the name of a modifier
				months = normal_modifier_time # this is a pre-defined value, but you can substitute in your own duration if you wish
				is_decaying = yes # this is an optional argument that makes the modifier get weaker as it's duration counts down
			}
		}
		if = { # this effect will only happen if its limit is true
			limit = { # triggers go here
				country_has_primary_culture = cu:yankee # the cu: is telling the game to look for a culture definition, since that's what this trigger wants
			}
			hidden_effect = { # effects that are executed if limit evaluates to true; in this case, hidden_effect also hides this from the player
				trigger_event = { # fires the specified event
					id = example_event.2 # the ID of the event being triggered 
					days = 30 # an optional argument; fires the event after this duration has passed
					popup = yes # an optional argument; makes the event pop up without the player having to click on it; note this does NOT pause the game
				}
			}
		}
	}
```

### After

The `after` block is an optional effect block that executes the enclosed effects after an option has been chosen. The vast majority of vanilla events don't use this function, but it can be very useful in case you want to ensure something happens regardless of what option is chosen or as a convenient place to have some clean up effects after a long event chain:

```
	after = {
		set_variable = example_event_completed
		trigger_event = {
			id = example_event.2
		}
	}
```

### Other features

If you are developing a mod that has a dlc icon, you can add `dlc = <dlc_key>` to your event to make your mod's icon and name appear in the lower left of the event, similar to Paradox DLC.

In debug mode, you can manually trigger events using the command `event <event_id>`.

## Hidden events

Sometimes, you don't necessarily want an event to be presented to a player, but you need some effects to be executed based on certain triggers. In this case, you can make a hidden event.

Hidden events require less structure than normal events. Namely, hidden events do not require any localization, audio, or visual elements. They also do not require any options, nor do any options work since the event is not shown. To create a hidden event, simply add `hidden = yes` to the event:

```
example_event.1 = { # every event always needs an ID
	type = country_event # remember, this can be state_event or character_event too
	hidden = yes # you must include this line or you'll get errors
	
	trigger = {
		<your_triggers_here> # this works exactly like normal events
	}

	immediate = {
		<your_effects_here> # this works exactly like normal events
	}
	
}
```

Here is a more complicated example of a hidden event:

```
example_event.1 = {
	type = country_event # This means that, root is the country in which the event happened, instead of state or character.
    hidden = yes # remember, if there are no options, make it hidden or else the game will think this is a normal event
	
	immediate = {
		random_diplomatic_play = { # this searches for and scopes to a diplomatic play that meets the criteria specified in the "limit" block
			limit = { # this is where you tell the game what exactly you want it to look for
				is_war = yes
				any_scope_play_involved = {
					THIS = ROOT # THIS means the "current scope", in this case the "THIS" is any_scope_play_involved
				}
				NOR = { # Means "not or"; returns true only if all contained triggers are false
					initiator = ROOT # initiator and target is the event target of diplomatic_play
					target = ROOT
				}
			}
			initiator = { # this scope is only available in the diplomatic_play scope
				save_scope_as = initiator_scope # So if we want to use it later, we use this effect to provide a reference for it later
			}
			target = {
				save_scope_as =  target_scope
			}
			if = { # the contents of an "if" effect are only executed if its "limit" block is satisfied
				limit = { # place your triggers in this block
					ROOT = { # We want to evaluate this from the ROOT scope
						is_diplomatic_play_enemy_of = scope:initiator_scope
					}
				}
				if = { # you can nest "if" effects inside of other "if" effects to provide more dynamism to your events
					limit = {
						scope:initiator_scope = { # This is the scope we saved earlier, but used an effect that doesn't have access to "scope:initiator"
							infamy >= infamy_threshold:infamous 
						} 
					}
					ROOT = { change_infamy = 5 }
				}
				ROOT = {
					set_owes_obligation_to = {
						country = scope:target_scope
						setting = yes
					}
				}
				remove_target_backers = { ROOT } # The remove_target_backers effect only works in the  diplomatic_play scope, which was provided by random_diplomatic_play.
			}
		}
	}

}
```

## Event templates

Here is a template for a normal event:

```
temp_event.123 = {
	type = country_event
	placement = root
	
	title = temp_event.123.t
	desc = temp_event.123.d
	flavor = temp_event.123.f
	
	event_image = {
		video = "######"
	}
	
	icon = "gfx/interface/icons/event_icons/event_######.dds"
	
	on_opened_soundeffect = "event:/SFX/UI/Alerts/event_appear"
	
	duration = 3
	
	trigger = {
	}
	
	cancellation_trigger = {
	}
	
	cooldown = {
	}	
	
	immediate = {
	}
	
	option = {
		name = temp_event.123.a
		default_option = yes
	}
	
	option = {
		name = temp_event.123.b
	}
	
	after = {
	}

}
```

Here is a template for a hidden event:

```
temp_event.123 = {
	type = country_event
	hidden = yes
	
	trigger = {
	}

	immediate = {
	}
	
}
```

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • Events • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

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

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

---

Retrieved from "[https://vic3.paradoxwikis.com/Event_modding](https://vic3.paradoxwikis.com/Event_modding)"

Categories:
-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [1.11](/Category:1.11 "Category:1.11")
-   [Modding](/Category:Modding "Category:Modding")