from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lobby import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register('queue',api.IndexApi)
router.register('category',api.CategoryApi)
router.register('user',api.UserApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('', include('lobby.urls')),
    path('api/',include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
