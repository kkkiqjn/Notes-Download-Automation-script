
import os
import googleapiclient.discovery
import pytube
import time
import re
import gdown
api_key='replace your api key'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" 

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Define the function to retrieve the video description
def get_video_description(video_id):
    # Make a request to the API to get the video details
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    # Extract and return the video description
    items = response["items"]
    if items:
        return items[0]["snippet"]["description"]
    else:
        return "Video not found."



def playlst(link):
    vids=pytube.Playlist(link)
    ids=[]
    for video in vids.videos:
        ids.append(video.video_id)
    return ids    

def notes_link(desc):
    st=desc
    newst=((st.split('Link:'))[1])

    return newst.split("\n\n")[0].strip()

ids=playlst("https://youtube.com/playlist?list=PLDzeHZWIZsTpukecmA2p5rhHM14bl2dHU")
print(len(ids))
descs=[]
for id in ids[1:-1]:
    desc=get_video_description(id)
    descs.append(desc)
    time.sleep(0.5)
    print("Extracting desc")
    
links=[]
for st in descs:
    link=re.search("(?P<url>https?://drive[^\s]+)", st).group("url")
    links.append(link)
    print(link)

print(len(links))
for link in links:
    gdown.download_folder(link,quiet=True,use_cookies=False)
    time.sleep(1)
    print("Wait.......")
    
    
print("Done")    


        

