from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader


# Create your views here.
"""
def home(request):
    template = loader.get_template('home.html')
    home_content = template.render()
    return HttpResponse(home_content)
    # return HttpResponse(template.render())

"""

def home(request):
    return render(request, 'home.html')