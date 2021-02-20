from django.conf import settings
from django.db import models

# from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # AUTH_USER_MODELS 디폴트값 auth.User
    message = models.TextField()
    # title = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")

    def __str__(self):
        #    return "Custom Post object({})".format(self.id)
        return self.message

    # ?
    class Meta:
        ordering = ["-id"]

    def message_length(self):
        return len(self.message)

    # 인자없는함수만 가능
    message_length.short_description = "메세지길이"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )  # 가상의 이름 실제 데이터베이스필드와는 다름 post_id
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
