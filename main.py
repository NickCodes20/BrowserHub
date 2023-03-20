import customtkinter
import os
import bhubfuncs

bhf = bhubfuncs.BhubFunctionality()

# TODO add option to choose size of window upon launch for each browser, Full Screen (default), iPad, or Mobile
# TODO ^^^ this could be done by changing the checkboxes to dropdown arrows, and having checkbox options for sizes

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# TKinter arguments
PRIMARY = "#2e3034"
ACCENT = "#4f535a"
HOVER_COLOR = "#1e2c40"

root = customtkinter.CTk()
root.title("BrowserHub")
root.iconbitmap("Internet-Explorer.ico")

if os.name == "nt":  # Windows OS window size
    root.geometry("400x450")
elif os.name == "posix":  # macOS window size
    root.geometry("500x500")

check_chrome = customtkinter.BooleanVar()
check_firefox = customtkinter.BooleanVar()
check_edge = customtkinter.BooleanVar()
check_brave = customtkinter.BooleanVar()
check_opera = customtkinter.BooleanVar()
check_safari = customtkinter.BooleanVar()
select_all_var = customtkinter.BooleanVar()

checkbox_variables = [check_chrome, check_firefox, check_edge, check_brave, check_opera]


def select_all(checkboxes):
    """Toggles all checkboxes on or off"""
    for checkbox in checkboxes:
        for checkvar in checkbox_variables:
            if not checkvar.get():
                checkbox.toggle()
            else:
                checkbox.toggle()

# TODO if a box is already checked it should be left on when switch is activated
# TODO when switch is deactivated it should uncheck all boxes
# TODO if box is already unchecked then it should stay off when switch is deactivated


frame = customtkinter.CTkFrame(master=root)
frame.grid(pady=20, padx=60, rowspan=1, columnspan=1)

label = customtkinter.CTkLabel(master=frame, text="Select Browsers", font=("Sans Serif", 24))
label.grid(pady=12, padx=10, row=0, column=0, columnspan=2, sticky="nsew")

# Chrome's checkbox
chromebox = customtkinter.CTkCheckBox(master=frame, text="Chrome", command=bhf.append_chrome, variable=check_chrome)
chromebox.configure(command=lambda: bhf.append_chrome(check_chrome.get()))
chromebox.grid(pady=12, padx=10, row=2, column=0)
# Chrome's drop down menu
chromedrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                         button_color=ACCENT, dropdown_fg_color=PRIMARY,
                                         dropdown_hover_color=HOVER_COLOR)
chromedrop.grid(pady=12, padx=10, row=2, column=1)

# Firefox's checkbox
foxbox = customtkinter.CTkCheckBox(master=frame, text="Firefox", command=bhf.append_firefox, variable=check_firefox)
foxbox.configure(command=lambda: bhf.append_firefox(check_firefox.get()))
foxbox.grid(pady=12, padx=10)
# Firefox's drop down menu
foxdrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                      button_color=ACCENT, dropdown_hover_color=HOVER_COLOR)
foxdrop.grid(pady=12, padx=10, row=3, column=1)

# Edge's checkbox
edgebox = customtkinter.CTkCheckBox(master=frame, text="Edge", command=bhf.append_edge, variable=check_edge)
edgebox.configure(command=lambda: bhf.append_edge(check_edge.get()))
edgebox.grid(pady=12, padx=10)
# Edge's drop down menu
edgedrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                       button_color=ACCENT, dropdown_hover_color=HOVER_COLOR)
edgedrop.grid(pady=12, padx=10, row=4, column=1)

# Brave's checkbox
bravebox = customtkinter.CTkCheckBox(master=frame, text="Brave", command=bhf.append_brave, variable=check_brave)
bravebox.configure(command=lambda: bhf.append_brave(check_brave.get()))
bravebox.grid(pady=12, padx=10)
# Brave's drop down menu
bravedrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                        button_color=ACCENT, dropdown_hover_color=HOVER_COLOR)
bravedrop.grid(pady=12, padx=10, row=5, column=1)

# Opera's checkbox
operabox = customtkinter.CTkCheckBox(master=frame, text="Opera", command=bhf.append_opera, variable=check_opera)
operabox.configure(command=lambda: bhf.append_opera(check_opera.get()))
operabox.grid(pady=12, padx=10)
# Opera's drop down menu
operadrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                        button_color=ACCENT, dropdown_hover_color=HOVER_COLOR)
operadrop.grid(pady=12, padx=10, row=6, column=1)

# Safari's checkbox
if os.name == "posix":  # Only adds safari checkbox to macOS
    safaribox = customtkinter.CTkCheckBox(master=frame, text="Safari", command=bhf.append_safari,
                                          variable=check_safari)
    safaribox.configure(command=lambda: bhf.append_safari(check_safari.get()))
    safaribox.grid(pady=12, padx=10)
    # Safari's drop down menu
    safaridrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                             button_color=ACCENT, dropdown_hover_color=HOVER_COLOR)
    safaridrop.grid(pady=12, padx=10, row=7, column=1)


# Checkbox List
all_checkboxes = [chromebox, foxbox, edgebox, bravebox, operabox]  # Add safaribox

select_all_switch = customtkinter.CTkSwitch(master=frame, switch_width=40, switch_height=20, border_width=2,
                                            corner_radius=10, progress_color="green", text="Select All",
                                            command=select_all, variable=select_all_var)
select_all_switch.configure(command=lambda: select_all(all_checkboxes))
select_all_switch.grid(pady=12, padx=10)

# Launch button launches all browsers that have been selected via checkbox
button = customtkinter.CTkButton(master=frame, text="Launch", command=bhf.launch)
button.grid(pady=12, padx=10, columnspan=2, sticky="nsew")

root.mainloop()
