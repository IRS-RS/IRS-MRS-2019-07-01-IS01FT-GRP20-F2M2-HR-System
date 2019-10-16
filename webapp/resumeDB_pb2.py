# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resumeDB.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='resumeDB.proto',
  package='hr.domain',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b(
    '\n\x0eresumeDB.proto\x12\thr.domain\"\xd4\x01\n\nExperience\x12\x13\n\x0b\x63ompanyName\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x19\n\x11\x64\x61tesEmployedText\x18\x03 \x01(\t\x12\x19\n\x11startDateYYYYMMDD\x18\x04 \x01(\t\x12\x1e\n\x16\x65mploymentDurationText\x18\x05 \x01(\t\x12\"\n\x1a\x65mploymentDurationInMonths\x18\x06 \x01(\x05\x12\x10\n\x08location\x18\x07 \x01(\t\x12\x16\n\x0e\x65xperienceText\x18\x08 \x01(\t\"_\n\tEducation\x12\x12\n\nschoolName\x18\x01 \x01(\t\x12\x12\n\ndegreeName\x18\x02 \x01(\t\x12\x15\n\rstartDateYYYY\x18\x03 \x01(\t\x12\x13\n\x0b\x65ndDateYYYY\x18\x04 \x01(\t\"\xcf\x02\n\x06Resume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\trawResume\x18\x02 \x01(\t\x12\x12\n\nprofileURL\x18\x03 \x01(\t\x12\x15\n\rmonthlySalary\x18\x04 \x01(\x02\x12\x13\n\x0b\x63ompanyName\x18\x05 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12\x10\n\x08\x61\x62outRaw\x18\x07 \x01(\t\x12\x15\n\rexperienceRaw\x18\x08 \x01(\t\x12\x14\n\x0c\x65\x64ucationRaw\x18\t \x01(\t\x12!\n\x19licensesCertificationsRaw\x18\n \x01(\t\x12\x1d\n\x15skillsEndorsementsRaw\x18\x0b \x01(\t\x12*\n\x0b\x65xperiences\x18\x10 \x03(\x0b\x32\x15.hr.domain.Experience\x12(\n\neducations\x18\x11 \x03(\x0b\x32\x14.hr.domain.Education\".\n\x08ResumeDB\x12\"\n\x07resumes\x18\x01 \x03(\x0b\x32\x11.hr.domain.Resumeb\x06proto3')
)




_EXPERIENCE = _descriptor.Descriptor(
  name='Experience',
  full_name='hr.domain.Experience',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='companyName', full_name='hr.domain.Experience.companyName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='hr.domain.Experience.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datesEmployedText', full_name='hr.domain.Experience.datesEmployedText', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDateYYYYMMDD', full_name='hr.domain.Experience.startDateYYYYMMDD', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='employmentDurationText', full_name='hr.domain.Experience.employmentDurationText', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='employmentDurationInMonths', full_name='hr.domain.Experience.employmentDurationInMonths', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='hr.domain.Experience.location', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experienceText', full_name='hr.domain.Experience.experienceText', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=30,
  serialized_end=242,
)


_EDUCATION = _descriptor.Descriptor(
  name='Education',
  full_name='hr.domain.Education',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schoolName', full_name='hr.domain.Education.schoolName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='degreeName', full_name='hr.domain.Education.degreeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDateYYYY', full_name='hr.domain.Education.startDateYYYY', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endDateYYYY', full_name='hr.domain.Education.endDateYYYY', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=244,
  serialized_end=339,
)


_RESUME = _descriptor.Descriptor(
  name='Resume',
  full_name='hr.domain.Resume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hr.domain.Resume.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rawResume', full_name='hr.domain.Resume.rawResume', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profileURL', full_name='hr.domain.Resume.profileURL', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monthlySalary', full_name='hr.domain.Resume.monthlySalary', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='hr.domain.Resume.companyName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='hr.domain.Resume.title', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aboutRaw', full_name='hr.domain.Resume.aboutRaw', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experienceRaw', full_name='hr.domain.Resume.experienceRaw', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='educationRaw', full_name='hr.domain.Resume.educationRaw', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='licensesCertificationsRaw', full_name='hr.domain.Resume.licensesCertificationsRaw', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skillsEndorsementsRaw', full_name='hr.domain.Resume.skillsEndorsementsRaw', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiences', full_name='hr.domain.Resume.experiences', index=11,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='educations', full_name='hr.domain.Resume.educations', index=12,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=342,
  serialized_end=677,
)


_RESUMEDB = _descriptor.Descriptor(
  name='ResumeDB',
  full_name='hr.domain.ResumeDB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resumes', full_name='hr.domain.ResumeDB.resumes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=679,
  serialized_end=725,
)

_RESUME.fields_by_name['experiences'].message_type = _EXPERIENCE
_RESUME.fields_by_name['educations'].message_type = _EDUCATION
_RESUMEDB.fields_by_name['resumes'].message_type = _RESUME
DESCRIPTOR.message_types_by_name['Experience'] = _EXPERIENCE
DESCRIPTOR.message_types_by_name['Education'] = _EDUCATION
DESCRIPTOR.message_types_by_name['Resume'] = _RESUME
DESCRIPTOR.message_types_by_name['ResumeDB'] = _RESUMEDB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Experience = _reflection.GeneratedProtocolMessageType('Experience', (_message.Message,), {
  'DESCRIPTOR': _EXPERIENCE,
  '__module__': 'resumeDB_pb2'
  # @@protoc_insertion_point(class_scope:hr.domain.Experience)
})
_sym_db.RegisterMessage(Experience)

Education = _reflection.GeneratedProtocolMessageType('Education', (_message.Message,), {
  'DESCRIPTOR': _EDUCATION,
  '__module__': 'resumeDB_pb2'
  # @@protoc_insertion_point(class_scope:hr.domain.Education)
})
_sym_db.RegisterMessage(Education)

Resume = _reflection.GeneratedProtocolMessageType('Resume', (_message.Message,), {
  'DESCRIPTOR': _RESUME,
  '__module__': 'resumeDB_pb2'
  # @@protoc_insertion_point(class_scope:hr.domain.Resume)
})
_sym_db.RegisterMessage(Resume)

ResumeDB = _reflection.GeneratedProtocolMessageType('ResumeDB', (_message.Message,), {
  'DESCRIPTOR': _RESUMEDB,
  '__module__': 'resumeDB_pb2'
  # @@protoc_insertion_point(class_scope:hr.domain.ResumeDB)
})
_sym_db.RegisterMessage(ResumeDB)

# @@protoc_insertion_point(module_scope)
