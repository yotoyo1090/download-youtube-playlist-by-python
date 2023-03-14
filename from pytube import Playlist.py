from pytube import Playlist
import pytube 

# where to save 
SAVE_PATH = "G:/" #to_do 

p = Playlist('youtube playlist link')
for url in p.video_urls[236:238]: #list select
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = pytube.YouTube(url)
    except: 
        print("Connection Error") #to handle exception 
    
    # filters out all the files with "mp4" extension 
    mp4files = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    
    yt.title
    
    # get the video with the extension and
    # resolution passed in the get() function 
   
    try: 
        # downloading the video 
        mp4files.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
        
        
    print('Task Completed!') 
        
    
    print(url)