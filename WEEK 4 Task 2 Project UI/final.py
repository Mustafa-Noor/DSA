import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_service = Service('C:\\Users\\musno\\OneDrive\\Desktop\\SEMESTER 3\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Replace with your chromedriver path
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Function to scrape book data
def scrape_books(url, page):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Close popup if on page 2
    if page == 2:
        try:
            cross_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/button")
            cross_button.click()
            time.sleep(1)  # Allow time for the popup to close
        except Exception as e:
            print(f"Popup close error: {e}")

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    books = soup.find_all('tr', itemscope=True, itemtype="http://schema.org/Book")

    if not books:
        print(f"No books found on page {page}.")
        return []

    book_data = []
    for book in books:
        try:
            title = book.find('span', itemprop='name').get_text(strip=True)
            author = book.find('span', itemprop='author').get_text(strip=True)
            image_url = book.find('img', itemprop='image')['src']
            avg_rating = book.find('span', class_='minirating').get_text(strip=True).split(' — ')[0]
            ratings_count = book.find('span', class_='minirating').get_text(strip=True).split(' — ')[1]
            score = book.find('a', onclick=True).get_text(strip=True).split(': ')[1]
            voters_count = book.find('a', id=lambda x: x and 'people voted' in book.text).get_text(strip=True).split()[0]

            book_data.append({
                'Title': title,
                'Author': author,
                'Image URL': image_url,
                'Average Rating': avg_rating,
                'Ratings Count': ratings_count,
                'Score': score,
                'Voters Count': voters_count
            })
        except Exception as e:
            print(f"Error processing a book: {e}")

    return book_data

# Open CSV file to write
try:
    with open('allBooks.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Author', 'Image URL', 'Average Rating', 'Ratings Count', 'Score', 'Voters Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write header only once

        number_of_pages = 250
        for page in range(1, number_of_pages + 1):
            try:
                url = f'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page={page}'
                books = scrape_books(url, page)
                for book in books:
                    writer.writerow(book)
                    csvfile.flush()  # Flush data to file immediately after each write
            except Exception as e:
                print(f"Error on page {page}: {e}")
                continue  # Skip to the next page if there's an error

except KeyboardInterrupt:
    print("Scraping interrupted, saving progress...")

finally:
    driver.quit()  # Ensure the driver quits when the script ends
    print("Driver closed.")
