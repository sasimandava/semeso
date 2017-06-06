from django.shortcuts import render
import requests
from collections import OrderedDict
import logging
import random
"""
semeso=send me something.
When a user clicks on "Semeso" button on home page,
current news in different categories are displayed.
Each category has a list of source apis out of which
one api is selected randomly and urls are displayed.

"""

# Logging to an output file in write mode.
log_level = logging.DEBUG
format = '%(asctime)s %(levelname)s - %(module)8s - line:%(lineno)d - %(message)s'
logging.basicConfig(filename='semeso.log',
                    filemode='w',  # use 'a' if you want to preserve the old log file
                    format=format,
                    level=log_level)

def index(request):
    return render(request, 'udemy_first_app/index.html')

#NEWS APIs
news_google_api = "https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
news_cnn_api = "https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
news_bbc_api = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
news_ap_api = "https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
news_apis_list = [news_google_api, news_cnn_api, news_bbc_api, news_ap_api]

#FINANCE APIs
finance_cnbc_api = "https://newsapi.org/v1/articles?source=cnbc&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
finance_businessinsider_api = "https://newsapi.org/v1/articles?source=business-insider&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
finance_bloomberg_api = "https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
finance_apis_list = [finance_cnbc_api, finance_businessinsider_api, finance_bloomberg_api]

#SPORTS APIs
sports_espn_api = "https://newsapi.org/v1/articles?source=espn&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
sports_espn_cricinfo_api = "https://newsapi.org/v1/articles?source=espn-cric-info&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
sports_football_italia_api = "https://newsapi.org/v1/articles?source=football-italia&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
sports_apis_list = [sports_espn_api, sports_espn_cricinfo_api, sports_football_italia_api]

#ENTERTAINMENT APIs
entertainment_mashable_api = "https://newsapi.org/v1/articles?source=mashable&sortBy=latest&apiKey=febb4153f6374f69885c2c58fdd101d6"
entertainment_buzzfeed_api = "https://newsapi.org/v1/articles?source=buzzfeed&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
entertainment_apis_list = [entertainment_mashable_api, entertainment_buzzfeed_api]

#TECHNOLOGY APIs
technology_techradar_api = "https://newsapi.org/v1/articles?source=techradar&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
technology_engadget_api = "https://newsapi.org/v1/articles?source=engadget&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
technology_the_verge_api = "https://newsapi.org/v1/articles?source=the-verge&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
technology_apis_list = [technology_techradar_api, technology_engadget_api, technology_the_verge_api]

#GAMING APIs
gaming_polygon_api = "https://newsapi.org/v1/articles?source=polygon&sortBy=top&apiKey=febb4153f6374f69885c2c58fdd101d6"
gaming_apis_list = [gaming_polygon_api]

#ALL APIs
all_apis_dict = OrderedDict([('News',random.choice(news_apis_list)),
                             ('Finance',random.choice(finance_apis_list)),
                             ('Sports',random.choice(sports_apis_list)),
                             ('Entertainment',random.choice(entertainment_apis_list)),
                             ('Technology',random.choice(technology_apis_list)),
                             ('Gaming',random.choice(gaming_apis_list))])


def semeso_news(request):
    """Send me something """
    if request.method == "GET":
        try:
            all_semeso_dict = OrderedDict()
            for category,api in all_apis_dict.items():
                response = requests.get(api)
                js = response.json()
                all_semeso_dict[category] = [[article['url'], article['urlToImage']] for article in js['articles']]
        except requests.exceptions.ConnectionError:
            all_semeso_dict = {'Error':'Connection Error'}
            return render(request, 'udemy_first_app/semeso_error.html', {'all_semeso_dict':all_semeso_dict})
        logging.debug("This is what a user gets: {}".format(all_semeso_dict))
        return render(request, 'udemy_first_app/semeso.html', {'all_semeso_dict':all_semeso_dict})
    else:
        context_dict = {'Error':'Connection Error'}
        return render(request, 'udemy_first_app/semeso_error.html', {'all_semeso_dict':context_dict})
