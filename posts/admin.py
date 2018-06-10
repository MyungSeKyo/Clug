from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from posts.models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
