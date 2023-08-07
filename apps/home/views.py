from django.shortcuts import render
from .task import get_sum
from django.http import HttpResponse


# Create your views here.
class HomeRoutes:
    
    # Index url;
    def index(self, request):
        return render(request, 'web.index.html', name="home.index")
    
    
    # About url;
    def about(self, request):
        return render(request, 'web.about.html', name="home.about")
    

    # Testing Celery Workflow;;
    def test(self, request):
        job_id = get_sum.delay(5,10)
        return HttpResponse(f"Task With Job_id : {job_id}")