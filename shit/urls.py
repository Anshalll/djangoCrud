from django.urls import  path


from . import views
urlpatterns = [
    path('', views.index,  name="home"),
    path('delete/<int:pk>/', views.delete,  name="delete"),
    path('update/<int:pk>/', views.update,  name="update"),
 
    
]
