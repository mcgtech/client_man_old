from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Client, Note
from django.forms import modelformset_factory
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

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    # need to load notes assocaited with the client!
    note = get_object_or_404(Note, pk=1)
    blanks = 0 # increase this? - use js to hide and then show when I click add?
    NotesFormSet = modelformset_factory(Note, fields=('note', 'created_date', ), extra=blanks, can_delete=True, can_order=True) # in this we need to tell it what notest to load
    notes_form_set = [] # is this correct?
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        notes_form_set = NotesFormSet(request.POST, request.FILES)
        if form.is_valid() and notes_form_set.is_valid():
            client = form.save(commit=False)
            client.modified_by = request.user
            client.modified_date = timezone.now()
            client.save()
            notes_form_set.save();
            #return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
        #notes_form_set = NotesFormSet(instance=note)
        # get notes associated with this client
        client_notes = client.note.all # filter NotesFormSet based on this
        # notes_form_set = NotesFormSet(queryset=Note.objects.filter(person=client))
        notes_form_set = NotesFormSet(queryset=Note.objects.filter(person=client))
    #return render(request, 'client/client_edit.html', {'form': form})
    return render(request, 'client/client_edit.html', {'form': form, 'notes_form_set': notes_form_set})


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