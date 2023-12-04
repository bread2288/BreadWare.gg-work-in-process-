// [BreadWare.gg]

using ClickableTransparentOverlay;
using System.Numerics;
using ImGuiNET;
using Swed64;
using System.Runtime.InteropServices;
using Veldrid;

namespace cs2
{
    class Ware : Overlay
    {
        [DllImport("user32.dll")]
        static extern bool GetAsyncKeyState(int vKey);

        Swed mem;

        IntPtr client;


        // vars
        bool noflash = true;
        float noflash_alpha = 160.0f;
        bool bhop = true;

        protected override void Render()
        {
            // [IMGUI]
            ImGui.SetNextWindowSize(new Vector2(350, 400));
            ImGui.Begin("[BreadWare.gg] - Counter-Strike 2 [v0.12]", ImGuiWindowFlags.NoResize);
            if (ImGui.BeginTabBar("BreadWare"))
            {
                if (ImGui.BeginTabItem("General"))
                {
                    ImGui.Checkbox("NoFlash", ref noflash);
                    ImGui.SliderFloat("NoFlash Alpha", ref noflash_alpha, 0, 255);
                    ImGui.Checkbox("Bhop", ref bhop);
                }
            }
        }

        void GetBase()
        {
            Console.WriteLine($"[BreadWare.gg] - START attach to cs2.exe");
            while (true)
            {
                try
                {
                    mem = new Swed("cs2");
                    client = mem.GetModuleBase("client.dll");
                    break;
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine($"[BreadWare.gg] - WAIT cs2...");
                    Thread.Sleep(4000);
                    continue;
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[BreadWare.gg] - Unknow ERROR");
                    Console.WriteLine($"[BreadWare.gg] - ERROR: {ex}");
                    Thread.Sleep(6000);
                    continue;
                }
            }
            Console.WriteLine($"[BreadWare.gg] - END attach to cs2.exe");
        }

        void Logic()
        {
            GetBase();
            while (true)
            {
                NoFlash();
                Bhop();
                EntityTEST();
            }
        }

        // functions
        void NoFlash()
        {
            if (noflash)
            {
                IntPtr localPawn = mem.ReadPointer(client + 0x16C29E8);
                int flash = mem.ReadInt(localPawn + 0x1468);

                if (flash != 0)
                {
                    mem.WriteFloat(localPawn + 0x1464, noflash_alpha);
                }
            }
        }
        void Bhop()
        {
            if (bhop)
            {
                IntPtr localPawn = mem.ReadPointer(client + 0x16C29E8);
                int fFlag = mem.ReadInt(localPawn + 0x3C8);

                if (GetAsyncKeyState(0x20))
                {
                    if (fFlag == 65665 || fFlag == 65667)
                    {
                        Thread.Sleep(1);
                        mem.WriteInt(client + 0x16BBE50, 65537);
                    }
                    else
                    {
                        mem.WriteInt(client + 0x16BBE50, 256);
                    }
                }
                Thread.Sleep(5);
            }
        }
        void EntityTEST()
        {
            for (int i = 0; i < 64; i++)
            {
                IntPtr Entity = mem.ReadPointer(client + 0x17BB470);

                IntPtr listEntity = mem.ReadPointer(Entity + (8 * (i & 0x7FFF) >> 9) + 16);
                if (listEntity == 0) continue;

                IntPtr entityController = mem.ReadPointer(listEntity + (120) * (i & 0x1FF));
                if (entityController == 0) continue;

                IntPtr entityControllerPawn = mem.ReadPointer(entityController + 0x7EC);
                if (entityControllerPawn == 0) continue;

                IntPtr entityPawn = mem.ReadPointer(listEntity + (120) * (entityControllerPawn & 0x1FF));
                if (entityPawn == 0) continue;

                IntPtr entityAddress = mem.ReadPointer(entityController + 0x750);

                char entityName = mem.ReadChar(entityAddress);
            }
            
        }

        static void Main(string[] args)
        {
            Ware ware = new Ware();
            ware.Start().Wait();

            Thread thread = new Thread(ware.Logic) { IsBackground = true };
            thread.Start();
        }
    }
}