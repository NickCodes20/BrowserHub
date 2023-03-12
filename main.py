import os
import subprocess
import customtkinter

# TODO add safari
# TODO add code to check if browsers are installed on system, if so then proceed, if not then pass over them
# TODO ^^^ start this process by tweaking launch function to check if browser is installed before launching
# TODO add functionality to be compatible across operating systems
# TODO clean up code by adding a functionality class, move functions into the class and import them

home_dir = os.path.expanduser("~")

# Browser path's
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
opera = os.path.join(home_dir, "AppData", "Local", "Programs", "Opera", "Launcher.exe")

# Host address's
localhost = "http://127.0.0.1:5500/index.html"
folder_structured_localhost = "http://127.0.0.1:5500/html/index.html"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x450")

check_chrome = customtkinter.BooleanVar()
check_firefox = customtkinter.BooleanVar()
check_edge = customtkinter.BooleanVar()
check_brave = customtkinter.BooleanVar()
check_opera = customtkinter.BooleanVar()
select_all_var = customtkinter.BooleanVar()

checkbox_variables = [check_chrome, check_firefox, check_edge, check_brave, check_opera]

processes = []

browser_list = []

# TODO tweak launch() code to check if browser is installed, if so then launch it


def launch():
    """Launches browsers from the browser list."""
    if browser_list:
        for browser in browser_list:
            process = subprocess.Popen(browser)
            processes.append(process)
        print("Launch Successful")
    else:
        print("Please select a browser.")


def append_chrome(box_value):
    """Appends Chrome browser to browser list """
    if box_value is True:
        browser_list.append([chrome, localhost])
    elif box_value is False:
        browser_list.remove([chrome, localhost])
    print(browser_list)


def append_firefox(box_value):
    """Appends Firefox browser to browser list """
    if box_value is True:
        browser_list.append([firefox, localhost])
    elif box_value is False:
        browser_list.remove([firefox, localhost])
    print(browser_list)


def append_edge(box_value):
    """Appends Edge browser to browser list """
    if box_value is True:
        browser_list.append([edge, localhost])
    elif box_value is False:
        browser_list.remove([edge, localhost])
    print(browser_list)


def append_brave(box_value):
    """Appends Brave browser to browser list """
    if box_value is True:
        browser_list.append([brave, localhost])
    elif box_value is False:
        browser_list.remove([brave, localhost])
    print(browser_list)


def append_opera(box_value):
    """Appends Opera browser to browser list """
    if box_value is True:
        browser_list.append([opera, localhost])
    elif box_value is False:
        browser_list.remove([opera, localhost])
    print(browser_list)

# TODO tweak this code to check if checkbox is already checked, all boxes checked when switch is on
# TODO if switch is already on it should be left on when switch is activated
# TODO when switch is deactivated it should turn off all switches
# TODO if switch is already off then it should stay off when switch is deactivated


def select_all(checkboxes):
    for checkbox in checkboxes:
        for checkvar in checkbox_variables:
            if not checkvar.get():
                checkbox.toggle()
            else:
                checkbox.toggle()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Select Browsers", font=("Sans Serif", 24))
label.pack(pady=12, padx=10)

# Chrome's checkbox
chromebox = customtkinter.CTkCheckBox(master=frame, text="Chrome", variable=check_chrome)
chromebox.configure(command=lambda: append_chrome(check_chrome.get()))
chromebox.pack(pady=12, padx=10)

# Firefox's checkbox
foxbox = customtkinter.CTkCheckBox(master=frame, text="Firefox", command=append_firefox, variable=check_firefox)
foxbox.configure(command=lambda: append_firefox(check_firefox.get()))
foxbox.pack(pady=12, padx=10)

# Edge's checkbox
edgebox = customtkinter.CTkCheckBox(master=frame, text="Edge", command=append_edge, variable=check_edge)
edgebox.configure(command=lambda: append_edge(check_edge.get()))
edgebox.pack(pady=12, padx=10)

# Brave's checkbox
bravebox = customtkinter.CTkCheckBox(master=frame, text="Brave", command=append_brave, variable=check_brave)
bravebox.configure(command=lambda: append_brave(check_brave.get()))
bravebox.pack(pady=12, padx=10)

# Opera's checkbox
operabox = customtkinter.CTkCheckBox(master=frame, text="Opera", command=append_opera, variable=check_opera)
operabox.configure(command=lambda: append_opera(check_opera.get()))
operabox.pack(pady=12, padx=10)

all_checkboxes = [chromebox, foxbox, edgebox, bravebox, operabox]

select_all_switch = customtkinter.CTkSwitch(master=frame, switch_width=40, switch_height=20, border_width=2,
                                            corner_radius=10, progress_color="green", text="Select All",
                                            command=select_all, variable=select_all_var)
select_all_switch.pack(pady=12, padx=10)
select_all_switch.configure(command=lambda: select_all(all_checkboxes))

select_all_switch.pack()

# Launch button launches all browsers that have been selected via checkbox
button = customtkinter.CTkButton(master=frame, text="Launch", command=launch)
button.pack(pady=12, padx=10)

root.mainloop()
