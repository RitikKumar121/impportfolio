from django.urls import path
from projects import views
urlpatterns = [
 path('projects.html/',views.projects),

]
