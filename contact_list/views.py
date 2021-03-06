from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, HttpResponse
from contact_list.forms import ContactForm
from contact_list.models import Contact

@csrf_protect
def create_contact(request):
	context = RequestContext(request)

	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)

		if contact_form.is_valid():
			contact_form.save()
			return HttpResponseRedirect('/list/')

	else:
		contact_form = ContactForm()

	return render_to_response('contact_list/new_con.html', {'form' : contact_form}, context)


def contact_list(request):
	context = RequestContext(request)
	contacts = Contact.objects.all()

	return render_to_response('contact_list/list.html', {'contacts' : contacts}, context)


def contact_detail(request, contact_id):
	context = RequestContext(request)
	contact = Contact.objects.get(pk=contact_id)

	return render_to_response('contact_list/detail.html', {'contact' : contact}, context)


def edit_contact(request, contact_id):
	context = RequestContext(request)
	contact = Contact.objects.get(pk=contact_id)

	if request.method == 'POST':
		contact_form = ContactForm(request.POST, instance=contact)

		if contact_form.is_valid():
			contact_form.save()
			return HttpResponseRedirect('/list/')

	else:
		contact_form = ContactForm(instance=contact)
	return render_to_response('contact_list/edit_contact.html', {'form' : contact_form}, context)


def delete_contact(request, contact_id):
	context = RequestContext(request)
	contact = Contact.objects.get(pk=contact_id)

	if request.method == 'POST':
		contact.delete()
		return HttpResponseRedirect('/list/')

	return render_to_response('contact_list/delete_contact.html', {'contact' : contact}, context)


def search(request):
	context = RequestContext(request)

	if request.method == 'POST':
		contact = request.POST['search_contact']

		try:
			result = Contact.objects.get(name=contact)
			index = str(result.id)
		except Contact.DoesNotExist:
			result = None

		if result == None :
			return HttpResponse("Contact not Found")
		else :
			return HttpResponseRedirect('/detail/'+ index + '/')
	
	return render_to_response('contact_list/search.html', {}, context)
