
from django.shortcuts import render, get_object_or_404,redirect
from .models import citoyen
from finance.models import Citoyen
from django.http import HttpResponse
# Create your views here.
    
def index (request):
    CIN=''
    if request.method=='POST':
        CIN=request.POST['cin']
        citoyens = citoyen.objects.filter(cin=CIN)
        citoyenf = Citoyen.objects.filter(cin=CIN)
        return render(request,'show.html',{'citoyens':citoyens , 'citoyenf':citoyenf})
    return render(request,'index.html')