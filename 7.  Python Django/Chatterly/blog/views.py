from django.shortcuts import render


from django.http import HttpResponse



# Create your views here.

def home(request):
    return HttpResponse("Hey there whats up could not get up what's going onnn ")

def about(request):
    return HttpResponse("ye wala page about us ka hai. Mere ko kuch kuch samajh aa raha hai but i want to a expert in django")

def contact(request):
    return HttpResponse("ye wala page contact ka hai ")
