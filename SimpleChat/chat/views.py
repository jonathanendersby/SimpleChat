import string
import random
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.conf import settings

import models


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


def json_new(request):
    party_a_id = random10()
    party_b_id = random10()

    c = models.Chat()
    c.party_a_id = party_a_id
    c.party_b_id = party_b_id
    c.save()

    jc = {'party_a_id': c.party_a_id,
          'party_b_id': c.party_b_id,
          'party_a_url': "%s%s" % (settings.BASE_URL, reverse('json_chat', kwargs={'chat_id': c.party_a_id})),
          'party_b_url': "%s%s" % (settings.BASE_URL, reverse('json_chat', kwargs={'chat_id': c.party_b_id})),
          }

    return HttpResponse(json.dumps(jc, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


def json_chat(request, chat_id):
    c = models.Chat.objects.filter(Q(party_a_id=chat_id) | Q(party_b_id=chat_id))

    if len(c) != 1:
        return HttpResponse(json.dumps({}), content_type="application/json")

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

    if party == "a":
        jc = {'party_a_id': c.party_a_id,
              'party_b_id': c.party_b_id,
              'party_a_url': "%s%s" % (settings.BASE_URL, reverse('chat', kwargs={'chat_id': c.party_a_id})),
              'party_b_url': "%s%s" % (settings.BASE_URL, reverse('chat', kwargs={'chat_id': c.party_b_id})),
              'lines': None}
    else:
        jc = {'party_b_id': c.party_b_id, 'lines': None}
    jl = []
    for l in c.line_set.all():
        jl.append({'party': l.party,
                   'message': l.message,
                   'date_created': l.date_created,
                   'seen_by_other_party': l.seen_by_other_party})

    jc['lines'] = jl

    return HttpResponse(json.dumps(jc, indent=4, cls=DjangoJSONEncoder), content_type="application/json")


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