from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
#...
from django.shortcuts import render
from .forms import NameForm

def test_redirect(request):
    return HttpResponseRedirect("http://erakam.mod.gov.my/")



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
	
	
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_ic(request):

	ic = request.POST.get('user', '')
	print (ic)
	return HttpResponse (ic)


	# request.session.get('icNoHT')
    # return render(request, 'ic.html')
	
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
	# request.POST.get("icNoHT", "")
	
	# # if (isset($_SESSION['icNoHT'])) {
	# # $username = $_SESSION['icNoHT'];
	# # $_SESSION['username']=$username;
        # # create a form instance and populate it with data from the request:
        # form = get_ic(request.POST)
        # # check whether it's valid:
        # if form.is_valid():
            # # process the data in form.cleaned_data as required
            # # ...
            # # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
        # form = NameForm()

    # return render(request, 'ic.html', {'form': form})	