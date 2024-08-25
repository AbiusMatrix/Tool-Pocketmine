import time
import os
import datetime

RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

class FileManager:
    def __init__(self, pluginName, apiPlugin, versionPlugin, mainPlugin, authorPlugin):
        self.mainPlugin = mainPlugin.replace("\\", "/")
        print(f"\n{YELLOW}Plugin is creating now..{RESET}\n")
        time.sleep(5)
        self.register_result_folder()
        self.register_current_folder(pluginName)
        self.createPluginYAML(pluginName, apiPlugin, versionPlugin, mainPlugin, authorPlugin)
        self.createSource(pluginName, apiPlugin, versionPlugin, self.mainPlugin, authorPlugin)

    def register_result_folder(self):
        result_dir = "result"
        if not os.path.exists(result_dir):
            os.mkdir(result_dir)
        print(f"{GREEN}Folder Result Is Creating [100%]{RESET}")

    def register_current_folder(self, plugin_Name):
        if not os.path.exists("result/" + plugin_Name):
            os.mkdir("result/" + plugin_Name)
            print(f"{GREEN}This Plugin Is Creating [100%]{RESET}")
        else:
            print(f"{RED}This Plugin Already Exists.{RESET}")

    def createPluginYAML(self, pluginName2, apiPlugin2, versionPlugin2, mainPlugin2, authorPlugin2):
        data = "name: " + pluginName2 + "\napi: " + apiPlugin2 + "\nversion: " + versionPlugin2 + "\nmain: " + mainPlugin2 + "\nauthor: " + authorPlugin2
        file = open("result/" + pluginName2 + "/plugin.yml", "w");
        file.write(data)

    def createSource(self, pluginName2, apiPlugin2, versionPlugin2, mainPlugin2, authorPlugin2):
        main = mainPlugin2.split("/")
        os.mkdir("result/" + pluginName2 + "/src")
        os.mkdir("result/" + pluginName2 + "/src/" + main[0])
        os.mkdir("result/" + pluginName2 + "/src/" + main[0] + "/" + main[1])
        file = open("result/" + pluginName2 + "/src/" + main[0] + "/" + main[1] + "/" + main[2] + ".php", "w")
        default_code = "<?php\n\nnamespace " + main[0] + "*" + main[1] + ";\n\nuse pocketmine*plugin*PluginBase;\nuse pocketmine*player*Player;\nuse pocketmine*Server;\n\nclass " + main[2] + " extends PluginBase {\n\n     public function onEnable():void{\n\n    }\n}"
        default_code = default_code.replace("*", chr(92))
        file.write(default_code)
