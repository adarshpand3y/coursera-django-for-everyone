from django.shortcuts import render
from django.http import HttpResponse
from djangoForEveryone.settings import UNIQUE_CODE

# Create your views here.
def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. {UNIQUE_CODE}")

def owner(request):
    return HttpResponse(f"Hello, world. {UNIQUE_CODE} is the polls index. {UNIQUE_CODE}")

def detail(request, question_id):
    return HttpResponse(f"{UNIQUE_CODE} You're looking at question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"{UNIQUE_CODE} You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"{UNIQUE_CODE} You're voting on question %s." % question_id)