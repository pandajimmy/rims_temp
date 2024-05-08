from django.shortcuts import render
from django.conf import settings

def tablelist(request):
    try:
        # Get the base URL of the current Django server
        base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash

        context = {
            'base_url': base_url
        }
    
        return render(request, 'nav_list/tablelist.html', context)
    
    except Exception as e:
        # Handle any exceptions that might occur during hamster creation
        context = {
            'error_message': str(e)
        }
