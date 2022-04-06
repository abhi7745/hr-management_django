from django.urls import path

from unicorn.components.admin.add_technologies import AddTechnologiesView
from unicorn.components.admin.add_questions import AddQuestionsView
from unicorn.components.admin.update_technology import UpdateTechnologyView
from unicorn.components.admin.update_questions import UpdateQuestionsView

from hr_admin.views import *

urlpatterns = [
    # dashboard
    path("dashboard",  dashboard, name="admin.dashboard"),
    # recruiter_list
    path("recruiter_list",  recruiter_list, name="admin.recruiter_list"),
    # job_list
    path("job_list",  job_list, name="admin.job_list"),
    # job_schedules
    path("job_schedules",  job_schedules, name="admin.job_schedules"),

    # candidate_list
    path("candidate_list",  candidate_list, name="admin.candidate_list"),

    # add technologies
    path("add_technologies", AddTechnologiesView.as_view(component_name='admin.add_technologies'), name="admin.add_technologies"),
    # view_technology
    path("view_technology",  view_technology, name="admin.view_technology"),
    # update_technology
    path("update_technology/<int:pk>", UpdateTechnologyView.as_view(component_name='admin.update_technology'), name="admin.update_technology"),
    # delete_technology
    path("delete_technology/<int:pk>",  delete_technology, name="admin.delete_technology"),

    # add questions
    path("add_questions", AddQuestionsView.as_view(component_name='admin.add_questions'), name="admin.add_questions"),
    # view_questions
    path("view_questions",  view_questions, name="admin.view_questions"),
    # update_questions
    path("update_questions/<int:pk>", UpdateQuestionsView.as_view(component_name='admin.update_questions'), name="admin.update_questions"),
    # delete_questions
    path("delete_questions/<int:pk>",  delete_questions, name="admin.delete_questions"),
]
