import string
import random

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.conf import settings

import models


# Create your views here.
def home(request):
    return render(request, 'home.html')


def random10():
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))


def new(request):

    party_a_id = random10()
    party_b_id = random10()

    c = models.Chat()
    c.party_a_id = party_a_id
    c.party_b_id = party_b_id
    c.save()

    return redirect(reverse('chat', kwargs={'chat_id': party_a_id}))


def chat(request, chat_id):

    c = models.Chat.objects.filter(Q(party_a_id=chat_id) | Q(party_b_id=chat_id))

    if len(c) != 1:
        return render(request, 'gone.html')

    c = c[0]

    if c.party_a_id == chat_id:
        party = "a"
        clines = models.Line.objects.filter(chat=c, party='b', seen_by_other_party=False)

    else:
        party = "b"
        clines = models.Line.objects.filter(chat=c, party='a', seen_by_other_party=False)


    for l in clines:
        l.seen_by_other_party = True
        l.save()


    if request.method == "POST":
        lines = request.POST.get("lines")
        if lines.strip() != "":
            line = models.Line()
            line.chat = c
            line.message = lines
            line.party = party
            line.save()

        return redirect(reverse('chat', kwargs={'chat_id': chat_id}))  # refresh protection.

    return render(request,'chat.html', {'c': c, 'party':party, 'base_url': settings.BASE_URL})