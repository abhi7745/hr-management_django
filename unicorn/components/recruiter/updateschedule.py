from django_unicorn.components import UnicornView

from recruiter.models import *

from django.db.models import Q # this is for multiple to conditions
from django.contrib import messages

class UpdatescheduleView(UnicornView):
    
    job: Jobs = None
    test_schedule: Test_schedule = None
    other_category = '' 

    job_category_id = ''  #job_category_id from unicorn form


    def mount(self):
        # try:
        # self.job=Jobs.objects.get(jobs_id=self.kwargs['pk'])
        # print(self.job.jobs_id,'///////////////////////')
        

 
        print('each test_schedule "id" ',self.kwargs['pk'])
        # showing specfic values
        self.test_schedule = Test_schedule.objects.get(id=self.kwargs['pk'])
        print(self.test_schedule.job_id, 'successssss')

        # for other category list purpose
        self.other_category=Test_schedule.objects.filter(~Q(job_id=self.test_schedule.job_id))
        for x in self.other_category:
            print(x.job_id,'other_category')

            # self.job_title = self.job.job_title
            # self.min_exp = self.job.min_experience
        # except:
        #     print('exception for no job available',self.kwargs['pk'])


    def update(self):
        print(self.test_schedule.job_id,'updation schedule test...............')



        # # job id
        # if self.job_category_id == '' :
        #     print('job_category_id Required.......................')
        #     self.call("toast","Error","Required Job Category","warning")
        #     messages.error(self.request,'Required Job Category',extra_tags='job_category_id')
        # date
        if self.test_schedule.date == '' :
            print('date Required.......................')
            self.call("toast","Error","Required Test Date","warning")
            messages.error(self.request,'Required Test Date',extra_tags='date')
        # descripiton
        elif self.test_schedule.description == '' :
            print('descripiton Required.......................')
            self.call("toast","Error","Required Descripiton","warning")
            messages.error(self.request,'Required Descripiton',extra_tags='descripiton')

        else:
            # self.test_schedule = Test_schedule.objects.get(id=self.job_category_id)
            # print(self.test_schedule.job_id)
            # print(self.job_category_id)

            # self.test_schedule.job_id=self.job_category_id


            self.test_schedule.save() # updating all fields from form data
            print('form saved...............')
            self.call("toast","Schedule","updated","success")