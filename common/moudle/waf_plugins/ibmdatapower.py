#!/usr/bin/env python


NAME = 'IBM DataPower'


def is_waf(self):
    # Added by Mathieu Dessus <mathieu.dessus(a)verizonbusiness.com>
    detected = False
    if self.match_header(('X-Backside-Transport', '^(OK|FAIL)')):
        detected = True
    return detected
