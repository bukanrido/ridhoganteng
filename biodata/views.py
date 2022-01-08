from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


# Create your views here.
def biodata(request):
    template_name = "biodata.html"
    context = {
        'title':'biodata',
    }
    return render(request, template_name, context)
