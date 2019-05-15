from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm


def home_page(request):
    my_title = "Hello Bikash"
    # doc ="<h1>{title}</h1>".format(title=title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "home.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "About Page"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html", context)


def example_page(request):
    context = {"title": "Example"}
    something_here = "hello_world.html"
    template_obj = get_template(something_here)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
