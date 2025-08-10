import requests
result = requests.get("https://example.com")
#print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")
#print(soup)
#print(soup.select("title")[0].getText())
print() 
#print(soup.select("p"))


req = requests.get("https://simple.wikipedia.org/wiki/Grace_Hopper")
soup1 = bs4.BeautifulSoup(req.text,"lxml")
print()
#print(soup1.select(".vector-toc-text"))
#for item in soup1.select(".vector-toc-text"):
    #print(item.getText())

res = requests.get("https://simple.wikipedia.org/wiki/Picture")
soup = bs4.BeautifulSoup(res.text,"lxml")
print()
item = soup.select(".mw-file-element")[0]
img_link = requests.get("https:" + item["src"])
with open("E:\Python_Programs\WebsiteImage1.jpg","wb") as file1:
    file1.write(img_link.content)
