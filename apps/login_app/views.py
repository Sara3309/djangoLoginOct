from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    request.session.clear()
    if 'user' not in request.session:
        request.session['user'] = None
    return render(request,"login/login.html")

def register(request):
    request.session.clear()
    errors = User.objects.basic_validator(request.POST)
    
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value, extra_tags="register_error:"+str(key))
        return redirect("/")

    else:
        user = User.objects.create()
        user.first_name = request.POST['first_name']
        user.last_name= request.POST['last_name']
        user.email = request.POST['email']
        hash1 = bcrypt.hashpw(request.POST['code'].encode(), bcrypt.gensalt())
        user.password = hash1
        
        user.save()
        request.session['user'] = user.first_name
        request.session['id']= user.id
        messages.success(request, "User successfully added.")
        return redirect("/wall")

# def success(request):
#     if "id" in request.session:
#         return render(request,"login/success.html",)
#     if "user" in request.session:
#         return render(request,"login/success.html",)
#     else:
#         response="I know you, don't do that again."
#         return HttpResponse(response)


def login(request):
    request.session.clear()
    if len(request.POST['email2']) < 1:
        messages.error(request, "Email cannot be blank.", extra_tags='suggest_email')
    if len(request.POST['code2']) < 1:
        messages.error(request,"Password cannot be blank", extra_tags="suggest_pw")
    if len(request.POST['email2']) > 1 and len(request.POST['code2']) > 0:

        if User.objects.filter(email=request.POST['email2']):
            user = User.objects.filter(email=request.POST['email2'])
            
            if bcrypt.checkpw(request.POST['code2'].encode(), user[0].password.encode()):
                request.session['user'] = user[0].first_name
                request.session['id'] = user[0].id
                return redirect("/wall")
            else:
                messages.error(request,'Wrong Password', extra_tags='suggest_pw')
                return redirect("/")
        else:
            messages.error(request,'User does not exist, please register', extra_tags='suggest_email')
            return redirect("/")
    return redirect("/")


def back(request):
    request.session.clear()
    return redirect("/")

def wall(request):
    if "id" in request.session:
        context={
            "messages":Message.objects.all().order_by("-created_at"),
            "comments":Comment.objects.all()
        }
        return render(request,"login/wall.html", context)
    else:
        response="Don't even try to hack my site."
        return HttpResponse(response)

def post_message(request):
   
    sender=User.objects.get(id=request.session['id'])
    # print(User.objects.filter(first_name=request.session['user'])[0])
    Message.objects.create(content=request.POST['message'], message_sender=sender)
    return redirect('/wall')

def post_comment(request,id):
    if request.method=="POST":
        Comment.objects.create(content=request.POST['comment'], message=Message.objects.get(id=id),comment_sender=User.objects.get(id=request.session['id']),comment_receiver=Message.objects.get(id=id).message_sender)

    return redirect("/wall")

def delete_message(request,id):
    if "id" in request.session:
        message=Message.objects.get(id=id).delete()
    return redirect("/wall")

def delete_comment(request,id):
    comment=Comment.objects.get(id=id).delete()
    return redirect("/wall")
