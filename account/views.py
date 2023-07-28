from django.shortcuts import render,get_object_or_404

# Create your views here.
from account.models import User
from account.forms import UserForm
from django.core.exceptions import ObjectDoesNotExist

def home(request):

    hello = str( 'Hello, World!')
    context = {
        "hello":hello,
    }
    return render(request, "account/home.html", context)


def list_users(request):
    #user_list = User.objects.all()
    user_list = User.objects.raw("SELECT * FROM users;")
    context = {'user_list':user_list}
    return render(request, "account/list_users.html", context)

from django.http import Http404

def user_detail(request, id):
    try:
        #user_info = get_object_or_404(User, id=id)
        user_info = User.objects.raw("SELECT * FROM users WHERE id = '%s'", [id])[0]
        context = {
            'user_info': user_info
        }
    except Http404:
          #raise Http404('The user was not found.')
          return render(request, 'account/error.html')


    return render(request, 'account/user_detail.html', context)


    





# def register_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid ():
#             new_user = form.save(commit=False)
#             #new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             return render(request,'account/register_done.html',{'new_user': new_user})
#     else:
#         form = UserForm()
#     return render(request,'account/register.html',{'form': form})
from django.db import connection
from django.utils import timezone
from django.db import connection
from django.utils import timezone

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            
            # Use raw SQL to insert new user record
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO users (name, email, role, password, is_superuser, is_staff, is_active, first_name, last_name, date_joined, last_login) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    [new_user.name, new_user.email, new_user.role, new_user.password, False, False,True,'', '', timezone.now(), None]
                )
            
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        form = UserForm()
    return render(request,'account/register.html',{'form': form})
