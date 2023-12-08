# [BreadWare.gg]
#   [external]


# [libs]
import memory
import gui

def no_flash():
    memory.pm.write_float(memory.local_player + 0x1464, 255.0)
    while (True):
            pm = memory.pm
            local_player = memory.local_player

            if (gui.dpg.get_value("noflash")):
                pm.write_int(local_player + 0x1468, 0)
            else:
                pass