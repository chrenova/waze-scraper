import requests
import json
import datetime
import os

URL = 'https://www.waze.com/row-rtserver/web/TGeoRSS?ma=600&mj=100&mu=0&left=16.93&right=17.25&bottom=48.08&top=48.25'
DATA_HOME = '~/data'


def main():
    headers = {
        'Host': 'www.waze.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.waze.com/livemap',
    }

    response = requests.get(URL, headers=headers)
    print(response)
    data = response.json()

    datestring = datetime.datetime.today().strftime('%Y/%m/%d')
    name = 'waze.%s.json' % data['startTimeMillis']
    path = '{}/{}/{}'.format(DATA_HOME, datestring, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        print('Usage: python -m waze_scraper')
        exit(1)
    main()
