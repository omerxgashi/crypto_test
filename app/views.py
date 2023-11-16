from django.shortcuts import render
import requests
import json
def index(request):
    api_url = "https://api.coincap.io/v2/assets"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        # assets = data.get()
        assets = data.get('data')
        context = {
            'assets': assets,
            "data":data,
        }
    else:
        print("Failed to retrieve data. Status code:", response.status_code) #200
        context = {}
    return render(request, 'a.html', context)