import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO rename project to "WindowPain"?

# TODO ask user if they're working out of a folder structure, if so change localhost to folder_structured_localhost var
# TODO ^^^ accomplish this by using a checkbox
class BhubFunctionality:

    def __init__(self):
        self.chrome_driver = webdriver.Chrome
        self.fox_driver = webdriver.Firefox
        self.edge_driver = webdriver.Edge
        self.localhost = "http://127.0.0.1:5500/index.html"
        self.folder_structured_localhost = "http://127.0.0.1:5500/html/index.html"
        self.processes = []
        self.desktop = "--start-maximized"
        self.tablet = "--window-size=1200,800"
        self.mobile = "--window-size=400,800"
        self.size_menu = {"Desktop": self.desktop, "Tablet": self.tablet, "Mobile": self.mobile}
        self.window_size = self.size_menu["Desktop"]  # SUBJECT TO CHANGE
        self.browser_dict = {}

    home_dir = os.path.expanduser("~")
    if os.name == "nt":  # Windows
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        opera = os.path.join(home_dir, "AppData", "Local", "Programs", "Opera", "Launcher.exe")
        # safari = os.path.join(home_dir, "Applications", "Safari.app")
    elif os.name == "posix":  # Mac or Linux
        chrome = os.path.join(home_dir, "Applications", "Google Chrome.app")
        firefox = os.path.join(home_dir, "Applications", "Firefox.app")
        edge = os.path.join(home_dir, "Applications", "Microsoft Edge.app")
        brave = os.path.join(home_dir, "Applications", "Brave Browser.app")
        opera = os.path.join(home_dir, "Applications", "Opera.app")
        safari = os.path.join(home_dir, "Applications", "Safari.app")

    # TODO if browser is not installed ask user if they want to install it, launch default browser with link to install
    def launch(self):
        """Launches browsers from the browser list."""
        if self.browser_dict:
            for browser, path in self.browser_dict.items():
                if os.path.exists(path[0]):
                    process = subprocess.Popen(path)
                    self.processes.append(process)
                    print(f"Launch Successful: {browser}")
                else:
                    print(f"{browser} is not installed")
        else:
            print("Please select a browser.")

    def update_window_size(self, size):
        for browser in self.browser_dict:
            if size == "Desktop":
                self.window_size = self.size_menu["Desktop"]
                self.browser_dict[browser][1] = self.window_size
                print(f"{browser} size: {self.browser_dict[browser][1]}")
            elif size == "Tablet":
                self.window_size = self.size_menu["Tablet"]
                self.browser_dict[browser][1] = self.window_size
                print(f"{browser} size: {self.browser_dict[browser][1]}")
            elif size == "Mobile":
                self.window_size = self.size_menu["Mobile"]
                self.browser_dict[browser][1] = self.window_size
                print(f"{browser} size: {self.browser_dict[browser][1]}")

    # TODO create functions to add screen sizes to OptionMenu, options should be named "Desktop", "Tablet", and "Mobile"
    def append_chrome(self, box_value, size):  # CAN THIS CONDENS INTO update_window_size() to prevent error when unchecked?
        """Appends Chrome browser to browser list """
        if box_value is True:
            self.browser_dict["Chrome"] = [self.chrome, size, self.localhost]
            self.update_window_size(size)
        elif box_value is False:
            del self.browser_dict["Chrome"]
            # print(f"Chrome Size: {size}")
        print(self.browser_dict)

    def append_firefox(self, box_value, size):
        """Appends Firefox browser to browser list """
        if box_value is True:
            self.browser_dict["Firefox"] = [self.firefox, size, self.localhost]
        elif box_value is False:
            del self.browser_dict["Firefox"]
        print(self.browser_dict)

    def append_edge(self, box_value, menu_var):
        """Appends Edge browser to browser list """
        if box_value is True:
            self.browser_dict["Edge"] = [self.edge, menu_var, self.localhost]
        elif box_value is False:
            del self.browser_dict["Edge"]
        print(self.browser_dict)

    def append_brave(self, box_value, menu_var):
        """Appends Brave browser to browser list """
        if box_value is True:
            self.browser_dict["Brave"] = [self.brave, menu_var, self.localhost]
        elif box_value is False:
            del self.browser_dict["Brave"]
        print(self.browser_dict)

    def append_opera(self, box_value, menu_var):
        """Appends Opera browser to browser list """
        if box_value is True:
            self.browser_dict["Opera"] = [self.opera, menu_var, self.localhost]
        elif box_value is False:
            del self.browser_dict["Opera"]
        print(self.browser_dict)

    def append_safari(self, box_value, menu_var):
        """Appends Safari browser to browser list """
        if box_value is True:
            self.browser_dict["Safari"] = [self.safari, menu_var, self.localhost]
        elif box_value is False:
            del self.browser_dict["Safari"]
        print(self.browser_dict)

    def prime_for_launch(self):
        pass
