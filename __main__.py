import os
import csv
import bs4
import requests
from logs import logger

def get_clean_text (article, selector): 
    return article.select(selector)[0].text.replace("\n", "").strip()

def main (): 
    
    # get page content
    page = "https://couponscorpion.com/"
    res = requests.get(page)
    res.raise_for_status()
    logger.debug (f"page scraped code: {res.status_code}")
    
    # parse page content
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    articles = soup.select('div[data-template="compact_grid"] > article')
    
    # Open and read history file
    history_path = os.path.join (os.path.dirname(__file__), "history.csv")
    with open (history_path, encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        history = list(csv_reader)
    
    # Loop for each article found
    new_articles = []
    for article in articles:
        
        # Get articles data
        article_image = article.select("a > img")[0]["data-src"]
        article_price = get_clean_text(article, "figure.mb15 > span.grid_onsale")
        article_name = get_clean_text(article, ".grid_row_info > h3")
        article_date = get_clean_text (article, ".date_for_grid > span.date_ago")
        
        # Merge data and validate if it is new
        article_data = [article_image, article_price, article_name, article_date]
        if article_data not in history:
            new_articles.append(article_data)
            
        # Debug articles scraped
        logger.debug (f"article scraped: {article_name} ({article_date})")
            
    # Show status of the new articles found
    logger.info (f"new articles found: {len(new_articles)}")
        
    # Validate new articles  
    if new_articles:
        
        # Save new articles in history
        with open (history_path, "w", encoding="utf-8", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(new_articles)
        
            
        # TODO: Submit email with new articles data
        
        
        
        
if __name__ == "__main__":
    main()