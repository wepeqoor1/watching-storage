from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visit = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            'who_entered': person_visit.passcard.owner_name,
            'entered_at': person_visit.entered_at,
            'duration': person_visit.get_duration,
        } for person_visit in visit
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
