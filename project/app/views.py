from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    
    
    return render(request,'index.html')

def conceitual(request):

    return render(request, 'conceitual.html')

def pd(request):

    return render(request, 'pd.html')
def pp(request):

    return render(request, 'pp.html')



def avaliacao(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        r1 = request.POST.get('r1','')
        r2 = request.POST.get('r2','')
        r3 = request.POST.get('r3','')
        file = open('C:/Users/Pc/Desktop/respostas/'+name+'.txt',"w")
        file.write(r1+"\n")
        file.write(r2+"\n")
        file.write(r3+"\n")
        return redirect('index')
    else:
        return render(request, 'avaliacao.html')

def slide(request):
    return render(request,'slide.html')
    