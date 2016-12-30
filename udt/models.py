from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from udt.choices import REQUEST_TYPE_CHOICES, REQUEST_VIA_CHOICES, GEO_CHOICES, FILTER_BY_TOOL_CHOICES, SEVERITY_CHOICES


class Dispatcher(models.Model):
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    requested_via = models.CharField(max_length=20, choices=REQUEST_VIA_CHOICES)
    geo = models.CharField(max_length=15, choices=GEO_CHOICES)
    filter_by_tool = models.CharField(max_length=20, choices=FILTER_BY_TOOL_CHOICES)
    task = models.CharField(max_length=250)
    assign_to = models.ForeignKey(User, related_name='work_orders')
    slug = models.SlugField(max_length=50, unique_for_date='task_received')
    task_received = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=500)
    severity = models.CharField(max_length=5, choices=SEVERITY_CHOICES)
    request_contained = models.PositiveIntegerField(default=1)
    affected_items = models.PositiveIntegerField(default=1)
    subject = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ('-task_received',)

    def __str__(self):
        return self.subject
