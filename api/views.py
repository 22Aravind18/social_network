from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import SignUpForm, LoginForm
from .serializers import UserSerializer, FriendRequestSerializer
from .models import FriendRequest
from django.db.models import Q

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                return redirect('login')
            except IntegrityError:
                form.add_error('email', 'A user with that email already exists.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    keyword = request.GET.get('keyword', '')
    view = request.GET.get('view', '')
    users = User.objects.filter(Q(email__icontains=keyword) | Q(username__icontains=keyword)) if keyword else None
    pending_requests = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)

    friends = None
    if view == 'friends':
        friends = User.objects.filter(received_requests__from_user=request.user, received_requests__is_accepted=True) | \
                  User.objects.filter(sent_requests__to_user=request.user, sent_requests__is_accepted=True)

    return render(request, 'home.html', {
        'users': users,
        'pending_requests': pending_requests,
        'friends': friends,
        'view': view
    })

@api_view(['POST'])
@login_required
def send_friend_request(request, user_id):
    try:
        to_user = User.objects.get(id=user_id)
        from_user = request.user
        if to_user == from_user:
            return redirect('home')  # Redirect to home page
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return redirect('home')  # Redirect to home page
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return redirect('home')  # Redirect to home page
    except User.DoesNotExist:
        return redirect('home')  # Redirect to home page

@api_view(['POST'])
@login_required
def respond_friend_request(request, request_id, action):
    try:
        friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
        if action == 'accept':
            friend_request.is_accepted = True
            friend_request.save()
        elif action == 'reject':
            friend_request.delete()
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        return redirect('home')
    except FriendRequest.DoesNotExist:
        return redirect('home')

@api_view(['GET'])
@login_required
def list_friends(request):
    friends = User.objects.filter(received_requests__from_user=request.user, received_requests__is_accepted=True) | \
              User.objects.filter(sent_requests__to_user=request.user, sent_requests__is_accepted=True)
    serializer = UserSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
def list_pending_requests(request):
    requests = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)
    serializer = FriendRequestSerializer(requests, many=True)
    return Response(serializer.data)

from django.contrib.auth import logout

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')