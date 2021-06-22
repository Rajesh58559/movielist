
from django.urls import path
from . import views
app_name='movielistapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.detail,name='details'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]