from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"one": "two"}
    return render(request,'index.html',context)