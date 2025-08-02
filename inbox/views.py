from django.shortcuts import render
# My import
from django.contrib.auth.decorators import login_required # Login required to access private pages
from django.views.decorators.cache import cache_control # Destroy the section after logout
from .models import Customer # From models.py
from .forms import CustomerForm, EmailForm # From forms.py
from django.contrib import messages # Return messages
from django.http import HttpResponseRedirect # Redirect the pages
from django.core.paginator import Paginator # Pagination
from django.db.models import Q # Global search
from datetime import datetime # Used (in this example) to get message received today
from django.core.mail import EmailMessage # Send emails
from django.contrib.auth import logout # Used to get auto logout




# |==================== FRONTEND =====================|
# Function to home(front-end)
def home(request):
    return render(request, 'inbox/home.html')


# Function to send a message.
def send_message(request):
    if request.method == "POST" and request.FILES.get('file'):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        file = request.FILES['file']

        customer = Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message,
            file=file
        )
        customer.save()
        messages.success(request, 'Message sent successfully..!')
        return HttpResponseRedirect('/')
    return render(request, 'inbox/home.html')


# |==================== BACKEND =====================|
# Function to inbox(back-end)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_customer_list = Customer.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) |
            Q(email__icontains=q) | Q(subject__icontains=q) |
            Q(status__icontains=q) | Q(message__icontains=q)
        ).order_by('-created_at')
    else:
        all_customer_list = Customer.objects.all().order_by('-created_at')
    paginator = Paginator(all_customer_list, 5)
    page = request.GET.get('page')
    all_customer = paginator.get_page(page)
    # ------------------------ MESSAGES COUNTER -------------------- |
    # -- 1 --// TOTAL // ----- |
    total = Customer.objects.all().count()
    # -- 2 --// READ // ----- |
    read = Customer.objects.filter(status='Read')
    # -- 3 --// UNREAD // ----- |
    unread = Customer.objects.filter(status='Pending')
    # -- 4 --// TODAY // ----- |
    base = datetime.now().date()
    today = Customer.objects.filter(created_at__gt=base)

    context = {
        'customers': all_customer,
        'total': total,
        'read': read,
        'unread': unread,
        'today': today,
    }
    return render(request, 'inbox/inbox.html', context)


# Function to delete the messages.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_message(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    messages.success(request, "Message successfully deleted !")
    return HttpResponseRedirect('/inbox')


# Function to view the message individually.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if customer != None:
        return render(request, 'inbox/customer.html', {'customer': customer})
    

# Function to mark the message as read.
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mark_message(request):
    if request.method == 'POST':
        customer = Customer.objects.get(id=request.POST.get('id'))
        if customer != None:
            customer.status = request.POST.get('status')
            customer.save()
            messages.success(request, "Message marked as READ !")
            return HttpResponseRedirect('/inbox')
        

# Function to reply the message.
def email(request):
    if request.method == 'POST':

        company = "Reply MessageBox"

        subject = request.POST.get('subjects')
        message = request.POST.get('message')
        email = request.POST.get('email')
        cc = request.POST.get('cc')
        files = request.FILES.getlist('attach')

        mail = EmailMessage(subject, message, company, [cc], [email])
        for f in files:
            mail.attach(f.name, f.read(), f.content_type)
        mail.send()

        messages.success(request, "Reply sent successfully !")
        return HttpResponseRedirect('/inbox')


# Auto Logout Function.
def AutoLogoutUser(request):
    logout(request)
    request.user = None
    messages.info(request, ".") # I put dot because the argument cannot be empty.
    return HttpResponseRedirect('/')