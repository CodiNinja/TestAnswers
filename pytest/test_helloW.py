def	test_hello_world(client):
				response	=	client.get('/hi/')
			assert	response.status_code	==	200
			assert	response.content	==	'Hello	World!'