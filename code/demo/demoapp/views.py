from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from demoapp.models import Project

class ProjectListView(TemplateView):
    template_name = 'template1.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()

        return render(request, self.template_name,{
            'projects': projects
        })