import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36
#https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100
sids = [100,101,102]
base_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1='
urls = []
for i in sids:
    url = base_url + str(i)
    print(url)
    urls.append(url)
    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
res = requests.get(urls[0], headers=headers)
print(res.status_code)

soup = BeautifulSoup(res.text, 'lxml')
lists = soup.find('cluster_text_headline')



import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

# url 참고 
# https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36

sids= [100,101,102]

base_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1='

urls = []
for i in sids:
    url = base_url + str(i)
    print(url)
    urls.append(url)
    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
res = requests.get(urls[0], headers=headers)
print(res.status_code)

soup = BeautifulSoup(res.text, 'lxml')

lists = soup.find('cluster_text_headline')
