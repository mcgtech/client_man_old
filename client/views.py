from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Client, Note
from django.forms import modelformset_factory, inlineformset_factory
from .forms import ClientForm
# from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'client/home_page.html', {})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client/client_detail.html', {'client': client})


# http://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created
def manage_client(request, id):
    if id:
        # if this is an edit form, replace the client instance with the existing one
        client = get_object_or_404(Client, pk=id)
    else:
        client = Client()
    client_form = ClientForm(instance=client) # setup a form for the parent

    NotesFormSet = inlineformset_factory(Client, Note, fields=('note', 'created_date', ), extra=1, can_delete=True, can_order=True)
    notes_form_set = NotesFormSet(instance=client)

    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if id:
            client_form = ClientForm(request.POST, instance=client)
        notes_form_set = NotesFormSet(request.POST, request.FILES)
        if client_form.is_valid():
            created_client = client_form.save(commit=False)
            created_client.modified_by = request.user
            created_client.modified_date = timezone.now()
            notes_form_set = NotesFormSet(request.POST, request.FILES, instance=created_client)
            if notes_form_set.is_valid():
                created_client.save()
                notes_form_set.save()
                #return HttpResponseRedirect(created_client.get_absolute_url())

    return render(request, 'client/client_edit.html', {'form': client_form, 'notes_form_set': notes_form_set})


def client_new(request):
    return manage_client(request, None)


def client_edit(request, pk):
    return manage_client(request, pk)


def fs_test(request):
    blanks = 1
    ClientFormSet = modelformset_factory(Client, fields=('first_name', 'last_name'), extra=blanks, can_delete=True, can_order=True)
    if request.method == 'POST':
        formset = ClientFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            formset.save();
            pass
    else:
        formset = ClientFormSet()
    return render(request, 'client/fs_test.html', {'formset': formset})