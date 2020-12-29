from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail as sm

def send_mail(request):
    res = sm(
        subject = 'Subject here',
        message = 'Here is the message.',
        from_email = 'bernardleigh94@gmail.com',
        recipient_list = ['bernardleigh94@gmail.com'],
        fail_silently=False,
    )    

    return HttpResponse(f"Email sent to {res} members")
    #return HttpResponse("Email sent to "+ res +" members")