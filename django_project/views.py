from django.views import View
from django.shortcuts import render
from .models import TicketLog
from .forms import TicketLogForm, DisplayForm


class TicketLogView(View):
    def get(self, request):
        return render(request, 'index.html', {'form': TicketLogForm})

    def post(self, request):
        form = TicketLogForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid form")
        return render(request, 'index.html', {'form': form})


class TicketLogListView(View):
    def get(self, request):
        return render(request, 'display.html', {'form': DisplayForm})

    def post(self, request):
      myDay = str(request.POST["myDay"])
      myRegion = str(request.POST["myRegion"])
      tickets = TicketLog.objects.filter(day= myDay, region__name = myRegion)
      # print(tickets)
      return render(request, 'display.html', {'form': DisplayForm, 'tickets': tickets})