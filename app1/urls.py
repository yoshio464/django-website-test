from django.urls import path

#viewとurlsとの紐づけ
from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view())
]
