from django.shortcuts import render
def index(requests):
    return render(requests, 'main/index.html')

def about(requests):
    return render(requests, 'main/news.html')
