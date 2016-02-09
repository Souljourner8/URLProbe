"""
Testing module
"""

import urlp.urllink as ulink

content = ulink.load_url("http://www.example.org")

# print ulink.lcount(content[1])
print ulink.mlcount(content[1])