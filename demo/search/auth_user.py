from google_auth_oauthlib import flow
import googleapiclient.discovery 



def fun_aut_user():
    launch_browser = True
    api_service_name = "youtube"
    api_version = "v3"
    # scopes = ["https://www.googleapis.com/auth/youtube",
    #       "https://www.googleapis.com/auth/youtube.force-ssl",
    #       "https://www.googleapis.com/auth/youtubepartner"]
    scopes =["https://www.googleapis.com/auth/youtubepartner", "https://www.googleapis.com/auth/youtube"]
    

    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        '/home/jesus/ProyectosDjango/DemoApiYtDjango/demo/search/client_secret.json', scopes
    )
    appflow.run_console()
    # if launch_browser:
    #     appflow.run_local_server()
    # else:
    #     appflow.run_console()

    credentials = appflow.credentials
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return youtube
    