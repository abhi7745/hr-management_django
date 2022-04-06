from django_unicorn.components import UnicornView
from django import forms
from recruiter.models import Recruiter

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ('company_name', 'description', 'address', 'email', 'phonenumber')
        
    def __init__(self, data, *args, **kwargs):
        cb = {}        
        if isinstance(data['profile'], dict):
            cb = data['profile']
        elif isinstance(data['profile'], Recruiter):
            cb = forms.model_to_dict(data['profile'], fields=[
                               field.name for field in data['profile']._meta.fields])

        super().__init__(cb, *args, **kwargs)

class ProfileView(UnicornView):
    # form_classes = {
    #     "profile": ProfileForm,
    # }
    form_class = ProfileForm
    
    profile:Recruiter = None
    
    def mount(self):
        try:
            self.profile = self.request.user.recruiter
        except:
            self.profile = Recruiter()
            self.profile.user = self.request.user  
            self.profile.email = self.request.user.username
            self.profile.save()
            
            
    def save(self):
        if self.is_valid():
            self.profile.save()
            self.call("toast","Profile","saved","success")
            
        
        

