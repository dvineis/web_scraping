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

#### empty list to store dictionary ####
l=[]
##### loop though all elements #######
for item in all:
    ## start each iteration with empty dictionary
    d={}
    d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
    d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ", "")
    try:
        d["Beds"]=item.find("span", {"class":"infoBed"}).find("b").text
    except:
        #pass #this will go to the next iteration in the loop
        d["Beds"]=None

    try:
        d["Area"]=item.find("span", {"class":"infoSqFt"}).find("b").text
    except:
        #pass #this will go to the next iteration in the loop
        d["Area"]=None

    try:
        d["Full Baths"]=item.find("span", {"class":"infoValueFullBath"}).find("b").text
    except:
        #pass #this will go to the next iteration in the loop
        d["Full Baths"]=None

    try:
        d["Half Baths"]=item.find("span", {"class":"infoValueHalfBath"}).find("b").text
    except:
        #pass #this will go to the next iteration in the loop
        d["Half Baths"]=None
    #### create special loop to extract a specific item that has the same class as other items
    for column_group in item.find_all("div", {"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),column_group.find_all("span", {"class":"featureName"})):
            #print(feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    ## append the dictionaries to the empty list
    l.append(d)
    ##### insert data into a data frame #####
    import pandas
    df=pandas.DataFrame(l)
    # print dataframe
    print(df)

    """ output to a csv file """
    df.to_csv("Output.csv")



