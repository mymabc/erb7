from django.shortcuts import render
# Create your views here.

#def index(request):
#    return HttpResponse("<h1>Hello, world !</h1>")

def index(request):
    #print(request.path)
    return render(request, 'pages/index.html')

def about(request):
    #print(request.path)
    return render(request,'pages/about.html')