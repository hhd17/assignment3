from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('myapp1/', include('myapp1.urls', namespace='myapp1')),  # Include with the namespace
    path('admin/', admin.site.urls),
]