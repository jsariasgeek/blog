from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Entry


# Create your views here.

class EntryList(ListView):
	model = Entry


class EntryDetail(DetailView):
	model = Entry

	def get_object(self, *args, **kwargs):
		entry_id = self.kwargs.get('id')
		obj = get_object_or_404(Entry, id=entry_id)
		return obj

