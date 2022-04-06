from django_unicorn.components import UnicornView

from hr_admin.models import *

from django.db.models import Q # this is for multiple to conditions

from django.contrib import messages

class UpdateQuestionsView(UnicornView):
    
    test_questions: Test_questions = None
    other_category = '' 
    correct_option = ''

    answer: str ='' # for re-assign 'option' value with correct 'answer' value

    def mount(self):
        print('each Test_questions "id" ',self.kwargs['pk'])

        # showing specfic values
        self.test_questions = Test_questions.objects.get(id=self.kwargs['pk'])
        print(self.test_questions.id, 'id.......')

        # for other category list purpose
        self.other_category=Technologies.objects.filter(~Q(tech_name=self.test_questions.technology_id.tech_name))
        for x in self.other_category:
            print(x.tech_name,'other_category///')


        # for correct answer option to pass value in 'select option part in html form'
        if self.test_questions.answer == self.test_questions.option1:
            print('match option1')
            self.correct_option= 'Option1'

        elif self.test_questions.answer == self.test_questions.option2:
            print('match option2')
            self.correct_option='Option2'

        elif self.test_questions.answer == self.test_questions.option3:
            print('match option3')
            self.correct_option= 'Option3'

        else:
            print('match option4')
            self.correct_option='Option4'

    

    def update(self):
        print(self.test_questions.technology_id.tech_name)
        print(self.test_questions.question)
        print(self.test_questions.option1)
        print(self.test_questions.option2)
        print(self.test_questions.option3)
        print(self.test_questions.option4)
        print(self.test_questions.answer,'-default answer')


        # technology_id_id
        if self.test_questions.technology_id_id == '' :
            print('Select Technology Required.......................')
            self.call("toast","Error","Required Select Technology","warning")
            messages.error(self.request,'Required Select Technology',extra_tags='tech_category_id')
        # question
        elif self.test_questions.question == '' :
            print('question Required.......................')
            self.call("toast","Error","Required Question","warning")
            messages.error(self.request,'Required Question',extra_tags='question')
        # Option1 is null 
        elif self.test_questions.option1 == '' :
            print('option1 Required.......................')
            self.call("toast","Error","Required Option 1","warning")
            messages.error(self.request,'Required Option 1',extra_tags='option1')
        # Option2 is null 
        elif self.test_questions.option2 == '' :
            print('option2 Required.......................')
            self.call("toast","Error","Required Option 2","warning")
            messages.error(self.request,'Required Option 2',extra_tags='option2')
        # Option3 is null 
        elif self.test_questions.option3 == '' :
            print('option3 Required.......................')
            self.call("toast","Error","Required Option 3","warning")
            messages.error(self.request,'Required Option 3',extra_tags='option3')
        # Option4 is null 
        elif self.test_questions.option4 == '' :
            print('option4 Required.......................')
            self.call("toast","Error","Required Option 4","warning")
            messages.error(self.request,'Required Option 4',extra_tags='option4')
        # # answer is null    
        # elif self.answer == '' :
        #     print('Select Answer Required.......................')
        #     self.call("toast","Error","Required Select Answer","warning")
        #     messages.error(self.request,'Required Select Answer',extra_tags='answer')

        # same question and technology_id exist
        # elif Test_questions.objects.filter(Q(question=self.test_questions.question) and Q(technology_id=self.test_questions.technology_id_id)).exists():
        #     print('Same Question & Technoloy Exist.......................')
        #     self.call("toast","Error","Same Question & Technoloy Exist","warning")
        #     messages.error(self.request,'Same Question & Technoloy Exist',extra_tags='same_ques_tech')

        else:
            # re-assigning 'answer' variable with correct option value 
            # option1
            if self.answer == 'option1':
                print('answer 1')
                self.test_questions.answer=self.test_questions.option1
                print(self.test_questions.answer,'- assigning correct answer')
            # option2
            if self.answer == 'option2':
                print('answer 2')
                self.test_questions.answer=self.test_questions.option2
                print(self.test_questions.id,'- assigning correct answer')
                # option3
            if self.answer == 'option3':
                print('answer 3')
                self.test_questions.answer=self.test_questions.option3
                print(self.test_questions.id,'- assigning correct answer')
                # option4
            if self.answer == 'option4':
                print('answer 4')
                self.test_questions.answer=self.test_questions.option4
                print(self.test_questions.id,'- assigning correct answer')


            
            self.test_questions.save() # updating all fields from form data
            print('form saved...............')
            self.call("toast","Question","updated","success")