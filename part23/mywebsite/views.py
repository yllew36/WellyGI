from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Home<h1>")

def link(request,page):
	str = "<h1>Ini Page {}</h1>".format(page)
	return HttpResponse(str)

def angka(request,input):
	heading = "<h1> Page Angka <h1>"
	inputs = input
	str = heading + inputs
	return HttpResponse(str)

def tanggal(reqest,**input):
	print(input)
	tahun = input['tahun']
	bulan = input['bulan']
	tanggal = input['tanggal']
	heading = "<h1> Page Tanggal </h1>"
	dataTanggal = "<h2>tahun : {} / bulan : {} / tanggal : {}</h2>".format(tahun,bulan,tanggal)
	return HttpResponse(heading + dataTanggal)

# def tanggal(request,tahun,bulan,tanggal):
# 	heading = "<h1> Page Tanggal </h1>"
# 	strTahun = "<h2>tahun : " + tahun +"</h2>"
# 	strBulan = "<h3>bulan : " + bulan  +"</h3>"
# 	strTanggal = "<h4>tanggal : " + tanggal +"</h4>"
# 	str = heading + strTahun  + strBulan  + strTanggal
# 	return HttpResponse(str)