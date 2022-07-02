from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    # path('', home),
    path('student/', StudentAPI.as_view()),
    path('register/', RegisterUser.as_view()),
    # path('student/', post_student),
    # path('update-student/<id>/', update_student),
    # path('delete-student/<id>/', delete_student),
    path('get-book/', get_book),
]
