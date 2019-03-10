from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import get_template
# Create your views here.
posts=models.Post.objects.all()

def home(request):
    clients=models.Client.objects.all()
    context={
        'title':'home',
        'posts':posts,
        'clients':clients

    }
    return render (request,'kibz/home.html',context)

def about_us(request):
    teamprofiles_list=models.TeamProfile.objects.all()
    companygalleries_list=models.CompanyGallery.objects.all()
    paginator = Paginator(teamprofiles_list, 4)
    paginator2=Paginator(companygalleries_list,2)


    page = request.GET.get('page')
    page2 = request.GET.get('page')
    teamprofiles = paginator.get_page(page)
    companygalleries=paginator2.get_page(page2)

    context={
        'title':'about-us',
        'teamprofiles':teamprofiles,
        'companygalleries':companygalleries
    }
    return render(request,'kibz/team-page.html',context)
def services(request):
    context={
        'title':'services'
    }
    return render(request,'kibz/services.html',context)
def music(request):
    artists=models.Artist.objects.all()
    
    context={
        'title':'music',
        'artists':artists,
    }
    return render(request,'kibz/music.html',context)

def gallery(request):
    posts_list=models.Post.objects.all()
    paginator=Paginator(posts_list,4)
    page=request.GET.get('page')
    gallery_posts=paginator.get_page(page)

    video_list=models.Video.objects.all()
    paginator2=Paginator(video_list,4)
    page2=request.GET.get('page')
    video_galleries=paginator2.get_page(page2)
    context={
        'title':'gallery',
        'gallery_posts':gallery_posts,
        'video_galleries':video_galleries
        }
    return render(request,'kibz/gallery.html',context)
def blog(request):
    post_list=models.Post.objects.all()
    paginator=Paginator(post_list,3)
    page=request.GET.get('page')
    blog_posts=paginator.get_page(page)
    context={
        'title':'blog',
        'blog_posts':blog_posts
    }
    return render(request,'kibz/blog.html',context)

def blog_detail(request,pk):
    blog_post=get_object_or_404(models.Post,pk=pk)
    recent_posts=models.Post.objects.order_by('-created_on')[:5]
    context={
        'blog_post':blog_post,
        'title':'blog_detail',
        'recent_posts':recent_posts

    }
    return render(request,'kibz/blog_detail.html',context)

def contact(request):
    context={
        'title':'contact'
    }
    if request.method == 'GET':
        return render(request,'kibz/contact.html',context)
     
    else:
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        name = request.POST.get('name', '')
        print(subject)
        try:
            send_mail(
                subject,
                get_template('kibz/email.html').render(
                        {'subject': subject,
                            'message': message,
                            'from_email': from_email,
                            'name': name
                         }
                ),
                from_email,
                ['customengineeringugltd@gmail.com','aggrey256@gmail.com'],
                fail_silently=False
                )
            messages.success(request, ' Thank You ,Email Sent Successfully')
            return render(request, "kibz/contact.html",context)
        except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # messages.success(request, ' Thank You ,Email Sent Successfully')
           
    return render(request, "kibz/contact.html",context)
