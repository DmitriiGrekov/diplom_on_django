from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EmailPostForm
from django.core.mail import send_mail


def index(request):
    """
    Функция, выводящая главную станицу сайта
    """
    context = None
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            subject = "Отзыв о сайте nips"
            sender = form.cleaned_data['to']
            name = form.cleaned_data['name']
            messages = form.cleaned_data['comments']
            context = name
            message = "Отзыв от "+sender+"("+name+")"+" "+messages
            send_mail(subject, message, 'powerstrike001@gmail.com',
                      ['docvampir95@gmail.com'])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'mainpage/firstpage.html', {
                                                    'form': form,
                                                    'sent': sent,
                                                    'name': context})


class RobotTxtView(TemplateView):
    """
    Класс, генерирующий файл robots.txt
    """
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SitemapXmlView(TemplateView):
    """
    Класс, генерирующий карту сайта
    """
    template_name = 'sitemap.xml'
    content_type = 'application/xml'
