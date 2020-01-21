from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('headline', 'slug', 'status', 'pub_date')
	list_filter = ("status",)
	search_fields = ['headline', 'body_text']
	prepopulated_fields = {'slug': ('headline',)}


admin.site.register(Post, PostAdmin)