from django.http                    import HttpResponseRedirect
from django.shortcuts               import render_to_response
from django.template                import RequestContext
from django.contrib.auth.decorators import login_required

import datetime

from pymongo.connection import Connection


db = Connection().browner


@login_required
def main(request):
	browns = db.browns.find_one({'browned' : request.user.username} , {'browns' : 1})

	numbers = ["one", "two", "three", "four"]
	tasklist = []

	if browns:
		for k in range(0, len(numbers)):
			try:
				tasklist.append( { "number" : numbers[k] , "brown" : browns['browns'][k]['brown'] } )
			except IndexError:
				break

	return render_to_response('browner.html',
	                          {'tasklist' : tasklist},
	                          context_instance = RequestContext(request))


@login_required
def pop(request):
	db.browns.update({'browned' : request.user.username} , {"$pop" : {'browns' : -1}})

	return HttpResponseRedirect('/')


@login_required
def add(request):
	if request.method == 'POST':
		if 'add' in request.POST and 'user' in request.POST:
			if db.browns.find_one({'browned' : request.POST['user']}):
				db.browns.update({'browned' : request.POST['user']},
				                 {"$push" : {'browns' : {'brown' : request.POST['task'] , 'timestamp' : datetime.datetime.utcnow()}}})
			else:
				db.browns.insert({'browned' : request.POST['user'] , 'browns' : [ {'brown' : request.POST['task'] , 'timestamp' : datetime.datetime.utcnow()} ] })
		elif 'remove' in request.POST and 'user' in request.POST:
			db.browns.update({'browned' : request.POST['user']}  , {"$pop" : {'browns' : -1}})

		return HttpResponseRedirect('/add')
	else:
		allbrowns = db.browns.find(fields={'browns' : 1})

		brownlist = []
		for brown in allbrowns:
			brownlist.extend(brown['browns'])
		brownlist.sort(key=lambda brown: brown['timestamp'])

		tasklist = []

		for brown in brownlist:
			tasklist.append(brown['brown'])

		return render_to_response('add.html',
								  {'tasklist' : tasklist},
								  context_instance = RequestContext(request))

