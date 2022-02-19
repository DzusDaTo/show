from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('testing/', include('testing.urls')),
    path('register/', include('register.urls')),
    path('aboutt/', include('aboutt.urls')),
    path('mainn/', include('mainn.urls')),
    path('resumeout/', include('resumeout.urls')),
    path('vacan/',include('vacan.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
