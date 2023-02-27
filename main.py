import subprocess
import customtkinter

# Browser path's
chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# Host address's
localhost = "http://127.0.0.1:5500/index.html"
folder_structured_localhost = "http://127.0.0.1:5500/html/index.html"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

check_chrome = customtkinter.BooleanVar()
check_firefox = customtkinter.BooleanVar()
check_edge = customtkinter.BooleanVar()

processes = []

browser_list = []


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

# Launch button launches all browsers that have been selected via checkbox
button = customtkinter.CTkButton(master=frame, text="Launch", command=launch)
button.pack(pady=12, padx=10)

root.mainloop()
