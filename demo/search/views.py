from multiprocessing import context
from urllib import response
import requests
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from . import auth_user


# objet youtube auth
youtube = auth_user.fun_aut_user()



def index(request):
    
    videos = []
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        s_params = {
            'part' : 'snippet',
            'q' : request.POST['search']+'karaoke',
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video',
        }
        video_ids = []
        r = requests.get(search_url, params=s_params)
        print(request)
        results = r.json()['items']
        
        for result in results:
            video_ids.append(result['id']['videoId'])

        
        v_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9,
        }

        r = requests.get(video_url, params=v_params)

        results = r.json()['items']

        print(results[0]['contentDetails']['licensedContent'])

        for result in results:
            video_data = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"] }',
                #'url' : f'https://www.youtube.com/embed/{ result["id"] }',
                'duration' :parse_duration(result['contentDetails']['duration']).total_seconds()//60,
                'thumbnail': result['snippet']['thumbnails']['high']['url'],
                'licencia' : result['contentDetails']['licensedContent'],
            }

            videos.append(video_data)
    
    context = {
        'videos' : videos 
    }

    return render(request, 'search/index.html', context)

def listV(request, video_id):

    requests = youtube.playlistItems().insert(
        part="snippet",
        body={
             'snippet': {
                  #id de play list de tu lista
                  'playlistId': 'PL3DaZVxO6YJMfDRl0cPrzIAEO67eQIrhD', 
                  'resourceId': {
                          'kind': 'youtube#video',
                          'videoId': video_id,
                   },
                  #'position': 0
                }
        }
    ).execute()
    print(requests)
    
    return render(request,'search/list.html')
