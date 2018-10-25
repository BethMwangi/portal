from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from  .models import Course, Student,  User


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super(TeacherSignUpForm, self).save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super(StudentSignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user






class StudentCourseForm(forms.ModelForm):
    CATEGORIES = (
        ( 'MATH', 'Mathematics'),
        ( 'SCI', 'Science'),
        ( 'COMP', 'COMPUTER'),
        ( 'ENG', 'English'),
        ( 'PHYC', 'Physics'),
        )

    course = forms.ChoiceField(choices=CATEGORIES, required=True)

    class Meta:
        model = Course

        exclude = ('user',)


        def save(self):
            course = super(StudentCourseForm, self).save(commit=False)
            course.first_name = self.cleaned_data["first_name"]
            course.last_name = self.cleaned_data["last_name"]
            course.course = self.cleaned_data["course"]
            course.save()
            student_course = Course.objects.create(course=course)
            return course




# class StudentCourseForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         fields = ("course", "subject")

#     @transaction.atomic
#     def save(self):
#         course = super(StudentCourseForm, self).save(commit=False)
#         course.course = self.cleaned_data["course"]
#         course.subject = self.cleaned_data["subject"]
#         course.save()
#         course = Course.objects.create(course=course)
#         return course