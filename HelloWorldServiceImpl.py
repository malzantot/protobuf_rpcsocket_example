import example_pb2
import time

class HelloWorldServiceImpl(example_pb2.HelloWorldService):
    def HelloWorld(self, controller, request, done):
        print "In Hello World method"
        name = request.my_name
        print "Recieved name = %s" %name

        # Create a response
        response = example_pb2.HelloResponse()
        response.hello_world = "Hello %s" %name

        #time.sleep(1)
        done.run(response)
