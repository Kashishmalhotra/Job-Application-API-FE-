from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        title = request.POST.get("title")  # Corrected to "title"
        api_url = f'http://127.0.0.1:8000/jobs/{title}/'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        job_data = response.json()
        if response.status_code == 200:
            return render(request, 'job_details.html', {'job_data': job_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch job details. Please try again!'})
    
    return render(request, 'index.html')
