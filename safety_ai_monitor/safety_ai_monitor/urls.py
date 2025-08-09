
from django.contrib import admin
from django.urls import path
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detect/', views.detect_view, name='detect'),

    path('detection/', views.detection_view, name='detection'),
    path('about/', views.about, name='about'),
]
