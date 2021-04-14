from django.urls import path

from . import views

app_name='myblog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail')

]