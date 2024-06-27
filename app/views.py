from django.shortcuts import render


# Create your views here.
def jinja_print(request):
    d={'name':'shanthkumar','age':27}
    return render(request,'jinja_print.html',d)