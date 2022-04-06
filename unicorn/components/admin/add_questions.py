from django_unicorn.components import UnicornView

from hr_admin.models import Technologies,Test_questions
from django.contrib import messages

class AddQuestionsView(UnicornView):
    

    tech_db : Technologies = None

    tech_category_id = ''
    question: str = ''
    option1: str = ''
    option2: str = ''
    option3: str = ''
    option4: str = ''
    answer: str = ''

    def mount(self):
        # try:
        # passing recruiter all job_titles to html form
        self.tech_db = Technologies.objects.all()

    
    def save(self):
        print(self.tech_category_id)
        print(self.question)
        print(self.option1)
        print(self.option2)
        print(self.option3)
        print(self.option4)
        print(self.answer,'default answer')

        # tech_category_id
        if self.tech_category_id == '' :
            print('Select Technology Required.......................')
            self.call("toast","Error","Required Select Technology","warning")
            messages.error(self.request,'Required Select Technology',extra_tags='tech_category_id')
        # question
        elif self.question == '' :
            print('question Required.......................')
            self.call("toast","Error","Required Question","warning")
            messages.error(self.request,'Required Question',extra_tags='question')
        # Option1 is null 
        elif self.option1 == '' :
            print('option1 Required.......................')
            self.call("toast","Error","Required Option 1","warning")
            messages.error(self.request,'Required Option 1',extra_tags='option1')
        # Option2 is null 
        elif self.option2 == '' :
            print('option2 Required.......................')
            self.call("toast","Error","Required Option 2","warning")
            messages.error(self.request,'Required Option 2',extra_tags='option2')
        # Option3 is null 
        elif self.option3 == '' :
            print('option3 Required.......................')
            self.call("toast","Error","Required Option 3","warning")
            messages.error(self.request,'Required Option 3',extra_tags='option3')
        # Option4 is null 
        elif self.option4 == '' :
            print('option4 Required.......................')
            self.call("toast","Error","Required Option 4","warning")
            messages.error(self.request,'Required Option 4',extra_tags='option4')
        # answer is null    
        elif self.answer == '' :
            print('Select Answer Required.......................')
            self.call("toast","Error","Required Select Answer","warning")
            messages.error(self.request,'Required Select Answer',extra_tags='answer')

        # same question and technology_id exist
        elif Test_questions.objects.filter(question__contains=self.question,technology_id=self.tech_category_id).exists():
            print('Same Question & Technoloy Exist.......................')
            self.call("toast","Error","Same Question & Technoloy Exist","warning")
            messages.error(self.request,'Same Question & Technoloy Exist',extra_tags='same_ques_tech')

        else:

            # re-assigning 'answer' variable with correct option value 
            # option1
            if self.answer == 'option1':
                print('answer 1')
                self.answer=self.option1
                print(self.answer,'- assigning correct answer')
            # option2
            if self.answer == 'option2':
                print('answer 2')
                self.answer=self.option2
                print(self.answer,'- assigning correct answer')
            # option3
            if self.answer == 'option3':
                print('answer 3')
                self.answer=self.option3
                print(self.answer,'- assigning correct answer')
            # option4
            if self.answer == 'option4':
                print('answer 4')
                self.answer=self.option4
                print(self.answer,'- assigning correct answer')

  

          

            Test_questions.objects.create(
                    technology_id=Technologies.objects.get(id=self.tech_category_id), # technologies db object
                    question=self.question,
                    option1=self.option1,
                    option2=self.option2,
                    option3=self.option3,
                    option4=self.option4,
                    answer=self.answer

                )
        
            print('form saved...............')
            self.call("toast","Question","added successfully","success")

            self.tech_category_id = ''
            self.question = ''
            self.option1 = ''
            self.option2 = ''
            self.option3 = ''
            self.option4 = ''
            self.answer = ''