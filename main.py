import customtkinter
import bhubfuncs

bhf = bhubfuncs.BhubFunctionality()

# TODO add safari
# TODO tweak launch function to check if checked browsers are installed before launching
# TODO if browser is not installed ask user if they want to install it, and launch default browser with link to install
# TODO add option to choose size of window upon launch for each browser, Full Screen (default), iPad, or Mobile
# TODO add functionality to be compatible across operating systems

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
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
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Select Browsers", font=("Sans Serif", 24))
label.pack(pady=12, padx=10)

# Chrome's checkbox
chromebox = customtkinter.CTkCheckBox(master=frame, text="Chrome", command=bhf.append_chrome, variable=check_chrome)
chromebox.configure(command=lambda: bhf.append_chrome(check_chrome.get()))
chromebox.pack(pady=12, padx=10)

# Firefox's checkbox
foxbox = customtkinter.CTkCheckBox(master=frame, text="Firefox", command=bhf.append_firefox, variable=check_firefox)
foxbox.configure(command=lambda: bhf.append_firefox(check_firefox.get()))
foxbox.pack(pady=12, padx=10)

# Edge's checkbox
edgebox = customtkinter.CTkCheckBox(master=frame, text="Edge", command=bhf.append_edge, variable=check_edge)
edgebox.configure(command=lambda: bhf.append_edge(check_edge.get()))
edgebox.pack(pady=12, padx=10)

# Brave's checkbox
bravebox = customtkinter.CTkCheckBox(master=frame, text="Brave", command=bhf.append_brave, variable=check_brave)
bravebox.configure(command=lambda: bhf.append_brave(check_brave.get()))
bravebox.pack(pady=12, padx=10)

# Opera's checkbox
operabox = customtkinter.CTkCheckBox(master=frame, text="Opera", command=bhf.append_opera, variable=check_opera)
operabox.configure(command=lambda: bhf.append_opera(check_opera.get()))
operabox.pack(pady=12, padx=10)

# Safari's checkbox
# safaribox = customtkinter.CTkCheckBox(master=frame, text="Safari", command=bhf.append_safari, variable=check_safari)
# safaribox.configure(command=lambda: bhf.append_safari(check_safari.get()))
# safaribox.pack(pady=12, padx=10)

# Checkbox List
all_checkboxes = [chromebox, foxbox, edgebox, bravebox, operabox] # Add safaribox

select_all_switch = customtkinter.CTkSwitch(master=frame, switch_width=40, switch_height=20, border_width=2,
                                            corner_radius=10, progress_color="green", text="Select All",
                                            command=select_all, variable=select_all_var)
select_all_switch.pack(pady=12, padx=10)
select_all_switch.configure(command=lambda: select_all(all_checkboxes))

select_all_switch.pack()

# Launch button launches all browsers that have been selected via checkbox
button = customtkinter.CTkButton(master=frame, text="Launch", command=bhf.launch)
button.pack(pady=12, padx=10)

root.mainloop()
