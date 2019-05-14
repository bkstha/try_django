from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.


from .models import BlogPost


# def blog_post_detail_page(request, slug):
#     obj = get_object_or_404(BlogPost, slug=slug)
#     # queryset = BlogPost.objects.filter(slug=slug)
#     # if queryset.count() == 0:
#     #     raise Http404
#     # else:
#     #     obj = queryset.first()
#     # try:
#     #     obj = BlogPost.objects.get(id=id)
#     # except BlogPost.DoesNotExists:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404
#     template_name = 'blog_post_detail.html'
#     context = {"object": obj}
#     return render(request, template_name, context)


def blog_list_page(request):
    obj = BlogPost.objects.get
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)
    # return context

def blog_post_create_view(request):
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
