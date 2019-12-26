from django.contrib import admin
from testapp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['text',]
admin.site.register(Post,PostAdmin)
