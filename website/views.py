from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from website.forms import contactForm,NewsLetterForm
from django.contrib import messages
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            contact = form.save(commit=False)
            contact.name = "unknown"
            form.save()
            messages.success(request,'Thanks for contact us')
        else:
            messages.error(request,'Error')
    form = contactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = NewsLetterForm()
    return HttpResponseRedirect('/')

