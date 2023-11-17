import django.db.models as models


class Region(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"Region: {self.name}"

class TicketLog(models.Model):
    date_time = models.DateTimeField()
    day = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=60)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket no: {self.id}, time: {self.date_time}, Street: {self.location}, Region: {self.region}"
