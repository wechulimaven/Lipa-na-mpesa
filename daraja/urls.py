
from django.urls import path
from .views import InitateSTKPush

app_name="daraja"
urlpatterns = [
    path('',InitateSTKPush.as_view(), name="initatestkpush"),
    
]
