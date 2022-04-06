from django_unicorn.components import UnicornView

from django.shortcuts import redirect
from django.contrib import messages
from candidate.models import Candidate #database

class ProfileView(UnicornView):
    candidate: Candidate = None


    def mount(self):
        self.candidate = Candidate.objects.get(email=self.request.user)

        print(self.candidate.name,'fffffffff') 


    def save(self):
        print(self.candidate.name)
        print(self.candidate.email,'email not editable')
        print(self.candidate.phone)
        print(self.candidate.experience_level)
        print(self.candidate.expected_ctc)
        print(self.candidate.companies_experience)
        print(self.candidate.year_of_exp)
        print(self.candidate.current_ctc)
        print(self.candidate.notice_period_from)
        print(self.candidate.notice_period_to)
        print(self.candidate.willingtowork_shifts)
        print(self.candidate.willingtowork_contract)
        print(self.candidate.qualification)
        print(self.candidate.address)
        print(self.candidate.primary_skill)
        print(self.candidate.primary_skill_rating)
        print(self.candidate.secondary_skill)
        print(self.candidate.secondary_skill_rating)
        print(self.candidate.other_skill)
        print(self.candidate.other_skill_rating)
        print(self.candidate.certification)

        try:

            if self.candidate.experience_level == 'fresher':
                self.candidate.companies_experience = ''
                self.candidate.year_of_exp = None
                self.candidate.current_ctc = ''
                self.candidate.notice_period_from = None
                self.candidate.notice_period_to = None


            # name
            if self.candidate.name == '' :
                print('name null.......................')
                self.call("toast","Error","Required Username","warning")
                messages.error(self.request,'Required Username',extra_tags='name')

            # phone
            elif self.candidate.phone == '' :
                print('phone null.......................')
                self.call("toast","Error","Required Phone Number","warning")
                messages.error(self.request,'Required Phone Number',extra_tags='phone')

            elif len(self.candidate.phone) < 10 or len(self.candidate.phone) > 10 or int(self.candidate.phone) < 0 :
                print('phone Invalid.......................')
                self.call("toast","Error","Invalid Phone Number","warning")
                messages.error(self.request,'Invalid Phone Number',extra_tags='phone_invalid')
            
            # experience_level
            elif self.candidate.experience_level == '' :
                print('experience_level null.......................')
                self.call("toast","Error","Required Experience Level","warning")
                messages.error(self.request,'Required Experience Level',extra_tags='experience_level')
            # experience_level fresher
            # elif not self.candidate.experience_level == '' :
            #     if self.candidate.experience_level == 'fresher' :
            #         print('experience_level fresher.......................')
            #         if self.candidate.expected_ctc == '':
            #             print('Expected CTC.......................')
            #             self.call("toast","Error","Required Expected CTC","warning")
            #             messages.error(self.request,'Required Expected CTC',extra_tags='fresher')
                
                        
                        

            #     if self.candidate.experience_level == 'experienced':
            #         print('experience_level experienced.......................')
            #         if self.candidate.companies_experience == '':
            #             print('companies_experience.......................')
            #             self.call("toast","Error","Required Companies worked","warning")
            #             messages.error(self.request,'Required Companies worked',extra_tags='experienced')
            
            # willingtowork_shifts
            elif self.candidate.willingtowork_shifts == '' :
                print('willingtowork_shifts null.......................')
                self.call("toast","Error","Required Willing to work in Shifts","warning")
                messages.error(self.request,'Required Field',extra_tags='shifts')

            # willingtowork_contract
            elif self.candidate.willingtowork_contract == '' :
                print('willingtowork_shifts null.......................')
                self.call("toast","Error","Required Willing to work as Contract","warning")
                messages.error(self.request,'Required Field',extra_tags='contract')

            # Qualification
            elif self.candidate.qualification == '' :
                print('qualification null.......................')
                self.call("toast","Error","Required Qualification","warning")
                messages.error(self.request,'Required Qualification',extra_tags='qualification')

            # address
            elif self.candidate.address == '' :
                print('address null.......................')
                self.call("toast","Error","Required Address","warning")
                messages.error(self.request,'Required Address',extra_tags='address')
            
            # primary_skill
            elif self.candidate.primary_skill == '' :
                print('primary_skill null.......................')
                self.call("toast","Error","Required Primary skill","warning")
                messages.error(self.request,'Required Primary skill',extra_tags='primary_skill')
            
            # primary_skill_rating
            elif self.candidate.primary_skill_rating == '':
                print('primary_skill_rating null.......................')
                self.call("toast","Error","Required Primary skill Rating ","warning")
                messages.error(self.request,'Required Primary skill Rating ',extra_tags='primary_skill_rating')

            elif int(self.candidate.primary_skill_rating) < 0 or int(self.candidate.primary_skill_rating) > 5 :
                print('primary_skill_rating invalid.......................')
                self.call("toast","Error","Invalid ","warning")
                messages.error(self.request,'Invalid ',extra_tags='primary_skill_rating_invalid')


            # secondary_skill
            elif self.candidate.secondary_skill == '' :
                print('secondary_skill null.......................')
                self.call("toast","Error","Required Secondary skill","warning")
                messages.error(self.request,'Required Secondary skill',extra_tags='secondary_skill')
            
            # secondary_skill_rating
            elif self.candidate.secondary_skill_rating == '':
                print('secondary_skill_rating null.......................')
                self.call("toast","Error","Required Secondary skill Rating ","warning")
                messages.error(self.request,'Required Secondary skill Rating ',extra_tags='secondary_skill_rating')

            elif int(self.candidate.secondary_skill_rating) < 0 or int(self.candidate.secondary_skill_rating) > 5 :
                print('secondary_skill_rating invalid.......................')
                self.call("toast","Error","Invalid ","warning")
                messages.error(self.request,'Invalid ',extra_tags='secondary_skill_rating_invalid')


            # other_skill
            elif self.candidate.other_skill == '' :
                print('other_skill null.......................')
                self.call("toast","Error","Required Other skill","warning")
                messages.error(self.request,'Required Other skill',extra_tags='other_skill')
            
            # other_skill_rating
            elif self.candidate.other_skill_rating == '':
                print('other_skill_rating null.......................')
                self.call("toast","Error","Required Other skill Rating ","warning")
                messages.error(self.request,'Required Other skill Rating ',extra_tags='other_skill_rating')

            elif int(self.candidate.other_skill_rating) < 0 or int(self.candidate.other_skill_rating) > 5 :
                print('other_skill_rating invalid.......................')
                self.call("toast","Error","Invalid ","warning")
                messages.error(self.request,'Invalid ',extra_tags='other_skill_rating_invalid')

            
            
            else:
                self.candidate.save()
                print('form saved...............')
                self.call("toast","Profile","updated","success")
        
        except:
            print('Exception error .......................')
            self.call("toast","Error","Server Error","warning")
           
            # return redirect('candidate.profile')  

