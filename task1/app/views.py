from django.shortcuts import render
from django.views.generic import TemplateView
import csv

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        with open('inflation_russia.csv', newline='', encoding='utf8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar=' ')
            file_list = []
            for line in f:
                file_list.append(line)
            new_file_list = []
            header = file_list.pop(0)
            for line in file_list:
                new_line = []

                for i, el in enumerate(line):
                    if i == 0:
                        new_line.append(el)
                        continue
                    try:
                        new_line.append(float(el))
                    except ValueError:
                        new_line.append('')
                        continue
                new_file_list.append(new_line)

            context = {
                'header': header,
                'file_list': new_file_list}
        return render(request, self.template_name,
                      context)