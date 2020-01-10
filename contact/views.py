from .forms import ContactForm
from django.contrib import auth, messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_subject = request.POST.get(
                'contact_subject'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Message Sent Successfully!')
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })