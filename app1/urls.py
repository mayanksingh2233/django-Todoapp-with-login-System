from django.urls import path,include
from .views import home,about,Contact, delete_as_complete, login_page, register, todo,mark_as_complete
urlpatterns = [
    path("",home,name="home"),
    path("contact/",Contact,name='contact'),
    path("about/",about,name="about"),
    path("todo/",todo,name="todo"),
    path("delete_as_complete/<id>",delete_as_complete , name="delete_as_complete"),
    path("mark_as_complete/<id>",mark_as_complete , name="mark_as_complete"),
    path("login_page/",login_page,name="login_page"),
    path("register_page/",register,name="register_page")
]
