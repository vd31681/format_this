# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from djangoform.formater.formater_form import This
import datetime
import csv


def this(request):
    form = This(request.GET)
    if form.is_valid():
        A1 = [form.clean_segmentA1(),
              form.clean_versionA1()]
        B1 = [form.clean_segmentB1(),
              form.clean_versionB1()]


        filename = str(form.clean_segmentA1()) + "-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#         output_file = open("/home/vic/workspace/djangoform/djangoform/files/" + filename, "w")
#         output_file.write(output_utf)
#         output_file.close()
        class dialect(csv.excel):
            delimiter = '\t'
            skipinitialspace = True
            quotechar = '"'
            doublequote = True
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % (filename)
        writer = csv.writer(response, dialect=dialect)
        writer.writerow([i.encode('utf8') for i in A1])
        writer.writerow([i.encode('utf8') for i in B1])

        return response

    return render_to_response("formater/this.html", {"form": form})


