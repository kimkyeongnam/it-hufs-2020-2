import os
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import json
import re

# get target tree pest encyclopedia
def get_target_url(treePestList):
    def hangul(text):
        pattern = re.compile(r'\s+')
        res = re.sub(pattern, '', text)
        return res

    for bug in treePestList:
        base_url = 'https://terms.naver.com/search.nhn?query=' + bug + '&searchType=&dicType=&subject='
        req = requests.get(base_url)
        soup = BeautifulSoup(req.content, "html.parser")
        candidates = soup.select('div.info_area > div.subject')[0]
        test = candidates.get_text()
        print(test)
#        if candidates == bug:
#            print(bug)
        #find(class_ = 'title').get_text()
        #print(title)
        #if title == bug:
        #    print(title)

#    base_url = 'https://terms.naver.com/search.nhn?query=' + fff + '&searchType=&dicType=&subject='
#    req = requests.get(base_url)
#    soup = BeautifulSoup(req.content, "html.parser")
    
#    for tag in soup.select('li'):
#        candidate_name = hangul(tag.text)
#        if candidate_name in treePestList.keys():
#            print(candidate_name)
        #print(hangul(tag.text.replace(" ",""))
        #if hangul.sub('', tag.text) in treePestList.keys():
        #    print(tag.find_all('a'))


# get target tree pest list
def get_target_list():
    cur_path = os.getcwd() + '\crawling\\target.txt'
    file = open(cur_path, mode = 'r', encoding='utf-8')

    treePestList = defaultdict(str)
    for line in file:
        treePestList[line.strip('\n')] = []
    return treePestList

treePestList = get_target_list()

if __name__ == '__main__':
    treePestList = get_target_list()
    #treePestURLList = get_target_url(treePestList)
    get_target_url(treePestList)