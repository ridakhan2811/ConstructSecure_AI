#safety_ai_monitor urls.py
from django.contrib import admin
from django.urls import path
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detect_frame/', views.detect_frame, name='detect_frame'),  # NEW endpoint for JS
    path('detection/', views.detection_view, name='detection'),
    path('about/', views.about, name='about'),
]
