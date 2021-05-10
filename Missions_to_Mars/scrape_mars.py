# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # splinter
    executable_path = {'executable_path': '/desktop/web-scraping-challenge/Mission_to_Mars/chromedriver'}
    return Browser('chrome', **executable_path headless=False)

def scrape():
    # News Titles
    mars_browser = init_browser()
    mars_collection = {}

    # Url
        url = "https://mars.nasa.gov/news/"
        mars_browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve the most recent article's title and paragraph.
    # Store in news variables.
    news_title = news_soup.find("div", class_="content_title").find('a').text
    news_paragraph = news_soup.find("div", class_="article_teaser_body").get_text()
    # Exit Browser.
        mars_browser.quit()

    # Print Title and Text.
    print(f'Title: {news_title}\nText: {news_paragraph}')

##Mars Space Images

#Run init_browser/ChromeDriverManager
mars_browser = init_browser
# Visit the url
space_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
mars_browser.visit(space_image_url)

#select "Full IMAGE"
mars_browser.visit(space_image_url )

# Find "more info" for first image, set to variable, and command click.
mars_browser.is_element_present_by_text("more info", wait_time=1)
more_info_element = mars_browser.find_link_by_partial_text("more info")
more_info_element.click()

# HTML Object.
html = mars_browser.html

# Parse HTML with Beautiful Soup
mars_image_soup = BeautifulSoup(html, "html.parser")

#Scrape image
mars_image_url = mars_image_soup.find('figure', class_='lede'.a ['href'])


# Concatentate https://www.jpl.nasa.gov with image_url.
  featured_image_url = f'https://www.jpl.nasa.gov{image_url}'
# Exit Browser.
 mars_browser.quit

# Print Faetured Image URL.
   print(featured_image_url)

   # Run init_browser/driver.
       mars_browser = init_browser()

       # Visit the url for USGS Astrogeology.
       astrogeology_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
       mars_browser.visit(astrogeo_url)

       # HTML Object.
       html = mars_browser.html

       # Parse HTML with Beautiful Soup
       astrogeology_soup = BeautifulSoup(html, "html.parser")

       # Store main URL in a variable so that 'href' can be appended to it after each iteration.
       main_astrogeology_url = "https://astrogeology.usgs.gov"

       # Each link is located in 'div' tag, class "item".
       # Locate all 4 and store in variable.
       hems_url = astrogeology_soup.find_all("div", class_="item")

       # Create empty list for each Hemisphere URL.
       hemis_url = []


       for hem in hems_url:
           hem_url = hem.find('a')['href']
           hemis_url.append(hem_url)

        mars_browser.quit

        # Create list of dictionaries called hemisphere_image_urls.
        # Iterate through all URLs saved in hemis_url.
        # Concatenate each with the main_astrogeo_url.
        # Confirm the concat worked properly: confirmed.
        # Visit each URL.

        hemisphere_image_urls = []
            for hemi in hemis_url:
            hem_astrogeology_url = main_astrogeology_url + hemi
            print(hem_astrogeology_url)

        #Run init_browser/driver.
        mars_browser = init_browser()
        mars_browser.visit(hem_astrogeology_url)

       # HTML Object.
       html = mars_browser.html

       # Parse HTML with Beautiful Soup
       hemisphere_soup = BeautifulSoup(html, "html.parser")
       # Locate each title and save to raw_title, to be cleaned.
           raw_title = hemisphere_soup.find("h2", class_="title").text

           # Remove ' Enhanced' tag text from each "title" via split on ' Enhanced'.
           title = raw_title.split(' Enhanced')[0]

           # Locate each 'full.jpg' for all 4 Hemisphere URLs.
           img_url = hemisphere_soup.find("li").a['href']

           # Append both title and img_url to 'hemisphere_image_url'.
           hemisphere_image_urls.append({'title': title, 'img_url': img_url})

           browser.quit()

print(hemisphere_image_urls)

##Mars Data Dictionary -mongodb
all_mars_data = {}

# Append news_title and news_paragraph to mars_data.
all_mars_data['news_title'] = news_title
all_mars_data['news_paragraph'] = news_paragraph

# Append featured_image_url to mars_data.
all_mars_data['featured_image_url'] = featured_image_url

# Append mars_weather to mars_data.
all_mars_data['mars_weather'] = mars_weather

# Append hemisphere_image_urls to mars_data.
all_mars_data['hemisphere_image_urls'] = hemisphere_image_urls
all_mars_data

print("Scrape Complete!!!")

    return mars_data
