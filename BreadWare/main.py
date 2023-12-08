# [BreadWare.gg]
#   [external]

# [banner]
print("[BreadWare.gg] - Бесплатный чит на CS2, с открытым исходным кодом.")
print("[BreadWare.gg] - github: https://github.com/bread2288/BreadWare.gg/tree/main \n")


# [libs]
import memory
import gui

# [utils]
from utils import noflash
from utils import bhop

from utils import entity



# [main]
memory.threading.Thread(target=noflash.no_flash, name="noflash", daemon=True).start()
memory.threading.Thread(target=bhop.bhop, name="bhop", daemon=True).start()
memory.threading.Thread(target=entity.get_entity, name="ent", daemon=True).start()

gui.dpg.start_dearpygui()