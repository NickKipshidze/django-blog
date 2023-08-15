from django.shortcuts import render, redirect
from django.views import View
from . import forms

# Create your views here.


class CreateBlogPostView(View):
    def post(self, request):
        form = forms.CreateBlogPostForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect("home")
        
        return render(request, "newblog.html", {"form": form})
    
    def get(self, request):
        form = forms.CreateBlogPostForm()
        return render(request, "newblog.html", {"form": form})
