#!/usr/bin/env python2.7

"""
I used this script to calculate the longest line in a log file that 
rsyslog was ingesting in order to forward the contents to a remote 
server. I kept having issues with outgoing messages hanging and it 
appeared that it was always when heavy activity was taking place 
on the web app generating the local log file. This helped me determine 
that the input message was larger than the max message size currently 
configured.
"""

import sys

log_file = sys.argv[1]

def get_longest_line(filename):
    """Return the longest line number and its size from the requested file"""

    max_line_length = 0
    max_line_number = 0

    with open(filename) as f:
        for line_no, line in enumerate(f):

            # Remember not to count the newline character
            line_length = len(line.strip())

            if line_length > max_line_length:
                max_line_length = line_length
                max_line_number = line_no

    return {'number':max_line_number, 'length': max_line_length}

longest_line = get_longest_line(log_file)

print "Longest line is %s with a length of %s" % \
    (longest_line['number'], longest_line['length'])
