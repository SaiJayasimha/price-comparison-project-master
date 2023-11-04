import time
from django.shortcuts import render

# from django.http import HttpResponse


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, "homepage.html")


def search(request):
    query = request.GET.get('q')
    results = SearchResult.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results})




def logout():
    # Delete the session data
    session.delete()
    # Wait for the session to expire
    time.sleep(1)
    # Redirect the user to the login page
    return redirect('/login')