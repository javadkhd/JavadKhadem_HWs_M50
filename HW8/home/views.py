from django.shortcuts import render


# Create your views here.
def home(request):
    """
    This view will show home page
    """
    return render(request, template_name='home/home.html')
