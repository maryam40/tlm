import logging

from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_GET

LOGGER = logging.getLogger(__name__)


@require_GET
def index(request):
    """
    Render view for homepage.
    """
    user_full_name = ''
    if request.user.is_authenticated:
        user_full_name = request.user.full_name or request.user.email
        messages.success(
            request,
            'Welcome "{user_full_name}" to our website.'.format(
                user_full_name=user_full_name
            )
        )
    else:
        messages.info(request, 'Welcome to our website (This is sample info message).')
        messages.warning(request, 'Welcome to our website (This is sample warning message).')
        messages.success(request, 'Welcome to our website (This is sample success message).')
        messages.error(request, 'Welcome to our website (This is sample error message).')

    context = {
        'user_full_name': user_full_name,
    }

    return render(request, 'core/dashboard.html', context)
