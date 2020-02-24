from django.shortcuts import render
from django.http import HttpResponse
from .models import CalculationLog
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    return render(request,'index.html')

def calApi(request):

    X = float(request.POST['X'])
    Y = float(request.POST['Y'])
    op = request.POST['op']
    print(X,op,Y)

    c = CalculationLog()
    c.X = X
    c.Y = Y
    
    Result = 0

    if (op=='+'):
        Result = X+Y
        c.Result = Result
    elif op=="-":
        Result = X-Y
        c.Result = Result
    elif op=="*":
        Result = X*Y
        c.Result = Result
    elif op=="/":
        Result = X/Y
        c.Result = Result
    elif op=="%":
        Result = X%Y
        c.Result = Result
    
    c.save()
    print(Result)
    return render(request,'index.html',
                {'X':X, 
                 'Y':Y, 
                 'Result':Result})


