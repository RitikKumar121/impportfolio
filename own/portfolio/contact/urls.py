from django.urls import path
from contact import views
urlpatterns = [
 path('contacts.html/',views.contact),

]
