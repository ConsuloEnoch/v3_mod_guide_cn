# Scripted test

From Victoria 3 Wiki

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") 1.10.

Scripted tests are utility files used to check how often a defined game state is achieved. They do not affect gameplay in any way.

## Contents

-   [1 Definition](#Definition)
    -   [1.1 Elements](#Elements)
-   [2 Usage](#Usage)
-   [3 Output](#Output)
-   [4 References](#References)

## Definition

Scripted tests are defined in /tools/scripted_tests/.

They take the form like the following:

last_date = "1900.1.1"

tests = {
    GER_forms = {
        acceptable_fail_rate = 0.0
        success = {
            exists = c:GER 
        }
        fail = {
            game_date > "1890.1.1"
        }
    }
    another_test = {
        ...
    }
    ...
}

### Elements

A scripted test file contains a number of elements, most required. Each file can contain any number of tests. All tests are contained within the `tests = { }` block.

-   `last_date` determines how long tests in the file are valid. If that date passes, the tests are no longer checked. If neither trigger returned true, the test is marked as "skipped".
-   `success` is a [trigger](/Trigger "Trigger") block that marks the test as "passed" if it returns true before the fail trigger and before the `last_date`.
-   `fail` is a trigger block that marks the test as "failed" if it returns true before the success trigger returns true and before the `last_date`. Both triggers are checked daily and if they both return true on the same day, the test is marked as "passed".
-   `acceptable_fail_rate` is a decimal percent value used for metadata analysis. It does not impact the test behavior at all. It defaults to 0 if not defined.
-   `run_count` is an integer value that defines the number of times a test is run. Only runs that either fail or pass are counted. A value less than 0 causes the test to run indefinitely, that is until the `last_date`. Only the final run is recorded for the output. It defaults to 1 if not defined.

## Usage

Scripted tests can be enabled through a command line argument or console command.

There are three command lines arguments related to scripted tests:

-   `-run_tests` / `-scripted_tests` – This enables the scripted tests
-   `-no_save_after_failed_test` – This disables creating saves the day after a failed test; otherwise enabled by default
-   `-save_before_failed_test` – This disables creating saves the day after a test fails. This is very slow and not generally recommended.

There is one console command for scripted tests `scripted_tests`. It can take an optional argument to create saves before, after (default), or not at all

-   `scripted_tests` – Save is created after the tests
-   `scripted_tests before` – Save is created before the tests
-   `scripted_tests none` – No save is created

If scripted tests are active, entering the command again disables the tests.

## Output

At the end of the tests, a text file with the results is created in the Documents folder. Additionally, an XML file is created in the game's binaries folder.

## References

-   Information adapted from /Victoria 3/game/tools/scripted_tests/scripted_tests.md

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

[AI](/AI_modding "AI modding") • [Console commands](/Console_commands "Console commands") • [Checksum](/Checksum "Checksum") • [Mods](/Mod "Mod") • [Mod compatibility](/Mod_compatibility "Mod compatibility") • [Mod structure](/Mod_structure "Mod structure") • Scripted tests • [Troubleshooting](/index.php?title=Mod_troubleshooting&action=edit&redlink=1 "Mod troubleshooting (page does not exist)")

Guides

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • [Save-game editing](/Save-game_editing "Save-game editing") • [State modding guide](/State_modding_guide "State modding guide")

Source: [https://vic3.paradoxwikis.com/Scripted_test](https://vic3.paradoxwikis.com/Scripted_test)
