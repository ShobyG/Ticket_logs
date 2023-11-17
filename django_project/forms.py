from django import forms
from .models import TicketLog, Region


class TicketLogForm(forms.ModelForm):
    class Meta:
        model = TicketLog
        fields = ["date_time", "day", "location", "region"]

    region = forms.ModelChoiceField(queryset=Region.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        date_time = cleaned_data.get('date_time')

        if date_time:
            # Calculate the 'day' based on the 'date_time'
            day = date_time.strftime(
                '%A')  # %A gives the full day name (e.g., Monday)
            cleaned_data['day'] = day

        return cleaned_data
      
class DisplayForm(forms.Form):
    days = forms.ModelChoiceField(queryset=TicketLog.objects.values('day').distinct().order_by('day').values_list('day', flat=True))
    regions = forms.ModelChoiceField(queryset=TicketLog.objects.values('region__name').distinct().order_by('region__name').values_list('region__name', flat=True))