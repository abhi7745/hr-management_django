from django.urls import path
# from unicorn.components.recruiter.profile import ProfileView

from candidate.views import *

from unicorn.components.candidate.profile import ProfileView

urlpatterns = [
    path("dashboard",  dashboard, name="candidate.dashboard"),
    # profile
    path("profile", ProfileView.as_view(component_name='candidate.profile'), name="candidate.profile"),
    # search job
    path("search_job",  search_job, name="candidate.search_job"),
    # job_view
    path("job_view/<int:pk>",  job_view, name="candidate.job_view"),
    # apply
    path("apply/<int:pk>",  apply, name="candidate.apply"),
    # application_cancel
    path("application_cancel/<int:pk>",  application_cancel, name="candidate.application_cancel"),
    # applied_jobs
    path("applied_jobs",  applied_jobs, name="candidate.applied_jobs"),
]
