from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Event, Project, Update
from .forms import UserAccountForm
from django.utils import timezone

def index(request):
    if request.user.is_authenticated:
        return render(request, 'club/index.html')
    else:
        return render(request, 'club/splash.html')

def about(request):
    return render(request, 'club/about.html')

def user_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserAccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            
            messages.success(request, 'Successfully updated your profile!')

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserAccountForm({'first_name':request.user.first_name,'last_name':request.user.last_name})

    return render(request, 'registration/account.html', {'form':form})

# EVENTS
def event_index(request):
    '''
    Display upcoming and past Events. Also shows a Google Calendar widget displaying all
    events.

    **Context**

    ``upcoming_events``
        A list of all non-hidden :model:`club.Event` that start on or after the current day.
    
    ``past_events``
        A list of all non-hidden :model:`club.Event` that ended before the current day. 

    **Template:**

    :template:`club/events/index.html`
    '''
    today = timezone.now().date()

    upcoming_events = Event.objects.filter(start__gt=today, hidden=False).order_by('start')
    past_events = Event.objects.filter(end__lt=today, hidden=False).order_by('created_at')

    return render(request, 'club/events/index.html', {'upcoming_events':upcoming_events, 'past_events':past_events})

def event_detail(request, event_id):
    '''
    Display an individual :model:`club.Event`.

    **Context**

    ``event``
        An instance of :model:`club.Event`.
    ``ongoing``
        Whether the event is ongoing at the moment.
    ``past``
        Whether the event ended in the past.
    ``show_attendance_code``
        Whether or not to show the event attendance code (for Core Team members).

    **Template:**

    :template:`club/events/detail.html`
    '''
    event = get_object_or_404(Event, pk=event_id)
    ongoing = event.start <= timezone.now() <= event.end
    past = event.end < timezone.now()

    # Handle form submissions
    if request.method == 'POST':
        if 'create-document' in request.POST and request.POST['create-document'] == 'meeting-notes':
            messages.success(request, 'Successfully created meeting notes document!')
            event.create_meeting_notes()
        if 'attendance-code' in request.POST:
            if request.POST['attendance-code'] == event.attendance_code:
                # Member submitted correct attendance code
                if ongoing:
                    messages.success(request, 'Successfully recorded your attendance. Thanks for coming!')
                    # TODO: actually record attendance
                else:
                    messages.error(request, 'You can only submit an attendance code during the event! Please let a Core Team member know if you have an issue.')
            else:
                # Member submitted incorrect code
                messages.warning(request, 'Wrong attendance code. Please make sure you\'re on the right event and have typed in the code correctly.')
    
    show_attendance_code = 'show_attendance_code' in request.GET and request.GET['show_attendance_code'] == '1'

    return render(request, 'club/events/detail.html', {'event':event, 'ongoing':ongoing, 'past':past, 'show_attendance_code':show_attendance_code})

def project_index(request):
    '''
    Display all :model:`club.Project` that users have created.

    **Context**

    ``projects``
        A list of all projects, ordered by most recently updated.
    
    **Template:**

    :template:`club/projects/index.html`
    '''
    projects = Project.objects.all().order_by('updated_at')

    return render(request, 'club/projects/index.html', {'projects':projects})

def update_index(request):
    '''
    Lists all club :model:`club.Update` (posts, news, recaps, etc.)

    **Context**
        ``updates`` List of all non-hidden updates ordered by creation date
    '''
    updates = Update.objects.filter(hidden=False).order_by('created_at')
    return render(request, 'club/updates/index.html', {'updates':updates})

def update_detail(request, update_id):
    '''
    Display a specific update (post, news, recap, etc.) and comments.

    **Context**
        ``update`` The :model:`club.Update` to display

    **Template**
    :template:'club/updates/detail.html'
    '''
    update = get_object_or_404(Update, pk=update_id)
    return render(request, 'club/updates/detail.html', {'update':update})

@login_required
def member_index(request):
    members = User.objects.all()
    return render(request, 'club/members/index.html', {'members':members})