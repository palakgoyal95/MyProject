from django.urls import path
from . import views

# Set the app namespace for organization
app_name = 'myapp'

urlpatterns = [
    # Example: map the root of this app to a view function named 'home'
    path('', views.index, name='index'),

    # Add more paths as your app grows
    # path('about/', views.about, name='about'),
]