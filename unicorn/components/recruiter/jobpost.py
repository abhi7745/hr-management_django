from django_unicorn.components import UnicornView

from django.contrib import messages

from django import forms
from recruiter.models import Jobs #database

# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Jobs
#         fields = ('job_title', 'min_experience','max_experience',
#         'min_salary','max_salary', 'location', 'qualification',
#         'certification', 'discription', 'vacancies_no',
#         'closing_date')
        
    # def __init__(self, data, *args, **kwargs):
    #     cb = {}        
    #     if isinstance(data['profile'], dict):
    #         cb = data['profile']
    #     elif isinstance(data['profile'], Jobs):
    #         cb = forms.model_to_dict(data['profile'], fields=[
    #                            field.name for field in data['profile']._meta.fields])

    #     super().__init__(cb, *args, **kwargs)

class JobpostView(UnicornView):

    # form_class = JobForm

    job_title: str = ''
    min_exp= ''
    max_exp= ''
    min_salary= ''
    max_salary= ''
    location: str = ''
    descripiton: str = ''
    qualification: str = ''
    certification: str = ''
    vacancies= ''
    closing_date: str = ''

    job: Jobs = None

    def mount(self):
        # self.job = Jobs.objects.all()
        # print('mount.............')
        try:
            self.job = self.request.user.recruiter
        except:
            self.job = Jobs()
            self.job.recruiter_id = self.request.user
            self.job.save()



    def save(self):
        try:
            # job_title
            if self.job_title == '' :
                print('Job Title.......................')
                self.call("toast","Error","Required Job Title","warning")
                messages.error(self.request,'Required Job Title',extra_tags='jobtitle')
            # min_exp 
            elif self.min_exp == '':
                print('Minimum Exp.......................')
                self.call("toast","Error","Required Minimum Experience","warning")
                messages.error(self.request,'Required Minimum Experience',extra_tags='min_exp')

            elif (int(self.min_exp) < 0  or int(self.min_exp) > 20):
                print('Minimum Exp Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='min_exp_case2')
            # max_exp
            elif self.max_exp == '' :
                print('Maximum Exp.......................')
                self.call("toast","Error","Required Maximum Experience","warning")
                messages.error(self.request,'Required Maximum Experience',extra_tags='max_exp')

            elif (int(self.max_exp) < 0  or int(self.max_exp) > 20):
                print('Maximum Exp Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='max_exp_case2')
            # min_salary
            elif self.min_salary == '':
                print('min_salary .......................')
                self.call("toast","Error","Required Minimum Salary","warning")
                messages.error(self.request,'Required Minimum Salary',extra_tags='min_salary')
            
            elif (int(self.min_salary) < 7000):
                print('min_salary Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='min_salary_case2')
            # max_salary
            elif self.max_salary == '':
                print('max_salary .......................')
                self.call("toast","Error","Required Maximun Salary","warning")
                messages.error(self.request,'Required Maximun Salary',extra_tags='max_salary')
            
            elif (int(self.max_salary) < 7000):
                print('max_salary Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='max_salary_case2')
            # location
            elif self.location == '':
                print('location .......................')
                self.call("toast","Error","Required Location","warning")
                messages.error(self.request,'Required Location',extra_tags='location')
            # descripiton
            elif self.descripiton == '':
                print('descripiton .......................')
                self.call("toast","Error","Required Descripiton","warning")
                messages.error(self.request,'Required Descripiton',extra_tags='descripiton')
            # qualification
            elif self.qualification == '':
                print('qualification .......................')
                self.call("toast","Error","Required Qualification","warning")
                messages.error(self.request,'Required Qualification',extra_tags='qualification')
            # certification
            elif self.certification == '':
                print('certification .......................')
                self.call("toast","Error","Required Certification","warning")
                messages.error(self.request,'Required Certification',extra_tags='certification')
            # vacancies
            elif self.vacancies == '':
                print('vacancies .......................')
                self.call("toast","Error","Required Vacancies","warning")
                messages.error(self.request,'Required Vacancies',extra_tags='vacancies')
            
            elif (int(self.vacancies) <= 0):
                print('vacancies Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='vacancies_case2')
            # closing Date
            elif self.closing_date == '':
                print('closing_date .......................')
                self.call("toast","Error","Required Closing Date","warning")
                messages.error(self.request,'Required Closing Date',extra_tags='closing_date')

            else:
                print(self.job_title)
                print(type(self.job_title))
                print('ok...........................')

                # self.job.recruiter_id = self.request.user 
                # self.save()
                Jobs.objects.create(
                    recruiter_id = self.request.user.recruiter,
                    job_title=self.job_title,
                    min_experience=self.min_exp,max_experience=self.max_exp,
                    min_salary=self.min_salary,max_salary=self.max_salary,
                    location=self.location,qualification=self.qualification,
                    certification=self.certification,discription=self.descripiton,
                    vacancies_no=self.vacancies,closing_date=self.closing_date)

                print('form saved...............')
                self.call("toast","Job","updated","success")

                self.job = Jobs.objects.all()
                self.job_title = '' # empty the textbox
                self.min_exp = '' # empty the textbox
                self.max_exp= '' # empty the textbox
                self.min_salary= '' # empty the textbox
                self.max_salary= '' # empty the textbox
                self.location: str = '' # empty the textbox
                self.descripiton: str = '' # empty the textbox
                self.qualification: str = '' # empty the textbox
                self.certification: str = '' # empty the textbox
                self.vacancies= '' # empty the textbox
                self.closing_date: str = '' # empty the textbox

        except:
            print('Exception error .......................')
            self.call("toast","Error","Server Error","warning")



    # def save(self):
    #     data=JobForm(self.request.POST)
    #     if data.is_valid:
    #         self.job.save()
    #         print('saved job...........')
    #         self.call("toast","Profile","saved","success")