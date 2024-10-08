from django.shortcuts import render, HttpResponseRedirect
from login.models import Review, Portfolio
from main.forms import ReviewForm
from django.http import HttpResponse



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def lensess(request):
    return render(request, 'main/lensess.html')

def sale(request):
    return render(request, 'main/sale.html')

def portfolio(request):
    portfolio=Portfolio.objects.all()
    context={
        "list":portfolio, 
    }
    return render(request, 'main/portfolio.html', context)

def frame(request):
    return render(request, 'main/frame.html')

def organizations(request):
    return render(request, 'main/organizations.html')



def review(request):
    rev=Review.objects.all()
    context={
        "list":rev, 
        "form":ReviewForm()
    }
    return render(request, 'main/review.html', context)

def addreview(request):
    if request.method=='POST':
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            obj=Review(**form.cleaned_data) # ** - создает именованные аргументы
            obj.answer=1 # заплатка, позже исправить
            obj.user=request.user 
            obj.save()
            return HttpResponseRedirect('/review')
        else:
            return HttpResponse(form.as_p() )
    else:
        return HttpResponse (ReviewForm().as_p()   )
    
def deletreview(request, idobj):
    if request.method=='POST':
        Review.objects.get(id=idobj).delete()
    return HttpResponseRedirect('/review')
        
        
    
          