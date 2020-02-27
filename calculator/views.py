from django.shortcuts import render
from django.http import HttpResponse
from .models import CalculationLog
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):

    return render(request,'index.html')

def calApi(request):
    X = request.POST['X']
    Y = request.POST['Y']
    op = request.POST['op']

    c = CalculationLog()
    try:
        c.X = float(X)
        c.Y = float(Y)
        if op in ['+','-','*','/','%'] :
            c.op = op
        else:
            raise(ValueError)
    except:
        c.delete()
        return render(request,'index.html',
                {'X':X,
                 'op':op,
                 'Y':Y,})

    
    Result = 0
    if op=='+':
        c.Result = c.X + c.Y
    elif op=="-":
        c.Result = c.X - c.Y
    elif op=="*":
        c.Result = c.X * c.Y
    elif op=="/":
        c.Result = c.X / c.Y
    elif op=="%":
        c.Result = c.X % c.Y
    
    c.save()
    print(Result)
    return render(request,'index.html',
                {'X':X,
                 'op':op,
                 'Y':Y,
                 'Result':c.Result})


