from django.shortcuts import render


# Create your views here.
def blog(request):
    """
    This view will show blog posts
    """
    return render(request, template_name='blog.html')
