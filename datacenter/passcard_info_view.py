from datacenter.models import Passcard
from datacenter.models import Visit, format_values
from django.shortcuts import get_list_or_404, get_object_or_404, render


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visit = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = [
        {
            'entered_at': person_visit.entered_at,
            'duration': format_values(person_visit.get_duration),
            'is_strange': person_visit.is_visit_long
        } for person_visit in visit
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
