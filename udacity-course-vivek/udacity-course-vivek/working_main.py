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
import webapp2
# add action="/testform" in form to run the testhandler
form="""
<form method="post">
  What is your birthday?
  <br>
  <label>Month
  <input type="text" name="month"></label>
  <label>Day
  <input type="text" name="day"></label>
  <label>Year
  <input type="text" name="year"></label>
  <div style="color: red">%(error)s</div>
  <br>
  <br>
  <input type="submit">
</form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
    
def valid_day(day):
    
    if day and day.isdigit():
        d = int(day)
        if d > 0 and d < 32:
            return d
        
def valid_year(year):
    if year and year.isdigit():
        y = int(year)
        if y >=1900 and y <=2020:
            return y

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.write(form % {"error": error})

    def get(self):
      #self.response.write(form)
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_year and user_day and user_month):
            self.write_form("That doesn't look valid to me, friend.")
        #self.response.write(form)
        else:
            self.response.write("Thanks! That's a totally valid day!")

      

"""class TestHandler(webapp2.RequestHandler):
    def post(self):
        #q = self.request.get("q")
        #self.response.write(q)
        self.response.write(self.request)
"""
app = webapp2.WSGIApplication([
    ('/', MainHandler)
    #,('/testform', TestHandler)
], debug=True)