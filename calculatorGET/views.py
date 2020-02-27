from django.shortcuts import render
from django.http import HttpResponse
from .models import CalculationGetLog
from django.http import HttpResponseRedirect


# Create your views here.

def main(request):
    if request.GET :
        X = request.GET.get('X')
        Y = request.GET.get('Y')
        op = request.GET.get('op')

        c = CalculationGetLog()
        try:
            c.X = float(X)
            c.Y = float(Y)
            if op in ['+', '-', '*', '/', '%']:
                c.op = op
            else:
                raise (ValueError)
        except:
            c.delete()
            return render(request, 'index_get.html',
                          {'X': X,
                           'op': op,
                           'Y': Y, })

        Result = 0
        if op == '+':
            c.Result = c.X + c.Y
        elif op == "-":
            c.Result = c.X - c.Y
        elif op == "*":
            c.Result = c.X * c.Y
        elif op == "/":
            c.Result = c.X / c.Y
        elif op == "%":
            c.Result = c.X % c.Y

        c.save()
        print(Result)
        return render(request, 'index_get.html',
                      {'X': X,
                       'op': op,
                       'Y': Y,
                       'Result': c.Result})
    return render(request, 'index_get.html')

