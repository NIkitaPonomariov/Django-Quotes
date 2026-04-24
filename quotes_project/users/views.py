from django.shortcuts import render
from .forms import CustomRegisterForm
from django.views import View



class RegisterView(View):
    template_name = "users/register.html"
    form_class = CustomRegisterForm

    def get(self,request):
        return render(request, self.template_name, context={"form": self.form_class})
    

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
