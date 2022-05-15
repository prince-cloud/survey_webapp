from urllib import response
from django.shortcuts import get_object_or_404, render, redirect

from survey.forms import ResponseForm, SurveyForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.


## home page
def index(request):
    return render(request, 'index.html', {
        "surveys": Survey.objects.all(),
    })

## creating survey
@login_required

def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            response_form = form.save(commit=False)
            response_form.owner = request.user
            response_form.save()
            return redirect("/my-surveys/")
    else:
        form = SurveyForm()
    return render(request, 'create_edit_survey.html', {
        "form": form,
    })


## edit survey 
@login_required

def edit_survey(request, slug):
    survey = get_object_or_404(Survey, slug=slug)
    if request.method == 'POST':
        form = SurveyForm(data=request.POST, files=request.FILES, instance=survey)
        if form.is_valid():
            response_form = form.save(commit=False)
            response_form.owner = request.user
            response_form.save()
            return redirect("/my-surveys/")
    else:
        form = SurveyForm(instance=survey)
    return render(request, 'create_edit_survey.html', {
        "form": form,
    })


## survey list
@login_required
def my_surveys(request):
    return render (request, 'my-surveys.html', {
        "surveys": Survey.objects.filter(owner=request.user)
    })


## survey instance
def survey_response(request, slug):
    survey_url = request.build_absolute_uri
    survey = get_object_or_404(Survey, slug=slug)
    if request.method == 'POST':
        form = ResponseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            response_form = form.save(commit=False)
            response_form.survey = survey
            response_form.save()
            return redirect(f"/{survey.slug}")
    else:
        form = ResponseForm()
    return render(request, 'survey_response.html', {
        "form": form,
        "survey": survey,
        "survey_url": survey_url,
    })


## survey detail for tabulations
@login_required

def survey_detail(request, slug):
    survey = get_object_or_404(Survey, slug=slug)
    responses = SurveyResponse.objects.filter(survey=survey)
    return render(request, 'survey_detail.html', {
        "survey": survey,
        "responses": responses,
    })

