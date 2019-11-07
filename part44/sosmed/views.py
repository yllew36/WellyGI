from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView, View
# Create your views here.

from .models import Instagram
from .forms import InstagramForm


class SosmedSubList:
	def get_list_data(self,get_request):
		if len(get_request) == 0:
			sublist = Instagram.objects.all()
		elif get_request.__contains__('content_filter'):
			sublist = Instagram.objects.filter(content =get_request['content_filter'])
		else:
			sublist = Instagram.objects.none()
		return sublist


class SosmedListView(SosmedSubList ,TemplateView):
    template_name = 'sosmed/list.html'

    def get_context_data(self):
        # semua_akun = Instagram.objects.all()
        list_akun = self.get_list_data(self.request.GET)
        list_content = Instagram.objects.values_list('content',flat = True).distinct()
        print(list_akun)    

        context = {
            'page_title': 'Sosial_media memakai class based view',
            'semua_akun': list_akun,
            'list_content':list_content,
        }
        return context


class SosmedDeleteView(RedirectView):
    pattern_name = 'sosmed:list'
    # permanent	= False
    # query_string = False

    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs)
        delete_id = kwargs['delete_id']
        # print(delete_id)
        Instagram.objects.filter(id=delete_id).delete()
        return super().get_redirect_url()


class SosmedFormView(View):
    template_name = 'sosmed/create.html'
    form = InstagramForm()
    mode = None
    context = {}

    def get(self, *args, **kwargs):
    	if self.mode == 'update':
    		akun_update = Instagram.objects.get(id=kwargs['update_id'])
    		data = ''
    		self.context = {
    			'page_title':'Tambah Akun'
    		}
    		self.form = InstagramForm(initial=data,instance=akun_update)

    	
    	self.context = {
    		'page_title':'Update Form',
    		'akun_form':self.form,
    	}
    	return render(self.request,self.template_name,self.context)

    def post(self,*args,**kwargs):
    	print(kwargs)

    	if kwargs.__contains__('update_id'):
    		akun_update = Instagram.objects.get(id=kwargs['update_id'])
    		self.form = InstagramForm(self.request.POST,instance=akun_update)
    	else:
    		self.form = InstagramForm(self.request.POST)

    	if self.form.is_valid():
    		self.form.save()

    	return redirect('sosmed:list')


# def delete(request, delete_id):
#     Instagram.objects.filter(id=delete_id).delete()
#     return redirect('sosmed:list')


def update(request, update_id):
    akun_update = Instagram.objects.get(id=update_id)

    data = {
        # 'nama_depan'		: akun_update.nama_depan,
        # 'nama_belakang'	: akun_update.nama_belakang,
        # 'username'		: akun_update.username,

    }

    akun_form = InstagramForm(request.POST or None,
                              initial=data, instance=akun_update)

    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()

        return redirect('sosmed:list')

    dict = {
        'page_title': 'Update Akun',
        'akun_form': akun_form,
    }

    return render(request, 'sosmed/create.html', dict)

    return redirect('sosmed:list')


def create(request):
    akun_form = InstagramForm(request.POST or None)

    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()

        return redirect('sosmed:list')

    dict = {
        'page_title': 'Tambah Akun',
        'akun_form': akun_form,
    }

    return render(request, 'sosmed/create.html', dict)


# def list(request):
#     semua_akun = Instagram.objects.all()

#     dict = {
#         'page_title': 'Sosial Media',
#         'semua_akun': semua_akun,
#     }
#     return render(request, 'sosmed/list.html', dict)
