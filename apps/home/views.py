from django.shortcuts import render

# Create your views here.
class HomeRoutes:
    
    # Index url;
    def index(self, request):
        return render(request, 'views/index.html')
    
    
    # About url;
    def about(self, request):
        return render(request, 'views/about.html')
    