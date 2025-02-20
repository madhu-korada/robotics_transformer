# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensor2robot/proto/t2r.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensor2robot/proto/t2r.proto',
  package='third_party.py.tensor2robot',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ctensor2robot/proto/t2r.proto\x12\x1bthird_party.py.tensor2robot\"\xb3\x01\n\x12\x45xtendedTensorSpec\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\r\n\x05\x64type\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bis_optional\x18\x04 \x01(\x08\x12\x14\n\x0cis_extracted\x18\x05 \x01(\x08\x12\x13\n\x0b\x64\x61ta_format\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x61taset_key\x18\x07 \x01(\t\x12\x1c\n\x14varlen_default_value\x18\x08 \x01(\x02\"\xc4\x01\n\x10TensorSpecStruct\x12N\n\tkey_value\x18\x01 \x03(\x0b\x32;.third_party.py.tensor2robot.TensorSpecStruct.KeyValueEntry\x1a`\n\rKeyValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.third_party.py.tensor2robot.ExtendedTensorSpec:\x02\x38\x01\"\xa8\x01\n\tT2RAssets\x12\x43\n\x0c\x66\x65\x61ture_spec\x18\x01 \x01(\x0b\x32-.third_party.py.tensor2robot.TensorSpecStruct\x12\x41\n\nlabel_spec\x18\x02 \x01(\x0b\x32-.third_party.py.tensor2robot.TensorSpecStruct\x12\x13\n\x0bglobal_step\x18\x03 \x01(\x05'
)




_EXTENDEDTENSORSPEC = _descriptor.Descriptor(
  name='ExtendedTensorSpec',
  full_name='third_party.py.tensor2robot.ExtendedTensorSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.dtype', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_optional', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.is_optional', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_extracted', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.is_extracted', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_format', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.data_format', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_key', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.dataset_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='varlen_default_value', full_name='third_party.py.tensor2robot.ExtendedTensorSpec.varlen_default_value', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=62,
  serialized_end=241,
)


_TENSORSPECSTRUCT_KEYVALUEENTRY = _descriptor.Descriptor(
  name='KeyValueEntry',
  full_name='third_party.py.tensor2robot.TensorSpecStruct.KeyValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='third_party.py.tensor2robot.TensorSpecStruct.KeyValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='third_party.py.tensor2robot.TensorSpecStruct.KeyValueEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=440,
)

_TENSORSPECSTRUCT = _descriptor.Descriptor(
  name='TensorSpecStruct',
  full_name='third_party.py.tensor2robot.TensorSpecStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_value', full_name='third_party.py.tensor2robot.TensorSpecStruct.key_value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSORSPECSTRUCT_KEYVALUEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=440,
)


_T2RASSETS = _descriptor.Descriptor(
  name='T2RAssets',
  full_name='third_party.py.tensor2robot.T2RAssets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_spec', full_name='third_party.py.tensor2robot.T2RAssets.feature_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_spec', full_name='third_party.py.tensor2robot.T2RAssets.label_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='global_step', full_name='third_party.py.tensor2robot.T2RAssets.global_step', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=443,
  serialized_end=611,
)

_TENSORSPECSTRUCT_KEYVALUEENTRY.fields_by_name['value'].message_type = _EXTENDEDTENSORSPEC
_TENSORSPECSTRUCT_KEYVALUEENTRY.containing_type = _TENSORSPECSTRUCT
_TENSORSPECSTRUCT.fields_by_name['key_value'].message_type = _TENSORSPECSTRUCT_KEYVALUEENTRY
_T2RASSETS.fields_by_name['feature_spec'].message_type = _TENSORSPECSTRUCT
_T2RASSETS.fields_by_name['label_spec'].message_type = _TENSORSPECSTRUCT
DESCRIPTOR.message_types_by_name['ExtendedTensorSpec'] = _EXTENDEDTENSORSPEC
DESCRIPTOR.message_types_by_name['TensorSpecStruct'] = _TENSORSPECSTRUCT
DESCRIPTOR.message_types_by_name['T2RAssets'] = _T2RASSETS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtendedTensorSpec = _reflection.GeneratedProtocolMessageType('ExtendedTensorSpec', (_message.Message,), {
  'DESCRIPTOR' : _EXTENDEDTENSORSPEC,
  '__module__' : 'tensor2robot.proto.t2r_pb2'
  # @@protoc_insertion_point(class_scope:third_party.py.tensor2robot.ExtendedTensorSpec)
  })
_sym_db.RegisterMessage(ExtendedTensorSpec)

TensorSpecStruct = _reflection.GeneratedProtocolMessageType('TensorSpecStruct', (_message.Message,), {

  'KeyValueEntry' : _reflection.GeneratedProtocolMessageType('KeyValueEntry', (_message.Message,), {
    'DESCRIPTOR' : _TENSORSPECSTRUCT_KEYVALUEENTRY,
    '__module__' : 'tensor2robot.proto.t2r_pb2'
    # @@protoc_insertion_point(class_scope:third_party.py.tensor2robot.TensorSpecStruct.KeyValueEntry)
    })
  ,
  'DESCRIPTOR' : _TENSORSPECSTRUCT,
  '__module__' : 'tensor2robot.proto.t2r_pb2'
  # @@protoc_insertion_point(class_scope:third_party.py.tensor2robot.TensorSpecStruct)
  })
_sym_db.RegisterMessage(TensorSpecStruct)
_sym_db.RegisterMessage(TensorSpecStruct.KeyValueEntry)

T2RAssets = _reflection.GeneratedProtocolMessageType('T2RAssets', (_message.Message,), {
  'DESCRIPTOR' : _T2RASSETS,
  '__module__' : 'tensor2robot.proto.t2r_pb2'
  # @@protoc_insertion_point(class_scope:third_party.py.tensor2robot.T2RAssets)
  })
_sym_db.RegisterMessage(T2RAssets)


_TENSORSPECSTRUCT_KEYVALUEENTRY._options = None
# @@protoc_insertion_point(module_scope)
