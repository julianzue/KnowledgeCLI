from colorama import Fore, Style, init
import os
import time

init()

# colors
r = Fore.LIGHTRED_EX
c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
re = Fore.RESET

# styles
dim = Style.DIM
res = Style.RESET_ALL

class App():
    def __init__(self):
        
        self.commands = [
            {"name": "add", "command": self.add, "description": "Adds a new theme or a new item in a theme."},
            {"name": "show", "command": self.show, "description": "Shows the content of the notes."},
            {"name": "help", "command": self.help, "description": "Shows this help."}, 
            {"name": "clear", "command": self.clear, "description": "Clears the screen."},  
            {"name": "search", "command": self.search, "description": "Searches a keyword in the themes."}, 
            {"name": "exit", "command": self.close, "description": "Closes this program."},   
        ]

        #for index, command in enumerate(self.commands, 1):
        #    print("[" + str(index) + "] " + command["name"])

        cmd = input(y + "[+] "  + re)

        invalid_command = True

        if cmd.isnumeric():
            self.commands[int(cmd) - 1]["command"]()
            invalid_command = False
        else:
            for command in self.commands:
                if command["name"] == cmd:
                    invalid_command = False
                    command["command"]()

        if invalid_command:
            print("")
            print(r + "[!] " + re + "Invalid commmand.")
            print("")
            self.__init__()
            

    def add(self):
        
        print("")
        print("ADD")
        print("---")
        print("[1] Theme")
        print("[2] Item in Theme")

        choose_type = input(y + "[+] Choose: " + re)

        if choose_type == "1":
            name = input(y + "[+] Enter name of new theme: " + re)

            os.system("mkdir notes/" + name)

            print(c + "[*] " + re + "Theme " + c + name + re + " successfully added.")

        elif choose_type == "2":
            
            print("")

            themes = []

            for index, item in enumerate(os.scandir("notes"), 1):
                print("[" + str(index) + "] " + item.name)
                themes.append(item)

            choose_theme = input(y + "[+] Enter theme number: " + re)

            content = input(y + "[+] Enter content: " + re)

            filename = time.strftime("%Y-%m-%d_%H-%M") + ".txt"


            with open("notes/" + themes[int(choose_theme) - 1].name + "/" + filename, "w") as fw:
                fw.write(content)                

            print(c + "[*] " + re + "Item " + c + filename + re + " successfully added!")

        else:
            print(r + "[!]" + re + "Invalid command.")

        print("")
        self.__init__()

    def show(self):

        print("")
        print("SHOW")
        print("----")
        print("")

        counter = 0
        themes_list = []

        for themes in os.scandir("notes"):
            themes_list.append(themes.name)
            
        themes_list.sort()

        for theme in themes_list:

            print(c + theme + re)

            items = []

            for index, item in enumerate(os.scandir("notes/" + theme), 1):
                # print(c + "\t" + item.name + re)

                items.append(item.name)

            items.sort()

            for i, item in enumerate(items, 1):
                with open("notes/" + theme + "/" + item, "r") as fr:
                    for line in fr.readlines():
                        counter += 1

                        name = line.split(", ")[0]

                        print("[" + str(i) + "] " + dim + item.split(".")[0] + " " + y + name + " " + res + ", ".join(line.strip("\n").split(", ")[1:]))

            print("")
                
        print("Count: " + str(counter))
        print("")

        self.__init__()

    def close(self):
        print(r + "[!] " + re + "Program closed!")
        quit()

    def help(self):

        print("")
        print("Help")
        print("----")

        for command in self.commands:
            print(c + command["name"] + re + "\t" + command["description"])

        print("")

        self.__init__()

    def clear(self):
        os.system("clear")
        self.__init__()

    def search(self):

        print("")
        print("SEARCH")
        print("------")
        query = input(y + "[+] Enter Keyword: " + re)

        print("")

        themes_list = []

        for themes in os.scandir("notes"):
            themes_list.append(themes.name)
            
        themes_list.sort()

        counter = 0

        for theme in themes_list:

            print(c + theme + re)

            items = []

            for index, item in enumerate(os.scandir("notes/" + theme), 1):
                # print(c + "\t" + item.name + re)

                items.append(item.name)

            items.sort()

            for i, item in enumerate(items, 1):
                with open("notes/" + theme + "/" + item, "r") as fr:
                    for line in fr.readlines():

                        if query in line.strip("\n"):

                            counter += 1

                            name = line.split(", ")[0]

                            print("[" + str(i) + "] " + dim + item.split(".")[0] + " " + y + name + " " + res + ", ".join(line.strip("\n").split(", ")[1:]))

            print("")
                
        print("Count: " + str(counter))
        print("")

        self.__init__()

App()