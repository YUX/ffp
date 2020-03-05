import re
 
pattern = re.compile(r'http(s:\/\/|:\/\/)')
s = """
http://apple.com
https://apple.com
httpksncks
httpsdjkse
cvdfvhttpsvd
fvdfhttpsvd
"""
 
print(re.sub(pattern,'https://localhost/http'+r'\1', s))