from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime
import requests
import random

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date' : now
    }
    return render(request, 'first/index.html', context)

def select(request):
    context = {}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = int(request.GET['number']) #int형으로 받아줘야함
    
    results = []                        #사용자가 선택한 수 하나를 미리 넣는다 (로또 추첨 사이트는 사용자가 고른 수 이외 나머지를 골라줌))
    if chosen >=1 and chosen <= 45:
        results.append(chosen)
    
    
    box = [] #값을 꺼낼 박스
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)
            
    random.shuffle(box)
    while len(results)<6:
        results.append(box.pop())
        
    context = {'numbers':results}
    return render(request, 'first/result.html', context)