"""
Goal: Get every book on the website that has 2 star rating.
"""



import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

two_star_titles = []   
for page_num in range(1,51):
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text,"lxml")
    products = soup.select(".product_pod")
    for book in products:
        if len(book.select(".star-rating.Two")) != []:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)
print(*two_star_titles,sep= "\n")