from locust import HttpLocust, TaskSet, task
import extended_methods #modulo para operaciones con los responses

class UserBehavior(TaskSet):
        def on_start(self):
                """ on_start is called when a Locust start before any task is scheduled """

        @task(1)
        def index(self):
                #response = self.client.get("/")
                #print "Response status code:", response.status_code
                #print "Headers:", response.headers
                #print "Response content:", response.content
                with self.client.get("/", catch_response=True) as response:
                        Message = extended_methods.CheckContent(response,"hola")

                #print "Cookies:", response.cookies
                #print "Codigos previos (redirects):", response.history

        @task(1)
        def dedicados(self):
                self.client.get("/dedicados-e-hibridos")

class WebsiteUser(HttpLocust):
        task_set = UserBehavior # creamos objeto de la clase TaskSet
        min_wait=5000
        max_wait=9000
