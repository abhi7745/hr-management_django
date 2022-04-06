from django.urls import path

from . import views

urlpatterns = [

    # account app url.py

    # basic urls
    path('recruiter/signup/',views.recruiter_signup,name='recruiter_signup_url'),
    path('candidate/signup/',views.candidate_signup,name='candidate_signup_url'),

    path('login/',views.loginpage,name='login_url'),
    
    path('logout/',views.logoutpage,name='logout_url'),

    # # HR admin area
    # path('hr/admin',views.hr_admin,name='hr_admin'),

    # # recruiter area
    # path('recruiter/profile/',views.recruiter_profile,name='recruiter_profile'),


    # # candidate area
    # path('candidate/profile',views.candidate_profile,name='candidate_profile'),
]