from django.contrib import admin
from .models import Tweet
from .models import Contact

# Register your models here.

admin.site.register(Tweet)
admin.site.register(Contact)

