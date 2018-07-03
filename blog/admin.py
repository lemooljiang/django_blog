from django.contrib import admin
from blog import models
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','pub_date','last_modify','status','priority')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','set_as_top_menu','slug','position_index')
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.Category,CategoryAdmin)
