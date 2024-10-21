from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from portfolio import api_views

urlpatterns = [
    path("projects/", api_views.ProjectList.as_view(), name="project-list"),
    path("projects/<int:pk>/", api_views.ProjectDetail.as_view(), name="project-detail"),
    path("skills/", api_views.SkillList.as_view(), name="skill-list"),
    path("skills/<int:pk>/", api_views.SkillDetail.as_view(), name="skill-detail"),
    path("experiences/", api_views.ExperienceList.as_view(), name="experience-list"),
    path("experiences/<int:pk>/", api_views.ExperienceDetail.as_view(), name="experience-detail"),
    path("educations/", api_views.EducationList.as_view(), name="education-list"),
    path("educations/<int:pk>/", api_views.EducationDetail.as_view(), name="education-detail"),
    path("contacts/", api_views.ContactList.as_view(), name="contact-list"),
    path("contacts/<int:pk>/", api_views.ContactDetail.as_view(), name="contact-detail"),
    path("about/", api_views.AboutDetail.as_view(), name="about-detail"),
    path("about/<int:pk>/", api_views.AboutDetail.as_view(), name="about-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
