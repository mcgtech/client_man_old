from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Client, Note
from django.forms import modelformset_factory, inlineformset_factory
from .forms import ClientForm, NoteForm
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
# https://gist.github.com/ibarovic/3092910
def manage_client(request, client_id=None):
    if client_id is None:
        client = Client()
        the_action_text = 'Create'
        is_edit_form = False
        NoteInlineFormSet = inlineformset_factory(Client, Note, form=NoteForm, extra=2, can_delete=False)
    else:
        the_action_text = 'Edit'
        is_edit_form = True
        client = get_object_or_404(Client, pk=client_id)
        NoteInlineFormSet = inlineformset_factory(Client, Note, form=NoteForm, extra=2, can_delete=True)

    if request.method == "POST":
        if request.POST.get("delete_client"):
            client = get_object_or_404(Client, pk=client_id)
            client.delete()
            return redirect('/client_list')
        form = ClientForm(request.POST, request.FILES, instance=client, prefix="main")
        formset = NoteInlineFormSet(request.POST, request.FILES, instance=client, prefix="nested")

        if form.is_valid() and formset.is_valid():
            created_client = form.save(commit=False)
            created_client.modified_by = request.user
            created_client.modified_date = timezone.now()
            created_client.save()
            formset.save()
            #return redirect('/bookauthor/formset')
    else:
        form = ClientForm(instance=client, prefix="main")
        formset = NoteInlineFormSet(instance=client, prefix="nested")

    return render(request, 'client/client_edit.html', {'form': form, 'notes_form_set': formset, 'the_action_text' : the_action_text, 'edit_form' : is_edit_form})

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