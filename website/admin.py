from django.contrib import admin
from website.models import Contact,Newsletter


# Register your models here.
admin.site.register(Contact)
admin.site.register(Newsletter)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_date',)