# [BreadWare.gg]
#   [external]


# [libs]
import memory
import menu

def no_flash():
    while (True):
            pm = memory.pm
            local_player = memory.local_player

            pm.write_float(local_player + 0x1464, menu.dpg.get_value("alpha"))