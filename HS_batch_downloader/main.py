import requests,os,re
from bs4 import BeautifulSoup

url_clean = "https://horriblesubs.info/shows/black-clover/"

print('''Input a link to one of the show listings on horriblesubs.info\n
    The format is "https://horriblesubs.info/shows/show-name/"''')

# url = input('URL : ')
# while True:
#     print('''Save to text file or start downloading(input number)?:
#             1.)Save to Text File
#             2.)Start Downloading''')
#     choice = input()
#     if (int(choice)>0 and int(choice)<3) :
#         break

res = requests.get(url_clean)
res.raise_for_status()
soup = BeautifulSoup(res.text,features="html.parser")
temp =soup.find_all(string=re.compile("hs_showid"))
hs_showid = str(temp[0]).split('=')[1].replace(';','').strip()
url_api = "https://horriblesubs.info/api.php?method=getshows&type=show&showid=" + str(hs_showid) + "&nextid=0"
res = requests.get(url_api)
res.raise_for_status()
soup = BeautifulSoup(res.text,features="html.parser")
episodes =[]
counter = 0
while soup.text!='DONE':
    print(url_api)
    episodes += soup.select('.rls-info-container')
    counter+=1
    url_api = url_api[:-1] + str(counter)
    res = requests.get(url_api)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,features="html.parser")
minimum = int(input('min:'))
maximum = int(input('max:'))

episodes= episodes[minimum:maximum]

magnet_links = []
for episode in episodes :
    magnet_links.append(episode.select_one('.hs-magnet-link > a')['href'])
print(f'Found {len(episodes)} episodes')
    


# if int(choice) == 1 :
#     print(f'Found {len()} episodes')
#     mini = 0
#     maxi = 0
#     while True:
#         print('Enter the span of episodes you wish to save to file, inclusive bound, format = "min,max", enter 0 for all')
#         ranges = input()
#         rangelist = ranges.split(',')
#         if int(rangelist[0]) == 0:
#             current_show_instance.get_resource_by_method(0,0)
#             current_show_instance.save_magnetlinks_to_file()
#             break
#         mini = int(rangelist[0])
#         maxi= int(rangelist[1])
#         if len(rangelist)==2 and mini > 0 and maxi<len(current_show_instance.episodes) :
#             current_show_instance.get_resource_by_method(mini,maxi)
#             current_show_instance.save_magnetlinks_to_file()    
#             break
    
# else :
#     print(f'Found {len(current_show_instance.episodes)} episodes')
#     mini = 0
#     maxi = 0
#     while True:
#         print('Enter the span of episodes you wish to download, inclusive bound, format = "min,max", enter 0 for all')
#         ranges = input()
#         rangelist = ranges.split(',')
#         if int(rangelist[0]) == 0:
#             current_show_instance.get_resource_by_method(0,0)
#             current_show_instance.download_magnetlinks()
#             break
#         mini = int(rangelist[0])
#         maxi= int(rangelist[1])
#         if len(rangelist)==2 and mini > 0 and maxi<=len(current_show_instance.episodes) :
#             current_show_instance.get_resource_by_method(mini,maxi)
#             current_show_instance.download_magnetlinks()
#             break
