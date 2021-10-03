from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from bugtracker.models import Author, Ticket
from bugtracker.forms import TicketForm, TicketEdit, LoginForm, AuthorEdit
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def index_view(request):
    tickets = Ticket.objects.all()
    return render(request, 'index.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


@login_required
def user_detail(request, id):
    author = Author.objects.get(id=id)
    tickets = Ticket.objects.all()
    # originally had it as ^.filter(author=author) but that was filtering it so only tickets created by user displays
    # Thank your Marcus for the help
    return render(request, 'user_detail.html', {'author': author, 'tickets': tickets})


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket = Ticket.objects.create(
                title=data['title'],
                body=data['body'],
                author=request.user,
                # create_at=data['create_at'],
                # ticket_status=data['New'],
                # assigned_to=data['assigned_to'],
                # closed_by=data['closed_by']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = TicketForm()
    return render(request, 'form.html', {'form': form})


@login_required
def ticket_edit(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketEdit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.body = data['body']
            ticket.save()
            return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))
    form = TicketEdit(initial={
        'title': ticket.title,
        'body': ticket.body
    })
    return render(request, 'form.html', {'form': form})


@login_required
def grab_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'Progress'
    ticket.assigned_to = request.user
    ticket.closed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))


@login_required
def return_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'New'
    ticket.assigned_to = None
    ticket.closed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))


@login_required
def ticket_done(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'Done'
    ticket.closed_by = request.user
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))


@login_required
def ticket_invalid(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'Invalid'
    ticket.closed_by = None
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))


# @login_required
# def user_edit(request, id):
#     enduser = Author.objects.get(id=id)
#     if request.method == 'POST':
#         form = AuthorEdit(request.POST, instance=enduser)
#         form.save()
#         return HttpResponseRedirect(reverse('user_detail', args=(id,)))
#     form = AuthorEdit()
#     return render(request, 'form.html', {'form': form})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage'))) 
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
