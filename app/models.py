from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    banner_photo = models.ImageField(upload_to='event_photos/')
    heading_photo = models.ImageField(upload_to='event_photos/')
    description = models.TextField()
    other_photos = models.ManyToManyField('Photos', related_name='event_photos', null=True, blank=True)
    youtube_video_url = models.ManyToManyField('MediaUrls', related_name='event_links', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')
    event_date = models.DateField()
    duration = models.CharField(help_text="Duration in hours", max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200)
    event_title = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name + ' - ' + str(self.event_date)
    
class Program(models.Model):
    name = models.CharField(max_length=100)
    banner_photo = models.ImageField(upload_to='event_photos/')
    heading_photo = models.ImageField(upload_to='event_photos/')
    heading_text = models.CharField(max_length=100)
    description = models.TextField()
    other_photos = models.ManyToManyField('Photos', related_name='program_photos', null=True, blank=True)
    youtube_video_url = models.ManyToManyField('MediaUrls', related_name='programs_links', blank=True, null=True)

    def __str__(self):
        return self.name


class Photos(models.Model):
    photo = models.ImageField(upload_to='event_photos/')

    def __str__(self):
        return self.photo.url
    

class MediaUrls(models.Model):
    url = models.URLField()


class YoutubeUrls(models.Model):
    url = models.URLField()


class NewTable(models.Model):
    name = models.CharField(max_length=100)