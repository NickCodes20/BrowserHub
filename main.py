import subprocess

chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

dev_server = "http://127.0.0.1:5500/index.html"

browser_list = [
    [chrome, dev_server],
    [firefox, dev_server],
    [edge, dev_server],
]

processes = []

for browser in browser_list:
    process = subprocess.Popen(browser)
    processes.append(process)
