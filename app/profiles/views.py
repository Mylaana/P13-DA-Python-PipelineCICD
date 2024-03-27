"""
App's views definition
"""
from django.shortcuts import render
from .models import Profile
import logging
from django.core.exceptions import ObjectDoesNotExist


def profiles_index(request):
    """
    View function for displaying a list of profiles.

    Retrieves all profiles from the database and renders them in the
    'profiles/index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function for displaying details of a profile.

    Retrieves the profile with the specified username from the database
    and renders its details in the 'profiles/profile.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered response containing the details
        of the profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except ObjectDoesNotExist:
        logging.error("username does not exist", extra=dict(username=username))
        return render(request, '404.html')

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
