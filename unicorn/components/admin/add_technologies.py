from django_unicorn.components import UnicornView

from django.contrib import messages

from hr_admin.models import * # hr_admin all models

class AddTechnologiesView(UnicornView):

    tech_name: str = ''
    question_mark = ''

    def mount(self):
        pass

    def save(self):
        print(self.tech_name)
        print(self.question_mark)

        # tech_name
        if self.tech_name == '' :
            print('tech_name Required.......................')
            self.call("toast","Error","Required Tech Name","warning")
            messages.error(self.request,'Required Tech Name',extra_tags='tech_name')
        
        # question_mark
        elif self.question_mark == '' :
            print('question_mark Required.......................')
            self.call("toast","Error","Required Mark For Each Question","warning")
            messages.error(self.request,'Required Mark For Each Question',extra_tags='question_mark_case1')

        elif (int(self.question_mark) <= 0):
                print('question_mark Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='question_mark_case2')
        
        # tech_name already exist
        elif Technologies.objects.filter(tech_name__contains=self.tech_name).exists():
            self.call("toast","Error","Technology already exist ","warning")
            messages.error(self.request,'Tech name already exist',extra_tags='tech_name')

        else:

            Technologies.objects.create(
                tech_name=self.tech_name,
                question_mark=self.question_mark
            )

            print('form saved...............')
            self.call("toast","Technology","added successfully","success")

            self.tech_name = ''
            self.question_mark = ''