from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Client
from .forms import ClientForm
# from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'client/home_page.html', {})

def client_list(request):
    clients = Client.objects()
    return render(request, 'client/client_list.html', {'clients': clients})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.modified_by = request.user
            client.modified_date = timezone.now()
            client.save()
            # return redirect('client_detail', pk=post.pk)
    else:
        form = ClientForm()
    return render(request, 'client/client_edit.html', {'form': form})