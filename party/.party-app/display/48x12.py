from time import sleep
from subprocess import run
try:
    from colorama import init, Fore
except ImportError:
    print("""
Missing or corrupted dependency: colorama
Install with:

$ pip install colorama
""")
    exit()
          
init()

party = f"""
████████████████████████████████████████████████
██     ████     ███     ████        ██   ██   ██
██  ██  ██  ███  ██  ███  █████  ██████  ██  ███
██  ██  ██  ███  ██  ███  █████  ██████  ██  ███
██  ██  ██  ███  ██  ███  █████  ███████    ████
██     ███       ██      ██████  ████████  █████
██  ██████  ███  ██  ██  ██████  ████████  █████
██  ██████  ███  ██  ███  █████  ████████  █████
██  ██████  ███  ██  ███  █████  ████████  █████
██  ██████  ███  ██  ███  █████  ████████  █████
████████████████████████████████████████████████
████████████████████████████████████████████████
"""

for color in [Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.BLUE]:
    run(["clear"])
    print(f"{color}{party}")
    sleep(0.5)