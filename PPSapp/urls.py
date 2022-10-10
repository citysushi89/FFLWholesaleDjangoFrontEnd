from django.urls import path
from . import views
from .views import TableListView

# App level
urlpatterns = [
    path('', views.index, name='PPS-index'),
    path('home/', TableListView.as_view(), name='PPS-home'),
    path('about/', views.about, name='PPS-about'),
    path('report/', views.report, name='PPS-report'),
]
