def search(request):

    
    # Get the search query from the request.
    query = request.GET.get('q')

    # Create a Google Maps API client.
    client = googlemaps.Client()

    # Search for places that match the query.
    results = client.places(query)

    # Return the search results to the template.
    return render(request, 'my_app/search.html', {'results': results})

def home_view(request):
    return render(request, 'home.html')