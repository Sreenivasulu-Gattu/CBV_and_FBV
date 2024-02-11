from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
from app.models import *


'''     -------------> Returning the String <----------------------'''
def fbs(request):
    return HttpResponse('Hello, this is function based response')

class cbs(View):
    def get(self,request):
        return HttpResponse('Hi This is class based response')
    

'''    ------------------> Rendering the html pages <-------------------     '''

def fbt(request):
    return render(request,'temp1.html')

class cbt(View):
    def get(self,request):
        return render(request,'temp1.html')
    


'''     ---------------------> Inserting the data into models <---------------   '''

def insertfbv(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Successfully inserted..')
        
    return render(request,'insertfbv.html',d)

class insertcbv(View):
    def get(self,request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request,'insertcbv.html',d)
    def post(self,request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted..')


'''     ----------------> rendering of template <-----------------      '''

class rendertv(TemplateView):
    template_name = 'rendertv.html'