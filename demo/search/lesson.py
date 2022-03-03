from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['http://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

playlist_id: 'PL3DaZVxO6YJM1n6PI2nkYbM6SUudSqphM'

response = service.playlistItems().list(
    part = 'contentDetails',
    playListId = playlist_id,
    maxResults=9
).execute()

playlistItems = response['items']

print(playlistItems)