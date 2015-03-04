from locust import HttpLocust, TaskSet, task
import extended_methods #modulo para operaciones con los responses

class UserBehavior(TaskSet):
        def on_start(self):
                """ on_start is called when a Locust start before any task is scheduled """
		#self.client.headers = {"Accept-Encoding":""}
	@task(1)
	def index(self):
                #response = self.client.get("/")
                #print "Response status code:", response.status_code
                #print "Headers:", response.headers
                #print "Response content:", response.content
		#response = self.client.post("/login", {"username":"testuser", "password":"secret"})
		with self.client.get("/", catch_response=True) as response:
                        extended_methods.CheckContent(response,"Barcelona")
                #print "Cookies:", response.cookies
                #print "Codigos previos (redirects):", response.history

        @task(1)
	def dedicados(self):
                self.client.get("/dedicados-e-hibridos")
		print "dedicados"

class WebsiteUser(HttpLocust): #usamos la subclase Http de locust
        task_set = UserBehavior # el atributo task_set debe apuntar a la clase TaskSet para definir el comportamiento del usuario
        # tiempo min y max entre tareas. Se puede sobreescribir en clase TaskSet
	host = "http://ackstorm.es"
	min_wait=5000 
        max_wait=9000
