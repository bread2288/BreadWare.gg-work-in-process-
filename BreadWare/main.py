# [BreadWare.gg]
#   [external]

# [banner]
print("[BreadWare.gg] - Free cheat for cs2, with open source.")
print("                 github: https://github.com/bread2288/BreadWare.gg/tree/main \n")


# [libs]
import memory
import menu

# [utils]
from utils import noflash
from utils import bhop



# [main]
memory.threading.Thread(target=noflash.no_flash, name="noflash", daemon=True).start()
memory.threading.Thread(target=bhop.bhop, name="bhop", daemon=True).start()

menu.dpg.start_dearpygui()