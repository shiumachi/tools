#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from questionnaire_aggr import *

class AttendeesTest(unittest.TestCase):

    def setUp(self):
        pass

    def testIteration(self):
        data = [
            ["testuser01","comment01","2011/07/12 07:24","aaa","00001"],
            ["testuser02","comment02","2011/07/12 07:25","aaa,bbb","00002"],
            ["testuser03","comment03","2011/07/12 07:26","aaa,bbb,ccc","00003"]
            ]
        testdata01 = Attendee(["testuser01","comment01","2011/07/12 07:24","aaa","00001"])
        testdata02 = Attendee(["testuser02","comment02","2011/07/12 07:25","aaa,bbb","00002"])
        testdata03 = Attendee(["testuser03","comment03","2011/07/12 07:26","aaa,bbb,ccc","00003"])
        attendees = Attendees()
        for row in data:
            attendees.add(row)

        self.assertEqual(testdata01, attendees.attendee_list[0])
        self.assertEqual(testdata02, attendees.attendee_list[1])
        self.assertEqual(testdata03, attendees.attendee_list[2])
        
if __name__=='__main__':
    unittest.main()
    
