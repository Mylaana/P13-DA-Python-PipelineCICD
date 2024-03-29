"""
App's views definition
"""
from django.shortcuts import render
from .models import Letting
import logging
from django.core.exceptions import ObjectDoesNotExist


def lettings_index(request):
    """
    View function for displaying a list of lettings.

    Retrieves all lettings from the database and renders them in the
    'lettings/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for displaying details of a letting.

    Retrieves the letting with the specified ID from the database and renders
    its details in the 'lettings/letting.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered response containing the details
        of the letting or 404 if the letting doesnt exist.
    """

    try:
        letting = Letting.objects.get(id=letting_id)
    except ObjectDoesNotExist:
        logging.error("letting does not exist", extra=dict(letting_id=letting_id))
        return render(request, '404.html')

    context = {
        'title': letting.title,
        'address': letting.address,
        }
    return render(request, 'lettings/letting.html', context)
