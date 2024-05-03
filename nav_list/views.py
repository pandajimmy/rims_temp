from django.shortcuts import render

def tablelist(request):
    try:
        return render(request, 'nav_list/tablelist.html')
    
    except Exception as e:
        # Handle any exceptions that might occur during hamster creation
        context = {
            'error_message': str(e)
        }
