from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TravelIdea

# Create your views here.

def homepage(request):
    travel_ideas = TravelIdea.objects.all()[:5] # pagination
    context = {
        'greeting': "Let's see what travel ideas are here!",
        'ideas': travel_ideas
        }
    return render(request, "travels/homepage.html", context)

def idea_detailed(request, idea_id):
    idea = TravelIdea.objects.get(pk=idea_id)
    return render(request, 'travels/detailed.html', {"idea": idea})

def new_idea(request):
    return render(request, 'travels/newidea.html')

def add_idea(request):
    description = request.POST.get('short_description')
    detailed_description = request.POST.get('detailed')
    new_idea = TravelIdea(short_description=description, detailed=detailed_description)
    new_idea.save() #try - except -?
    return HttpResponseRedirect(reverse("travels:idea_detailed", args=(new_idea.id,)))
