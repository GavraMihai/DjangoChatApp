from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message
from django.core.mail import send_mail
from ChatApp.settings import EMAIL_HOST_USER


# Create your views here.
from ChatApplication.forms import CreateUserForm


@login_required(login_url='login')
def index(request):

    return redirect('/MainRoom')


@login_required(login_url='login')
def room(request, room):

    current_user = request.user

    if request.method == 'POST':
        room_name = request.POST.get('create_room_name')
        room_password = request.POST.get('create_room_password')

        if Room.objects.filter(name=room_name).exists():
            return redirect('/'+room_name)
        else:
            new_room = Room.objects.create(name=room_name, password=room_password)
            new_room.save()
            return redirect('/'+room_name)

    if Room.objects.filter(name=room).exists() and Room.objects.get(name=room).id < 5:
        room_details = Room.objects.get(name=room)
        return render(request, 'home.html', {

            'room_name': room,
            'username': current_user.username,
            'room_id': room_details.id,
        })
    else:
        return redirect('/MainRoom')


@login_required(login_url='login')
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, room=room_id, user=username)
    new_message.save()
    return HttpResponse(status=200)


@login_required(login_url='login')
def uploadImage(request):
    message = ''
    username = request.POST['username']
    room_id = request.POST['room_id']
    room_name = request.POST['room_name']
    image = request.FILES.get('image_input')

    current_user = request.user

    new_message = Message.objects.create(value=message, room=room_id, user=username, image=image)
    new_message.save()
    return render(request, 'home.html', {

        'room_name': room_name,
        'username': current_user.username,
        'room_id': room_id,
    })


def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages_list = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages_list.values())})


def loginRoom(request):
    current_user = request.user
    room_name = request.POST['login_room_name']
    room_password = request.POST['login_room_password']

    try:
        Room.objects.get(name=room_name, password=room_password)
        room_details = Room.objects.get(name=room_name)
        return render(request, 'home.html', {

            'room_name': room_name,
            'username': current_user.username,
            'room_id': room_details.id,
        })
    except Room.DoesNotExist:
        return redirect('/MainRoom')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/MainRoom')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/MainRoom')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/MainRoom')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def GamesRoom(request):
    return redirect('/MainRoom')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

