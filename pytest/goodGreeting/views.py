from	datetime	import	time
from	django.http	import	HttpResponse
from	.greeter	import	greeting_at
def	greet(request):
				now	=	datetime.now().time()
				greeting	=	greeting_at(now)
				return	HttpResponse('Good	%s!'	%
																								greeting)