from django.contrib import admin
from django.urls import path
import Main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.views.index, name='index'),
]
