from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'pages/index.html')



def about(request, pk):
    return render(request, 'pages/about.html')



def investment(request, pk):
    return render(request, 'pages/investment.html')



def news(request, pk):
    return render(request, 'pages/news.html')