import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    time.sleep(3)  # Wait for the page to load

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find_all('div', class_='movieDetails')  # Update this to match the provided HTML structure

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

            # Get only the first actor
            main_cast = movie.find_all('a', href=lambda x: x and 'actor=' in x)
            first_actor = main_cast[0].get_text(strip=True) if main_cast else ''  # Get the first actor's name

            # Extract genres and split into two columns
            genres = [genre.get_text(strip=True) for genre in movie.find('p', class_='genre').find_all('a', class_='filterLink')]
            genre_1 = genres[0] if len(genres) > 0 else ''  # First genre
            genre_2 = genres[1] if len(genres) > 1 else ''  # Second genre

            movie_data.append({
                'Title': title,
                'Release Year': release_year,
                'Duration': duration,
                'Director': director,
                'Main Cast': first_actor,
                'Genre 1': genre_1,
                'Genre 2': genre_2
            })
        except Exception as e:
            print(f"Error processing a movie: {e}")

    return movie_data

# Open CSV file to write
try:
    with open('final.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Release Year', 'Duration', 'Director', 'Main Cast', 'Genre 1', 'Genre 2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write header only once

        number_of_pages = 3  # Adjust based on how many pages you need
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
