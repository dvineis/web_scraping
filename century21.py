import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content
""" test url """
#print(c)
""" Beautify the html so it can be readable """
soup=BeautifulSoup(c, "html.parser")
""" check to make sure page loads correctly """
#print(soup.prettify())

all=soup.find_all("div",{"class":"propertyRow"})
## check if results match page 
#print(len(all))
""" this is a python string """
### extract prices #################
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ", ""))
## using the replace to remove white space and returns.

##### loop though all elements #######
for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ", ""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span", {"class":"infoBed"}).find("b").text)
    except:
        #pass #this will go to the next iteration in the loop
        print(None)

    try:
        print(item.find("span", {"class":"infoSqFt"}).find("b").text)
    except:
        #pass #this will go to the next iteration in the loop
        print(None)

    try:
        print(item.find("span", {"class":"infoValueFullBath"}).find("b").text)
    except:
        #pass #this will go to the next iteration in the loop
        print(None)

    try:
        print(item.find("span", {"class":"infoValueHalfBath"}).find("b").text)
    except:
        #pass #this will go to the next iteration in the loop
        print(None)
    #### create special loop to extract a specific item that has the same class as other items
    for column_group in item.find_all("div", {"class":"columnGroup"}):
        #print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),column_group.find_all("span", {"class":"featureName"})):
            #print(feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    print(" ")



