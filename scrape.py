import requests
from bs4 import BeautifulSoup
import pprint
a=True
while a==True:
    print('Enter the page number:')
    i=input()

    res=requests.get('https://news.ycombinator.com/news?p='+i)
    soup=BeautifulSoup(res.text,'html.parser')
    links=soup.select('.storylink')
    subtext=soup.select('.subtext')

    def create_custom_hn(links,subtext):
        hn=[]
        for idx,item in enumerate(links):
            title=links[idx].getText()
            href=links[idx].get('href',None)
            vote=subtext[idx].select('.score')
            if len(vote):
                points=int(vote[0].getText().replace(' points'," "))
            if points>99:
                hn.append({'title':title,'link':href,'votes':points})
        return sort_stories_by_votes(hn)

    def sort_stories_by_votes(hnlst):
         return sorted(hnlst,key=lambda k:k['votes'],reverse=True)


    new_hn=create_custom_hn(links, subtext)
    #print(new_hn)
    for element in new_hn:
        for j in element:
            print(j+":"+str(element.get(j)))
        print('------------------------')
    print("Are you done reading[y/n]")
    if(input()=='y'):
        print('Ok!Byee')
        print('------------------------')
        break
    else:
        print('------------------------')
        continue



