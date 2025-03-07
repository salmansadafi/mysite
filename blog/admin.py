from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)  # Decorator to register the Post model with the admin site
class PostAdmin(admin.ModelAdmin):
    date_hierarchy ="created_date"  # Adds a date-based drill-down navigation in the admin list view
    empty_value_display = "-empty-"  # Customizes the display of empty values in the admin list view
    #fields = ('title',)  # Specifies the fields to display in the form view for the Post model
    list_display = ('title', 'status', 'counted_views', 'created_date' , 'published_date')  # Specifies the fields to display in the list view for the Post model
    list_filter =('status',)
    search_fields = ['title', 'content']  # Adds a search box to the admin list view
#admin.site.register(Post,PostAdmin)