from django.urls import path
from . import views



urlpatterns=[
    path('', views.home, name='home'),
    path('jobs/', views.jobListView, name='jobs'),
    path('job-detail/<int:pk>', views.jobDetail, name='job-detail'),
    path('contacts/<int:pk>', views.Contacts, name='contacts'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register-job-seeker/', views.registerUser, name='register'),
    path('register-recruiter/', views.registerRcruiter, name='recruiter'),
    path('searches/', views.searchJobs, name='search'),
    path('contact-form/', views.postContact, name='contact'),
    path('contact-edit/', views.updateContact, name='update-contact'),
    path('contact-delete/', views.deleteContact, name='delete-contact'),
    path('posted-jobs/', views.postedJobs, name='posted-jobs'),
    path('job-post/',views.newJob, name='new-job'),
    path('edit-job/<int:pk>', views.updateJob, name='update-job'),
    path('delete-job/<int:pk>', views.deleteJob, name='delete-job'),
    path('save-job/<int:pk>', views.saveJob, name='save-job'),
    path('saved-jobs', views.savedJobs, name='saved-jobs'),
    path('unsave-job/<int:pk>', views.unsaveJob, name='unsave-job'),
    path('profile/', views.jobSeekerProfile, name='profile'),
    path('education/', views.jobSeekerEducation, name='education'),
    path('profile-edit/', views.updateJobSeekerProfile, name='profile-edit'),
    path('home/', views.jobSeekerHomePage, name='j-home'),
    path('educations/', views.educationsView, name='educations'),
    path('education-delete/<int:pk>', views.educationsDelete, name='education-delete'),
    path('education-edit/<int:pk>', views.editEducation, name='education-edit'),
    path('work-experience/', views.jobSeekerWork, name='job-experience'),
    path('work-experiences/', views.workView, name='job-experiences'),
    path('work-delete/<int:pk>', views.workDelete, name='work-delete'),
    path('work-edit/<int:pk>', views.editWork, name='work-edit'),
    path('skill/', views.jobSeekerSkill, name='skill'),
    path('skills/', views.skillView, name='skills'),
    path('skill-delete/<int:pk>', views.skillDelete, name='skill-delete'),
    path('skill-edit/<int:pk>', views.editSkill, name='skill-edit'),
    path('resume/', views.resumeView, name='resume'),
    path('apply/<int:pk>', views.applyJob, name='apply'),
    path('applied-job-seekers/<int:pk>', views.appliedJobSeekers, name='applieds'),
    path('applied-jobs/', views.appliedJobs,name='applied-jobs'),
    path('unapply/<int:pk>', views.unapplyJob,name='unapply-job'),
    path('job-seeker-resume/<int:pk>',views.jobSeekerResumeView, name='job-seeker-resume'),
]