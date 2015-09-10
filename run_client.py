import example_pb2
from protobuf.socketrpc import RpcService

host_name = 'localhost'
port = 8090

# create a request
request = example_pb2.HelloRequest()
request.my_name = "Moustafa Alzantot"

service = RpcService(example_pb2.HelloWorldService_Stub,
        port, host_name)

response = service.HelloWorld(request, timeout=10000)
print "Recieved : %s" %response.hello_world



