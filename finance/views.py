from django.shortcuts import render, get_object_or_404,redirect
from .models import Citoyen
from django.http import HttpResponse
# Create your views here.
    
def indexf (request):
    CIN=''
    if request.method=='POST':
        CIN=request.POST['cin']
        citoyenf = Citoyen.objects.filter(cin=CIN)
        return render(request,'show.html',{'citoyenf':citoyenf})
    return render(request,'index.html')