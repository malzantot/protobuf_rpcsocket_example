import sys

import protobuf.socketrpc.server as server
import HelloWorldServiceImpl as impl

hello_world_service = impl.HelloWorldServiceImpl()
server = server.SocketRpcServer(8090)
server.registerService(hello_world_service)

print "Serving on port 8090"
server.run()

