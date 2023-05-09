from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

#add below decorator  so that we know we have a logged in user in that view
@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")