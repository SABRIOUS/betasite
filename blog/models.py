from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = datetime.now()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]

    def date_pretty(self):
        return self.date.strftime('%b %e %Y')
