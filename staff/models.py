from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator,MinLengthValidator,validate_email
from django.utils import timezone

def validate_all_num(string):
	if not string.isdigit():
		raise ValidationError('必需都是數字')

def validate_mobile(string):
	RegexValidator(regex='^\d{4}-\d{6}$',message='格式：0987-654321')(string)

def validate_phone(string):
	RegexValidator(regex='^\d+-\d+(#\d+)?$',message='格式：區碼-號碼#分機')(string)


class Staff(AbstractUser):
	GENDER = (('M', u'男生'), ('F', u'女生'))
	ROLE = (
			(u'就輔部',         u'就輔部'       ),
			(u'行政部 - 總召',  u'行政部 - 總召'),
			(u'行政部 - 副召',  u'行政部 - 副召'),
			(u'行政部 - 執秘',  u'行政部 - 執秘'),

			(u'公關部 - 部長',  u'公關部 - 部長'),
			(u'公關部 - 部員',  u'公關部 - 部員'),

			(u'設計部 - 部長',  u'設計部 - 部長'),
			(u'設計部 - 部員',  u'設計部 - 部員'),

			(u'企畫部 - 部長',  u'企畫部 - 部長'),
			(u'企畫部 - 部員',  u'企畫部 - 部員'),

			(u'資訊部 - 部長',  u'資訊部 - 部長'),
			(u'資訊部 - 部員',  u'資訊部 - 部員'),

			(u'編輯部 - 部長',  u'編輯部 - 部長'),
			(u'編輯部 - 部員',  u'編輯部 - 部員'),

			)

	id = models.AutoField(primary_key=True)
	name = models.CharField(u'姓名',max_length=10)
	g2_email = models.EmailField(u'G2信箱',max_length=100,
                              help_text='Google Drive權限使用(無則留空)', default='', blank=True)
	gender = models.CharField(u'性別', choices=GENDER, max_length=1)
	birthday = models.DateField(u'出生年月日', default=timezone.now,help_text='格式: YYYY/MM/DD')
	idno= models.CharField(u'身份證字號',max_length=10)
	role = models.CharField(u'職位', choices=ROLE, blank=True, max_length=10)
	mobile = models.CharField(u'手機',max_length=12,help_text='格式: 0912-345678')
	fb_url = models.CharField(u'FB個人首頁連結', default='', max_length=100)
	account = models.CharField(u'郵局或玉山帳號', max_length=25,help_text='帳戶必需是自己的',
			blank=True, null=True
			)

	class Meta:
		managed = True
		db_table = 'staff'

		verbose_name = u"OpenHouse 工作人員"
		verbose_name_plural =u"OpenHouse 工作人員" #上面的複數ZZZ

	def __str__(self):
		return self.get_full_name()
