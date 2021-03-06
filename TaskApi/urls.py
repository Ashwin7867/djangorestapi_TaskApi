from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from TaskApp import views

router = routers.SimpleRouter()

router.register(r'task', views.TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
