from django.shortcuts import render

# Create your views here.
def bucky(request):
    d={'name':'avengers','cast':7}
    return render(request,'bucky.html',context=d)
