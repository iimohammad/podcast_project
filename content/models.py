from django.db import models
from django.contrib.auth.models import User

# class Episode(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     audio_file = models.FileField(upload_to='podcasts')
#     publish_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     channel = models.ForeignKey('Channel', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
