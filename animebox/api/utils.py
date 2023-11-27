import jwt

def get_user_id_by_token(token: str):
  try:
    decoded = jwt.decode(token, "secret", algorithms=["HS256"])
    return decoded['id']
  except:
    return None

def get_user_role_by_token(token: str):
  try:
    decoded = jwt.decode(token, "secret", algorithms=["HS256"])
    return decoded['role']
  except:
    return None

def create_user_token(id: int, role: str):
  token = jwt.encode({ 'id': id, 'role': role }, "secret", algorithm="HS256")
  return token