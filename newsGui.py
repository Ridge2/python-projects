from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk

def scrape_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure successful request
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract headlines (customize based on website structure)
        headlines = soup.find_all('h2')  # Replace 'h2' with the appropriate tag/class
        return [headline.get_text(strip=True) for headline in headlines]
    except Exception as e:
        return [f"Error scraping {url}: {e}"]
    
def display_news(news_list):
    for i, news in enumerate(news_list):
        text_area.insert(tk.END, f"{i + 1}. {news}\n")

# Initialize GUI
root = tk.Tk()
root.title("News Scraper")

frame = ttk.Frame(root, padding=10)
frame.grid()

# Input field for URL
url_label = ttk.Label(frame, text="Enter News Website URL:")
url_label.grid(row=0, column=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=0, column=1)

# Text area to display news
text_area = tk.Text(frame, width=70, height=20, wrap='word')
text_area.grid(row=2, column=0, columnspan=2, pady=10)

# Button to fetch news
def fetch_news():
    url = url_entry.get()
    if url:
        news = scrape_news(url)
        text_area.delete(1.0, tk.END)  # Clear previous results
        display_news(news)

fetch_button = ttk.Button(frame, text="Fetch News", command=fetch_news)
fetch_button.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()