import googlemaps
import requests
import sys
import json

gmaps = googlemaps.Client(key='AIzaSyBXSUnZz0d00Noy_GZo5Hin7kHbaQiOKkU')

# Request address from user
address = input('address: ')
# for example, address = '1600 Amphitheatre Parkway, Mountain View, CA'

# Get Place ID
get_place_id = gmaps.find_place(address, input_type='textquery')
# print(get_place_id)

# parse place ID JSON response
place_id = json.dumps(get_place_id['candidates'][0]['place_id'])
# print(place_id)

# Get Place Details, removing quote marks for compatibility with googlemaps library
get_place_details = gmaps.place(place_id.strip('\"'))
# Get address_component a few levels above city - generally county or township
place_details = json.dumps(get_place_details['result']['address_components'][3]['short_name'])
# print(place_details)

# Get News
url = ('https://newsapi.org/v2/everything?' +
       'q=' + 
       place_details +
       '&' +
       'from=2018-11-26&' +
       'sortBy=popularity&' +
       'apiKey=c552ee53c272469e818b73b18c7be26a')

r = requests.get(url).json()
news1 = r['articles'][0]['title']
news2 = r['articles'][1]['title']
news3 = r['articles'][2]['title']
news4 = r['articles'][3]['title']
news5 = r['articles'][4]['title']

print(news1)
print(news2)
print(news3)
print(news4)
print(news5)
