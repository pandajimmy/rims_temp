from django.shortcuts import render

def tablelist(request):
    try:
        context = {
            # Add any context data you want to pass to the template
            'title': 'RIMS API Endpoint Access Table',
            'last_updated_time': '3:14 PM 24/4/2024'
        }
        return render(request, 'nav_list/tablelist.html', context)
    
    except Exception as e:
        # Handle any exceptions that might occur during hamster creation
        context = {
            'error_message': str(e)
        }

def errorlist(request):
    try:
        context = {
            'title': 'RIMS API Endpoint Error List',
            'last_updated_time': '3:14 PM 24/4/2024'
        }
        return render(request, 'nav_list/errorlist.html', context)
    
    except Exception as e:
        # Handle any exceptions that might occur during hamster creation
        context = {
            'error_message': str(e)
        }
