from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'pages/index.html')



def aboutpage(request):
    return render(request, 'pages/about.html')



def investmentpage(request):
    return render(request, 'pages/investment.html')



def news(request):
    return render(request, 'pages/news.html')