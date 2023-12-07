# [BreadWare.gg]
#   [external]


# [libs]
import dearpygui.dearpygui as dpg
import webbrowser as web

dpg.create_context()
dpg.create_viewport(title="[BreadWare.gg] - Counter-Strike 2", width=400, height=325, always_on_top=True, resizable=False)

with dpg.window(tag="main"):
    with dpg.tab_bar():
        with dpg.tab(label="General"):
            dpg.add_slider_float(label="NoFlash", min_value=0, max_value=255, width=200, tag="alpha")
        
        with dpg.tab(label="Info"):
            dpg.add_text("Information")
            dpg.add_separator()
            dpg.add_text("[BreadWare.gg] - free cheat for cs2,")
            dpg.add_text("with open source.")
            dpg.add_text("It is a russian project.")
            dpg.add_text("More information in the Discord.")
            dpg.add_text("")
            dpg.add_text("Links:")
            dpg.add_button(label="GitHub", callback=lambda: web.open("https://github.com/bread2288/BreadWare.gg/tree/main"))
            dpg.add_button(label="Discord", callback=lambda: web.open("https://discord.gg/kZP2Xw9TNw"))
            dpg.add_button(label="yougame", callback=lambda: web.open("https://yougame.biz/"))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main", True)

dpg.start_dearpygui()