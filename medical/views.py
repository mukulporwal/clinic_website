from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
# from appointments.forms import AppointmentForm
from django.conf import settings
from indexapp.models import maincarousel, mainbox, difcontent
from serviceapp.models import fertiService, endometriosis, laparoscopy, riskdelivery
from blogapp.models import blogdata

def index(request):
    carousel = maincarousel.objects.all()
    boxes = mainbox.objects.all()
    difcont = difcontent.objects.all()

    indexdic = {'carousel':carousel,'boxes':boxes,'difcont':difcont}
    
    return render(request, 'index.html', indexdic)

def about(request):
    return render(request, 'about.html')

def servicespage(request):
    endoservices=endometriosis.objects.all()
    ferservices=fertiService.objects.all()
    lapaservices = laparoscopy.objects.all()
    highdelservices = riskdelivery.objects.all()

    context={'ferservices':ferservices,
             'endoservices':endoservices,
             'lapaservices':lapaservices,
             'highdelservices':highdelservices
             }


    return render(request, 'services.html', context)

def fertility(request,id):
    fertility=fertiService.objects.get(id=id)
    fertidic = {'fertility':fertility}
    return render(request, 'fertility.html', fertidic)

def endometriosispage(request,id):
    endo=endometriosis.objects.get(id=id)
    endodic = {'endo':endo}
    return render(request, 'endometriosis.html', endodic)

def laparoscopypage(request,id):
    lapa=laparoscopy.objects.get(id=id)
    lapadic = {'lapa':lapa}
    return render(request, 'laparoscopy.html', lapadic)

def riskdeliverypage(request,id):
    highdel=riskdelivery.objects.get(id=id)
    highdeldic = {'highdel':highdel}
    return render(request, 'riskdelivery.html', highdeldic)

def Blog(request):

    blogitems = blogdata.objects.all()

    blogdic = {'blogitems':blogitems}

    return render(request, 'Blog.html', blogdic)


def blog_detail(request, id):
    blogdetail = blogdata.objects.get(id=id)
    blogdetaildic = {'blogdetail':blogdetail}
    return render(request, 'blog_detail.html', blogdetaildic)

def contact(request):
    return render(request, 'contact.html')

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        appointment_date = request.POST.get('appointment_date')
        message = request.POST.get('message')
            
            # Email bhejne ka code
        subject = "New Appointment"
        message = f"""
            New appointment :
            Name: {name}
            Email: {email}
            Phone: {phone}
            Date: {appointment_date}
            Message: {message}
            """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['mukultech2002@gmail.com']  # Yahan par aap apna email address daal sakte hain
            
        send_mail(subject, message, from_email, recipient_list)
            
        return redirect('book')
    
    return render(request, 'book.html')

def gallery(request):
    return render(request, 'gallery.html')

