from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world.")

def select(request):
    message = "수 하나를 입력해 주세요"
    return HttpResponse(message)

def result(request):
    message = "추첨 결과 입니다."
    return HttpResponse(message)