from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from ..models import User, Student, Course



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            print "yolo teacher"
            # return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:course')
    return render(request, 'classroom/home.html')



from ..forms import StudentSignUpForm


class StudentUserView(TemplateView):
    template_name = 'registration/signup.html'



# class StudentUserView(CreateView):
#     model = Student

#     template_name = 'registration/signup_form.html'
#     fields = '__all__'


#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)


#     def form_valid(self, form):
#         user = form-save()
#         login(self.request, user)
#         return redirect('students:courses')

