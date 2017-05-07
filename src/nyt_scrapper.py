from nytimesarticle import articleAPI
api = articleAPI('5f5e542cc9de4c45a7583aaae28a293d')
import requests
import json
import datetime as dt

def date_to_string(some_date):
    '''converts date format into string
    so the api can accept it
    '''
    y = str(some_date.year)
    m = str(some_date.month)
    d = str(some_date.day)
    if len(m) == 1:
         m = '0' + m
    if len(d) == 1:
        d = '0' + d
    return(y+m+d)

def get_todays_news():
    '''Hits the NY Times api, and pulls down a JSON of articles for each day
    '''  
    today = dt.date.today()
    yesterday = today -dt.timedelta(1)
    today_string = date_to_string(today)
    yesterday_string = date_to_string(yesterday)
    articles = api.search(begin_date = yesterday_string, end_date=today_string)
    with open ('articles', 'w') as f:
        json.dump(articles, f)       

if __name__ == '__main__':
    print 'scrapping'
