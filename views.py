from django_media.models import MediaGallery 
from django.shortcuts import render, get_object_or_404

def view(request, media_gallery_id):
    gallery = get_object_or_404(MediaGallery, pk=media_gallery_id)   
    return render(request, 'gallery/view.html', {'gallery': gallery})