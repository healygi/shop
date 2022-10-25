from django.shortcuts import render

def view_bag(request):
    """ A view that renders the bags contents """

    return render(request, 'bag/bag.html')