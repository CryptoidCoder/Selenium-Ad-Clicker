import random
import requests
import re
import os
import subprocess
import time
import numpy as np
import pandas as pd
import socket
import speedtest
st = speedtest.Speedtest()
import http.client as httplib
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import undetected_chromedriver as uc
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity


# Gets new useragents # https://pypi.org/project/random-user-agent/
software_names = [SoftwareName.CHROME.value, SoftwareName.EDGE.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
operating_systems = [OperatingSystem.WINDOWS.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100) #popularity=popularity
user_agent = user_agent_rotator.get_random_user_agent()


print("Starting Bot", flush=True)

# Change this to your own domain (without https)
URL = 'http://example.com'


# Gets the available proposals
s = subprocess.Popen(["/opt/myst/myst connection proposals --location-type residential"], shell=True, stdout=subprocess.PIPE).stdout
proposals = s.read().splitlines()
del proposals[0]

# gets a random node that is not in the blacklist file (slow shitty nodes)
def Random_Node():
    random_node = proposal_list[random.randrange(len(proposal_list))] # pulls random mysterium node

    Blacklisted_Nodes_File = open("/root/Dockerdata/blacklist.txt", "r")
    Blacklisted_Nodes = Blacklisted_Nodes_File.read()

    while random_node in Blacklisted_Nodes:
        random_node = proposal_list[random.randrange(len(proposal_list))] # pulls random mysterium node
    return random_node


# sanitizes myst servers
proposal_list = []
for x in proposals:
    x = str(x)
    x = x.replace("b'| Identity: ", '')
    x = x[:42]

    proposal_list.append(x)


def Run_Selenium():
    # Sets up random information for browsers
    List_Of_Displays = {1: (1366, 768), 2: (1920, 1080), 3: (1536, 864), 4: (1440, 900), 5: (
        1280, 720), 6: (1600, 900), 7: (1280, 800), 8: (1280, 1024), 9: (1024, 768), 10: (768, 1024)}
    List_Of_Locals = {}

    #Random_Display_Size = random.randrange(1,11)
    #display = Display(visible=0, size=(1366, 768)) #List_Of_Displays.get(Random_Display_Size)[0], print(List_Of_Displays.get(Random_Display_Size)[1])))
    #display = Display(visible=0, size=(1024, 768))
    #display.start()

    # Selenium settings
    opts = uc.ChromeOptions()
    opts.add_argument('--disable-extensions')
    opts.add_argument('--profile-directory=Default')
    opts.add_argument("--incognito")
    opts.add_argument("--disable-plugins-discovery")
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument('--enable-javascript')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--ignore-certificate-errors')  # says its unsupported
    driver = uc.Chrome(use_subprocess=True, options=opts) # version_main=100, 
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {
                           "userAgent": user_agent})
    driver.delete_all_cookies()
    driver.set_window_size(random.randrange(360, 1440),
                           random.randrange(640, 1080))  # changes window size
    driver.set_window_position(0, 0)

    #driver.manage().timeouts().pageLoadTimeout(4, TimeUnit.SECONDS);

    driver.get(URL)  # go to url
    driver.implicitly_wait(10)  # seconds
    driver.find_element(By.XPATH, '/html/body/a').click()
    #driver.find_element_by_xpath('/html/body/a').click()  # deprecated

    driver.close()
    driver.quit()

    # display.stop()


# Uses speedtest to rank node
def have_internet():
    if st.download() > 10000000:
        return True
    else:
        return False



if __name__ == "__main__":
    # does loop to switch Nodes and uses selenium to click ad links
    while True == True:

        #gets new node
        random_node = Random_Node()
        Temp_Random_Node = Random_Node()

        print("Running new myst session", flush=True)
        os.system("/opt/myst/myst connection down")  # stops vpn
        time.sleep(2)
        os.system(str("/opt/myst/myst connection up " + Temp_Random_Node))  # starts new connection with node
        time.sleep(2)

        print("Going to try to run selenium", flush=True)
        time.sleep(random.randrange(1, 5)) # 4, 305 # amount of time to wait before loading the page again

        Connected = have_internet()
        print("Connected is "+ str(Connected), flush=True)
        
        if Connected == False:
            print("Failed to connect to " + Temp_Random_Node + " moving on anyway and adding it to the blacklist", flush=True)
            print("Failed network check")
            os.system("echo " + Temp_Random_Node + " >> /root/Dockerdata/blacklist.txt")
        
        if Connected == True:
                Run_Selenium()
                print("Just ran a successful run of selenium", flush=True)