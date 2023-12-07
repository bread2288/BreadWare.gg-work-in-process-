# [BreadWare.gg]
#   [external]


# [libs]
import memory
import menu
import keyboard
import time

def bhop():
    while (True):
            pm = memory.pm
            client = memory.client
            local_player = memory.local_player

            fflags = pm.read_uint(local_player + 0x3C8)

            if (keyboard.is_pressed("space")):
                if (fflags & (1<<0)):
                    pm.write_int(client + 0x16BC240, 256)
                    pm.write_int(client + 0x16BC240, 65537)
                else:
                    pm.write_int(client + 0x16BC240, 256)
                    pm.write_int(client + 0x16BC240, 65537)