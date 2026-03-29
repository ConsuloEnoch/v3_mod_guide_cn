# Console commands

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") unknown.

Please help improve this article or section by **expanding it** with: Updated console commands information.

Victoria 3 offers a debug mode **(disabled by default)** that allows the inputting of console commands. This page lists the codes that may be input into the Console Window, a special debugging window that may be accessed in non-ironman games while in debug mode. Debug mode must be toggled on before starting the game. Then the console commands window can be accessed by pressing Shift+2, ALT+2+1, Shift+3,§, ~, ^, °, ², or ` (key varies based upon keyboard layout). For QWERTY keyboards, the key is `. Otherwise, Shift + Alt + C may work if the prior combinations did not. Press the up or down arrow keys to traverse through previously executed commands. Press ⇆Tab after entering the beginning of a command to autocomplete it or display which commands contain the entered sequence. Many codes can be turned off by repeating the command, but sometimes reloading the save or exiting the game is necessary.

## Contents

- [1 Debug mode](#Debug_mode)
    - [1.1 Enabling debug mode](#Enabling_debug_mode)
        - [1.1.1 Mods](#Mods)
        - [1.1.2 Launcher](#Launcher)
        - [1.1.3 Steam](#Steam)
        - [1.1.4 Windows](#Windows)
    - [1.2 Disabling debug mode](#Disabling_debug_mode)
    - [1.3 Debug info](#Debug_info)
- [2 List of console commands](#List_of_console_commands)
    - [2.1 Console command arguments](#Console_command_arguments)
- [3 References](#References)

## Debug mode

Debug mode is a set of game tools that allows the modification of game behavior outside of normal means. It includes:

- Console Window (accepts console commands)
- Debug Menus (including the GUI Editor, Script explorer and others)
- [Debug Info](#Debug_info)
- Ctrl + clicking on a country on the map takes control of the country
- Ctrl + alt + clicking on a state on the map takes the state
- File watcher that automatically reloads changed files (including mods) into memory

### Enabling debug mode

Debug mode can be enabled before launching the game and/or toggled in the game using mods. It can be disabled from the console, but can't be re-enabled after it's closed (unless with mods).

How to enable it:

#### Mods

There are a number of mods, like [Free Console Access](https://steamcommunity.com/sharedfiles/filedetails/?id=2879839709), which allow the toggling of debug mode between on and off, making it convenient to use the console and play, but this doesn't enable instant reloading of files. For modding, it's better to use both a mod and launch options.

#### Launcher

In the game Launcher:

1. Switch to Game Settings on the left
2. Scroll down to "Open game in Debug Mode" section and click Launch

#### Steam

On Steam:

1. Right-click the game, open Properties
2. Add `-debug_mode` to the Launch Options at the bottom
3. Start the game

#### Windows

Without Steam, on Windows:

1. Go to your Victoria 3 directory, "binaries" folder
2. Right-click victoria3.exe and create a shortcut
3. Right-click the shortcut, open Properties
4. In the Target field add `-debug_mode` at the end (so it looks like this `"...\victoria3.exe" -debug_mode`)
5. Launch the game using the shortcut

### Disabling debug mode

To activate achievements again, disable all active mods and remove -debug_mode from launch options. After launching the game, make sure you have the [correct checksum](/Patches "Patches"). It can be found in the right corner in the Main Menu.

### Debug info

When debug mode is activated, some tooltips (especially on the map) will show debug info which is normally hidden during normal gameplay.

## List of console commands

| Command | Description |
|---------|-------------|
| 3dstats | Toggles 3D Stats |
| 3dstats.EnableGfxZoneStats | Toggles 3D Gfx Zone Stats |
| Adjacencies.Rebuild | Rebuild all adjacencies |
| Application.ChangeResolution | Change the resolution through the console |
| Browser.OpenURL [<url>] | Opens up a browser with the provided URL |
| Camera.Debug | Prints out camera debug information |
| Camera.Load | Load camera position |
| Camera.Save | Save camera position |
| Checksum.Log | Log the game state checksums to the game log. |
| CrashReporter.DeleteCrashData | Delete local crash dumps older than X days. |
| CrashReporter.SimulateCrash | Simulates a crash (resulting in the game exiting). |
| Complete_journal_entry [<journal entry type>] | Completes a specific journal entry for the player country |
| Debug.Achievements.Lock [<key>] | Locks an achievement again |
| Debug.Achievements.ResetAll | Locks all achievements again |
| Debug.Achievements.ToggleDebug [<value>] | Puts the achievements system in debug mode |
| Debug.Achievements.Unlock [<key>] | Unlocks an achievements given the key |
| Debug.TextureMode [Name of debug mode] | Enables a texture mode for debugging |
| Dockables.Create [Dockable name] | Create dockable |
| Dockables.CreateUserLayout [Dockable layout name] | Create a new user layout copy of current layout, with new name. |
| Dockables.DeleteUserLayout [Dockable layout name] | Delete layout as user layout |
| Dockables.HideLayout | Hide any shown dockable layout |
| Dockables.SaveUserLayout | Save current layout to disk as user layout, optionally under a new name. |
| Dockables.ShowLayout [Dockable layout name] | Show an existing (user) layout, hide current layout |
| Dockables.ShowManager | Show dockable layout manager |
| GUI.AnimationTimeline.LogStats | Dump stats of the GUI Animation Timeline system to the debug log. |
| GUI.ClearWidgets | Clear dummy widget |
| GUI.CreateDockable [File name] [Widget name] [Dockable id. If doesn't exist, it will be registered] | Create dummy dockable widget. With 0 arguments the file name will be gui/test_gui.gui, and the widget name will be test_window |
| GUI.CreateWidget | Create dummy widget. With 0 arguments the file name will be gui/test_gui.gui, and the widget name will be test_window |
| GenerateCoastalRegionNavalExits | |
| Graphics.CapFramerate | |
| Graphics.DumpMemoryInformation | |
| Localization.ToggleIncludeKeyInLocOutput | Includes the loc key in localization output |
| Localization.ToggleOnlyKeyInLocOutput | Shows only the loc key in localization output |
| Localization.ToggleSkipDataSystemInLocOutput | Don't run the data system at all in loc |
| Log.ClearAll | Clears all logs |
| Log.ClearErrorLog | Clears out the error log and resets the error count |
| Map.SavePNG [<map mode>] [<file name>] [<yes/no> Should render flat (optional)] | Save a PNG screenshot of the map for a specific map mode. The only map mode which is known to work is "countries". |
| MapObjects.Debug | Prints out map object debug information |
| MapObjects.GenerateGameLocators [<type>] [<filename> (optional)] | Generates locators for the game's map objects |
| MapObjects.Painter.AddPosition | Place a map object under the cursor |
| ModifierNode.Graph | Open a graph view of the tick tasks |
| ModifierNode.List | Open a graph view of the tick tasks |
| Music.PauseFactor | Shows or sets the current pause_factor of the music system |
| Music.PlayTrack [<track name>] | Plays the specified track |
| Music.Reset | Resets the music system |
| Music.StopTrack | Stops the currently playing track |
| PopsFileStorage.Sync | Sync POP File Storage |
| Portrait.ClearCache | Clears the portrait cache. Forces all portraits to refresh |
| Print.EventDebug | Print event debug statistics, needs to set Debug.Events to collect statistics |
| RandomLog | Toggles random logging |
| RandomLog.Dump [Frame count to dump, or * to dump all available frames (defaults to *)] [Target filename (defaults to random.log)] | Dump random log data to a file. |
| SDL.EventLogging | |
| ScriptProfiling.Dump | |
| SplineNetwork.AppendAssets | |
| SplineNetwork.ClearAssets | |
| SplineNetwork.Database.Reload | |
| SplineNetwork.Graphics.AddAllSplines | |
| SplineNetwork.Graphics.ClearAllSplines | |
| SplineNetwork.SetAssetGenerationMode | Sets mode for spline strips and anchors generation <naval/default> |
| SplineNetwork.ValidateSplines | Validate the integrity of in-game spline system |
| Terrain.Regenerate | Regenerates terrain bitmap |
| Terrain.Save | |
| Threading.TaskThreadCount [The number of task threads] | Set or get the number of task threads |
| TickTask.Graph | Open a graph view of the tick tasks |
| TickTask.List | Open a graph view of the tick tasks |
| add_approval [[interest group name](/Console_commands#Console_command_arguments "Console commands")] [amount] [time] | Adds an approval timed modifier to a given interest group, [amount] is optional (default=1), [time] in months and optional (default=1), e.g: add_approval ig_armed_forces 20(approval) 20(months) find group name in game/common/interest_groups |
| add_clout [[interest group name](/Console_commands#Console_command_arguments "Console commands")] [amount] [time] | Adds or removes clout of the interest group by changing their political strength with timed modifier, [amount] is optional (default=1), [time] in months and optional (default=1) |
| add_ideology [[interest group name](/Console_commands#Console_command_arguments "Console commands")] [Ideology to add.] | Add an ideology to a given interest group |
| add_loyalists [culture] [amount] | Adds loyalists to culture by fraction of population |
| add_mandates [amount] | Adds mandates to current power bloc |
| add_radicals [culture] [amount] | Adds radicals to culture by fraction of population |
| add_relations [<country tag>] [amount] | Changes relations with country by a given value |
| add_war_support [country_tag] [amount] | Alters wars support of country in ALL of their wars by amount |
| add_liberty_desire [country_tag] [amount] | Changes liberty desire with country by a given value |
| ai.debug [tag] | dumps debug info for country |
| ai.goal [tag] [goal type] | Checks ai goal. The ai goals do not refer to the secret goals in ai_strategies but the ai_goals obtained via using ai.debug. |
| ai_evaluate_autonomous_construction [<building key> <state region key>] | Prints AI debug data for selected state & building type. |
| ai_evaluate_company [<company type key>] | Prints AI debug data for selected company. |
| ai_evaluate_government_construction [<building key> <state region key>] | Prints AI debug data for selected state & building type. |
| ai_evaluate_interest [<strategic region key>] | Prints AI debug data for selected strategic region declared interest. |
| ai_evaluate_mobilization | Prints AI debug data for mobilization. |
| ai_evaluate_privatization [<building key> <state region key>] | Prints AI debug data for selected state & building type. |
| ai_evaluate_production_method [<building key> <pm key> <state region key>] | Prints AI debug data for selected production method in state for building type. |
| ai_evaluate_state [<state region key> <country tag>] | Prints AI strategic value for selected state. |
| ai_evaluate_subject [<country tag>] | Prints AI debug data for selected subject. |
| ai_evaluate_trade_route [<goods key> <country tag>] | Prints AI debug data for selected goods & country trade partner. |
| ai_evaluate_treaty_port [<state region key> <country tag>] | Prints AI treaty port score. |
| ai_evaluate_wargoal [<wargoal type> <country tag> <state region key>] | Prints AI debug data for wargoal. |
| annex [<country tag/id>] | Annexes a country |
| annex_all | Annexes all other countries |
| audio.cpu_info | Shows current cpu usage |
| audio.list_events | List audio event |
| audio.play_event [audio event] | Play audio event |
| callstack | Print the callstack |
| change_law | Changes a Law to the specified key (like "law_monarchy", etc) |
| changestatepop [state_id] [pop_type / all] [factor] | Changes the pop size of the given pop type ( can be 'all' ) by at most the given factor. **Will be capped by max employment for each pop**. |
| check_pollution_level [state region tag] | Print out pollution for specified state region |
| check_save | Checks that saving and loading is consistent |
| clearlines | Clear lines |
| clearspawnedentities | Clears entities spawned with spawnentity command |
| coa_preview_window | Open the Coat of Arms Preview Window |
| compound_nodeeditor | Compound Node Editor |
| conquerall [country tag] | Set all enemy provinces under our control. |
| crash | Cause the application to crash |
| create_ai [self/all/tag] | Creates AI for country or countries |
| create_building_history | Creates a game-history compliant .txt file of all buildings in the world / state ID as well as their PM / subsidy configurations. |
| create_country [country definition] [country type] [culture] [state id] | Creates a country |
| create_political_movement [<movement type key>] | Creates a political movement |
| create_pop_history | Creates a dump in debug.log with a complete pop history |
| create_state_region_data | Creates a game-database compliant .txt file of all state regions in the world and their provinces/resources |
| cthulhu | ? |
| data_types_explorer | Opens the data types explorer dockable |
| data_wrappers_stats [Filter] | Prints statistics about data wrappers |
| date [date in format yyyy.mm.dd.hh] | Changes current date |
| debug [arguments] | Various debugging actions. See [console command arguments](/Console_commands#Console_command_arguments "Console commands"). |
| debug_lens_option | toggles the cheat mode debug_lens_option |
| debug_mode | Toggles debug mode |
| debugcharacters | Creates a semi-colon delimited logfile with debug info regarding all characters. |
| debugcountrybudgets | Creates a semi-colon delimited logfile with debug info regarding all countries and their budgets. |
| debugemployment | Creates and appends a comma-delimited logfile with debug info regarding employment in the specified state ID. |
| debugmarkets | Creates a semi-colon delimited logfile with debug info regarding all goods and markets. |
| debugpopconsumption | Creates a semi-colon delimited logfile with debug info regarding all pops' consumption |
| debugpopwealth | Creates a semi-colon delimited logfile of the current wealth status of all pops. |
| debugstates | Write a semi-colon delimited logfile with debug info regarding all states. |
| debugterrainweights | Prints out the number of |
| debugtheaters | Write a semi-colon delimited logfile with debug info regarding all theaters. |
| deiron | Disables Ironman mode |
| disable_ai [all/tag] | Disables AI |
| disable_pop_growth | toggles the cheat mode disable_pop_growth |
| disable_retooling | toggles the cheat mode disable_retooling |
| drawcmdsviewer | Draw Cmds Viewer |
| dump_data_types | dumps the registered data types |
| dump_ref_lookup_memory_report | |
| enable_ai [all/tag] | Enables AI |
| entity_editor | Entity Editor Dockable |
| escalate [<amount>] | Adds escalation to player diplomatic plays. |
| event [event name] [<country_tag/province_id>] | Executes an event |
| explorer | Shows an object explorer window |
| exportbuildings | Write a semi-colon delimited logfile with all building type info |
| fastbattle | toggles the cheat mode fastbattle (battles take one tick)**(affects AI)** |
| fastbuild | toggles the cheat mode fastbuild (makes all constructions instant) **(affects AI)** |
| fastcivilwars | toggles the cheat mode fastcivilwars |
| fastcolonize | toggles the cheat mode fastcolonize **(affects AI)** |
| fastenact | toggles the cheat mode fastenact (enactment of policies is instant) |
| fasthire | toggles the cheat mode fasthire |
| fastincorporate | toggles the cheat mode fastincorporate (makes incorporation of states take 1 day) |
| fastinstitutions | toggles the cheat mode fastinstitutions |
| fastinterests | toggles the cheat mode fastinterests |
| fastlobbies | toggles the cheat mode fastlobbies |
| fastmobilize | toggles the cheat mode fastmobilize |
| fastmovements | toggles the cheat mode fastmovements |
| fastresearch | toggles the cheat mode fastresearch |
| fastrevolution | toggles the cheat mode fastrevolution |
| fastsecession | toggles the cheat mode fastsecession |
| fastsecretgoals | toggles the cheat mode fastsecretgoals |
| fasttravels | toggles the cheat mode fasttravels |
| find_unemployed | Find and report all unemployed pops with an optional cutoff |
| fix_state_regions | Fix state regions. |
| force_oos | Make this client go out of sync in multiplayer |
| generate_province_center_objects | generates a file with meshes in the center of each province |
| gfx.reloadtexture | Reload textures |
| gfx.skin | select active gfx skin |
| gfx.texture_limit | Set texture video memory limit in megabytes |
| gui_animation_editor | GUI Animation Timeline Dockable |
| gui_editor | Spawns gui editor (removed in 1.9) |
| help [command name] | Print out all console commands or a specific command description. |
| hq_show_id | toggles the cheat mode hq_show_id |
| ignore_government_support | toggles the cheat mode ignore_government_support |
| ignore_power_bloc_requirements | toggles the cheat mode ignore_power_bloc_requirements (leverage requirements to leave and join) |
| invalidate_character [character id] | Invalidate the modifier on the character with the specified ID |
| invalidate_country [country id] | Invalidate the modifier on the country with the specified ID |
| invalidate_ig [interest group id] | Invalidate the modifier on the interest group with the specified ID |
| invalidate_state [state id] | Invalidate the modifier on the state with the specified ID |
| io_stats | Toggles IO Stats |
| io_stats.Reset | Resets IO Stats |
| kill_character [character name] | kills the named character |
| log_status | Log Status Dockable |
| log_ticktask_performance | Start outputing ticktask performance data to profiling.log |
| log_viewer | Log Viewer Dockable |
| map_editor | Toggle map editor |
| mapmode [mapmode] | Switches to a given mapmode |
| measure_frame_time ["start" or "stop" measuring] | Measures avg/min/max frame time and prints the result to debug.log once stopped |
| memory_stats | Toggles Memory Stats |
| memory_stats.Reset | Resets Memory Stats |
| minidump [file path] | Creates a minidump |
| money [amount] | Adds specified amount of money |
| net_debuginfo | Print debug info about the networking layer |
| net_stats | Toggles Net Stats |
| net_stats.Reset | Resets Net Stats |
| norevolution | toggles the cheat mode norevolution |
| nosecession | toggles the cheat mode nosecession |
| nosupportloss | Prevent countries from losing war support |
| noshortages | Prevents penalties for supply shortages in buildings |
| observe | start observing the game |
| own [province id/state region tag] [country tag] | Change the owner of specified province or state region. The state region tags can be found in the [list of state regions](/List_of_state_regions "List of state regions") |
| particleeditor | Particle Node Editor |
| permitmarginalizedingovernment | toggles the cheat mode permitmarginalizedingovernment |
| pops_account_disconnect_steam | Disconnect Paradox account from Steam |
| pops_account_login [email] [password] | Login to a POPS Account |
| pops_account_logout | Logout from a POPS Account |
| pops_account_status | Show whether you are currently logged into POPS or not. |
| popstat | Prints out amount of active pops. |
| portrait_editor | Open the portrait editor |
| print_gamestate_modifiers | Prints Gamestate Modifiers |
| province_borders [true/false] | Toggles showing of province borders |
| pseudoLoc | Enable/Disable Pseudo Localization on Text Widgets |
| recalc_cached_data | Recalculate cached gamestate data. |
| release_mode | Toggles release mode |
| reload [file name] | Reloads assets |
| rendertype | Reports what render backend is used |
| research | Acquire technologies |
| save_game_analyzer | Open the save game analyzer |
| savegames.delete_all | Deletes all local save games |
| savegames.delete_cloud | Deletes all cloud save games |
| screenshot | Take screenshot |
| script_docs | Prints script documentation |
| set_devastation_level [state region tag] [amount] | Set devastation level in specified state region |
| set_cohesion [committee] [value] | sets cohesion to value for committee |
| set_pollution_level [state region tag] [amount] | Set pollution level in specified state region |
| settings | Spawns a settings GUI with an optional argument for an initially selected category |
| shader_debug | |
| shader_editor | Shader Editor Dockable |
| show_goals | Show AI goals. |
| skip_migration | toggles the cheat mode skip_migration |
| sleep | Sleep for specified amount of milliseconds |
| social_addfriend [Context Index] [Account ID] | Add a friend to friends list |
| social_debuginfo | Print debug info about the social layer |
| social_joinroom [Context Index] [Room Name] [Nick Name] | Join a chat room using the given social context |
| social_sendmessage [Context Index] [Room Name] [Message] | Send a message to a chat room. |
| spawnentity [<entity name>] [<state> (optional)] | Spawns specified entity at cursor position |
| spawnentity_at [<entity name>] [x] [y] [<state> (optional)] | Spawns specified entity at xy-position |
| spawnline [<line name>] [<start position 'x,y,z'> (no spaces)] [<end position x,y,z> (no spaces)] | Spawns specified line between 2 positions |
| spawnnotification [notificationtype] [<scopeindex>] | Spawns notification of specified type. |
| swapchain.buffers | Query/Set swapchain buffers |
| switchlanguage [language name] | Reload localization files and switch language |
| tag [country_tag] | Switch control to another country |
| testaipacts | Test whether AI would dissolve current pacts |
| testevent [event name] [<country_tag/province_id>] | Tests an event |
| testobjective [<subgoal key (optional)>] | Tests objective triggered effects |
| texturelist | Texture List |
| textureviewer | Texture Viewer |
| time | What time is it? |
| tools.skins | Skin Editor |
| treatyport [<state region tag>] | Takes treaty port in state region |
| tweak | Spawns a tweaker GUI |
| update_distribution | Updates garrison unit distribution in HQ of specified State ID |
| update_employment | Transfers employees between buildings in the specified state ID. |
| validate_employment | Print out unemployment in states. |
| validate_hubs | |
| validate_income | Print out countries with income deficits. |
| validate_naval_exits | |
| validate_pops | Ensures all pops have valid params and prints them to the error log otherwise. |
| version | Shows current build information, put 1 as second parameter for long version |
| vsync | Toggle main swapchains vsync |
| wagerate [building_id] [value] | Get or Set a building's wage rate |
| yesmen | AI will agree to all diplomatic proposals & sway offers from players |

### Console command arguments

| Argument | Value | Description |
|----------|-------|-------------|
| Interest Group Name | ig_armed_forces | Armed Forces |
| | ig_devout | Devout |
| | ig_industrialists | Industrialists |
| | ig_intelligentsia | Intelligentsia |
| | ig_landowners | Landowners |
| | ig_petty_bourgeoisie | Petite Bourgeoisie |
| | ig_rural_folk | Rural Folk |
| | ig_trade_unions | Trade Unions |
| Debug Mode | ai | |
| | allmoney | |
| | alwaysdiplo | |
| | alwaysreform | |
| | alwaysupgradecolony | |
| | artisanchange | |
| | assert | |
| | cb_use | |
| | color | |
| | demotiondesc | |
| | eco | |
| | focusai | |
| | fow | |
| | influence | |
| | info | |
| | lines | |
| | market | |
| | minzoom | |
| | pops | |
| | profile | |
| | promotiondesc | |
| | render | |
| | textures | |
| | tooltips | |
| | wireframe | |
| | yesmen | |

## References

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

[AI](/AI_modding "AI modding") • Console commands • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=Console_commands&oldid=32389](https://vic3.paradoxwikis.com/index.php?title=Console_commands&oldid=32389)"

Categories:
- Potentially outdated
- Unknown version
- Expand
- Modding
- Guides

This page was last edited on 8 November 2025, at 07:16.
Content is available under Attribution-ShareAlike 3.0 unless otherwise noted.