import subprocess
import os


# TODO ask user if they're working out of a folder structure, if so change localhost to folder_structured_localhost var
# TODO ^^^ accomplish this by using a checkbox
class BhubFunctionality:

    def __init__(self):
        self.localhost = "http://127.0.0.1:5500/index.html"
        self.folder_structured_localhost = "http://127.0.0.1:5500/html/index.html"
        self.processes = []
        self.browser_dict = {}
        self.desktop = "fullscreen"
        self.tablet = "800x600"
        self.mobile = "400x800"
        self.size_menu = {"Desktop": self.desktop, "Tablet": self.tablet, "Mobile": self.mobile}

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

    # TODO create functions to add screen sizes to OptionMenu, options should be named "Desktop", "Tablet", and "Mobile"
    def append_chrome(self, box_value):
        """Appends Chrome browser to browser list """
        if box_value is True:
            self.browser_dict["Chrome"] = [self.chrome, self.localhost]
        elif box_value is False:
            del self.browser_dict["Chrome"]
        print(self.browser_dict)

    def append_firefox(self, box_value):
        """Appends Firefox browser to browser list """
        if box_value is True:
            self.browser_dict["Firefox"] = [self.firefox, self.localhost]
        elif box_value is False:
            del self.browser_dict["Firefox"]
        print(self.browser_dict)

    def append_edge(self, box_value):
        """Appends Edge browser to browser list """
        if box_value is True:
            self.browser_dict["Edge"] = [self.edge, self.localhost]
        elif box_value is False:
            del self.browser_dict["Edge"]
        print(self.browser_dict)

    def append_brave(self, box_value):
        """Appends Brave browser to browser list """
        if box_value is True:
            self.browser_dict["Brave"] = [self.brave, self.localhost]
        elif box_value is False:
            del self.browser_dict["Brave"]
        print(self.browser_dict)

    def append_opera(self, box_value):
        """Appends Opera browser to browser list """
        if box_value is True:
            self.browser_dict["Opera"] = [self.opera, self.localhost]
        elif box_value is False:
            del self.browser_dict["Opera"]
        print(self.browser_dict)

    def append_safari(self, box_value):
        """Appends Safari browser to browser list """
        if box_value is True:
            self.browser_dict["Safari"] = [self.safari, self.localhost]
        elif box_value is False:
            del self.browser_dict["Safari"]
        print(self.browser_dict)
