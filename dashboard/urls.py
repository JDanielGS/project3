from django.urls import path
from .views import dashboardHomeView, NewsLettersDashboardHomeView

app_name='dashboard'

urlpatterns = [
    path('', dashboardHomeView.as_view(), name='home'),
    path('list/', NewsLettersDashboardHomeView.as_view(), name='list')
]
