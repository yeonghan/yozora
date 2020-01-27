from django.contrib import admin
from blog.models import blog_basic
# Register your models here.

@admin.register(blog_basic)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('number','title','text','create_date','modify_date')
