from django.contrib import admin
from .models import Contact
from .models import Post

admin.site.register(Post)

admin.site.register(Contact)
# Register your models here.
