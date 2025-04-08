from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, 'new_year/index.html', {
        'new_year': "YES" if now.year == 1 and now.month == 1 else "NO",
    })