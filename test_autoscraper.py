from autoscraper import AutoScraper

url = "https://www.thestar.com.my/"

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["After-hours bargains in JB"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
