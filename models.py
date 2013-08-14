from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from wand.image import Image
import os

# Create your models here.
class Media(models.Model):
    MEDIA_TYPES = (
        ('Image', 'Image'),
        )
    title = models.CharField(_('title'), max_length=200)
    description = models.CharField(_('description'), max_length=255)
    type = models.CharField(_('type of media'), max_length=100, choices=MEDIA_TYPES, default='Image')
    media = models.FileField(_('file'),upload_to='gallery_images', max_length=150)
    pub_date = models.DateTimeField(('date published'), auto_now=True)
    owner = models.ForeignKey(User, related_name='attached_media', unique=False)
    
    
    class Meta:
        db_table = 'django_media'
        verbose_name = _('Media Resource')
        verbose_name_plural = _('Media Resources')
        
    def __str__(self):
        return self.title
    
    defwidth = 100
    defheight = 100
    
    def cacheUrl(self, width, height):
        
        if(width is None):
            width = self.defwidth
        if(height is None):
            height = self.defheight
        #@todo: make these dynamic via settings
        imageUrl = ('').join([settings.MEDIA_ROOT, self.media.name])
        name = str(width) + '_' + str(height) + '-' + self.media.name.split('/')[-1]
        print(name)
        smallImagePath = ('').join([settings.MEDIA_ROOT, 'cache/', name])
        smallImageUrl = 'cache/' + name
        print(imageUrl)
        print(smallImageUrl)
        if os.path.isfile( smallImagePath ):
            return smallImageUrl
        else:
            print('File Does Not exist')
            with Image(filename=imageUrl) as img:
                with img.clone() as i:
                    i.transform(resize=str(width)+'x'+str(height)+'^')
                    left = 0
                    top = 0
                    if ( i.width > width ):
                        left = ( i.width - width ) / 2
                    if ( i.height > height ):
                        top = ( i.height - height ) / 2
                    i.crop(int(left), int(top), width=width, height=height)
                    i.save(filename=smallImagePath)
            return smallImageUrl
    
class MediaGallery(models.Model):
    title = models.CharField(_('title'), max_length=200)
    description = models.CharField(_('description'), max_length=255)
    type = models.CharField(_('gallery type'), max_length=100)
    gallery_users = models.ManyToManyField(User, related_name='shared_gallery')
    gallery_admins = models.ManyToManyField(User, related_name='adminable_gallery')
    media = models.ManyToManyField(Media, related_name='attached_media')
    pub_date = models.DateTimeField(('date published'))
    is_private = models.BooleanField(_('is private'))
    
    class Meta:
        verbose_name = _('Media Gallery')
        verbose_name_plural = _('Media Galleries')
        
    def __str__(self):
        return self.title
