from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# def home(request):
#     context={
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post    
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post    

class PostCreateView(LoginRequiredMixin,CreateView):
    #PostCreateView call work with Post model and automatically the form will be generated 
    #in html using the fields mentioned and no need of form file.
    model=Post   
    fields=['title','content']   

    #setting the current user loggedin to the author
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post   
    fields=['title','content']   

    #setting the current user loggedin to the author
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)    

     
   
    


def about(request):
    return render(request,'blog/about.html',{'title':'welcome to about'})