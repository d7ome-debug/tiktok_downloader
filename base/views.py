import os
import requests
from django.shortcuts import render
from .forms import VideoForm

def download_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['url']
            response = requests.get(video_url)
            if response.status_code == 200:
                video_name = os.path.basename(video_url)
                # Save the video to your media directory
                video_path = os.path.join('media', video_name)
                with open(video_path, 'wb') as f:
                    f.write(response.content)
                return render(request, 'base/download_success.html', {'video_path': video_path})
            else:
                return render(request, 'base/download_error.html')
    else:
        form = VideoForm()
    return render(request, 'base/download_form.html', {'form': form})

