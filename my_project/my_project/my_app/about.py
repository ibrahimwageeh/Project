from django.http import HttpResponse

def about(request):
    return HttpResponse("This is the about page.")