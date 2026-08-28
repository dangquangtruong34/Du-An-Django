from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = RichTextUploadingField()
    image = models.ImageField(
        upload_to='blogs/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
class Rates(models.Model):
    rate = models.IntegerField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.rate)