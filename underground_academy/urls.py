
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("courses.urls")),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
]
