from	datetime	import	datetime,	time
from	django.http	import	HttpResponse
def	greet(request):
				now	=	datetime.now().time()
				if	time(5)	<	now	<	time(12):
								greeting	=	'morning'
				elif	time(18)	<	now	<	time(21):
								greeting	=	'evening'
				else:
								greeting	=	'day'
				return	HttpResponse('Good	%s!'	%	greeting)