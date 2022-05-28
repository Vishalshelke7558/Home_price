from email.policy import default
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
import csv


import pandas as pd
import numpy as np
from sklearn import linear_model
from django.contrib.messages import constants as messages


def front(request):
    return render(request, 'front.html')

def index(request):
    return render(request, 'index.html')


def Admin(request):
    return render(request,'Admin.html')

def Admin_1(request):
    Email = request.POST.get('email','default')
    Pass = request.POST.get('pass')
    if Email == "Vishal@gmail.com" and Pass == "King":
        return render(request, 'Admin_1.html')
    else:
        return render(request, 'invalid.html')
    
def admin_2(request):
    return render(request,'admin_2.html')

def invalid(request):
    return render(request, 'invalid.html')    
    
def about(request):
    return render(request,'about.html')
        
    

def analyze(request):
    area = request.POST.get('area','default')
    room = request.POST.get('room')
    bath =  request.POST.get('bath')
    balcony = request.POST.get('balcony')
    area_type = request.POST.get('area_type')
    floor_number = request.POST.get('floor')
    furniture = request.POST.get('furniture')
    hospital = request.POST.get('hospital')
    highway = request.POST.get('highway')
    gym = request.POST.get('gym')
    swimming_pool = request.POST.get('swimming')
    school = request.POST.get('school')

    area = int(area)
    room = int(room)
    bath = int(bath)
    balcony = int(balcony)

    data = pd.read_csv("C://Users//VISHAL SHELKE//Desktop//IT//Django//textutil//textutil//textutil//Pune_House.csv")
    reg = linear_model.LinearRegression()
    reg.fit(data[['size','total_sqft','bathrooms','balcony']],data.price)
    reg.coef_
    reg.intercept_
    prediction = float(reg.predict([[room,area,bath,balcony]]))
    prediction = round(prediction, 2)
    print("House_Price_is:",prediction)
    
    price = {'Rate':prediction}
    return render(request, 'analyze.html', price)

def contact(request):
    return render(request,'/index.html')

