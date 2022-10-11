from django.shortcuts import render
from constance import config
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

from muadh.models import Education, Experience, Message, Section, Skill, TeamMember, Testimonial
# Create your views here.
def index(request):
    context={
        "config":config,
        "skills":Skill.objects.all(),
        "experiences":Experience.objects.all(),
        "educations":Education.objects.all(),
        "teammembers":TeamMember.objects.all(),
        "testimonials":Testimonial.objects.all(),
        "sections":Section.objects.all(),
    }
    return render(request,'pages/home.html',context)

def get_person(request):
    print(request.GET.get("id"))
    person_id=request.GET.get("id",None)
    if person_id is not None:
        person = TeamMember.objects.get(id=person_id)
    else:
        person=None
    return JsonResponse({
        "name":person.name,
        "job_title":person.job_title,
        "image":person.image.url,
        "abstract":person.abstract,
    })

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def send_email_msg(to_email,msg, **kwargs):
    message = get_template("message.html").render({
        'message': msg,
    })
    mail = EmailMessage(
        subject="Portfolio message",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email],
        reply_to=[settings.EMAIL_HOST_USER],
    )
    mail.content_subtype = "html"
    return mail.send()
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from django.shortcuts import redirect
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['POST'])
@throttle_classes([OncePerDayUserThrottle])
def send_message(request):
    print(request.data)
    name = request.data.get("name")
    email = request.data.get("email")
    subject = request.data.get("subject")
    message = request.data.get("message")
    if (name,email,subject,message) is not None:
        msg=Message(name=name,email=email,subject=subject,message=message)
        msg.save()
        send_email_msg(msg=msg,to_email="Mowafifi@gmail.com")
    else:
       return redirect('index')
    return Response({"message": "Hello for today! See you tomorrow!"})