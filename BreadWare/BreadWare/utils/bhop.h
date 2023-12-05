// [BreadWare.gg]
//     Bhop

#pragma once
#include <iostream>
#include <thread>
#include "../scr/memory.h"

int Bhop()
{

	Memory mem{ "cs2.exe" };
	auto client = mem.GetModuleAddress("client.dll");

	auto local_player = mem.Read<uintptr_t>(client + 0x16C29E8);
	auto fFlag = mem.Read<int32_t>(local_player + 0x3C8);

	if (GetAsyncKeyState(VK_SPACE))
	{
		if (fFlag == 65665 || fFlag == 65667)
		{
			std::this_thread::sleep_for(std::chrono::milliseconds(1));
			mem.Write(client + 0x16BBE50, 65537);
		}
		else
		{
			mem.Write(client + 0x16BBE50, 256);
		}
		std::this_thread::sleep_for(std::chrono::milliseconds(5));
	}

	// end
	return 0;
}