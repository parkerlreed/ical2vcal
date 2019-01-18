#!/usr/bin/env python

import os, sys
import vcal

calendar = vcal.parse(sys.argv[1])

print(calendar.as_vcal())
