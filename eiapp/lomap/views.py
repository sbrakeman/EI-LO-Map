
 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

import numpy as np
import matplotlib.pyplot as plt

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class LO(TemplateView):
	def get(self, request, **kwargs):
		scope = ["https://spreadsheets.google.com/feeds"]
		creds = ServiceAccountCredentials.from_json_keyfile_name("lomap/client_secret.json", scope)
		client = gspread.authorize(creds)
		sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Fs_bF37oMIR7j71GTgVh_-V1v50s_lcMt0KwOk868qY/edit#gid=619321339").sheet1
		values_lists = sheet.col_values(3)
		lo_counts = {}
		for lo in values_lists:
			if lo in lo_counts:
				lo_counts[lo] += 1
			else:
				lo_counts[lo] = 1
		del lo_counts['']
		context = {}
		context['lo_counts'] = lo_counts

		return render(request, 'index.html', context)
