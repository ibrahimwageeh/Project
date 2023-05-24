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

def home(request):
    # Get the search term from the request.
    search_term = request.GET.get('q')

    # Get the results from Google Maps.
    results = google_maps.search(search_term)

    # Create a list of bubbles to display the results.
    bubbles = []
    for result in results:
        # Create a bubble for each result.
        bubble = {
            'location': result['geometry']['location'],
            'number': random.randint(1, 100)
        }

        # Add the bubble to the list of bubbles.
        bubbles.append(bubble)

    # Return the list of bubbles.
    return render(request, 'my_project/home.html', {'bubbles': bubbles})