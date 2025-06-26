from django.shortcuts import render, redirect
import datetime
from .models import Blog, Subscriber
import markdown
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.core.mail import send_mail
from .forms import SubscriberForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {"x": "Welcome to django"})

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string": "Hello World",
        "my_date": datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
    }
    return render(request, 'filters.html', context)

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs': blogs})    

# def subscribe(request):
#  if request.method =='POST':
#     email = request.POST['email']
#     if Subscriber.objects.filter(email=email).exists():
#         messages.error(request, 'you are already subscribed')
#     else: 
#         subscriber = Subscriber(email=email)
#         subscriber.save()
#         messages.success(request, 'Thank you for subscribing')
#         return redirect('subscribe')
#  return render(request, 'subscribe.html')

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, "This email is already subscribed.")
            else:
                form.save()
                # Send confirmation email
                send_mail(
                    subject='Subscription Confirmation',
                    message='Thank you for subscribing to our newsletter!',
                    from_email='your_email@example.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
                messages.success(request, "Subscribed successfully! Confirmation email sent.")
                return redirect('subscribe')
    else:
        form = SubscriberForm()
    
    return render(request, 'subscribe.html', {'form': form})

