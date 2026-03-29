# Sound modding

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.8.

***Note:** This article assumes you know how to use FMOD. If you need help, they have several tutorials on their Youtube page.*

Sound modding requires the use of FMOD Studio, available here: [FMOD](https://www.fmod.com/)

*Download version **2.02.03***. *This is the version recommended by the devs and is confirmed to work by modders.*

FMOD Studio allows modders to add and mix sounds for events which can be called via script in events, UI elements, etc.

## Contents

- [1 Starting a project using the template](#Starting_a_project_using_the_template)
- [2 Starting a project from scratch](#Starting_a_project_from_scratch)
- [3 Importing sounds](#Importing_sounds)
    - [3.1 Troubleshooting:](#Troubleshooting:)
- [4 Playing sounds in-game](#Playing_sounds_in-game)
- [5 References](#References)

## Starting a project using the template

Download this [FMOD Project Template](https://github.com/Victoria-3-Modding-Co-op/Vic3-FMOD-Template) and follow the instructions there. All of the vanilla **Groups** and **VCAs** have been defined for you. Otherwise, follow the instructions in the next section to create a project from scratch.

If using the template, **DELETE THE PROVIDED MASTER BANK!!!** *Using the provided master bank will break other mods that also fail to delete this bank.*

**DELETE** the provided bank, then right-click and select **New Bank** to make your own.

Name your master bank to something unique to avoid collisions with other mods. Ensure you name your master bank with something coming after `VFX`. *Attempting to load a .bank file ahead of any vanilla sound effect banks may break vanilla sound functionality.*

If you use any of the vanilla groups located within `MUSIC` or `SFX`, you will have to follow the instructions below to match the GUIDs.

## Starting a project from scratch

1. Open and create a new FMOD Project.
2. Create a new bank, then right-click it & mark it as a master bank.
    1. If your project will have a lot of different events (audio tracks), you may have multiple master banks simultaneously to organize them.
3. Name your master bank(s) with something coming after `VFX`.
    1. *Attempting to load a file ahead of any vanilla sound effect banks may break vanilla sound functionality.*
    2. The name of the banks within FMOD Studio do not *need* to be named something coming after `VFX`, but the FMOD Studio will name the bank files it generates the names of the corresponding banks within FMOD Studio, so doing this is recommended for convenience.
4. Create any **Groups** and **VCAs** you intend to use.
5. Save your project, click **Build**, then **Export GUIs.**
6. Go to Victoria 3's install directory, find `game\sound\GUIDs.txt`, grab the ID for `bus:/`. It will be a big string of numbers.
7. Go to your FMOD project's `\build` folder, find `GUIDs.txt`, and get the project's `bus:/` ID.
8. ***Close FMOD***
9. In your FMOD project's `Metadata` folder, search and replace all instances of your project's `bus:/` ID in all files with the ID from Victoria 3.
10. Repeat this process for *every* Group or VCA you use that matches one from Vanilla, such as: `bus:/MUSIC` `bus:/MUSIC/Mood``vca:/MUSIC`
11. ***Save your changes**, then close all files.*
12. Reopen the project in FMOD and do your sound effect/music stuff.
13. Click **Build** once finished.
14. Find the relevant files in your project's `\build` folder and copy them to the `\sound\banks` folder of your mod. *Check for typos! That's singular* `sound` *and plural* `banks`.

## Importing sounds

1. Switch to the Assets tab and drop your audio files there. *FMOD accepts wav, mp3, ogg, aiff, wma and flac.*
2. Right-click one of your imported assets and choose **Create Event**.
3. Select an event type. Any event type will work. *If unsure, use 2D Timeline. You can also select multiple files and create events for all of them at once.*
4. Switch to the Events tab and select your new event.
5. Right-click your event and choose Assign to Bank > Browse > Master. Do the same for any other events
6. Go to Window > Mixer Routing > VCA. *If using the template, these will already be defined for you. Otherwise, create the ones you need and follow the instructions in the above section.*
7. Assign your events to the appropriate groups and VCAs.
8. When you are finished, Select File > Build. This will create our bank files that will be used by the game.
9. Find the relevant files in your project's `\build` folder and copy them to the `\sound\banks` folder of your mod. *Check for typos! That's singular* `sound` *and plural* `banks`.

*Tip: you can tell FMOD to export banks to your mod folder. To do that:*

1. Go to to Edit > Preferences, Build tab.
2. Paste the path to your mod's sound folder in 'Build banks output directory'.
3. Select Desktop platform below and set its 'Output sub-directory' to banks.

### Troubleshooting:

- If the error log says it couldn't load a bank, you probably didn't replace the ids correctly or didn't rebuild the project after editing the IDs.
- If it can't find a specific event, double-check the path, the name and that it's assigned to a bank in FMOD.

## Playing sounds in-game

Sound effects can be played via script, UI elements, or models on the map.

**Console:**

Use the command `audio.play_event event:/myevent`

- Note, the console can't play events with spaces in them. This is not an issue for script and UI.
- If you put your events into folders in FMOD, then this path would include folder names, eg: `event:/somefolder/myevent`
- You do not need to reference the name of the bank here.

**UI buttons:**

- `clicksound = "event:/myevent"`
- `oversound = "event:/myevent"` - this plays when the cursor hovers over a button

**UI animation states:**

```
state = {
  name = "my_sound"
  start_sound = { soundeffect = "event:/myevent" }
  end_sound = { soundeffect = "event:/myevent" }
  soundparam = { name = parameterName value = 1 }
}
```

- `start_sound` will trigger the sound effect immediately.
- `end_sound` will play at the end of the animation if it has duration.
- `soundparam` is optional, used to modify the event using a parameter set in FMOD. *See Sound Parameters below.*
- Remember that states don't fire by themselves.
- You can also use a scripted gui that plays the sound in script and fire it from a button's `onclick` or a state's `on_finish`.

**3D models:**

Buildings (common/buildings):

```
asset = {
  ...
  soundeffect = { soundeffect = "event:/eventName" soundparameter = { "parameterName" = 0 } }
}
```

Units (gfx/models/units/infantry):

```
state = { 
  ...
  event = {
    time = 0.0
    soundparameter = { "parameterName" = 0.0 }
    sound = { soundeffect = "event:/eventName" }
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

[Decisions](/Decision_modding "Decision modding") • [Events](/Event_modding "Event modding") • [History](/History_modding "History modding") • [Journal](/Journal_modding "Journal modding") • [Modifiers](/Modifier_modding "Modifier modding") • [Objectives](/index.php?title=Objective_modding&action=edit&redlink=1 "Objective modding (page does not exist)") • [Scripted gui](/Scripted_gui "Scripted gui") • [Customizable localization](/Localization#Customizable_Localization "Localization")

Scripted types

[Buildings](/Building_modding "Building modding") • [Characters](/Character_modding "Character modding") • [Concepts](/index.php?title=Concept_modding&action=edit&redlink=1 "Concept modding (page does not exist)") • [Countries](/Country_modding "Country modding") • [Culture](/Culture_modding "Culture modding") • [Decrees](/Decree_modding "Decree modding") • [Diplomacy](/Diplomacy_modding "Diplomacy modding") • [Goods](/Goods_modding "Goods modding") • [Institutions](/Institution_modding "Institution modding") • [Interest groups](/Interest_group_modding "Interest group modding") • [Laws](/Law_modding "Law modding") • [Parties](/index.php?title=Party_modding&action=edit&redlink=1 "Party modding (page does not exist)") • [Pops](/Pop_modding "Pop modding") • [Power blocs](/Power_bloc_modding "Power bloc modding") • [Religion](/Religion_modding "Religion modding") • [Subject types](/index.php?title=Subject_type_modding&action=edit&redlink=1 "Subject type modding (page does not exist)") • [Technology](/Technology_modding "Technology modding") • [Treaties](/Treaty_modding "Treaty modding") • [War goals](/War_goal_modding "War goal modding")

Map

[Map](/Map_modding "Map modding") • [Geographic regions](/Geographic_region_modding "Geographic region modding") • [States](/State_modding "State modding")

Graphics

[3D Models](/Model_modding "Model modding") • [Interface](/Interface_modding "Interface modding") • [Graphical Assets](/Graphical_asset_modding "Graphical asset modding") • [Fonts](/index.php?title=Font_modding&action=edit&redlink=1 "Font modding (page does not exist)") • [Flags](/Flag_modding "Flag modding")

Audio

[Music](/index.php?title=Music_modding&action=edit&redlink=1 "Music modding (page does not exist)") • Sound

Other

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • [Scripted tests](/Scripted_test "Scripted test") • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=Sound_modding&oldid=34238](https://vic3.paradoxwikis.com/index.php?title=Sound_modding&oldid=34238)"

Categories:
- Potentially outdated
- 1.8
- Modding

This page was last edited on 24 January 2026, at 02:54.
Content is available under Attribution-ShareAlike 3.0 unless otherwise noted.