import customtkinter
import os
import bhubfuncs


bhf = bhubfuncs.BhubFunctionality()

# TODO edge and firefox are not respecting the window size feature, troubleshoot
# TODO add refresh all feature
# TODO ask for user input to add custom URL to launch
# TODO add feature to open inspector upon launch

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
    root.geometry("400x350")
elif os.name == "posix":  # macOS window size
    root.geometry("400x400")

check_chrome = customtkinter.BooleanVar()
check_firefox = customtkinter.BooleanVar()
check_edge = customtkinter.BooleanVar()
check_safari = customtkinter.BooleanVar()
select_all_var = customtkinter.BooleanVar()

chrome_menu_var = customtkinter.StringVar()
chrome_menu_var.set(list(bhf.size_menu.keys())[0])
firefox_menu_var = customtkinter.StringVar()
firefox_menu_var.set(list(bhf.size_menu.keys())[0])
edge_menu_var = customtkinter.StringVar()
edge_menu_var.set(list(bhf.size_menu.keys())[0])
safari_menu_var = customtkinter.StringVar()
safari_menu_var.set(list(bhf.size_menu.keys())[0])

checkbox_variables = [check_chrome, check_firefox, check_edge]


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
chromebox.configure(command=lambda: bhf.append_chrome(check_chrome.get(), bhf.size_menu[chrome_menu_var.get()]))
chromebox.grid(pady=12, padx=10, row=2, column=0)
# Chrome's drop down menu
chromedrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                         button_color=ACCENT, dropdown_fg_color=PRIMARY,
                                         dropdown_hover_color=HOVER_COLOR, variable=chrome_menu_var,
                                         command=lambda value: bhf.update_chrome_size(value))
chromedrop.grid(pady=12, padx=10, row=2, column=1)

# Firefox's checkbox
foxbox = customtkinter.CTkCheckBox(master=frame, text="Firefox", command=bhf.append_firefox, variable=check_firefox)
foxbox.configure(command=lambda: bhf.append_firefox(check_firefox.get(), bhf.size_menu[firefox_menu_var.get()]))
foxbox.grid(pady=12, padx=10)
# Firefox's drop down menu
foxdrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                      button_color=ACCENT, dropdown_fg_color=PRIMARY,
                                      dropdown_hover_color=HOVER_COLOR, variable=firefox_menu_var,
                                      command=lambda value: bhf.update_fox_size(value))
foxdrop.grid(pady=12, padx=10, row=3, column=1)

# Edge's checkbox
edgebox = customtkinter.CTkCheckBox(master=frame, text="Edge", command=bhf.append_edge, variable=check_edge)
edgebox.configure(command=lambda: bhf.append_edge(check_edge.get(), bhf.size_menu[edge_menu_var.get()]))
edgebox.grid(pady=12, padx=10)
# Edge's drop down menu
edgedrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                       button_color=ACCENT, dropdown_fg_color=PRIMARY,
                                       dropdown_hover_color=HOVER_COLOR, variable=edge_menu_var,
                                       command=lambda value: bhf.update_edge_size(value))
edgedrop.grid(pady=12, padx=10, row=4, column=1)

# Safari's checkbox
if os.name == "posix":  # Only adds safari checkbox to macOS
    safaribox = customtkinter.CTkCheckBox(master=frame, text="Safari", command=bhf.append_safari,
                                          variable=check_safari)
    safaribox.configure(command=lambda: bhf.append_safari(check_safari.get(), bhf.size_menu[safari_menu_var.get()]))
    safaribox.grid(pady=12, padx=10)
    # Safari's drop down menu
    safaridrop = customtkinter.CTkOptionMenu(master=frame, values=list(bhf.size_menu.keys()), fg_color=PRIMARY,
                                             button_color=ACCENT, dropdown_fg_color=PRIMARY,
                                             dropdown_hover_color=HOVER_COLOR, variable=safari_menu_var)
    safaridrop.grid(pady=12, padx=10, row=7, column=1)


# Checkbox List
all_checkboxes = [chromebox, foxbox, edgebox]  # Add safaribox

select_all_switch = customtkinter.CTkSwitch(master=frame, switch_width=40, switch_height=20, border_width=2,
                                            corner_radius=10, progress_color="green", text="Select All",
                                            command=select_all, variable=select_all_var)
select_all_switch.configure(command=lambda: select_all(all_checkboxes))
select_all_switch.grid(pady=12, padx=10)

# Launch button launches all browsers that have been selected via checkbox
button = customtkinter.CTkButton(master=frame, text="Launch", command=bhf.launch)
button.grid(pady=12, padx=10, columnspan=2, sticky="nsew")

root.mainloop()
