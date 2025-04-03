import os
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import Counter
import schedule # type: ignore
import time

# Websites to scrape
SITES = {
    "BleepingComputer": "https://www.bleepingcomputer.com/",
    "DarkReading": "https://www.darkreading.com/",
    "HackerNews": "https://news.ycombinator.com/"
}

# Function to scrape headlines

def scrape_news():
    articles = []
    for site, url in SITES.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if "bleepingcomputer" in url:
            news_items = soup.select('.bc_latest_news .bc_latest_news_text a')
        elif "darkreading" in url:
            news_items = soup.select('.listingNews .articleTitle a')
        elif "hackernews" in url:
            news_items = soup.select('.athing .titleline a')
        else:
            news_items = []
        
        for item in news_items[:10]:  # Limit to top 10 per site
            title = item.get_text()
            link = item['href']
            articles.append((title, link))
    
    return articles

# Function to filter top articles

def filter_top_articles(articles):
    title_counts = Counter([title for title, _ in articles])
    top_articles = [article for article in articles if title_counts[article[0]] > 1]
    return top_articles[:10]  # Limit to 10 articles

# Function to send email

def send_email(articles):
    sender_email = "sfrandsen@ceriumnetworks.com"
    receiver_email = "soc_team@ceriumnetworks.com"
    password = "Yk27x93d3292"  # Consider using environment variables
    print(f"Sender Email: {sender_email}")
    print(f"Receiver Email: {receiver_email}")
    print(f"Password: {'SET' if password else 'NOT SET'}")  # Hides actual password for security

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Cybersecurity News Update"
    
    html_content = """
    <html>
    <body>
        <h2>Today's Top Cybersecurity News</h2>
        <ul>
    """
    for title, link in articles:
        html_content += f'<li><a href="{link}">{title}</a></li>'
    
    html_content += """
        </ul>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule the script to run at 3 PM MST

if __name__ == "__main__":
    articles = scrape_news()
    top_articles = filter_top_articles(articles)
    send_email(top_articles)
