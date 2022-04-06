from django.shortcuts import redirect, render

from recruiter.models import *
from hr_admin.models import *

from django.db.models import Q # this is for multiple queryset conditions
# Create your views here.
# dashboard
def dashboard(request):
    posted_job_count = Jobs.objects.all().count()
    recruiter_count = Recruiter.objects.all().count()
    candidate_count = Candidate.objects.all().count()
    print(posted_job_count,'jobs')
    print(recruiter_count,'recruiters')
    print(candidate_count,'candidates')

    context={'posted_job_count':posted_job_count,'recruiter_count':recruiter_count,'candidate_count':candidate_count}
    return render(request, 'hr_admin/dashboard.html',context)

# recruiter_list
def recruiter_list(request):
    recruiter_db=Recruiter.objects.all()

    context={'recruiter_db':recruiter_db}
    return render(request,'hr_admin/recruiter_list.html',context)

# job_list
def job_list(request):
    job_db=Jobs.objects.all()

    context={'job_db':job_db}
    return render(request,'hr_admin/job_list.html',context)

# job_schedules   
def job_schedules(request):
    schedules_db=Test_schedule.objects.all().select_related('user_id')

    context={'schedules_db':schedules_db}
    return render(request,'hr_admin/job_schedules.html',context)

# candidate_list
def candidate_list(request):
    candidate_db=Candidate.objects.all()

    context={'candidate_db':candidate_db}
    return render(request,'hr_admin/candidate_list.html',context)

# view technology
def view_technology(request):
    print('view_technology............')
    technologies_db = Technologies.objects.all()


    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        print(search_key)

        # search key null
        if search_key == '':
            print('search_key empty //////////')
            context={'technologies_db':technologies_db,'required':'required'}
            return render(request, 'hr_admin/view_technology.html',context)

        # search key not found
        elif Technologies.objects.filter(tech_name__icontains=search_key).count() == 0:
            print('not found ')
            context={'not_found':'not_found','search_key':search_key}
            return render(request, 'hr_admin/view_technology.html',context)


        # search key avalilable
        else:
            print('search key avalilable')
            technologies_db=Technologies.objects.filter(tech_name__icontains=search_key)

            context={'technologies_db':technologies_db,'search_key':search_key}
            return render(request,'hr_admin/view_technology.html',context)    


    context={'technologies_db':technologies_db}
    return render(request,'hr_admin/view_technology.html',context)


# delete technology
def delete_technology(request,pk):
    print('delete_technology ...................')
    print(pk,'pk')
    technologies_db= Technologies.objects.get(id=pk)
    print(technologies_db.tech_name,'/ technologies_db')

    test_ques_db= Test_questions.objects.filter(technology_id=technologies_db.id)
    for x in test_ques_db:
        print(x.technology_id.tech_name,'/ test_ques_db')

    # 1-deleting technologies_db Technology
    if technologies_db:
        technologies_db.delete()
        print('technologies_db raw deleted')
        #2- deleting related test_ques_db Technology
        if test_ques_db:
            test_ques_db.delete()
            print('test_ques_db raw deleted')
        else:
            print('No related Questions in database')
    
    else:
        print('No pk related technologies in database')


    return redirect(view_technology)

# view questions
def view_questions(request):
    print('view_questions............')
    test_questions_db = Test_questions.objects.all()
    
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        print(search_key)

        # search key null
        if search_key == '':
            print('search_key empty')
            context={'test_questions_db':test_questions_db,'required':'required'}
            return render(request, 'hr_admin/view_questions.html',context)

        # search key not found
        elif Test_questions.objects.filter(Q(technology_id__tech_name__icontains=search_key) | Q(question__icontains=search_key)).count() == 0:
            print('not found ')
            context={'not_found':'not_found','search_key':search_key}
            return render(request, 'hr_admin/view_questions.html',context)

        # search key avalilable
        else:
            print('search key avalilable')
            test_questions_db=Test_questions.objects.filter(Q(technology_id__tech_name__icontains=search_key) | Q(question__icontains=search_key))
            
            context={'test_questions_db':test_questions_db,'search_key':search_key}
            return render(request, 'hr_admin/view_questions.html',context)
            

    context={'test_questions_db':test_questions_db}
    return render(request,'hr_admin/view_questions.html',context)



# delete questions
def delete_questions(request,pk):
    print('delete_question ...................')
    print(pk,'pk')

    test_questions_db=Test_questions.objects.get(id=pk)

    test_questions_db.delete()
    print('One test_questions deleted ')
    


    return redirect(view_questions)