// [BreadWare.gg]
//  No Flashbang

#pragma once
#include <iostream>
#include <thread>
#include "../scr/memory.h"

int NoFlash()
{
	Memory mem{ "cs2.exe" };
	auto client = mem.GetModuleAddress("client.dll");

	auto local_player = mem.Read<uintptr_t>(client + 0x16C29E8);
	auto flashDur = mem.Read<int>(local_player + 0x1468);

	if (flashDur != 0)
	{
		mem.Write(local_player + 0x1464, 80.f);
	}
	
	// end
	return 0;
}