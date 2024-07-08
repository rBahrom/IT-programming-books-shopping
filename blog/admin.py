from django.contrib import admin
from .models import Auther, Books, Commit
# Register your models here.

admin.site.register(Auther)
admin.site.register(Books)
admin.site.register(Commit)
