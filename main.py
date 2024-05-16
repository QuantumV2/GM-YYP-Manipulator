from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

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





def recover_yyp():
    pass

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
