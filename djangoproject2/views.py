from django.shortcuts import render

# Create your views here.


posts= [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27,2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_python manage.py startapp userposted': 'September 30,2018'
    }
]


def home(request):
    postList= Posts.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

