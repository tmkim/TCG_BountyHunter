from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, nakama. Welcome to the bounty index.")