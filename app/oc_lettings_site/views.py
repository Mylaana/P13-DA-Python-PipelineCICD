"""
App's views definition
"""
from django.shortcuts import render


def index(request):
    """
    View function for rendering the index page.

    This view renders the 'index.html' template, which serves as the homepage of the website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the index page.
    """
    return render(request, 'index.html')
