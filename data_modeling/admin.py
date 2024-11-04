from django.contrib import admin
from .models import Customer, Post, Comment, Like

admin.site.register(Customer)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
# Register your models here.
