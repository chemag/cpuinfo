# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cpuid.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cpuid.proto',
  package='cpuid',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x63puid.proto\x12\x05\x63puid\"\'\n\x0bImplementer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"8\n\x04Part\x12\x16\n\x0eimplementer_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"N\n\x08\x44\x61tabase\x12\'\n\x0bimplementer\x18\x01 \x03(\x0b\x32\x12.cpuid.Implementer\x12\x19\n\x04part\x18\x02 \x03(\x0b\x32\x0b.cpuid.Part'
)




_IMPLEMENTER = _descriptor.Descriptor(
  name='Implementer',
  full_name='cpuid.Implementer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cpuid.Implementer.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cpuid.Implementer.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=61,
)


_PART = _descriptor.Descriptor(
  name='Part',
  full_name='cpuid.Part',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='implementer_id', full_name='cpuid.Part.implementer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cpuid.Part.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cpuid.Part.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=119,
)


_DATABASE = _descriptor.Descriptor(
  name='Database',
  full_name='cpuid.Database',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='implementer', full_name='cpuid.Database.implementer', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='part', full_name='cpuid.Database.part', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=199,
)

_DATABASE.fields_by_name['implementer'].message_type = _IMPLEMENTER
_DATABASE.fields_by_name['part'].message_type = _PART
DESCRIPTOR.message_types_by_name['Implementer'] = _IMPLEMENTER
DESCRIPTOR.message_types_by_name['Part'] = _PART
DESCRIPTOR.message_types_by_name['Database'] = _DATABASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Implementer = _reflection.GeneratedProtocolMessageType('Implementer', (_message.Message,), {
  'DESCRIPTOR' : _IMPLEMENTER,
  '__module__' : 'cpuid_pb2'
  # @@protoc_insertion_point(class_scope:cpuid.Implementer)
  })
_sym_db.RegisterMessage(Implementer)

Part = _reflection.GeneratedProtocolMessageType('Part', (_message.Message,), {
  'DESCRIPTOR' : _PART,
  '__module__' : 'cpuid_pb2'
  # @@protoc_insertion_point(class_scope:cpuid.Part)
  })
_sym_db.RegisterMessage(Part)

Database = _reflection.GeneratedProtocolMessageType('Database', (_message.Message,), {
  'DESCRIPTOR' : _DATABASE,
  '__module__' : 'cpuid_pb2'
  # @@protoc_insertion_point(class_scope:cpuid.Database)
  })
_sym_db.RegisterMessage(Database)


# @@protoc_insertion_point(module_scope)
