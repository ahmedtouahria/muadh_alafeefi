from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from muadh.models import *
class TeamMemberForm(forms.ModelForm):
    abstract = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = TeamMember
        fields='__all__'
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberForm
# Register your models here.
admin.site.register(Testimonial)
admin.site.register(TeamMember,TeamMemberAdmin)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Section)
admin.site.register(SectionItem)
admin.site.register(Message)


