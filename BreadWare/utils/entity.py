# [BreadWare.gg]
#   [external]

# [libs]
import memory

def get_entity():
    while (True):
        pm = memory.pm
        client = memory.client
        local_player = memory.pm
        for i in range(1, 65):
            Entity = pm.read_longlong(client + 0x17BB820)
            if (Entity == 0): continue

            listEntity = pm.read_longlong(Entity + ((8 * (i & 0x7FFF) >> 9) + 16))
            if (listEntity == 0): continue

            entityController = pm.read_longlong(listEntity + (120) * (i & 0x1FF))
            if (entityController == 0): continue

            entityControllerPawn = pm.read_longlong(entityController + 0x7EC)
            if (entityControllerPawn == 0): continue

            listEntity = pm.read_longlong(Entity + (0x8 * (entityControllerPawn & 0x7FFF) >> 9) + 16)
            if (listEntity == 0): continue

            entityPawn = pm.read_longlong(listEntity + (120) * (entityControllerPawn & 0x1FF))
            if (entityPawn == 0): continue

            entityAddress = pm.read_longlong(entityController + 0x750)

            print(f"Entity: {i}, Health: {entityPawn + 0x32C}")