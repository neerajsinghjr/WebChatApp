from django.shortcuts import render

# Create your views here.

class HomeRoutes:
    
    # Index url;
    def index():
        return render(request, 'web.index.html', name="home.index")
    
    
    # About url;
    def about():
        return render(request, 'web.about.html', name="home.about")
    