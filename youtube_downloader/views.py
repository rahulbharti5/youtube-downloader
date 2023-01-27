# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
  
  
# defining function
def youtube(request):
  
    # checking whether request.method is post or not
    if request.method == 'POST':
        
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        
        urls = []
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
        for s in video.streams.filter(progressive=True):
        # for s in video.streams:
            print(s)
            urls.append(s)
        
        # # downloads video
        # # stream.download()
  
        # # returning HTML page
        return render(request, 'youtube1.html',{"urls":urls,"title":video.title,"thumb":video.thumbnail_url})
    return render(request, 'youtube1.html')

