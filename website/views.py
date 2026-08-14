from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # https://stackoverflow.com/questions/45221097/add-data-to-django-form-before-it-is-saved
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'anonymous'
            instance.save()
            messages.add_message(request, messages.INFO, 'Your message has been sent successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Please fill out the form correctly!')
    else:
        form = ContactForm()

    context = {'form': form}

    return render(request, 'website/contact.html',context)

def elements_view(request):
    return render(request, 'website/elements.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')