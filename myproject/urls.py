from django.contrib import admin
from django.urls import path
from enrollment.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Home page
]
