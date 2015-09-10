# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='nesl.ee.ucla',
  serialized_pb=_b('\n\rexample.proto\x12\x0cnesl.ee.ucla\"\x1f\n\x0cHelloRequest\x12\x0f\n\x07my_name\x18\x02 \x02(\t\"$\n\rHelloResponse\x12\x13\n\x0bhello_world\x18\x01 \x02(\t2Z\n\x11HelloWorldService\x12\x45\n\nHelloWorld\x12\x1a.nesl.ee.ucla.HelloRequest\x1a\x1b.nesl.ee.ucla.HelloResponseB\x06\x88\x01\x01\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='nesl.ee.ucla.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='my_name', full_name='nesl.ee.ucla.HelloRequest.my_name', index=0,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=62,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='nesl.ee.ucla.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello_world', full_name='nesl.ee.ucla.HelloResponse.hello_world', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:nesl.ee.ucla.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:nesl.ee.ucla.HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\210\001\001\220\001\001'))

_HELLOWORLDSERVICE = _descriptor.ServiceDescriptor(
  name='HelloWorldService',
  full_name='nesl.ee.ucla.HelloWorldService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=102,
  serialized_end=192,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloWorld',
    full_name='nesl.ee.ucla.HelloWorldService.HelloWorld',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLORESPONSE,
    options=None,
  ),
])

HelloWorldService = service_reflection.GeneratedServiceType('HelloWorldService', (_service.Service,), dict(
  DESCRIPTOR = _HELLOWORLDSERVICE,
  __module__ = 'example_pb2'
  ))

HelloWorldService_Stub = service_reflection.GeneratedServiceStubType('HelloWorldService_Stub', (HelloWorldService,), dict(
  DESCRIPTOR = _HELLOWORLDSERVICE,
  __module__ = 'example_pb2'
  ))


# @@protoc_insertion_point(module_scope)