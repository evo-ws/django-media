from django import template

register = template.Library()

@register.simple_tag
def image_cache_url(media, *args, **kwargs):
    """
    Takes original image url, check to see if a cache version exists
    if not it creates it and returns the url
    """
    if(kwargs['width'] is None):
        width = media.defwidth
    else:
        width = kwargs['width']
    if(kwargs['height'] is None):
        height = media.defheight
    else:
        height = kwargs['height']
   
    return media.cacheUrl(width, height)