from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "var1" :"Rahul",
        "var2" :"Vaidya"
    }
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("This is about page")
