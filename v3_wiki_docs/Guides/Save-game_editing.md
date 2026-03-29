# Save-game editing

From Victoria 3 Wiki

[Jump to navigation](#mw-head) [Jump to search](#searchInput)

 

Please help with verifying or updating older sections of this article.  
At least some were last verified for [version](/Victoria_3_Wiki:Versioning "Victoria 3 Wiki:Versioning") unknown.

## Format of a save-file\[[edit](/index.php?title=Save-game_editing&veaction=edit&section=1 "Edit section: Format of a save-file") | [edit source](/index.php?title=Save-game_editing&action=edit&section=1 "Edit section: Format of a save-file")\]

By default save-files consist of a zipped file with the extension '.v3'. It containes two files: one called 'meta' the other 'gamestate'. The gamestate file is in a **binary format**.

By editing the file `"pdx_settings.json"` under `"~/Documents/Paradox Interactive/Victoria 3/"` and changing "save\_file\_format": "zip\_binary\_all" to "text" save-files are saved in a **[simple text](http://en.wikipedia.org/wiki/simple_text "wikipedia:simple text")\-format**.

## Structure of a save-file\[[edit](/index.php?title=Save-game_editing&veaction=edit&section=2 "Edit section: Structure of a save-file") | [edit source](/index.php?title=Save-game_editing&action=edit&section=2 "Edit section: Structure of a save-file")\]

provinces\={
	0\={
	}

	1\={
		state\=4
	}
…
	40923\={
	}

	40924\={
	}

}

pops\={
	database\={
2113929216\={						\# ID of this POP
	type\="laborers"					\# the profession of this POP
	size\_wa\=498					\# number of individuals that are workers
	size\_dn\=1500					\# number of individuals that are dependants
	location\=119					\# location, 119 equals STATE\_SVEALAND
	interest\_group\_support\={ 0.14669 0.18189 0 0 0 0 0 0.17652 }	\# support for IGs, Σ < literates
	culture\=19							\# culture, 19 equals danish
	workplace\=2068							\# building this POP is employed at, if this line is missing, the POP is unemployed; the ID of the workplace corresponds to a building somewhere else in the save-file
	religion\="mahayana"						\# religion
	assimilation\_culture\=18						\# individual workers are in the process of being transfered to a different POP, whith this culture
	conversion\_religion\="protestant"				\# individual workers are in the process of being transfered to a different POP, whith this religion
	literate\=10							\# number of individuals that are literate (only workers count!)
	qualifications\={ 15 0\=1.64121 2\=2.76406 4\=1.32237 5\=6.92633 6\=0.49763 7\=6.73474 9\=6.9817 10\=0.07121 12\=1.42598 }  \# number of individuals that qualify to work as a different profession 0 equals academics
	wealth\=9							\# current wealth level 1–100
	previous\_quality\_of\_life\=9					\# previous wealth level 1–100
	loyalists\_and\_radicals\=2					\# a positive number equals loyalists, a negative number equals radicals
	weekly\_budget\={ 1.62679 0 0.87451 0 0 0 \-1.67994 0 \-0.28468 \-0.27778 0 \-0.12786 }	\# something to do with buying packages
	partial\_growth\_wa\=0.31659					\# goes towards the default relation of wa to dn
	partial\_growth\_dn\=0.08076					\# goes towards the default relation of wa to dn
}
…
states\={
	database\={
0\={
	capital\=23186
	country\=3
	arable\_land\=60
	incorporation\=1
	migration\_cache\={
		standard\_of\_living\=10.88086
		migration\_pull\=17.44632
	}
	market\=26
	infrastructure\=35.07777
	infrastructure\_usage\=36.8
	pop\_needs\={
		12\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

		45\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

		46\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

		49\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

		50\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

		51\={
			pop\_need\_entry\_data\={ {
					weights\={
						9\=2.12331
						12\=2.87664
					}
				}
 {
					weights\={
						10\=2.48246
						13\=2.51749
					}
				}
 {
					weights\={
						7\=3.43085
						8\=0.1909
						11\=0.6884
						36\=0.2389
						37\=0.10595
					}
				}
 {
					weights\={
						9\=2.15615
						10\=2.84375
						17\=0
						23\=0.00005
						28\=0
					}
				}
 {
					weights\={
						13\=3.96885
						14\=0.17575
						31\=0.67955
					}
				}
 {
					weights\={
						12\=1
					}
				}
 {
					weights\={
						15\=1
					}
				}
 {
					weights\={
						38\=3
						43\=0.343
						44\=0
					}
				}
 {
					weights\={
						39\=3
						40\=1.80325
						41\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						45\=0
					}
				}
 {
					weights\={
						15\=0.4
						16\=0
						46\=0.549
					}
				}
 {
					weights\={
						11\=2
						36\=1.60365
						37\=0.71115
						42\=0.1873
					}
				}
 {
					weights\={
						35\=1.86588
						47\=0
						48\=1.05142
						49\=2
					}
				}
 {
					weights\={
						15\=0.238
						51\=0.2393
					}
				}
 }
		}

	}
	building\_budget\={
		expenses\=9386.85014
		incomes\=2712.47848
		gov\_goods\_expenses\={ 44 43\=3424.69036 }
		gov\_salaries\_expenses\={ 82 43\=4290.60418 81\=319.76043 }
		construction\_goods\_expenses\={ 82 81\=1351.79517 }
		income\_taxes\={ 82 1\=105.02579 2\=84.02338 15\=35.60285 39\=80.41243 43\=300.34225 67\=95.93336 76\=182.25525 81\=22.38317 }
		poll\_taxes\={ 77 76\=1806.5 }
	}
	variables\={
	}
	region\="STATE\_MINSK"
	provinces\={
		provinces\={ 23168 20 }
	}
	pop\_statistics\={
		lower\_strata\_pops\=928279			\# number of individuals working in those professions
		middle\_strata\_pops\=100695			\# number of individuals working in those professions
		upper\_strata\_pops\=40285				\# number of individuals working in those professions
		radicals\=138187					\# number of individuals that are radicals
		loyalists\=33611					\# number of individuals that are loyalists
		total\_political\=317176				\# number of individuals that are eligible to engage in politics, i.e. support IGs
		salaried\_working\_adults\=172656
		subsisting\_working\_adults\=144520
		government\_working\_adults\=50000
		laborer\_working\_adults\=77350
		pop\_by\_strata\={ 3 0\=928279 1\=100695 2\=40285 }
		pop\_by\_type\={ 15 0\=1 1\=35155 2\=17158 3\=5130 4\=58565 5\=148018 6\=3344 7\=5475 8\=254556 9\=33003 10\=5 11\=487191 12\=21622 14\=36 }
		pop\_workforce\_by\_type\={ 15 1\=8870 2\=5000 3\=1500 4\=17386 5\=44100 6\=1000 7\=1600 8\=77350 9\=9750 11\=144520 12\=6100 }
		qualifications\={ 15 0\=39325 1\=15033 2\=36039 3\=12249 4\=32289 5\=75572 6\=15956 7\=85946 8\=317176 9\=36652 10\=6566 11\=317176 12\=96708 13\=317176 14\=317176 }
		employable\_qualifications\={ 15 0\=1418 1\=666 2\=1747 3\=718 4\=880 5\=5998 6\=485 7\=15822 8\=144520 9\=1311 10\=232 11\=144520 12\=6505 13\=144520 14\=144520 }
	}
	last\_week\_pop\_migration\_statistics\={
		immigration\=240
		immigration\_states\={ 725 728 745 749 750 755 756 757 759 760 761 762 763 764 768 770 771 772 773 775 776 777 843 845 847 848 }
	}
	base\_pop\_bureaucracy\_cost\=21.38518
}
…
laws\={
	database\={
0\={
	law\=law\_chiefdom	country\=1		\# 1 equals United Kingdom
}
1\={
	law\=law\_monarchy	country\=1
	active\=yes
	activation\_date\=1836.1.1
}
2\={
	law\=law\_presidential\_republic	country\=1
}
481\={
	law\=law\_laissez\_faire	country\=9
	random\_seed\=85341819			\# unknown
	enactment\_start\_date\=1854.3.23.18
	progress\=0.53856			\# % of time passed since enactment start. Change this to 0.99999 to accelerate
	enactment\_scope\={
		root\={
			type\=ctry
			identity\=9
		}
		seed\=145384830			\# unknown
	}
}

IGs: ig\_armed\_forces ig\_devout ig\_industrialists ig\_intelligentsia ig\_landowners ig\_petty\_bourgeoisie ig\_rural\_folk ig\_trade\_unions

qualifications: 0 academics 1 aristocrats 2 bureaucrats 3 capitalists 4 clergymen 5 clerks 6 engineers 7 farmers 9 machinists 10 officers 12 shopkeepers

8 laborers, seems to always be 100% 11 soldiers (servicemen), seems to always be 100%

## Using Vim\[[edit](/index.php?title=Save-game_editing&veaction=edit&section=3 "Edit section: Using Vim") | [edit source](/index.php?title=Save-game_editing&action=edit&section=3 "Edit section: Using Vim")\]

When using [Vim](http://en.wikipedia.org/wiki/vim "wikipedia:vim"), before saving, a ":set binary" command must be given, so that no extra EOF is added to the saved file.

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

[Mod translation](/Mod_translation "Mod translation") • [New country modding](/New_country_modding "New country modding") • Save-game editing • [State modding guide](/State_modding_guide "State modding guide")

Retrieved from "[https://vic3.paradoxwikis.com/index.php?title=Save-game\_editing&oldid=33465](https://vic3.paradoxwikis.com/index.php?title=Save-game_editing&oldid=33465)"

[Categories](/Special:Categories "Special:Categories"):

-   [Potentially outdated](/Category:Potentially_outdated "Category:Potentially outdated")
-   [Unknown version](/Category:Unknown_version "Category:Unknown version")
-   [Modding](/Category:Modding "Category:Modding")

-   This page was last edited on 18 December 2025, at 04:58.
-   Content is available under [Attribution-ShareAlike 3.0](https://central.paradoxwikis.com/Central:Copyrights "central:Central:Copyrights") unless otherwise noted.

-   [Privacy policy](/Victoria_3_Wiki:Privacy_policy)
-   [About Victoria 3 Wiki](/Victoria_3_Wiki:About)
-   [Disclaimers](/Victoria_3_Wiki:General_disclaimer)
-   [Mobile view](https://vic3.paradoxwikis.com/index.php?title=Save-game_editing&mobileaction=toggle_view_mobile)

-   [![Attribution-ShareAlike 3.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/3.0/)
-   [![Powered by MediaWiki](/resources/assets/poweredby_mediawiki_88x31.png)](https://www.mediawiki.org/)