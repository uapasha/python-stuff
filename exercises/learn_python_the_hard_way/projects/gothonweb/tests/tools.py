from nose.tools import *
import re

def assert_response(resp, contains = None, matches = None, headers= None, status = "200")
	
	assert status in resp.status, "Expected \
				response %r not in %r" % (status, resp.status)
	
	if status == "200":
		assert resp.data, "response data is empty"