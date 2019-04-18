from django.shortcuts import render
from django.views.generic import TemplateView
import csv


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        with open('inflation_russia.csv', newline='', encoding='utf8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar=' ')
            file_list = list(f)
            header = file_list.pop(0)
            context = {
                'header': header,
                'file_list': file_list}
        return render(request, self.template_name,
                      context)