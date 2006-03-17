#
# SchoolTool - common information systems platform for school administration
# Copyright (c) 2005 Shuttleworth Foundation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""Term sample data generation

$Id$
"""
import datetime
import zope.interface

from schooltool.term import term
from schooltool.sampledata.interfaces import ISampleDataPlugin

class SampleTerms(object):
    """Sample data generator for terms."""
    zope.interface.implements(ISampleDataPlugin)

    name = 'terms'
    dependencies = ()

    def generate(self, app, seed=None):
        date = datetime.date
        fall = term.Term('2005-fall', date(2005, 8, 22), date(2005, 12, 23))
        fall.addWeekdays(0, 1, 2, 3, 4)
        app['terms']['2005-fall'] = fall

        spring = term.Term('2006-spring', date(2006, 1, 26), date(2006, 5, 31))
        spring.addWeekdays(0, 1, 2, 3, 4)
        app['terms']['2006-spring'] = spring