// [BreadWare.gg]

#include <iostream>
#include <thread>
#include <Windows.h>

int witdh = 1280;
int height = 800;

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	switch (message)
	{
	case WM_CREATE:
	{
		SetWindowLong(hwnd, GWL_STYLE, GetWindowLong(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED);

		SetLayeredWindowAttributes(hwnd, RGB(255, 255, 255), 0, LWA_COLORKEY);

		break;
	}
	case WM_ERASEBKGND:
	{
		return TRUE;
	}

	case WM_PAINT:
	{
		PAINTSTRUCT ps;
		HDC hdc = BeginPaint(hwnd, &ps);

		SetBkMode(hdc, TRANSPARENT);
		HBRUSH brush = CreateSolidBrush(RGB(255, 255, 255));
		FillRect(hdc, &ps.rcPaint, brush);

		DeleteObject(brush);



		EndPaint(hwnd, &ps);

		InvalidateRect(hwnd, 0, TRUE);

		break;
	}

	case WM_DESTROY:
	{
		PostQuitMessage(0);
	}

	default:
	{
		return DefWindowProc(hwnd, message, wParam, lParam);
	}
	}
}

int __stdcall WinMain(HINSTANCE instance, HINSTANCE pInstance, LPSTR lpCmd, int cmdShow)
{
	const char* CLASS_NAME = "window class";

	WNDCLASSEX wc = { };

	wc.cbSize = sizeof(WNDCLASSEX);

	wc.lpfnWndProc = WndProc;
	wc.lpszClassName = CLASS_NAME;
	wc.hInstance = instance;
	wc.style = CS_HREDRAW | CS_VREDRAW;

	RegisterClassEx(&wc);

	HWND hwnd = CreateWindowEx( 0, CLASS_NAME, "esp cs2",
		WS_EX_TRANSPARENT | WS_EX_TOPMOST, CW_USEDEFAULT, CW_USEDEFAULT,
		witdh,
		height,
		NULL,
		NULL,
		instance,
		NULL
	);

	if (hwnd == NULL)
	{
		return 1;
	}

	SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE);

	ShowWindow(hwnd, cmdShow);

	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
}