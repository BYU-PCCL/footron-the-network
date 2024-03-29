# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network.proto',
  package='thenetwork',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rnetwork.proto\x12\nthenetwork\"!\n\x0c\x46rameRequest\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"S\n\rAlignmentBbox\x12 \n\x02ne\x18\x01 \x01(\x0b\x32\x14.thenetwork.Position\x12 \n\x02sw\x18\x02 \x01(\x0b\x32\x14.thenetwork.Position\".\n\x04Room\x12&\n\x08position\x18\x01 \x01(\x0b\x32\x14.thenetwork.Position\"Y\n\x0fNetworkMovement\x12#\n\x05start\x18\x01 \x01(\x0b\x32\x14.thenetwork.Position\x12!\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x14.thenetwork.Position\"\xa5\x01\n\tAlignment\x12\'\n\x04\x62\x62ox\x18\x01 \x01(\x0b\x32\x19.thenetwork.AlignmentBbox\x12/\n\x05rooms\x18\x02 \x03(\x0b\x32 .thenetwork.Alignment.RoomsEntry\x1a>\n\nRoomsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.thenetwork.Room:\x02\x38\x01\"B\n\x10NetworkMovements\x12.\n\tmovements\x18\x01 \x03(\x0b\x32\x1b.thenetwork.NetworkMovement2\xa0\x01\n\nTheNetwork\x12\x41\n\x0cGetAlignment\x12\x18.thenetwork.FrameRequest\x1a\x15.thenetwork.Alignment\"\x00\x12O\n\x13GetNetworkMovements\x12\x18.thenetwork.FrameRequest\x1a\x1c.thenetwork.NetworkMovements\"\x00\x62\x06proto3'
)




_FRAMEREQUEST = _descriptor.Descriptor(
  name='FrameRequest',
  full_name='thenetwork.FrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='thenetwork.FrameRequest.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=62,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='thenetwork.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='thenetwork.Position.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='thenetwork.Position.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='thenetwork.Position.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=107,
)


_ALIGNMENTBBOX = _descriptor.Descriptor(
  name='AlignmentBbox',
  full_name='thenetwork.AlignmentBbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ne', full_name='thenetwork.AlignmentBbox.ne', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sw', full_name='thenetwork.AlignmentBbox.sw', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=192,
)


_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='thenetwork.Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='thenetwork.Room.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=240,
)


_NETWORKMOVEMENT = _descriptor.Descriptor(
  name='NetworkMovement',
  full_name='thenetwork.NetworkMovement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='thenetwork.NetworkMovement.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='thenetwork.NetworkMovement.end', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=331,
)


_ALIGNMENT_ROOMSENTRY = _descriptor.Descriptor(
  name='RoomsEntry',
  full_name='thenetwork.Alignment.RoomsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='thenetwork.Alignment.RoomsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='thenetwork.Alignment.RoomsEntry.value', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=499,
)

_ALIGNMENT = _descriptor.Descriptor(
  name='Alignment',
  full_name='thenetwork.Alignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bbox', full_name='thenetwork.Alignment.bbox', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rooms', full_name='thenetwork.Alignment.rooms', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ALIGNMENT_ROOMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=499,
)


_NETWORKMOVEMENTS = _descriptor.Descriptor(
  name='NetworkMovements',
  full_name='thenetwork.NetworkMovements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='movements', full_name='thenetwork.NetworkMovements.movements', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=567,
)

_ALIGNMENTBBOX.fields_by_name['ne'].message_type = _POSITION
_ALIGNMENTBBOX.fields_by_name['sw'].message_type = _POSITION
_ROOM.fields_by_name['position'].message_type = _POSITION
_NETWORKMOVEMENT.fields_by_name['start'].message_type = _POSITION
_NETWORKMOVEMENT.fields_by_name['end'].message_type = _POSITION
_ALIGNMENT_ROOMSENTRY.fields_by_name['value'].message_type = _ROOM
_ALIGNMENT_ROOMSENTRY.containing_type = _ALIGNMENT
_ALIGNMENT.fields_by_name['bbox'].message_type = _ALIGNMENTBBOX
_ALIGNMENT.fields_by_name['rooms'].message_type = _ALIGNMENT_ROOMSENTRY
_NETWORKMOVEMENTS.fields_by_name['movements'].message_type = _NETWORKMOVEMENT
DESCRIPTOR.message_types_by_name['FrameRequest'] = _FRAMEREQUEST
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['AlignmentBbox'] = _ALIGNMENTBBOX
DESCRIPTOR.message_types_by_name['Room'] = _ROOM
DESCRIPTOR.message_types_by_name['NetworkMovement'] = _NETWORKMOVEMENT
DESCRIPTOR.message_types_by_name['Alignment'] = _ALIGNMENT
DESCRIPTOR.message_types_by_name['NetworkMovements'] = _NETWORKMOVEMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameRequest = _reflection.GeneratedProtocolMessageType('FrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.FrameRequest)
  })
_sym_db.RegisterMessage(FrameRequest)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.Position)
  })
_sym_db.RegisterMessage(Position)

AlignmentBbox = _reflection.GeneratedProtocolMessageType('AlignmentBbox', (_message.Message,), {
  'DESCRIPTOR' : _ALIGNMENTBBOX,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.AlignmentBbox)
  })
_sym_db.RegisterMessage(AlignmentBbox)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), {
  'DESCRIPTOR' : _ROOM,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.Room)
  })
_sym_db.RegisterMessage(Room)

NetworkMovement = _reflection.GeneratedProtocolMessageType('NetworkMovement', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKMOVEMENT,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.NetworkMovement)
  })
_sym_db.RegisterMessage(NetworkMovement)

Alignment = _reflection.GeneratedProtocolMessageType('Alignment', (_message.Message,), {

  'RoomsEntry' : _reflection.GeneratedProtocolMessageType('RoomsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALIGNMENT_ROOMSENTRY,
    '__module__' : 'network_pb2'
    # @@protoc_insertion_point(class_scope:thenetwork.Alignment.RoomsEntry)
    })
  ,
  'DESCRIPTOR' : _ALIGNMENT,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.Alignment)
  })
_sym_db.RegisterMessage(Alignment)
_sym_db.RegisterMessage(Alignment.RoomsEntry)

NetworkMovements = _reflection.GeneratedProtocolMessageType('NetworkMovements', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKMOVEMENTS,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:thenetwork.NetworkMovements)
  })
_sym_db.RegisterMessage(NetworkMovements)


_ALIGNMENT_ROOMSENTRY._options = None

_THENETWORK = _descriptor.ServiceDescriptor(
  name='TheNetwork',
  full_name='thenetwork.TheNetwork',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=570,
  serialized_end=730,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAlignment',
    full_name='thenetwork.TheNetwork.GetAlignment',
    index=0,
    containing_service=None,
    input_type=_FRAMEREQUEST,
    output_type=_ALIGNMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetNetworkMovements',
    full_name='thenetwork.TheNetwork.GetNetworkMovements',
    index=1,
    containing_service=None,
    input_type=_FRAMEREQUEST,
    output_type=_NETWORKMOVEMENTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_THENETWORK)

DESCRIPTOR.services_by_name['TheNetwork'] = _THENETWORK

# @@protoc_insertion_point(module_scope)
