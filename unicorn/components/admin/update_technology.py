from django_unicorn.components import UnicornView

from hr_admin.models import Technologies

from django.contrib import messages


class UpdateTechnologyView(UnicornView):
    
    technology_db: Technologies = None

    def mount(self):

       print('each tech_id ',self.kwargs['pk'])
       # showing specfic values
       self.technology_db = Technologies.objects.get(id=self.kwargs['pk'])
       print(self.technology_db.tech_name, 'successssss')



    def update(self):
        print(self.technology_db.tech_name)
        print(self.technology_db.question_mark) 

        # tech_name
        if self.technology_db.tech_name == '' :
            print('tech_name Required.......................')
            self.call("toast","Error","Required Tech Name","warning")
            messages.error(self.request,'Required Tech Name',extra_tags='tech_name')
        
        # question_mark
        elif self.technology_db.question_mark == '' :
            print('question_mark Required.......................')
            self.call("toast","Error","Required Mark For Each Question","warning")
            messages.error(self.request,'Required Mark For Each Question',extra_tags='question_mark_case1')

        elif (int(self.technology_db.question_mark) <= 0):
                print('question_mark Invalid entry.......................')
                self.call("toast","Error","Invalid entry","warning")
                messages.error(self.request,'Invalid entry',extra_tags='question_mark_case2')
        
        # tech_name already exist
        elif Technologies.objects.filter(tech_name=self.technology_db.tech_name,question_mark=self.technology_db.question_mark).exists():
            self.call("toast","Error","Technology already exist ","warning")
            messages.error(self.request,'Tech name already exist',extra_tags='tech_name')

        else:


            self.technology_db.save() # updating all fields from form data
            print('form saved...............')
            self.call("toast","Technology","updated","success")