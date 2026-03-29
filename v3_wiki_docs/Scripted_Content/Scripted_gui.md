# Scripted gui

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.8.

Scripted GUIs are used to execute effects after clicking a button in the UI, setting validity/visibility of a button or a UI element via trigger code usually used in events and common folders. They are stored as .txt files in game/common/scripted_guis and cannot be reloaded from the game, unlike the .gui files, you will have to restart your game to have them take effect/load.

Scripted Gui is a bridge between GUI and code, here naming the code in `/common/` `code in code` and the codes in `/gui/` is `code in GUI`.

The codes in code actually registered, they cannot effects unless raised them in code in GUI. Scripted GUI provides an effect context and serval trigger contexts to be raised in GUI.

## Contents

-   [1 Examples](#Examples)
    -   [1.1 Buttons:](#Buttons:)
        -   [1.1.1 Firstly, our file in game/common/scripted_guis will look like this:](#Firstly,_our_file_in_game/common/scripted_guis_will_look_like_this:)
        -   [1.1.2 Secondly, our button in the GUI file will look like this:](#Secondly,_our_button_in_the_GUI_file_will_look_like_this:)
-   [2 References](#References)

## Examples

### Buttons:

Let's say we want to create a button that adds a journal entry to the player who clicked the button.

#### Firstly, our file in game/common/scripted_guis will look like this:

```
give_journal_entry_scriptedgui = {
    # remember that every code below just register multiple context TO BE USED in GUI. If GUI code not use them, they never effects
    
	scope = country 		# the root scope, i.e. the target of the effects
	saved_scopes = {
        saved_gdp
    } 		# any additional targets
    
    # These are scope, it should be added in GUI to effect.
    
	is_shown = {
        always = yes
    } 		# is it visible on the UI?
    
	ai_is_valid = {
        always = yes
    } 		# is the AI allowed to use it? Disabled by default.
	is_valid = {
        always = yes
    } 		# can the player use it?
    
    # Three trigger context, you can use them as you like whatever it used for vaild or shown
    
    effect = {			# what it does
		custom_tooltip = "I am the tooltip"	# adds a tooltip
        add_treasury = scope:saved_gdp
	}
}
```

#### Secondly, our button in the GUI file will look like this:

```
button = {
	using = default_button_action
    datacontext = "[GetScriptedGui('give_journal_entry_scriptedgui')]"
    visible = "[ScriptedGui.IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    enabled = "[ScriptedGui.IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    # you can use some code like visible = "[ScriptedGui.IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"， it's OK.
	size = { 250 50 }
	position = { 0 123 }
	text = "HIDE_AND_SEEK_BTN"
    tooltip = "[ScriptedGui.BuildTooltip( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
	onclick = "[ScriptedGui.Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).AddScope('saved_gdp', MakeScopeValue(GetPlayer.GetGDP)).End )]"
}
button = {
    using = default_button_action
    visible = "[GetScriptedGui('give_journal_entry_scriptedgui').IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End)]"
    # you can use its 'is_vaild' context directly as you like
    size = { 250 50 }
	position = { 0 123 }
	text = "I_AM_ANOTHER_BTN"
}
```

## References

**[Modding](/Modding "Modding")**

Documentation

[Defines](/Defines "Defines") • [Effects](/Effect "Effect") • [Event targets](/Event_target "Event target") • [Scopes](/Scope "Scope") • [Triggers](/Trigger "Trigger")

[Macros](/Macro "Macro") • [Modifier types](/Modifier_types "Modifier types") • [On actions](/On_actions "On actions") • [Script value](/Script_value "Script value") • [Variables](/Variable "Variable")

[GUI script](/GUI_script "GUI script") • [Localization](/Localization "Localization")

Scripted content

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • Scripted gui • [Customizable localization](/Localization#Customizable_Localization "Localization")

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

Retrieved from "[https://vic3.paradoxwikis.com/Scripted_gui](https://vic3.paradoxwikis.com/Scripted_gui)"

Categories:
-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [1.8](/Category:1.8 "Category:1.8")
-   [Modding](/Category:Modding "Category:Modding")