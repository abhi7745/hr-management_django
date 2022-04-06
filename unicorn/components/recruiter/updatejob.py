from django_unicorn.components import UnicornView

from recruiter.models import Jobs
from django.contrib import messages

from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


class UpdatejobView(UnicornView):
    # job_title= ''
    # min_exp=''
    job: Jobs = None
    
    def mount(self):
        try:
            print('true////////////////////////')
            print('each joblist "id" ',self.kwargs['pk'])
            self.job = Jobs.objects.get(jobs_id=self.kwargs['pk'])
            print(self.job.job_title, 'successssss')

            # self.job_title = self.job.job_title
            # self.min_exp = self.job.min_experience
        except:
            print('exception for no job available',self.kwargs['pk'])

    def update(self):
        try:
            print(self.job.job_title,'updation ...............')

            # job_title
            if self.job.job_title == '' :
                print('Job Title.......................')
                self.call("toast","Error","Required Job Title","warning")
                messages.error(self.request,'Required Job Title',extra_tags='jobtitle')

            # min_exp 
            elif self.job.min_experience == '':
                print('Minimum Exp.......................')
                self.call("toast","Error","Required Minimum Experience","warning")
                messages.error(self.request,'Required Minimum Experience',extra_tags='min_exp')

            elif (int(self.job.min_experience) < 0  or int(self.job.min_experience) > 20):
                print('Minimum Exp Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='min_exp_case2')
            # max_exp
            elif self.job.max_experience == '' :
                print('Maximum Exp.......................')
                self.call("toast","Error","Required Maximum Experience","warning")
                messages.error(self.request,'Required Maximum Experience',extra_tags='max_exp')

            elif (int(self.job.max_experience) < 0  or int(self.job.max_experience) > 20):
                print('Maximum Exp Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='max_exp_case2')
            # min_salary
            elif self.job.min_salary == '':
                print('min_salary .......................')
                self.call("toast","Error","Required Minimum Salary","warning")
                messages.error(self.request,'Required Minimum Salary',extra_tags='min_salary')
                
            elif (int(self.job.min_salary) < 7000):
                print('min_salary Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='min_salary_case2')
            # max_salary
            elif self.job.max_salary == '':
                print('max_salary .......................')
                self.call("toast","Error","Required Maximun Salary","warning")
                messages.error(self.request,'Required Maximun Salary',extra_tags='max_salary')
                
            elif (int(self.job.max_salary) < 7000):
                print('max_salary Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='max_salary_case2')
            # location
            elif self.job.location == '':
                print('location .......................')
                self.call("toast","Error","Required Location","warning")
                messages.error(self.request,'Required Location',extra_tags='location')
            # descripiton
            elif self.job.discription == '':
                print('descripiton .......................')
                self.call("toast","Error","Required Descripiton","warning")
                messages.error(self.request,'Required Descripiton',extra_tags='descripiton')
            # qualification
            elif self.job.qualification == '':
                print('qualification .......................')
                self.call("toast","Error","Required Qualification","warning")
                messages.error(self.request,'Required Qualification',extra_tags='qualification')
            # certification
            elif self.job.certification == '':
                print('certification .......................')
                self.call("toast","Error","Required Certification","warning")
                messages.error(self.request,'Required Certification',extra_tags='certification')
            # vacancies
            elif self.job.vacancies_no == '':
                print('vacancies .......................')
                self.call("toast","Error","Required Vacancies","warning")
                messages.error(self.request,'Required Vacancies',extra_tags='vacancies')
                
            elif (int(self.job.vacancies_no) <= 0):
                print('vacancies Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='vacancies_case2')
            # closing Date
            elif self.job.closing_date == '':
                print('closing_date .......................')
                self.call("toast","Error","Required Closing Date","warning")
                messages.error(self.request,'Required Closing Date',extra_tags='closing_date')

            else:
                # # db object             #form edit field data
                # self.job.job_title = self.job.job_title
                # self.job.min_experience = self.job.min_experience

                # instance of Jobs - filter with dynamic value pk
                self.job.save() # updating all fields from form data
                print('form saved...............')
                self.call("toast","Job","updated","success")

        except:
            print('Exception error .......................')
            self.call("toast","Error","Server Error","warning")