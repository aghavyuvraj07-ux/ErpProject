from django.db import models


class LeadSource(models.Model):
    SourceId = models.AutoField(primary_key=True)
    SourceName = models.CharField(max_length=40)

    class Meta:
        db_table = "tbllead_sources"

    def __str__(self):
        return self.SourceName


class Leads(models.Model):
    LeadId = models.AutoField(primary_key=True)
    CandidateName = models.CharField(max_length=40)
    Source = models.ForeignKey(LeadSource, on_delete=models.CASCADE)
    Qualification = models.CharField(max_length=40)
    EmailAddress = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=20)

    class Meta:
        db_table = "tblleads"

    def __str__(self):
        return self.CandidateName