from django.template import loader
from django.http import HttpResponse
from .models import Company


def company(request):
    mycompanies = Company.objects.all().values()
    template = loader.get_template('all_companies.html')
    context = {
        'mycompanies': mycompanies,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycompany = Company.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mycompany': mycompany,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template("template.html")
    context = {
        'fruits':['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))