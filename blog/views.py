from django.shortcuts import render

posts=[
    {
        'author':'CoreyMs',
        'title':'Blog Post 1',
        'content':'First post',
        'date_posted':'Aug 27th 2019'
    },
    {
        
        'author':'NaveenMs',
        'title':'Blog Post 2',
        'content':'second post',
        'date_posted':'June 30th 2019'
    
    }




]
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'welcome to about'})