import requests,os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os
import sys

class hs_show:
   
    def __init__(self, url):
        self.url=url
        self.load_list()
        self.pick_quality()
        self.pick_method()
    class WebElementIdCompareWrapper(object):
        def __init__(self, content):
            self.content = content
            self.key = content.get_attribute('id')
        def __eq__(self, other):
            return self.key == other.key
        def __hash__(self):
            return hash(self.key)
    def load_list(self):
        options = Options()
        options.headless = True
        if getattr(sys, 'frozen', False): 
            # executed as a bundled exe, the driver is in the extracted folder
            firefox_path = os.path.join(os.getcwd(),r'geckodriver.exe')
            geckodriver_path = firefox_path
            self.browser = webdriver.Firefox(r'E:\Visual Studio\Python-Batch-Hs\VirtEnv\dist\geckodriver.exe')
        else:
            self.browser = webdriver.Firefox(options=options,executable_path= os.getcwd() + r'\geckodriver.exe')
        self.browser.get(self.url)
        while True:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "show-more")))
            element.click()
            if (len(element.find_elements_by_css_selector("*"))<=0):
                break
        episodes= self.browser.find_elements_by_class_name('rls-info-container')
        wts = set(self.WebElementIdCompareWrapper(episode) for episode in episodes)
        episodes = [wte.content for wte in wts]
        episodes.sort(key= lambda id: id.get_attribute('id'))
        self.episodes = episodes
    def pick_quality(self):
        while True :
            print('''Choose the quality you want (input the number): \n
                 1.) 480p \n
                 2.) 720p \n
                 3.) 1080p \n ''')
            choice = input()
            if int(choice)<4 and int(choice)>0:
                break
        quality_list = ['480p','720p','1080p']
        self.quality = 'link-' + quality_list[int(choice)-1]
    def pick_method(self):
        while True :
            print('''Choose the method you want to download with (input the number): \n
                 #Only magnet link available for now \n
                 1.) Magnet \n
                ''')
            choice = input()
            if int(choice)<2 and int(choice)>0:
                break
        method_list = ['Magnet']
        self.method = 'hs-'+method_list[int(choice)-1]+'-link' 
    def get_resource_by_method(self,mini,maxi):
        self.links = []
        if mini ==0 and maxi ==0:
            for episode in self.episodes:
                epquality =episode.find_element_by_class_name(self.quality)
                dlLink = epquality.find_element_by_tag_name('a').get_attribute('href')
                self.links.append(dlLink)
        else:
            episodes=self.episodes[mini-1:maxi]
            for episode in episodes:
                epquality =episode.find_element_by_class_name(self.quality)
                dlLink = epquality.find_element_by_tag_name('a').get_attribute('href')
                self.links.append(dlLink)
                self.browser.quit()

    def save_magnetlinks_to_file(self):
        if self.url[-1] == '/':
            url = self.url[0:-1]
        else:
            url = self.url
        tempsplit = url.rsplit('/',maxsplit=1)
        showname =tempsplit[-1]
        currentDT = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        filename = "magnetlinks_" + showname +"_"+currentDT+".txt"

        
        with open(filename,'w+') as savefile:
            for link in self.links:
                savefile.write(link+"\r\n")
    
    def download_magnetlinks(self):
        for link in self.links:
            os.startfile(link)
