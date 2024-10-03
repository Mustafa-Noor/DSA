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

# Function to scrape movie data
def scrape_movies(url, page):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find_all('div', class_='movieInfo')

    if not movies:
        print(f"No movies found on page {page}.")
        return []

    movie_data = []
    for movie in movies:
        try:
            # Extract the required movie attributes
            title = movie.find('span', itemprop='name').get_text(strip=True)
            release_year = movie.find('a', class_='chartsYear').get_text(strip=True)
            duration = movie.find('span', class_='minutes').get_text(strip=True).replace(',', '').strip()
            director = movie.find('a', href=lambda x: x and 'director=' in x).get_text(strip=True)
            main_cast = ', '.join([actor.get_text(strip=True) for actor in movie.find_all('a', href=lambda x: x and 'actor=' in x)])
            genres = ', '.join([genre.get_text(strip=True) for genre in movie.find_all('a', href=lambda x: x and 'genre=' in x)])

            # Streaming availability
            streaming_services = []
            itunes = movie.find('a', id='iTunesButton')
            if itunes:
                streaming_services.append('iTunes')
            netflix = movie.find('a', id='netflixButton')
            if netflix:
                streaming_services.append('Netflix')
            amazon = movie.find('a', id=lambda x: x and 'amazonButtonImage' in x)
            if amazon:
                streaming_services.append('Amazon.com')
            streaming_availability = ', '.join(streaming_services)

            movie_data.append({
                'Title': title,
                'Release Year': release_year,
                'Duration': duration,
                'Director': director,
                'Main Cast': main_cast,
                'Genres': genres,
                'Streaming Availability': streaming_availability
            })
        except Exception as e:
            print(f"Error processing a movie: {e}")

    return movie_data

# Open CSV file to write
try:
    with open('allMovies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Release Year', 'Duration', 'Director', 'Main Cast', 'Genres', 'Streaming Availability']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write header only once

        number_of_pages = 5  # Adjust based on how many pages you need
        for page in range(1, number_of_pages + 1):
            try:
                url = f'https://www.flickchart.com/charts.aspx?perpage=50000&page={page}'  # Replace with actual movie listing page URL
                movies = scrape_movies(url, page)
                for movie in movies:
                    writer.writerow(movie)
                    csvfile.flush()  # Flush data to file immediately after each write
            except Exception as e:
                print(f"Error on page {page}: {e}")
                continue  # Skip to the next page if there's an error

except KeyboardInterrupt:
    print("Scraping interrupted, saving progress...")

finally:
    driver.quit()  # Ensure the driver quits when the script ends
    print("Driver closed.")
