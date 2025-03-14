from django.urls import path
from .views import (
    home,
    register,
    user_login,
    user_logout,
    pet_list,
    pet_create,
    pet_update,
    pet_delete,
)

urlpatterns = [
    path("", home, name="home"),
    # User authentication
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # Pet management
    path("pets/", pet_list, name="pet_list"),
    path("pets/add/", pet_create, name="pet_create"),
    path("pets/<int:pet_id>/edit/", pet_update, name="pet_update"),
    path("pets/<int:pet_id>/delete/", pet_delete, name="pet_delete"),
]
