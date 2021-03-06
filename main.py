#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import logging
import os
import webapp2
import urllib2
import json
import random

destinations = ['London, England','Dublin, Ireland','Los Angeles, California',
'New York City, New York','Nuku\'alofa, Tonga','Berlin, Germany','Sydney, Australia',
'Vancouver, Canada'
]
#may need to eventually make this a dictionary depending on which API I use
'''
destinations = {
	'London, England' : ['something'],
	'Dublin, Ireland' : ['something']
}
'''

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {
        }
        template = jinja_environment.get_template('views/index.html')
        self.response.out.write(template.render(template_values))

class ThrowHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {'name' : self.request.get('name'),
    	'today' : self.request.get('today'),
    	'destination' : random.choice(destinations)
        }
        template = jinja_environment.get_template('views/throw.html')
        self.response.out.write(template.render(template_values))

routes = [('/', MainHandler),('/throw', ThrowHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 