from django.urls import path
from demoapp import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects'),
]