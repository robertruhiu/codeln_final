from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Create your models here.
class Transaction(models.Model):
    # TODO: allow user to specify framework for test

    STAGE_CHOICES = (
        ('created', 'created'),
        ('upload-candidates', 'upload-candidates'),
        ('payment-stage', 'payment-stage'),
        ('make-payment', 'make-payment'),
        ('payment-verified', 'payment-verified'),
        ('complete', 'complete'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    stage = models.CharField(choices=STAGE_CHOICES, default='upload_candidate', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now=True)

    def allcandidates(self):
        candidates = Candidate.objects.filter(transaction=self.id)
        count = candidates.count()
        return candidates, count

    def amount(self):
        total_amount = self.allcandidates() * 20
        return total_amount

    def __str__(self):
        return "{},{},{}".format(self.user.username, self.project.name, self.stage)


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def generate_link(self):
        pass

    def generate_temporary_password(self):
        pass

    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)
