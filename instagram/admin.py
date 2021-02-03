from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
#admin.site.register(Post)
@admin.register(Post) #장식자 wrapping 감싼 대상의 기능 변경 가능

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "photo_tag",
        "message",
        "message_length",#models에서 선언
        "is_public",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["message"]
    list_filter = ["is_public"]
    search_fields = ["message"]


    def message_length(self,post):
        return len(post.message)
        
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src ="{post.photo.url}" style="width: 72px;"/>')
            #사진 보안때문에 mark_safe써야함
        return None
