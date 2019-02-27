import requests,os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from validator_collection import checkers
from hs_show_file import hs_show
url = 'https://horriblesubs.info/shows/black-clover'

# class WebElementIdCompareWrapper(object):
#     def __init__(self, content):
#         self.content = content
#         self.key = content.get_attribute('id')
#     def __eq__(self, other):
#         return self.key == other.key
#     def __hash__(self):
#         return hash(self.key)



print('''Input a link to one of the show listings on horriblesubs.info\n
    The format is "https://horriblesubs.info/shows/show-name/"''')

url = input('URL : ')
# while not checkers.is_url(url):
#     print('Not a url, input a proper url:')
#     url=input('URL : ')
current_show_instance = hs_show(url)
while True:
    print('''Save to text file or start downloading(input number)?:/n
            1.)Save to Text File /n
            2.)Start Downloading''')
    choice = input()
    if (int(choice)>0 and int(choice)<3) :
        break
if int(choice) == 1 :
    print(f'Found {len(current_show_instance.episodes)} episodes')
    mini = 0
    maxi = 0
    while True:
        print('Enter the span of episodes you wish to save to file, inclusive bound, format = "min,max", enter 0 for all')
        ranges = input()
        rangelist = ranges.split(',')
        if int(rangelist[0]) == 0:
            current_show_instance.get_resource_by_method(0,0)
            current_show_instance.save_magnetlinks_to_file()
            break
        mini = int(rangelist[0])
        maxi= int(rangelist[1])
        if len(rangelist)==2 and mini > 0 and maxi<len(current_show_instance.episodes) :
            current_show_instance.get_resource_by_method(mini,maxi)
            current_show_instance.save_magnetlinks_to_file()    
            break
    
else :
    print(f'Found {len(current_show_instance.episodes)} episodes')
    mini = 0
    maxi = 0
    while True:
        print('Enter the span of episodes you wish to download, inclusive bound, format = "min,max", enter 0 for all')
        ranges = input()
        rangelist = ranges.split(',')
        if int(rangelist[0]) == 0:
            current_show_instance.get_resource_by_method(0,0)
            current_show_instance.download_magnetlinks()
            break
        mini = int(rangelist[0])
        maxi= int(rangelist[1])
        if len(rangelist)==2 and mini > 0 and maxi<=len(current_show_instance.episodes) :
            current_show_instance.get_resource_by_method(mini,maxi)
            current_show_instance.download_magnetlinks()
            break
