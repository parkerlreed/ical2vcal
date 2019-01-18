#!/usr/bin/env python

# ical2vcal.cgi by Charl P. Botha http://cpbotha.net/
# based on http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/273844
# integrated work by Mark Graves for VCS file downloading (much better
# than copying and pasting!)

import os, sys
import vcal

calendar = vcal.parse(sys.argv[1])

print(calendar.as_vcal())
