import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a request to the website
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find all book containers
books = soup.find_all('article', class_='product_pod')

# Step 3: Create a CSV file to store the data
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability'])

    # Step 4: Extract data for each book
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

        writer.writerow([title, price, availability])

print("Data scraped and saved to books.csv")