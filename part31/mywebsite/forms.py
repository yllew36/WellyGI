from django import forms


class FormField(forms.Form):
	#python data type
	integer_field 	= forms.IntegerField()
	decimal_field 	= forms.DecimalField()
	float_field 	= forms.FloatField()
	boolean_field 	= forms.BooleanField()
	char_field 		= forms.CharField()

#string input

	email_field 	= forms.EmailField(initial='email@gmail.com')
	regex_field 	= forms.RegexField(regex=r'(P?<test>)')
	slug_field  	= forms.SlugField()
	url_field 		= forms.URLField()
	ip_field 		= forms.GenericIPAddressField()

	#select input

	Pilihan = (
			('nilai1','Pilihan 1'),
			('nilai2','Pilihan 2'),
			('nilai3','Pilihan 3'),
		)

	choice_field 		= forms.ChoiceField(choices=Pilihan)
	multi_choice_field 	= forms.MultipleChoiceField(choices=Pilihan)
	multi_typed_choice	= forms.TypedMultipleChoiceField(choices=Pilihan)
	null_boolean_field	= forms.NullBooleanField()

	#date time

	date_field  		= forms.DateField()
	datetime_field		= forms.DateTimeField()
	duration_field		= forms.DurationField()
	time_field			= forms.TimeField()
	splitdatetime_field	= forms.SplitDateTimeField()

	#file input
	file_field			= forms.FileField()
	image_field			= forms.ImageField()