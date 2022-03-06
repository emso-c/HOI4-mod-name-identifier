import os

if(os.getcwd()[-("Steam\steamapps\workshop\content\\394360".__len__()):] != "Steam\steamapps\workshop\content\\394360"):
   print(f"Warning: You might've put the file in the wrong directory: '{os.getcwd()}'\nPlease put it under 'Your-path-to-Steam\Steam\steamapps\workshop\content\\394360'.\n")

mod_list = []
for root, dirs, files in os.walk("."):
   for file in files:
      if file == "descriptor.mod":
         with open(root+"\\"+file, "r") as f:
            for line in f.readlines():
               if line.startswith("name="):
                  mod_name = "_"+line[6:][:-2] # put underscore before mod name to make it easier to see
                  target_path = root+"\\"+mod_name
                  default_path = root+"\\"+"MOD_NAME.txt"
                  mod_list.append((root[2:], mod_name[1:]))
                  try:
                     open(target_path, "w").close()
                     print(f"Created file: {target_path}")
                  except OSError as e:
                     if e.errno==22:
                        print(f"Invalid characters: {target_path}\nWriting inside the file '{default_path}' instead")
                        with open(default_path, "w") as f:
                           f.write(mod_name)
                     else:
                        print(f"Unidentified error. Skipping this file: {target_path}")

with open("mod_list.txt", "w") as f:   
   [f.write(", ".join(mod)+"\n") for mod in mod_list]

os.system("pause")
