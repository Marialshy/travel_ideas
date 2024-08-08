from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:idea_id>', views.idea_detailed, name='idea_detailed'),
    path('add', views.add_idea, name='add_idea'),
    path('new', views.new_idea, name='new_idea'),
]