import os
import glob
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import json5

colorama_init()

print(f"""       
{Fore.GREEN} ██████╗        {Fore.RED}██╗   ██╗      {Fore.BLUE}███╗   ███╗
{Fore.GREEN}██╔════╝        {Fore.RED}╚██╗ ██╔╝      {Fore.BLUE}████╗ ████║
{Fore.GREEN}██║  ███╗       {Fore.RED} ╚████╔╝       {Fore.BLUE}██╔████╔██║
{Fore.GREEN}██║   ██║       {Fore.RED}  ╚██╔╝        {Fore.BLUE}██║╚██╔╝██║
{Fore.GREEN}╚██████╔╝       {Fore.RED}   ██║         {Fore.BLUE}██║ ╚═╝ ██║
{Fore.GREEN} ╚═════╝amemaker{Fore.RED}   ╚═╝YP       {Fore.BLUE}╚═╝     ╚═╝anipulator
{Style.RESET_ALL}
-The Ultimate Gamemaker Project File Editor-
""")




def recursive_search(directory, ext):
    output = []
    for filepath in glob.glob(f'{directory}/**/*.{ext}', recursive=True):
        normalized_path = os.path.normpath(filepath).replace('\\', '/')
        output.append(normalized_path)
    return output



def recover_yyp():
    projectfolder = ""
    while True:
        project_folder = os.path.normpath(input("Please input your project folder:")).replace('\\', '/')
        if not os.path.exists(project_folder):
            project_folder = ""
            print(f"{Fore.RED}ERROR! Path not valid! Try again.{Style.RESET_ALL}")
        else:
            break

    assets = recursive_search(project_folder, "yy")

    yyp = {
        "$GMProject":"",
        "%Name":f"{os.path.basename(project_folder)}",
        "configs":{
            "children":[],
            "name":"Default",
        },
        "defaultScriptType":1,
        "Folders":[
                {"$GMFolder":"","%Name":"Animation Curves","folderPath":"folders/Animation Curves.yy","name":"Animation Curves","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Extensions","folderPath":"folders/Extensions.yy","name":"Extensions","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Fonts","folderPath":"folders/Fonts.yy","name":"Fonts","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Notes","folderPath":"folders/Notes.yy","name":"Notes","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Objects","folderPath":"folders/Objects.yy","name":"Objects","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Paths","folderPath":"folders/Paths.yy","name":"Paths","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Rooms","folderPath":"folders/Rooms.yy","name":"Rooms","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Scripts","folderPath":"folders/Scripts.yy","name":"Scripts","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Sequences","folderPath":"folders/Sequences.yy","name":"Sequences","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Shaders","folderPath":"folders/Shaders.yy","name":"Shaders","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Sounds","folderPath":"folders/Sounds.yy","name":"Sounds","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Sprites","folderPath":"folders/Sprites.yy","name":"Sprites","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Tile Sets","folderPath":"folders/Tile Sets.yy","name":"Tile Sets","resourceType":"GMFolder","resourceVersion":"2.0",},
                {"$GMFolder":"","%Name":"Timelines","folderPath":"folders/Timelines.yy","name":"Timelines","resourceType":"GMFolder","resourceVersion":"2.0",},
        ],
        "IncludedFiles":[],
        "isEcma":False,
        "name":f"{os.path.basename(project_folder)}",
        "resources": [],
        "resourceType":"GMProject",
        "resourceVersion":"2.0",
        "templateType":None,
        


    }
    datafiles = recursive_search(project_folder+"/datafiles", "*")
    for datafile in datafiles:
        yyp["IncludedFiles"].append(
            {
                "$GMIncludedFile":"",
                "%Name": (os.path.basename(datafile)).replace(project_folder+"/datafiles", ""), 
                "CopyToMask":-1,
                "filePath":"datafiles",
                "name": (os.path.basename(datafile)).replace(project_folder+"/datafiles", ""), 
                "resourceType":"GMIncludedFile",
                "resourceVersion":"2.0",
            }
        )
    for asset in assets:
        with open(asset) as f:
            data = json5.load(f)
            if(data.get("parent", "NOTFOUND") is not "NOTFOUND"):
                folderpath = data["parent"]["path"]
                folderstruct  = {"$GMFolder":"","%Name":f"{os.path.splitext(os.path.basename(folderpath))[0]}","folderPath":f"{folderpath}","name":f"{os.path.splitext(os.path.basename(folderpath))[0]}","resourceType":"GMFolder","resourceVersion":"2.0"}
                if folderstruct not in yyp["Folders"]:
                    yyp["Folders"].append(folderstruct)
        yyp["resources"].append(
            {
                "id": {
                    "name": (os.path.basename(asset)).replace(project_folder+"/", "").replace(".yy", ""),
                    "path": asset.replace(project_folder+"/", "")
                }
            }
        )
    with open(f"{project_folder}\{os.path.basename(project_folder)}_recovered.yyp", "w") as outfile: 
        json5.dump(yyp, outfile, indent=4)

def run_gymscript():
    pass

def add_resource():
    pass

options = {
    "1": recover_yyp,
    "2": run_gymscript,
    "3": add_resource
}

while True:
    option = input("""
What would you like to do?
1. Regenerate/Recover YYP
2. Run a GYMScript
3. Add resource to YYP
""")
    if option in options:
        print("Starting... Please wait.")
        options[option]()
        break
    else:
        print(f"{Fore.RED}ERROR! Option not found! Try again.{Style.RESET_ALL}")
