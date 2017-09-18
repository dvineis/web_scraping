import requests
from bs4 import BeautifulSoup

""" load the source code """
r=requests.get("http://pythonhow.com/example.html")
""" store the content """
c=r.content

""" check to see if you are getting correct source """
#print(c)
""" beautify content """
soup=BeautifulSoup(c, "html.parser")

""" this will organize the source code """
#print(soup.prettify())
""" perform method using class or id"""
all=soup.find_all("div",{"class":"cities"})
#print(all)
""" print individual elements """
#all=soup.find("div",{"class":"cities"})
#print(all)
""" use list indexing """
#all=soup.find_all("div",{"class":"cities"})
#print(all)
""" Find specific element in a specific element, extract text"""
#title=all[0].find_all("h2")[0].text
for item in all:
    print(item.find_all("p")[0].text)

