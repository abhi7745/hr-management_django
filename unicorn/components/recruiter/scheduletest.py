from time import time
from django_unicorn.components import UnicornView

from recruiter.models import Jobs, Recruiter, Test_schedule
from django.contrib import messages
from django.contrib.auth.models import User

class ScheduletestView(UnicornView):
    # pass

    job_category_id = ''
    date = ''
    # time = ''
    descripiton: str = ''

    job: Jobs = None

    def mount(self):
        # try:
        # passing recruiter all job_titles to html form
        self.job = Jobs.objects.filter(recruiter_id=self.request.user.id)
        print(self.request.user.id,'job count',self.job.count())
        for x in self.job:
            print(x.job_title, 'successssss')
        # except:
        #     print('exception for')


    def save(self):

        print(self.job_category_id)
        print(self.date)
        # print(self.time)
        print(self.descripiton)

        # job id
        if self.job_category_id == '' :
            print('job_category_id Required.......................')
            self.call("toast","Error","Required Job Category","warning")
            messages.error(self.request,'Required Job Category',extra_tags='job_category_id')
        # date
        elif self.date == '' :
            print('date Required.......................')
            self.call("toast","Error","Required Test Date","warning")
            messages.error(self.request,'Required Test Date',extra_tags='date')
        # descripiton
        elif self.descripiton == '' :
            print('descripiton Required.......................')
            self.call("toast","Error","Required Descripiton","warning")
            messages.error(self.request,'Required Descripiton',extra_tags='descripiton')
        # # already exist
        # elif Test_schedule.objects.filter(date=self.date).exists():
        #     print('schedule already exist.......................')
        #     self.call("toast","Error","Schedule already exist","warning")
        #     messages.error(self.request,'Schedule already exist',extra_tags='schedule_exist')

        else:
            job_id_object=Jobs.objects.get(jobs_id=self.job_category_id) # job object for foreign key purpose
            print(job_id_object.job_title,'job_id_object') 
            print('form data')

            Test_schedule.objects.create(
                        user_id=User.objects.get(id=self.request.user.id), 
                        job_id=job_id_object,
                        date=self.date,
                        # time=self.time,
                        description=self.descripiton
                        )

            print('form saved...............')
            self.call("toast","Schedule","updated","success")

            self.job_category_id = '' # empty the textbox
            self.date = '' # empty the textbox
            # self.time = '' # empty the textbox
            self.descripiton = '' # empty the textbox