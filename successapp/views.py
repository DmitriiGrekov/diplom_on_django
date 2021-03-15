from django.http import HttpResponse


def search(request):
    if request.method == "POST":
        return HttpResponse(request.body)
