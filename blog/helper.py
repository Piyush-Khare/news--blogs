from django.utils.text import slugify

import string
import random

def generateRandom(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

def generateSlug(text):
    new_slug = slugify(text)
    from .models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        return generateSlug(text + generateRandom(3))
    return new_slug