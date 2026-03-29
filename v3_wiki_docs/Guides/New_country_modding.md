# New country modding

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.8.

*See also: [Country modding](/Country_modding "Country modding")*

This guide covers how to add a new country into the game so that it exists at the start of the game in 1836.

Important starting notes:

-   It is recommended to do text editing with a better editor than plain Notepad. My recommendations are Notepad++ (which is what this guide will use), Visual Studio Code, and Sublime.
-   All .txt files in the game must have the encoding UTF8-BOM. They may not work properly if they don't have that. If you don't know how to set the encoding, just copy an existing file and change its contents.
-   Everything after a `#` in a text file is "commented out", meaning the game ignores what's written after the #.
-   This guide is done in the context of a mod that is already set up and working properly, so make sure you've got that important step done first.

## Contents

-   [1 Defining the country](#Defining_the_country)
-   [2 The essential history files](#The_essential_history_files)
-   [3 Localization](#Localization)
-   [4 Population history](#Population_history)
-   [5 Characters](#Characters)
-   [6 Flag](#Flag)
-   [7 Dynamic country name and colors](#Dynamic_country_name_and_colors)
    -   [7.1 Dynamic country name](#Dynamic_country_name)
    -   [7.2 Dynamic country color](#Dynamic_country_color)
-   [8 References](#References)

## Defining the country\[[edit](/index.php?title=New_country_modding&veaction=edit&section=1 "Edit section: Defining the country") | [edit source](/index.php?title=New_country_modding&action=edit&section=1 "Edit section: Defining the country")\]

You can find the country definitions in /Victoria 3/game/common/country\_definitions.

By "defining" we mean two things:

-   A human meaning of "deciding where the country will be and what it will look like"
-   A code meaning of telling the game information about our country so that it knows what the country is

So first of all, think about what country you want, and especially where it will be located. The country in this guide will be called Cyrenaica and will be located here in Tripolitania's land. It will own the whole of the Libyan Desert state.

-   [![](/images/thumb/c/cb/Country_creation1.png/300px-Country_creation1.png)](/File:Country_creation1.png)
    
    [](/File:Country_creation1.png "Enlarge")
    
    The new example country will be here
    
-   [![](/images/thumb/5/59/Country_creation2.png/300px-Country_creation2.png)](/File:Country_creation2.png)
    
    [](/File:Country_creation2.png "Enlarge")
    
    The Libyan Desert state
    

Now it is time to decide on a tag (a three-character short script name for the country). CYR makes sense as a tag for Cyrenaica, but anything could be used. Make sure that CYR isn't already used in the base game by using Notepad++'s *Find in Files* function to see whether CYR shows up in the base game country definition files anywhere. And if it doesn't, great! Otherwise, just pick something else. Now go to the mod's country definition folder and add a definition for it.

-   [![](/images/thumb/c/c2/Country_creation4.png/450px-Country_creation4.png)](/File:Country_creation4.png)
    
    [](/File:Country_creation4.png "Enlarge")
    
    Make sure the path points at the Vic3 country definition folder and put your desired tag, then hit Find All
    
-   [![](/images/thumb/0/07/Country_creation3.png/450px-Country_creation3.png)](/File:Country_creation3.png)
    
    [](/File:Country_creation3.png "Enlarge")
    
    This is the path that the country definition file must be in
    
    [![](/images/thumb/9/98/Country_creation5.png/450px-Country_creation5.png)](/File:Country_creation5.png)
    
    [](/File:Country_creation5.png "Enlarge")
    
    Country definition code
    

As can be seen, there are some important parts to a country definition. For a full list of country definition parameters, see [Country modding § Country definition](/Country_modding#Country_definition "Country modding").

It starts with the tag, then add a colour (this can be in HSV360, HSV decimal, or RGB255 format). Use an online RGB color picking tool, or image editing software to find the desired colour.

After that, choose what type of country it will be:

-   recognized - Mostly used for "western" countries
-   unrecognized - Used for "non-western" countries, akin to Vic2's "uncivilized"
-   decentralized - For countries without a central system of government, usually used for indigenous people
-   colonial - For countries that are colonies or former colonies of recognized countries

Then state its tier, which is essentially the size of the country, as well as controlling in part whether it can form another country

-   city\_state
-   principality
-   grand\_principality
-   kingdom
-   empire
-   hegemony

After that, input the primary cultures. The in-game spellings are usually the same as the code spellings, but not always. Double check in the base game's /Victoria 3/game/common/cultures folder if unsure.

Finally, define the default capital state. As above, this is normally the same as what's written in game, except that spaces are always underscores, which is why CYR's state capital is STATE\_LIBYAN\_DESERT instead of Libyan Desert. A state will always be something like STATE\_(NAME). If unsure, check in /Victoria 3/game/map\_data/state\_regions or /Victoria 3/game/common/history/states.

Make sure there is a closing bracket, too. Most fancier word processors like Notepad++, Visual Studio Code and Sublime have some way of doing this. Proper bracketing is very important!

## The essential history files\[[edit](/index.php?title=New_country_modding&veaction=edit&section=2 "Edit section: The essential history files") | [edit source](/index.php?title=New_country_modding&action=edit&section=2 "Edit section: The essential history files")\]

History files location: /Victoria 3/game/common/history

History files required for editing: states, pops, buildings, countries

Now that the country is defined, it is time to make it show up in the game. Right now, the game only knows that CYR is a possible country, but it hasn't been told that it should exist. To do this, the history folder is needed, and specifically these three folders, as well as the countries folder.

-   [![](/images/thumb/b/ba/Country_creation6.png/450px-Country_creation6.png)](/File:Country_creation6.png)
    
    [](/File:Country_creation6.png "Enlarge")
    
    These three history folders are the most important ones
    
-   [![](/images/thumb/4/47/Country_creation7.png/450px-Country_creation7.png)](/File:Country_creation7.png)
    
    [](/File:Country_creation7.png "Enlarge")
    
    Here's the countries history folder
    

[![](/images/thumb/8/86/Country_creation10.png/230px-Country_creation10.png)](/File:Country_creation10.png)

[](/File:Country_creation10.png "Enlarge")

Remember to change TRI to CYR in the POPS history

[![](/images/b/b5/Country_creation11.png)](/File:Country_creation11.png)

[](/File:Country_creation11.png "Enlarge")

And in BUILDINGS, too

The order of editing doesn't matter, but this guide begins with states. Files in this folder tell the game who owns what states (or what provinces in the state) at the start of the game, as well as information about what cultures consider the state to be their homeland. Note that the state history files must use a `STATES = { }` block to enclose all state data. Navigate to STATE\_LIBYAN\_DESERT:

As seen from the highlighted section, TRI (Tripolitania) currently controls the state. Let's change that:

-   [![](/images/thumb/6/63/Country_creation8.png/300px-Country_creation8.png)](/File:Country_creation8.png)
    
    [](/File:Country_creation8.png "Enlarge")
    
    State history with TRI as the owner
    
-   [![](/images/thumb/a/a7/Country_creation9.png/300px-Country_creation9.png)](/File:Country_creation9.png)
    
    [](/File:Country_creation9.png "Enlarge")
    
    Now changed to CYR being the owner
    

If you launch the game now, CYR controls the state, but it's missing information about population and buildings, so it is not yet ready to play. So next is the pops folder, and once again find STATE\_LIBYAN\_DESERT, and there, too, change TRI to CYR. And do the same in the buildings folder. There are no defined buildings in the state. That makes sense, considering it's mostly desert and has a very small population, but remember that subsistence buildings are added automatically.

Copy another country's file in /Victoria 3/game/common/history/countries and paste in your mod's countries folder rename it `cyr - cyrenaica.txt`. You can change the content later.

And with that, the history folder entries are done for now.

## Localization\[[edit](/index.php?title=New_country_modding&veaction=edit&section=3 "Edit section: Localization") | [edit source](/index.php?title=New_country_modding&action=edit&section=3 "Edit section: Localization")\]

*See also: [Localization](/Localization "Localization")*

The country is now playable, but in game it is still called CYR instead of a proper country name. That's where localization comes in.

[![](/images/thumb/7/7e/Country_creation12.png/450px-Country_creation12.png)](/File:Country_creation12.png)

[](/File:Country_creation12.png "Enlarge")

Here's where the localization file is. The path is more important than the name of the file.

Localization is the way that code is translated into human languages like English. Time to go to our mod's localization folder.

New localization files can have any name as long as it fits a certain pattern. The file must:

-   be a `.yml` file
-   have `_l_english` at the end of the file name (if your localization is English, otherwise use the language's script name, typically its English name)
-   start with `l_english:` in the contents of the file

It is suggested just to copy a localization file from another mod or the base game and empty it (except for the `l_english:` part).

[![](/images/9/95/Country_creation13.png)](/File:Country_creation13.png)

[](/File:Country_creation13.png "Enlarge")

Example localization

The localization is pretty simple, as shown here:

TAG: "country name"
TAG\_ADJ: "country adjective"

`TAG` stands in here for the country's tag, i.e. CYR in this case.

Now the country works properly and the name looks acceptable.

[![](/images/thumb/6/6c/Country_creation14.png/450px-Country_creation14.png)](/File:Country_creation14.png)

[](/File:Country_creation14.png "Enlarge")

The country works, but maybe a custom flag and ruler would be better

## Population history\[[edit](/index.php?title=New_country_modding&veaction=edit&section=4 "Edit section: Population history") | [edit source](/index.php?title=New_country_modding&action=edit&section=4 "Edit section: Population history")\]

[![](/images/c/c4/Country_creation16.png)](/File:Country_creation16.png)

[](/File:Country_creation16.png "Enlarge")

Example population history entry

An quite optional file to do: Population history. Not to be confused with the Pops history, the population folder in the history folder gives information about the people who live in the country, specifically their wealth and their literacy. It typically uses two scripted effects, but can use any set of relevant effects. These modify the starting characteristics of a country's population, but the main effect depends on other factors, such as the buildings and production methods present at start for wealth, and technology and education institution for literacy. That is, even a country with `effect_starting_pop_literacy_very_high = yes` will be mostly illiterate if no education institution is present.

Wealth: (defined in /Victoria 3/game/common/scripted\_effects/00\_starting\_pop\_wealth.txt)

-   effect\_starting\_pop\_wealth\_low
-   effect\_starting\_pop\_wealth\_medium
-   effect\_starting\_pop\_wealth\_high
-   effect\_starting\_pop\_wealth\_very\_high

Literacy (defined in /Victoria 3/game/common/scripted\_effects/00\_starting\_pop\_literacy.txt)

-   effect\_starting\_pop\_literacy\_baseline
-   effect\_starting\_pop\_literacy\_very\_low
-   effect\_starting\_pop\_literacy\_low
-   effect\_starting\_pop\_literacy\_middling
-   effect\_starting\_pop\_literacy\_high
-   effect\_starting\_pop\_literacy\_very\_high

This is a good idea for helping with the initial balance of the country, and will have important effects on the country over time.

## Characters\[[edit](/index.php?title=New_country_modding&veaction=edit&section=5 "Edit section: Characters") | [edit source](/index.php?title=New_country_modding&action=edit&section=5 "Edit section: Characters")\]

*See also: [Character modding](/Character_modding "Character modding")*

[![](/images/4/46/Country_creation17.png)](/File:Country_creation17.png)

[](/File:Country_creation17.png "Enlarge")

Plenty to talk about for this!

If one prefers a ruler and flag which are not automatically generated, those, too, can be defined.

To have a specific character to be the country's ruler – or any other role, the country needs an entry in a file in the character history folder (/Victoria 3/game/common/history/characters). Again, it is recommended to go through the base game and/or a mod and copying information and files from there. Possible settings for characters can be found in the base game's common folder, look for folders mentioning character.

Cyrenaica's script is here. There is a first name and a family name. **Important note:** If your names are not already localized because they exist as character or culture names, you must add separate localization for them. In Cyrenaica's case, both names were already localized by something, great! If it is necessary to localize them, the localization can be put into any file (generally speaking, localization is only organized so that people can find where things are more easily).

If it is necessary to localize the name, it's pretty much the same as above with the country localization:

Name: "Localized name"

So if Cyrenaica's leader's family name needed new localization, it would have looked like this:

al-Idrisi: "al-Idrisi"

On the left is the script key of "al-Idrisi" and on the right is the English localization of "al-Idrisi." This may seem like extra steps, but it is important. If the game doesn't detect localization for a name, it won't use the name supplied and will instead use a random name.

Next is the birthdate, so age can be calculated.

Yahya is supposed to be the country's ruler, so the script for that `ruler = yes`. There are other roles, such as `heir`. See other character files in the base game or a mod to find out more. The UK has many of characters, for example. It is possible to set the ruler to be a general at the game start, but in Cyrenaica's case that's unnecessary. It has been commented it out so that the game ignores it, but the curious can see what it looks like.

Then one must define what Interest Group the character belongs to or represents. This character is a member of the Sunni Ulema, the Muslim devout interest group. Next is an ideology. These are found in /Victoria 3/game/common/ideologies/00\_leader\_ideologies. Since Cyrenaica is not very urbanized and primarily survives on subsistence, I think the Traditionalist ideology fits best. Finally, a couple of traits, which are in the /Victoria 3/game/common/character\_traits folder.

Here's what I've got!

[![](/images/thumb/9/99/Country_creation20.png/300px-Country_creation20.png)](/File:Country_creation20.png)

[](/File:Country_creation20.png "Enlarge")

There Yahya is, working like a charm!

## Flag\[[edit](/index.php?title=New_country_modding&veaction=edit&section=6 "Edit section: Flag") | [edit source](/index.php?title=New_country_modding&action=edit&section=6 "Edit section: Flag")\]

*See also: [Flag modding](/Flag_modding "Flag modding")*

[![](/images/thumb/7/7c/Country_creation18.png/300px-Country_creation18.png)](/File:Country_creation18.png)

[](/File:Country_creation18.png "Enlarge")

This will look great

The new flag will take inspiration from the flag of the Ottoman eyalet of Tripolitania and have some small changes.

To make a basic flag in Vic3, all that is needed is an entry for it in a file in /Victoria 3/game/common/coat\_of\_arms/coat\_of\_arms. Flags can put in as plain images, but it takes up a bit more space than writing them in script and isn't as flexible. Here is the script for Cyrenaica:

A brief explanation: All flags need a basic pattern to be based on. These are located in /Victoria 3/game/gfx/coat\_of\_arms/patterns. It's important that all flag components be put in quotes and include the file extension (.tga, .dds) for them to work.

What follows is `color1`, which refers to the first colour that can be used in the flag item. In Cyrenaica's case, `pattern_solid.tga` only has one colour, so that's all that is need. More colours can be added if the user would like to refer to them later with upcoming items (so instead of having `color1 = "yellow"` in all three of the crescents, the code could have been written as `color1 = color2` with `color2 = "yellow"` underneath my pattern's `color1`. This would be a quick way to change the colours of all three crescents without needing to change "yellow" to a different colour three times.

There are the three crescents which came from the files in /Victoria 3/game/gfx/coat\_of\_arms/colored\_emblems, and they are all the same emblem. A coloured emblem's colour needs to be specified, as mentioned above, but also you don't want the default size and in the center of the flag, it is necessary to tell the game that "this instance should be of this size and the center of the emblem should be located here", which is what the *instances* in Cyrenaica's flag are doing. The scale refers to the x and y axis distortion, so if distortion is not desired, just put the same number for both. This flag has shrunk both axes by half, so these crescents are a quarter of their default size. The first crescent has been placed at `{ 0.25 0.3 }`, which means that 0.25 is a quarter of the way from the left side to the right side (0 is at the left edge of the flag), and that 0.3 is 30% of the way from the top of the flag to the bottom of the flag (0 is at the top). A rotation value has been set for the two later crescents to make sure they don't face the same direction as the first one.

**Another important note:** To make your life easier when making flags, it is suggested that the user open the game's command line (right click the game in the Steam library and look at Preferences, and there on the bottom) they should write *\-filewatcher -debug\_mode*. The first will update some files in real time as they're saved, so it will not be necessary to restart the game to see flag adjustments, and the second makes it easier to hunt down bugs and find information in the game.

The flag is now done, as is the country as a whole.

[![](/images/thumb/e/e3/Country_creation19.png/300px-Country_creation19.png)](/File:Country_creation19.png)

[](/File:Country_creation19.png "Enlarge")

There's the flag

## Dynamic country name and colors\[[edit](/index.php?title=New_country_modding&veaction=edit&section=7 "Edit section: Dynamic country name and colors") | [edit source](/index.php?title=New_country_modding&action=edit&section=7 "Edit section: Dynamic country name and colors")\]

Many countries have alternative names and colors for certain circumstances. For example, Nejd gets dynamic name "Saudi Arabia" when Nejd fully owns Hedjaz and Germany turns green if it has the "council republic" law. Use of dynamic country names and colors may get a better experience in your mod.

### Dynamic country name\[[edit](/index.php?title=New_country_modding&veaction=edit&section=8 "Edit section: Dynamic country name") | [edit source](/index.php?title=New_country_modding&action=edit&section=8 "Edit section: Dynamic country name")\]

You can define a dynamic name in /Victoria 3/game/common/dynamic\_country\_names, just add a text file in the encoding of `UTF-8 with BOM`.

For example

CYR = {
	dynamic\_country\_name = {
		name = dyn\_CYR\_empire #This can be just the TAG to reuse the default name
		adjective = dyn\_CYR\_empire\_adj # This can be TAG\_ADJ to reuse the default adjective

		is\_main\_tag\_only = yes # default no, if yes then only the primary country for a definition can use this name (i.e. Poland, not a civil war revolt Poland)
		priority = 0 # default 0, if multiple names have valid triggers, higher priority is used. If same priority, first valid one in file is used
		
		trigger = { # Scripted trigger, country-scope
			coa\_def\_monarchy\_flag\_trigger = yes
			scope:actor = {
				owns\_entire\_state\_region = STATE\_TUNISIA
			}
		}
	}	
}

Then, localize the dynamic name and dynamic adjective:

dyn\_CYR\_empire:0 "Cyrenacia Empire"
dyn\_CYR\_empire\_adj:0 "Cyrenacian"

### Dynamic country color\[[edit](/index.php?title=New_country_modding&veaction=edit&section=9 "Edit section: Dynamic country color") | [edit source](/index.php?title=New_country_modding&action=edit&section=9 "Edit section: Dynamic country color")\]

You can define the color in /Victoria 3/game/common/named\_colors, and apply the name color in /Victoria 3/game/common/dynamic\_country\_map\_colors. Dynamic colors apply the first color that have a valid trigger.

In `named_colors`

colors = {	
	cyrenacia\_empire\_red = rgb { 1.0 0.15 0.15 } #This is "decimal" RGB, this value is similar to RBG 255 38 38 or hexcode ff2626
}

In `dynamic_country_map_colors`:

cyrenacia\_empire\_red = {
	color = "cyrenacia\_empire\_red"

	possible = {
		OR = {
			AND = {
				exists = c:CYR
				THIS = c:CYR
			}
			AND = {
				exists = c:TRI # dynamic color can be applied in other country
				THIS = c:TRI
			}
		}
		owns\_entire\_state\_region = STATE\_LIBYAN\_DESERT
		owns\_entire\_state\_region = STATE\_TUNISIA
	}
}

## References\[[edit](/index.php?title=New_country_modding&veaction=edit&section=10 "Edit section: References") | [edit source](/index.php?title=New_country_modding&action=edit&section=10 "Edit section: References")\]

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

[Mod translation](/Mod_translation "Mod translation") • New country modding • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=New\_country\_modding&oldid=21354](https://vic3.paradoxwikis.com/index.php?title=New_country_modding&oldid=21354)"

[Categories](/Special:Categories "Special:Categories"):

-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [1.8](/Category:1.8 "Category:1.8")
-   [Modding](/Category:Modding "Category:Modding")

-   This page was last edited on 11 March 2025, at 23:23.
-   Content is available under [Attribution-ShareAlike 3.0](https://central.paradoxwikis.com/Central:Copyrights "central:Central:Copyrights") unless otherwise noted.

-   [Privacy policy](/Victoria_3_Wiki:Privacy_policy)
-   [About Victoria 3 Wiki](/Victoria_3_Wiki:About)
-   [Disclaimers](/Victoria_3_Wiki:General_disclaimer)
-   [Mobile view](https://vic3.paradoxwikis.com/index.php?title=New_country_modding&mobileaction=toggle_view_mobile)

-   [![Attribution-ShareAlike 3.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/3.0/)
-   [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)