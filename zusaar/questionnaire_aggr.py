#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys

class Attendee(object):
    def __init__(self, row):
        self.name = row[0]
        self.comment = row[1]
        self.register_date = row[2]
        self.questionnaire = row[3]
        self.ticket_no = row[4]

    def __eq__(self, other):
        return (self.name == other.name
                and self.comment == other.comment
                and self.register_date == other.register_date
                and self.questionnaire == self.questionnaire
                and self.ticket_no == self.ticket_no
                )
    
        
class Attendees(object):
    def __init__(self):
        self.attendee_list = []

    def add(self, row):
        self.attendee_list.append(Attendee(row))

    def iter_list(self):
        for a in self.attendee_list:
            yield a
        

class Questionnaire(object):
    def __init__(self):
        self.aggr = {}

    def aggregate(self, attendees):
        for a in attendees.iter_list():
            arr = a.questionnaire.split(',')
            for b in arr:
                if len(b) == 0: continue
                self.aggr[b] = self.aggr.setdefault(b, 0) + 1

    def print_result(self):
        for k,v in self.aggr.iteritems():
            print "%s: %d" % (k,v)
        
        



if __name__=='__main__':
    reader = csv.reader(sys.stdin)
    attendees = Attendees()
    for row in reader:
        attendees.add(row)

    q = Questionnaire()
    q.aggregate(attendees)
    q.print_result()
