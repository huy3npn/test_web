from django.urls import path

# from chats.views.auth_view import *
from rest_framework.authtoken import views

from chats.views1.call_view import StartCall, EndCall
from chats.views1.message_view import MessageView
# from chat_app import settings

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    # path('login/', Login.as_view()),
    # path('registration/', RegisterView.as_view()),
    # path('logout/', LogOutView.as_view()),
    # path('users/', UsersView.as_view()),
    path('message/', MessageView.as_view()),
    path('start-call/', StartCall.as_view()),
    path('end-call/', EndCall.as_view()),
    # path('test-socket/', test_socket),
    # path("<str:room_name>/",room , name="room"),
]
