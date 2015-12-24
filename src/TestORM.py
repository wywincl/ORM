#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Models import Model
from Field import StringField, IntegerField


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12, name='John', email='a.a', password='a')

u.save()
