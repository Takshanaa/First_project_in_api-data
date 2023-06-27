from django.shortcuts import render
import requests 

# Create your views here.
def home(request):
    url = 'https://api.thingspeak.com/channels/2191824/feeds.json?api_key=0WWQ4ZBH8X62CBTV&results=10'
    response = requests.get(url).json()
    data = response['feeds']
    a = [response['channel'] ] 
    return render(request,'home.html', {'datas': data,'cnl': a})

def chart(request):
   url = 'https://api.thingspeak.com/channels/2191824/feeds.json?api_key=0WWQ4ZBH8X62CBTV&results=10'
   response = requests.get(url).json()
   data = response['feeds']
   return render(request,'index.html', {'a': data})
