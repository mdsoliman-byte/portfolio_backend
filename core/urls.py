from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # Updated path
    path('api/home/', include('home.urls')),  # Updated path
    path('api/skills/', include('skills.urls')),
    path('api/projects/', include('projects.urls')),  # Updated path
    path('api/about/', include('about.urls')),  # Updated path
    path('api/blog/', include('blog.urls')),  # Updated path
    path('api/shop/', include('shop.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)