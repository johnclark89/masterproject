# Create your views here.
from django.shortcuts import render


def index(request):
    #code

    return render(
        request,
        "chvote.html",
    )
	