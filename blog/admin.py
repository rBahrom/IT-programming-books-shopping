from django.contrib import admin
from .models import Auther, Books, Commit
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Auther)
class AutherAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_day', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ("create_date",)


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'auther', 'price', 'count', 'create_date')
    list_display_link = ('id', 'title', 'auther')
    search_fields = ('id', 'title', 'auther')
    ordering = ("create_date",)


# admin.register(Commit)

@admin.register(Commit)
class CommitAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'text', 'create_date')
    list_display_link = ('id', 'user')
    search_fields = ('id', 'user')
    ordering = ("create_date",)
