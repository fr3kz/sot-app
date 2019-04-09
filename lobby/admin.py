from django.contrib import admin
from lobby.models import (Queue,Category,Query,Invitation)

class QueueAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','members')
    list_display_links = ('id','title')
    list_filter = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Queue,QueueAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Query)
admin.site.register(Invitation)

