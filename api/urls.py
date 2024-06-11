from django.urls import path
from .views import chat_view, signup_view, login_view, home_view, logout_view, send_friend_request, respond_friend_request,SearchView, list_friends, list_pending_requests, MessageListCreateView

urlpatterns = [
    path('', login_view, name='login'),  # Default to the login view
    path('signup-page/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('friend-request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('respond-request/<int:request_id>/<str:action>/', respond_friend_request, name='respond_friend_request'),
    path('messages/<int:recipient_id>/', MessageListCreateView.as_view(), name='messages'),
    path('chat/<int:recipient_id>/', chat_view, name='chat'),
]