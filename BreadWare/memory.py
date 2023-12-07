# [BreadWare.gg]
#   [external]


# [libs]
import pymem
import pymem.process
import time
import threading


# [/]
print("[BreadWare.gg] - запускаем чит...")
while (True):
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        local_player = pm.read_ulonglong(client + 0x16C2DD8)
        break
    except:
        print("[BreadWare.gg] - ждёмс cs2...")
        time.sleep(5)
print("[BreadWare.gg] - подключились к cs2!")