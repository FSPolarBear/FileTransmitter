from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, FileResponse
import os
# Create your views here.

def list_files():
    result = []
    if not os.path.exists('files'):
        return result
    files = os.listdir('files')
    for file in files:
        path = f'files/{file}'
        if os.path.isfile(path):
            result.append(file)
    return result

def home(request):
    context = {'files': list_files()}
    return render(request, 'home.html', context)

def upload(request):
    try:
        file = request.FILES.get('uploader')
        name = file.name
        if not os.path.exists('files'):
            os.makedirs('files', exist_ok=True)
        path = f'files/{name}'
        with open(path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        message = 'Upload succeed'

    except:
        message = 'Upload failed'

    messages.error(request, message)
    return redirect(reverse('main:home'))



DIR_FILES = os.path.abspath('files')

def download(request, file):
    try:
        path = f'files/{file}'
        # This prevents downloading a file that is not in the "files" folder by "..".
        if os.path.dirname(os.path.abspath(path)) != DIR_FILES:
            raise Exception()
        response = FileResponse(open(path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = f'attachment; filename={file}'
        return response
    except:
        messages.error(request, 'Download failed')
        return redirect(reverse('main:home'))