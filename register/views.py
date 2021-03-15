from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

name = ''
passw = ''


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        global name, passw
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            name = username
            password = form.cleaned_data.get('password1')
            passw = password
            htmly = get_template('register/Email.html')
            d = {'username': username, 'password': password, 'email': email}
            print(password)
            subject, from_email, to = 'welcome', 'powerstrike001@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content,
                                         from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('/account/confirmed')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form,
                  'title': 'reqister here'})


def confirmed(request):
    return render(request, 'register/confirmed.html',
                  {"name": name, 'pass': passw})


def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("/account/profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'register/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def profile(request):
    return render(request, 'register/profile.html')
