from django.shortcuts import redirect, render

from recruiter.models import * # recruiter models
from candidate.models import * # candidate models

# Create your views here.

# dashboard
def dashboard(request):
    all_jobs_count=Jobs.objects.all().count()
    all_recruiter_count=Recruiter.objects.all().count()
    applied_jobs=Applications.objects.filter(candidate_id__user_id=request.user.id).count()

    context={'all_jobs_count': all_jobs_count,'all_recruiter_count':all_recruiter_count,
    'applied_jobs':applied_jobs}

    return render(request, 'candidate/dashboard.html',context)


# Search Job
def search_job(request):
    joblist_db=Jobs.objects.all() # showing all jobs
    
    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        print(search_key)

        # search key null
        if search_key == '':
            print('search_key empty')
            context={'joblist_db':joblist_db,'required':'required'}
            return render(request, 'candidate/search_job.html',context)

        # search key null not found
        elif Jobs.objects.filter(job_title__icontains=search_key).count() == 0:
            print('not found ')
            context={'not_found':'not_found','search_key':search_key}
            return render(request, 'candidate/search_job.html',context)

        # search key null avalilable
        else:
            joblist_db=Jobs.objects.filter(job_title__icontains=search_key)
            print(joblist_db)

            context={'joblist_db':joblist_db,'search_key':search_key}

            return render(request, 'candidate/search_job.html',context)



    context={'joblist_db':joblist_db}

    return render(request, 'candidate/search_job.html',context)

# job view 
def job_view(request,pk):
    job_db=Jobs.objects.get(jobs_id=pk) #job table object
    print(job_db.job_title)

    # check user applied this job-
    if Applications.objects.filter(job_id=pk,candidate_id__user_id=request.user.id).exists():
        applications_db=Applications.objects.get(job_id=pk,candidate_id__user_id=request.user.id) #Applications table for status
        print(applications_db,'///////')
        # pass job database data and application database
        context={'job_db':job_db,'applications_db':applications_db}
    else:
        # check user applied - pass individual job database data
        context={'job_db':job_db}

    return render(request,'candidate/job_view.html',context)

# Apply logic    
def apply(request,pk):
    print(pk,'pk')
    job_db=Jobs.objects.get(jobs_id=pk) # job table object
    print(job_db.job_title)
    print(job_db.jobs_id)

    candidate_db=Candidate.objects.get(user_id=request.user.id)# candidate table object
    print(candidate_db.name)

    # check user already applied - condition
    if Applications.objects.filter(job_id=pk,candidate_id__user_id=request.user.id).exists():
        print('candidate already applied')
    else:
        # user not applied - condition
        Applications.objects.create(
            candidate_id=candidate_db,
            job_id=job_db,
            status='applied'
        )
        print('applied successful')

    return redirect('/candidate/job_view/'+str(pk))

# application_cancel
def application_cancel(request,pk):
    print(pk,'pk')

    applications_db=Applications.objects.get(job_id=pk,candidate_id__user_id=request.user.id)
    applications_db.delete()
    print('Job application deleted')

    return redirect('/candidate/job_view/'+str(pk))

# applied_jobs search logic
def applied_jobs(request):
    application_db=Applications.objects.filter(candidate_id__user_id=request.user.id) # filter application_db with user_id
    for x in application_db:
        print(x.job_id.job_title,'//////////////////////////')


    if request.method == 'POST':
        search_key = request.POST.get('search_key')
        print(search_key)

        # search key null
        if search_key == '':
            print('search_key empty')
            context={'application_db':application_db,'required':'required'}
            return render(request, 'candidate/applied_jobs.html',context)

        # search key not found
        elif Applications.objects.filter(job_id__job_title__icontains=search_key,candidate_id__user_id=request.user.id).count() == 0:
            print('not found ')
            context={'not_found':'not_found','search_key':search_key}
            return render(request, 'candidate/applied_jobs.html',context)

        # search key avalilable
        else:
            print('search key avalilable')
            application_db=Applications.objects.filter(job_id__job_title__icontains=search_key,candidate_id__user_id=request.user.id)
            for x in application_db:
                print(x.job_id.job_title,'main...........')

            context={'application_db':application_db,'search_key':search_key}
            return render(request,'candidate/applied_jobs.html',context)

    # default render
    print('default render')
    context={'application_db':application_db}
    return render(request,'candidate/applied_jobs.html',context)