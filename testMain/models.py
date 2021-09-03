from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from hashlib import md5
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from testMain.API.utilis import create_shortened_url
class Url_service(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    short_url= models.CharField(max_length=200,blank=True ,unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.short_url
    def clicked(self):
        self.clicks += 1
        self.save()
    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
