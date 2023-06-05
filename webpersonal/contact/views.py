from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContacForm

# Create your views here.
def contact(request):
    contact_form=ContacForm()

    if request.method == "POST":
        contact_form=ContacForm(data=request.POST)

        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            contenct=request.POST.get('contenct','')
            #configuracion corre
            email=EmailMessage(
                "Tu valle!: Tiene una nueva notificacion",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,contenct),
                "no-contestar@inbox.mailtrap.io",
                ["juansospina2288@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            
            except:
                
                return redirect(reverse('contact')+"?fail")

    return render(request,"contact/contact.html",{'form':contact_form})