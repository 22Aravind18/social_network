from django.urls import path
from .views import signup_view, login_view, home_view, logout_view, send_friend_request, respond_friend_request, list_friends, list_pending_requests

urlpatterns = [
    path('', login_view, name='login'),  # Default to the login view
    path('signup-page/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Add logout URL
    path('home/', home_view, name='home'),
    path('friend-request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('respond-request/<int:request_id>/<str:action>/', respond_friend_request, name='respond_friend_request'),
    path('friends/', list_friends, name='list_friends'),
    path('pending-requests/', list_pending_requests, name='list_pending_requests'),
]