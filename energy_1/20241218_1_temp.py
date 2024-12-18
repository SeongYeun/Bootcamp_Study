# 라이브러리
import pandas as pd
import folium, requests
from folium.plugins import HeatMap
from geojson import Feature, FeatureCollection, Point

# 산불 정보 읽어오기기
api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
params={
    'category':'wildfires',
    'status':"open",
    'days':"1"
}
def get_wildfires_data(api_url):
    url = api_url
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None

data = get_wildfires_data(api_url)
print(data)


