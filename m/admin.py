from django.contrib import admin
from .models import Movie, Account, New

# Register your models here.

admin.site.register(Account)
admin.site.register(Movie)
admin.site.register(New)

