from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Link
from .forms import LinkForm


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }

    return render(request, 'LinkBlink/index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()  # increment click counter

    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        # while posting form data
        form = LinkForm(request.POST)

        if form.is_valid():
            # save data on databse & redirect to homepage
            form.save()
            return redirect(reverse('home'))

    # for GET request
    form = LinkForm()
    context = {
        "form": form
    }

    return render(request, 'LinkBlink/create.html', context)
