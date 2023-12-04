from api.utils import get_user_id_by_token, get_user_role_by_token
from django.http import HttpResponseForbidden

# VERIFICA SE O TOKEN DO USUÁRIO É VALIDO E ANEXA O ID NO CORPO DA REQUISIÇÃO.

def auth_middleware(get_response):
  def middleware(request):

    if (request.path.startswith('/media/') or
        request.path == '/account' and request.method == 'POST' or
        request.path == '/account/login' and request.method == 'POST'):
      return get_response(request)
    

    token = request.headers.get('Authorization').split(' ')[1]
    user_id = get_user_id_by_token(token)
    user_role = get_user_role_by_token(token)

    if (not user_id):
      return HttpResponseForbidden({'Token inválido'})

    request.user_id = user_id
    request.user_role = user_role

    return get_response(request)  
  return middleware
