from django.urls import path
from projects import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('projects.html/',views.projects),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
