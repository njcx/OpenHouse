from django.contrib import admin
from django.conf.urls import url
from .models import RecruitConfigs, RecruitSignup,JobfairSlot,JobfairInfo,SponsorItem,SponsorShip,\
    Files,RecruitConfigs,CompanySurvey, Company, SeminarSlot, SlotColor, SeminarOrder
from company.models import Company
from recruit import export

class SponsorshipInline(admin.TabularInline):
    model = SponsorShip
    extra = 0

class RecruitConfigAdmin(admin.ModelAdmin):
    list_display=['title']
    def title(self,obj):
        return '活動設定'
admin.site.register(RecruitConfigs, RecruitConfigAdmin)

class RecruitSignupAdmin(admin.ModelAdmin):
    search_fields = ('cid','seminar',)
    list_display = ('cid','company_name','seminar','jobfair','career_tutor','company_visit','lecture','payment')
    list_filter = ('seminar','career_tutor','company_visit','lecture','payment',)
    inlines = (SponsorshipInline,)

    def company_name(self,obj):
        return obj.get_company_name()
admin.site.register(RecruitSignup, RecruitSignupAdmin)

@admin.register(SeminarSlot)
class SeminarSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'session', 'company', 'place')

@admin.register(SeminarOrder)
class SeminarOrderAdmin(admin.ModelAdmin):
    list_display = ("company","time","updated")

@admin.register(SlotColor)
class SlotColorAdmin(admin.ModelAdmin):
    list_display=('place','css_color', 'place_info')

class JobfairSlotAdmin(admin.ModelAdmin):
    list_display = ('serial_number',)

admin.site.register(JobfairSlot, JobfairSlotAdmin)

class JobfairInfoAdmin(admin.ModelAdmin):
    list_display = ('company',)
admin.site.register(JobfairInfo, JobfairInfoAdmin)

class SponsorItemAdmin(admin.ModelAdmin):
    inlines = (SponsorshipInline,)
    list_display = ('name', 'description', 'price', 'number_limit', 'current_amount')

    def current_amount(self, obj):
        return SponsorShip.objects.filter(sponsor_item=obj).count()
    current_amount.short_description = '目前贊助數'

admin.site.register(SponsorItem, SponsorItemAdmin)

class SponsorShipAdmin(admin.ModelAdmin):
    pass
admin.site.register(SponsorShip, SponsorShipAdmin)

@admin.register(CompanySurvey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("company",)

    #define export URLs eg:...admin/recruit/signup/export
    def get_urls(self):
        urls = super(SurveyAdmin, self).get_urls()
        my_urls = [
                url(r'^export/$', export.ExportSurvey, name="recruit_survey_export"),
                ]
        return my_urls + urls

@admin.register(Files)
class RecruitFilesAdmin(admin.ModelAdmin):
    list_display=('title','category','upload_file','updated')
