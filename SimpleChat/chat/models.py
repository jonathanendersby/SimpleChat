from django.utils import timezone
from django.db import models

class Chat(models.Model):
    """
    Stores the Organisation which ties users together and stores a credit balance.
    """
    party_a_id = models.CharField(max_length=10, db_index=True)
    party_b_id = models.CharField(max_length=10, db_index=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)


class Line(models.Model):
    chat = models.ForeignKey(Chat)
    message = models.CharField(max_length=512)
    party = models.CharField(max_length=1)  # 'a' or 'b'
    date_created = models.DateTimeField(auto_now_add=True)
    seen_by_other_party = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def ago(self):
        delta = timezone.now() - self.date_created

        if delta.days:
            return "%s days ago" % delta.days
        elif delta.seconds > 3600:
            return "%s hours ago" % int(delta.seconds/3600)
        elif delta.seconds > 60:
            return "%s minutes ago" % int(delta.seconds/60)
        else:
            return "Seconds ago."
