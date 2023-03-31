from django.urls import path,include
from .views import (
    index,
    register,
    user_login,
    user_logout,professor_detail,create_professor,add_rating
)


urlpatterns = [
      path("",index, name='index'),
      path('register/', register, name='register'),
      path('login/', user_login, name='login'),
      path('logout/', user_logout, name='logout'),
      #path('professor/<int:professor_id>/', professor_detail, name='professor_detail'),
      #path('professor/create/', create_professor, name='create_professor'),
      path('create_professor/', create_professor, name='create_professor'),
      path('professor/<int:professor_id>/', professor_detail, name='professor_detail'),
      path('professor/<int:professor_id>/add_rating/', add_rating, name='add_rating')
]
