from django.urls import path
from unicorn.components.recruiter.profile import ProfileView
from unicorn.components.recruiter.jobpost import JobpostView
from unicorn.components.recruiter.applied_candidates import AppliedCandidatesView
from unicorn.components.recruiter.scheduletest import ScheduletestView
from unicorn.components.recruiter.updatejob import UpdatejobView
from unicorn.components.recruiter.updateschedule import UpdatescheduleView

from recruiter.views import * # Function based views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # dashboard
    path("dashboard",  login_required(dashboard), name="recruiter.dashboard"),
    # profile
    path("profile", login_required(ProfileView.as_view(component_name='recruiter.profile')), name="recruiter.profile"),
    # add job
    path("jobpost", login_required(JobpostView.as_view(component_name='recruiter.jobpost')), name="recruiter.jobpost"),
    # list all jobs
    path("joblist",  login_required(joblist), name="recruiter.joblist"),
    # update jobs
    path("updatejob/<int:pk>", login_required(UpdatejobView.as_view(component_name='recruiter.updatejob')), name="recruiter.updatejob"),
    # delete jobs
    path("deletejob/<int:pk>", login_required(deletejob), name="recruiter.deletejob"),
    # schedule a test
    path("scheduletest", ScheduletestView.as_view(component_name='recruiter.scheduletest'), name="recruiter.scheduletest"),
    # schedule list
    path("schedulelist",  login_required(schedulelist), name="recruiter.schedulelist"),
    # update schedule
    path("updateschedule/<int:pk>", login_required(UpdatescheduleView.as_view(component_name='recruiter.updateschedule')), name="recruiter.updateschedule"),
    # delete schedule
    path("deleteschedule/<int:pk>", login_required(deleteschedulelist), name="recruiter.deleteschedule"),

    # applied candidates list
    path("applied_candidates",  login_required(applied_candidates), name="recruiter.applied_candidates"),
    
    # candidates_view
    path("candidate_view/<int:pk>",  login_required(candidate_view), name="recruiter.candidate_view"),

    # path("abc", AppliedCandidatesView.as_view(component_name='recruiter.applied_candidates'), name=""),
]

