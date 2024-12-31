import requests
import tkinter as tk
from tkinter import ttk, messagebox


# Function to fetch news using NewsAPI
def fetch_news(api_key, country):
    url = f"https://newsapi.org/v2/top-headlines"
    params = {"country": country, "apiKey": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        messagebox.showerror("Error", f"Failed to fetch news: {response.status_code}")
        return []


# Function to display news in the GUI
def display_news():
    country = country_input.get().strip().lower()
    if not country:
        messagebox.showwarning("Input Error", "Please enter a country code (e.g., us, gb, in).")
        return

    articles = fetch_news(API_KEY, country)
    if not articles:
        messagebox.showinfo("No News", "No news articles found for the selected country.")
        return

    # Clear existing items in the Treeview
    for item in news_tree.get_children():
        news_tree.delete(item)

    # Populate the Treeview with news articles
    for article in articles:
        title = article.get("title", "N/A")
        source = article.get("source", {}).get("name", "N/A")
        url = article.get("url", "N/A")
        news_tree.insert("", "end", values=(title, source, url))


# Constants
API_KEY = "REPLACE WITH YOUR API"  # Replace with your actual API key

# GUI Setup
root = tk.Tk()
root.title("News Scraper by Country")

# Input for country
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Enter Country Code:").grid(row=0, column=0, padx=5, pady=5)
country_input = tk.Entry(frame)
country_input.grid(row=0, column=1, padx=5, pady=5)

# Fetch News Button
fetch_button = tk.Button(root, text="Fetch News", command=display_news)
fetch_button.pack(pady=10)

# Treeview to display news
columns = ("Title", "Source", "URL")
news_tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
news_tree.heading("Title", text="Title")
news_tree.heading("Source", text="Source")
news_tree.heading("URL", text="URL")
news_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Make columns stretchable
for col in columns:
    news_tree.column(col, stretch=tk.YES)

# Start the Tkinter event loop
root.mainloop()