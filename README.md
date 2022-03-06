# HOI4-mod-name-identifier

A small script to identify HOI4 mod names from the Steam directory.

Ever tried to check a HOI4 mod's files for whatever reason? Might be just to see the values, or edit them. I've tried it, encountered a bunch of numbers instead of mod names, got frustrated and wrote this thing in like half an hour. Feel free to use or edit.

##### Only tested it on Windows, but it should work fine on a different OS too.

## How to use

- Just put `hoi4_mod_identifier.exe` into `your/steam/path/steamapps/workshop/content/394360` and run the script. It will create a text file named `mod_list.txt`. You can check which number correlates to which mod. Alternatively, you can check any of the mod folders to see the mod name on an empty file in `_mod_name` format.

### For development

- Do the same for `hoi4_mod_identifier.py` and edit its content as you like. The only difference is you'll have to use python to run the script.
