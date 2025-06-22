
from django.urls import path
from .views import ZenApi
urlpatterns = [
    path('zenapi/',ZenApi.as_view(),name='zen-api'),
]