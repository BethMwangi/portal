from django.conf.urls import include, url

from .views import students, teachers, classroom



urlpatterns = [
    url(r'^$', classroom.home, name='home'),
    # url(r'^$student_course/', classroom.home, name='student_course'),
    url(r'^students/', include(([
        url(r'^', students.CourseView.as_view(), name='course')
    ], 'classroom'), namespace='students')),

    url(r'^teachers/', include(([
        url(r'^', teachers.CourseList.as_view(), name='course_list')
    ], 'classroom'), namespace='teachers')),

]




