# views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event
from .forms import EventForm

def countdown_timer(request):
    events = Event.objects.all()
    event_data = []
    for event in events:
        time_remaining = event.event_date - timezone.now()
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            "name": event.name,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
        event_data.append(data)
    return render(request, 'home/myapp.html', {'events': event_data})

def add_edit_event(request, event_id=None):
    if event_id:
        event = Event.objects.get(pk=event_id)
    else:
        event = None
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('countdown_timer')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'home/event_form.html', {'form': form})