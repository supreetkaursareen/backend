from django.contrib import admin
from django.urls import path, include
from my_app.views import home  # Ensure the home view is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_app.urls')),  # Including URLs from your app
    path('', home, name='home'),  # Define the base route for home
]
