from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    # title = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")

    def __str__(self):
        #    return "Custom Post object({})".format(self.id)
        return self.message
#?
    class Meta:
        ordering = ['-id']

    def message_length(self):
        return len(self.message)

    # 인자없는함수만 가능
    message_length.short_description = "메세지길이"


