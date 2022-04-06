from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from recruiter.models import *

# Create your views here.
# dashboard
def dashboard(request):
    joblist_count=Jobs.objects.filter(recruiter_id=request.user.id).count()
    print(joblist_count)
    return render(request, 'recruiter/dashboard.html',{'joblist_count':joblist_count})

# job list
def joblist(request):

    # user_db=User.objects.get(username__contains=request.user)
    # print(user_db.id, 'User')

    joblist_db=Jobs.objects.filter(recruiter_id=request.user.id)
    # for job in joblist_db:
    #     print(job.jobs_id,'deletion_id')

    context={'joblist_db':joblist_db}

    return render(request, 'recruiter/joblist.html',context)

# delete jobs
def deletejob(request,pk):
    print('This is delete view')
    print(pk,'pk value')
    # deletion purpose
    job_data=Jobs.objects.get(jobs_id=pk)
    print(job_data)
    job_data.delete()
    print('one job deleted')
    

    return redirect('recruiter.joblist')


# schedulelist
def schedulelist(request):
    print(request.user.id)
    test_schedule_db=Test_schedule.objects.filter(user_id=request.user.id) 
    for x in test_schedule_db:
        print(x.job_id)
        # pass
    
    # test_schedule_db=Test_schedule.objects.filter(job_id=x.jobs_id)
    # for y in test_schedule_db:
    #     print(y.job_id)

    return render(request,'recruiter/schedulelist.html',{'test_schedule_db':test_schedule_db})



# delete schedulelist
def deleteschedulelist(request,pk):
    print('This is schedulelist delete view')
    print(pk,'pk value')

    # deletion purpose
    schedule_data=Test_schedule.objects.get(id=pk)
    print(schedule_data.job_id)
    schedule_data.delete()
    print('one schedule deleted')
    

    return redirect('recruiter.schedulelist')


# applied candidates
def applied_candidates(request):

    application_db=Applications.objects.filter(job_id__recruiter_id=request.user.id) # filter application_db with user_id

    for x in application_db:
        print(x.job_id.job_title,'/////////////',request.user.username)

    # /////////////////////////////////////////////
    # abc=Applications.objects.filter(job_id__recruiter_id=request.user.id)
    # for y in abc:
    #     print(y.job_id)

    #     if Jobs.objects.filter(job_title=y.job_id.job_title,jobs_id=y.job_id_id).exists():

    #         # job=Jobs.objects.filter(recruiter_id=y.job_id.recruiter_id,job_title=y.job_id.job_title).count()
    #         job=Applications.objects.filter(job_id__recruiter_id=request.user.id,job_id_id=y.job_id_id).distinct().count()
    #         # for x in job:
    #         #     print(x.job_id_id)

    #         print(job)
    # abc=Applications.objects.filter(job_id__recruiter_id=request.user.id,job_id=6).count()
    # print(abc)
    # /////////////////////////////////////////////////////////

    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        print(search_key)

        # search key null
        if search_key == '':
            print('search_key empty')
            context={'application_db':application_db,'required':'required'}
            return render(request, 'recruiter/applied_candidates.html',context)

        # search key not found
        elif Applications.objects.filter(job_id__job_title__icontains=search_key,job_id__recruiter_id=request.user.id).count() == 0:
            print('not found ')
            context={'not_found':'not_found','search_key':search_key}
            return render(request, 'recruiter/applied_candidates.html',context)

        # search key avalilable
        else:
            print('search key avalilable')
            application_db=Applications.objects.filter(job_id__job_title__icontains=search_key,job_id__recruiter_id=request.user.id)
            for x in application_db:
                print(x.job_id.job_title,'main...........')

            context={'application_db':application_db,'search_key':search_key}
            return render(request,'recruiter/applied_candidates.html',context)    




    context={'application_db':application_db,
    'total_applications':Applications.objects.filter(job_id__recruiter_id=request.user.id).values('job_id__job_title','job_id').distinct(),
    }
    return render(request,'recruiter/applied_candidates.html',context)


# candidates view
def candidate_view(request,pk):
    print('candidates_view function',pk)

    candidate=Candidate.objects.get(id=pk)
    print(candidate.name)

    context={'candidate':candidate}
    return render(request,'recruiter/candidate_view.html',context)