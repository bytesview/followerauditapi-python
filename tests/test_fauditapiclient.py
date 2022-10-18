import os
from followeraudit.FauditAPIclient import FauditAPIclient
import unittest

class test_bytesviwapi(unittest.TestCase):

    def setUp(self):
        # your private API key.
        key = os.environ.get("PYTEST_API_TOKEN")
        self.api = FauditAPIclient(key)

    def test_newaudit_api(self):
        response = self.api.newaudit(username='iampiyushkhatri')
        self.assertEqual(response['status'], 'success')

    def test_bulkaudit_api(self):
        response = self.api.bulkaudit(username=['arjun077','iampiyushkhatri','RobertDowneyJr'])
        self.assertEqual(response['status'], 'success')

    
    def test_getaudit_api(self):
        response = self.api.auditstatus(audit_id='2d6c356eb3addb9159c0231d00b0c4cd')
        self.assertEqual(response['status'], 'success')
