import os
import csv
import bs4
import requests
from time import sleep
from logs import logger
from email_manager.sender import EmailManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv ()
WAIT_TIME = float(os.getenv("WAIT_TIME"))
FROM_EMAIL = os.getenv("FROM_EMAIL")
FROM_EMAIL_PASSWORD = os.getenv("FROM_EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def get_clean_text (article:bs4.element.Tag, selector:str): 
    """ Get clean text from article selector

    Args:
        article (bs4.element.Tag): bs5 tag of the article found
        selector (str): css selector

    Returns:
        str: text clean of the tag
    """
    
    return article.select(selector)[0].text.replace("\n", "").strip()

def checker (): 
    """ Check for new articles and send email if there are new articles """
    
    # Instance for submit emails
    email = EmailManager (FROM_EMAIL, FROM_EMAIL_PASSWORD)
    
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
        article_link = article.select("a")[0]["href"]
        article_price = get_clean_text(article, "figure.mb15 > span.grid_onsale")
        article_name = get_clean_text(article, ".grid_row_info > h3")
        article_date = get_clean_text (article, ".date_for_grid > span.date_ago")
        
        # Merge data and validate if it is new
        article_data = [article_link, article_price, article_name, article_date]
        if article_data not in history:
            new_articles.append(article_data)
            
        # Debug articles scraped
        logger.debug (f"article scraped: {article_name} ({article_date}) - {article_link}")
            
    # Show status of the new articles found
    logger.info (f"new articles found: {len(new_articles)}")
        
    # Validate new articles  
    if new_articles:
        
        # Save new articles in history
        with open (history_path, "a", encoding="utf-8", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(new_articles)
        
        # Submit email with new articles data
        logger.info (f"Sending email to: {TO_EMAIL}")
        body = ""
        for article in new_articles:
            body += f"{article[2].title()} \nPrice: {article[1]} \nDate: {article[3]} \nLink: {article[0]}\n\n"
        email.send_email (receivers=[TO_EMAIL], subject=f"{len(new_articles)} New offers found", body=body)
        
if __name__ == "__main__":
    # Main loop
    while True:
        checker()
        logger.info ("waiting for next check...")
        sleep(WAIT_TIME*60)