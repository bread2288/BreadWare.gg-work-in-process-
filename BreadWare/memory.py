# [BreadWare.gg]

import pymem
import pymem.process
import time
import os

# [Attach]
print("[BreadWare.gg] - START attach to cs2.exe")
while (True):
    try:
        pm = pymem.Pymem("cs2.exe")
        break
    except pymem.exception.ProcessNotFound:
        print("[BreadWare.gg] - WAIT cs2...")
        time.sleep(3)
    except:
        print("[BreadWare.gg] - Unknow ERROR")
        os.system("pause")
print("[BreadWare.gg] - END attach to cs2.exe")