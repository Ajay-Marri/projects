from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, ContactMessage
from django.views.generic import ListView,DetailView
from .form import commetform
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect

class dashboard(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "port"

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:3]
        

class posts(ListView):
    template_name="blog/all-posts.html"
    model=Post
    context_object_name = "recent_post"

    def get_queryset(self):
        return Post.objects.all().order_by("-date")

class post_details(View):
    def is_saved_post(self,request,post_id):
        saved_posts=request.session.get("saved_posts")
        if saved_posts is not None:
            is_saved_for_later=post_id in saved_posts
        else:
            is_saved_for_later=False

        return is_saved_for_later

    def get(self,request,slug):
        post_obj=Post.objects.get(slug=slug)
        context={
            "post":post_obj,
            "post_tag":post_obj.tag.all(),
            "comment_form":commetform(),
            "comments":post_obj.comments.all().order_by("-id")[:3],
            "saved_for_later":self.is_saved_post(request,post_obj.id)
        }
        return render(request,"blog/mainpost.html", context)

    def post(self,request,slug):
        post_obj=Post.objects.get(slug=slug)
        comment_form=commetform(request.POST)

        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.post=post_obj
            comment.save()
            return HttpResponseRedirect(reverse("post_details",args=[slug]))
        context={
            "post":post_obj,
            "post_tag":post_obj.tag.all(),
            "comment_form":comment_form,
            "comments":post_obj.comments.all().order_by("-id")[:3],
            "saved_for_later":self.is_saved_post(request,post_obj.id)
        }
        return render(request,"blog/mainpost.html", context)


class readlaterview(View):
    def get(self, request):
        context = {}
        saved_posts = request.session.get("saved_posts")

        if not saved_posts:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=saved_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/savedposts.html", context)

    def post(self, request):
        saved_posts = request.session.get("saved_posts")

        if saved_posts is None:
            saved_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in saved_posts:
            saved_posts.append(post_id)
        else:
            saved_posts.remove(post_id)

        request.session["saved_posts"]=saved_posts

        return HttpResponseRedirect("/")


class AboutPageView(TemplateView):
    template_name = "blog/about.html"

class ContactPageView(TemplateView):
    template_name = "blog/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your message has been submitted successfully!")
        return redirect("contact")

class PrivacyPolicyView(TemplateView):
    template_name = "blog/privacy_policy.html"

class TermsOfUseView(TemplateView):
    template_name = "blog/terms.html"













# def dashboard(request):
#     lastest_post=post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{
#         "port":lastest_post
#     })

# def posts(request):
#     recent_posts=post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/all-posts.html",{
#         "recent_post":recent_posts
#     })

# def post_details(request, slug):
#     identified_post = get_object_or_404(post, slug=slug)
#     return render(request, "blog/mainpost.html", {
#         "post": identified_post,
#         "post_tag":identified_post.tag.all()
#     })