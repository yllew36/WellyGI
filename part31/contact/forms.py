from django import forms

class ContactForm(forms.Form):
	nama			= forms.CharField(max_length=255, required=True)
	email 			= forms.EmailField(label='Alamat Email',initial='example@gmail.com')

	Pilihan = (
			('P', 'Pria'),
			('W', 'Wanita'),
		)
	jenis_kelamin	= forms.ChoiceField(choices=Pilihan)
	alamat 			= forms.CharField()
	kode_pos		= forms.CharField(max_length=5)
	kota			= forms.CharField()
	provinsi		= forms.CharField()
	photo			= forms.ImageField(required=False)
	agree			= forms.BooleanField()