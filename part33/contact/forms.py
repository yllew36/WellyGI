from django import forms


class ContactForm(forms.Form):

    nama_lengkap = forms.CharField(
        label='Nama Lengkap',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'masukan nama lengkap anda',
            }
        )
    )

    # Gender	=	(
    # 		('L','Laki-laki'),
    # 		('P', 'Perempuan'),
    # 	)
    # jenis_kelamin	= forms.ChoiceField(choices=Gender)

    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-check-input'
            }),

        choices=[
            ('L', 'Laki-laki'),
            ('P', 'Perempuan'),
        ])

    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(
        	attrs = {
        		'class':'form-control col-sm-2'
        	},
            years=range(1945, 2019, 1),
        )
    )
    email = forms.EmailField(
    	widget=forms.TextInput(attrs={
    		'class':'form-control',
    		'placeholder':'example@gmail.com',
    	}))
    alamat = forms.CharField(widget=forms.Textarea(
    	attrs = {
    		'class':'form-control',
    	}))

    agree = forms.BooleanField(
    	widget=forms.CheckboxInput(
    		attrs={'class':'form-check-input'}))
