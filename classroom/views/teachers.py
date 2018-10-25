# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Count, F, Value
from django.db.models import Exists, OuterRef


from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView


from django.contrib.auth.decorators import login_required
from django.db import transaction

from ..models import User, Student, Course

from ..forms import   TeacherSignUpForm
from ..decorators import teacher_required


from django.utils import timezone
# from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import Paragraph, Table, TableStyle
# from reportlab.lib.enums import  TA_LEFT, TA_CENTER
# from reportlab.lib import colors

# from io import BytesIO


# def coord(x, y, unit=1):
#     from reportlab.lib.pagesizes import A4, cm
#     width, height = 600, 700
#     x, y = x * unit, height - y * unit
#     return x, y

# def create_pdf(query, table_headers,query_data):
#     from reportlab.lib.units import inch
#     import math
#     TopMargin = 5 * inch
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Report File.pdf"'
#     width, height = A4
#     buffer = BytesIO()

#     p = canvas.Canvas(buffer, pagesize=(700,1050))

#     # p.drawString(5, ,40 "Report generated at " + timezone.now().strftime('%b %d, %Y %H:%M:%S'))
#     pages=len(query_data)/20
#     pages=math.ceil(pages)
#     c=20
#     for i in range(pages):
#         if c==20:
#             data=[table_headers]+query_data[:c]
#             c+=20
#         else:
#             try:
#                 data=[table_headers]+query_data[c:c+20]
#                 c+=20
#             except Exception as e:
#                 return Response(str(e), 422)
#                 pass
#         table = Table(data)

#         table.setStyle(TableStyle([
#             ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#             ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#         ]))
#         table.wrapOn(p, width, height)
#         # table.wrapOn(p, width, height)
#         table.drawOn(p, *coord(1, 4, cm))
#         p.showPage()

#     p.save()
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherSignUpView, self).get_context_data(**kwargs)
        context['user_type'] = 'teacher'
        return context


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:course_list')


@method_decorator([login_required, teacher_required], name='dispatch')
class CourseList(ListView):

    model = Course
    context_object_name = 'courses'
    template_name = 'classroom/teachers/course_list.html'


    def get_queryset(self, **kwargs):
        # courses = self.kwargs['course']
        #returns the students enrolled in a course
        students_applied = super(CourseList, self).get_queryset().filter(course__isnull = False)
        print "---------"
        return students_applied


        # students_applied = list(students_applied)
        # print "---------"

        # for course in students_applied:
        #     course = type(course)
        #     print course

        #     # if "MATH" in course:
        #     #     print "yolo"
        #     # else:
        #     #     print "none"
        # print(students_applied)




    def get_context_data(self, **kwargs):
        context = super(CourseList, self).get_context_data(**kwargs)
        # context['students'] = self.get_object().count()


        return context


    def get_data(request):
        count = Course.objects.all().count()
        context = {'count': count}
        print (context)
        return render(request, 'classroom/teachers/course_list.html', context)











