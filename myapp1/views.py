from .forms import CreateContactForm
from .models import ContactList
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from datetime import date
from dateutil.relativedelta import relativedelta


#Create your views here.


def home(request):
    return render(request, 'myapp1/home.html')
    
    
def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            formID = formdata['formID']
            name = formdata['name']
            gender = formdata['gender']
            address = formdata['address']
            profession = formdata['profession']
            telephone = formdata['telephone']
            email = formdata['email']
            birthday = formdata['birthday']

            ContactList.objects.create(id=formID, name=name, gender=gender, address=address, profession=profession, telephone=telephone, email=email, birthday=birthday)
            return HttpResponseRedirect('/myapp1/success')
    else:
        form = CreateContactForm()
    return render(request, 'myapp1/create_contact.html', {'form': form})
    
    
def contact_list(request):
    contact_lists = ContactList.objects.all()
    return render(request, 'myapp1/contact_list.html', {'contact_lists': contact_lists})

def contact_detail(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    return render(request, 'myapp1/contact_detail.html', {'contact': contact})

def update_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            # Update the fields of the contact instance with the form data
            contact.name = form.cleaned_data['name']
            contact.gender = form.cleaned_data['gender']
            contact.address = form.cleaned_data['address']
            contact.profession = form.cleaned_data['profession']
            contact.telephone = form.cleaned_data['telephone']
            contact.email = form.cleaned_data['email']
            contact.birthday = form.cleaned_data['birthday']
            
            contact.save()
            
            return redirect('myapp1:success') 
    else:
        # Populate the form fields with the existing data
        form = CreateContactForm(initial={
            'name': contact.name,
            'gender': contact.gender,
            'address': contact.address,
            'profession': contact.profession,
            'telephone': contact.telephone,
            'email': contact.email,
            'birthday': contact.birthday,
        })
    
    return render(request, 'myapp1/update_contact.html', {'form': form})

# Delete operation
def delete_contact(request, pk):
    contact = get_object_or_404(ContactList, pk=pk)
    current_date = date.today()
    eighteenyearsago = current_date - relativedelta(years= 18)
    if request.method == 'POST':
        if contact.birthday.date() >= eighteenyearsago:
            return redirect('myapp1:dateerror')
        else:
            contact.delete()
            return redirect('myapp1:home')
    return render(request, 'myapp1/delete_contact.html', {'contact': contact})
    
def success(request):
 return render(request, 'myapp1/success.html')


def dateerror(request):
 return render(request, 'myapp1/dateerror.html')
