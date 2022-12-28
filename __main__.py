import os
import requests
import bs4
from logs import logger

def main (): 
    
    # get page content
    page = "https://couponscorpion.com/"
    res = requests.get(page)
    res.raise_for_status()
    logger.info(f"page scraped code: {res.status_code}")
    
    # parse page content
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    articles = soup.select('div[data-template="compact_grid"] > article')
    
    # Loop for each article found
    for article in articles:
        
        # Get articles data
        article_image = article.select("a > img")[0]["data-src"]
        article_price = article.select("figure.mb15 > span.grid_onsale")[0].text.replace("\n", "")
        article_name = article.select(".grid_row_info > h3")[0].text.replace("\n", "")
        article_date = article.select(".date_for_grid > span.date_ago")[0].text.replace("\n", "")

if __name__ == "__main__":
    main()