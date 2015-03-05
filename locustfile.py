from locust import HttpLocust, TaskSet, task, events
import extended_methods #modulo para operaciones con los responses

class UserBehavior(TaskSet):
        def on_start(self):
                """ on_start is called when a Locust start before any task is scheduled """
		#self.client.headers = {"Accept-Encoding":""}
		
	#@task(1) # tarea a ejecutar n veces usando el decorador
	def index(self): #def = metodo
                #response = self.client.get("/")
                #print "Response status code:", response.status_code
                #print "Headers:", response.headers
                #print "Response content:", response.content
		#response = self.client.post("/subir", {"text":"olakase"})
		with self.client.get("/", catch_response=True) as response: #capturamos la respuesta siempre con el catch_response true
                        extended_methods.CheckContent(response,"Barcelona")
                #print "Cookies:", response.cookies
                #print "Codigos previos (redirects):", response.history

        #@task(1)
	def dedicados(self):
                self.client.get("/dedicados-e-hibridos")
		print "dedicados"
	
	#tasks = {index:1, dedicados:2} # lista de tareas a ejecutar
	
	def subir(self):
                response = self.client.post("/subir", {"text":"olakase"})

        tasks = {subir:1} # lista de tareas a ejecutar

#Hooks
def AllHatched(user_count, **kw):
	print "Hemos acabado!! Num de usuarios: %s" % (user_count)

events.hatch_complete += AllHatched #extendemos el listener hatch_complete

def ExitLocust( **kw):
	print "Se acabo"

events.quitting += ExitLocust

class WebsiteUser(HttpLocust): #usamos la subclase Http de locust
        task_set = UserBehavior # el atributo task_set debe apuntar a la clase TaskSet para definir el comportamiento del usuario
        # tiempo min y max entre tareas. Se puede sobreescribir en clase TaskSet
	#host = "http://ackstorm.es"
	host = "http://iaioos.com:8888"
	min_wait=1000 
        max_wait=2000
