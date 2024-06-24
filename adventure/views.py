from django.shortcuts import render, redirect
from django.views import View

class AdventurePageView(View):
    def get(self, request):
        return render(request, 'adventure/adventure.html')
