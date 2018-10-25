# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..decorators import student_required


from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import  ListView, UpdateView, FormView
from django.views.generic.edit import CreateView


from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.db import transaction

from ..models import User, Student, Course

from ..forms import StudentSignUpForm, StudentCourseForm


class StudentUserView(CreateView):
    model = User
    form_class = StudentSignUpForm

    template_name = 'registration/signup_form.html'
    # success_url = 'success'


    def get_context_data(self, **kwargs):
        context = super(StudentUserView, self).get_context_data(**kwargs)
        context['user_type'] = 'student'
        return context

        # return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:course')

@method_decorator([login_required, student_required], name='dispatch')
class CourseView(CreateView):
    model = Course
    form_class = StudentCourseForm
    # fields = ('first_name', 'last_name', )

    template_name = 'classroom/students/course.html'

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context['user_type'] = 'student'

        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()

        return HttpResponseRedirect('/')

        # return redirect('students:')


# def courseView(request):
#     course = get_object_or_404(Course)
#     student = request.user.student

#     if request.method == 'POST':
#         form = StudentCourseForm(first_name=first_name, last_name=last_name, course=course)
#         if form.is_valid():
#             obj.first_name = form.cleaned_data['first_name']
#             obj.last_name = form.cleaned_data['last_name']
#             obj.course = form.cleaned_data['course']
#             obj.save()

#             return HttpResponseRedirect('/student_course') # Redirect after POST

    #     else:
    #         form = StudentCourseForm(first_name=first_name, last_name=last_name, course=course)

    # return render(request, 'classroom/students/course.html', {


    #     'form': form,

    # })

