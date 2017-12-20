from libs.urlloader import load_url
from urllib.error import HTTPError


try:
    raise Exception ('esto no funciona ni a tiros')
    print('funcionara?')
except Exception as error:
    print('ha fallado:', repr(error))

try:
    load_url('https://estonoexistenidecoña.com')
    #load_url('https://swapi.co/api/people/')
except HTTPError as error:
    print('Error al cargar la url:', repr(error))
except Exception as ex:
    print('Error generico:', repr(ex))
