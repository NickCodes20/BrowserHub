import subprocess
import os


class BhubFunctionality:

    home_dir = os.path.expanduser("~")
    if os.name == "nt":  # Windows
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        opera = os.path.join(home_dir, "AppData", "Local", "Programs", "Opera", "Launcher.exe")
    elif os.name == "posix":  # Mac or Linux
        chrome = os.path.join(home_dir, "Applications", "Google Chrome.app")
        firefox = os.path.join(home_dir, "Applications", "Firefox.app")
        edge = os.path.join(home_dir, "Applications", "Microsoft Edge.app")
        brave = os.path.join(home_dir, "Applications", "Brave Browser.app")
        opera = os.path.join(home_dir, "Applications", "Opera.app")
        # safari = os.path.join(home_dir, "Applications", "Safari.app")

    localhost = "http://127.0.0.1:5500/index.html"
    folder_structured_localhost = "http://127.0.0.1:5500/html/index.html"

    processes = []

    browser_list = []

    # TODO tweak launch() code to check if browser is installed, if so then launch it
    def launch(self):
        """Launches browsers from the browser list."""
        if self.browser_list:
            for browser in self.browser_list:
                process = subprocess.Popen(browser)
                self.processes.append(process)
            print("Launch Successful")
        else:
            print("Please select a browser.")

    def append_chrome(self, box_value):
        """Appends Chrome browser to browser list """
        if box_value is True:
            self.browser_list.append([self.chrome, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.chrome, self.localhost])
        print(self.browser_list)

    def append_firefox(self, box_value):
        """Appends Firefox browser to browser list """
        if box_value is True:
            self.browser_list.append([self.firefox, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.firefox, self.localhost])
        print(self.browser_list)

    def append_edge(self, box_value):
        """Appends Edge browser to browser list """
        if box_value is True:
            self.browser_list.append([self.edge, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.edge, self.localhost])
        print(self.browser_list)

    def append_brave(self, box_value):
        """Appends Brave browser to browser list """
        if box_value is True:
            self.browser_list.append([self.brave, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.brave, self.localhost])
        print(self.browser_list)

    def append_opera(self, box_value):
        """Appends Opera browser to browser list """
        if box_value is True:
            self.browser_list.append([self.opera, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.opera, self.localhost])
        print(self.browser_list)

    def append_safari(self, box_value):
        """Appends Safari browser to browser list """
        if box_value is True:
            self.browser_list.append([self.safari, self.localhost])
        elif box_value is False:
            self.browser_list.remove([self.safari, self.localhost])
        print(self.browser_list)
