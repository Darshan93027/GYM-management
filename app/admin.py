from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from app.models import *


class PhotosInline(admin.TabularInline):
    model = Program.other_photos.through  # Through model for the ManyToManyField
    extra = 0  # Number of extra forms

class MediaUrlsInline(admin.TabularInline):
    model = Program.youtube_video_url.through  # Through model for the ManyToManyField
    extra = 0  # Number of extra forms


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inline  = [PhotosInline, MediaUrlsInline]


admin.site.register(Event, SomeModelAdmin)
admin.site.register(Photos, SomeModelAdmin)
admin.site.register(Program, SomeModelAdmin)
admin.site.register(MediaUrls, SomeModelAdmin)
admin.site.register(YoutubeUrls)