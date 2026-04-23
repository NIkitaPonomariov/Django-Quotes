from django.shortcuts import render
from .forms import CustomRegisterForm



form_class = CustomRegisterForm

def get(request):
    ...