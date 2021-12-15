from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Registro
import json

# Create your views here.

class Registroview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs ):
        return super().dispatch(request, *args, **kwargs)
#Buscar un usuario        

    def get(self,request, correo='', contrasena=''):
        if (correo!=''):
            register=list(Registro.objects.filter(correo=correo).values())
            if len(register)>0:
                registr=register[0]
                datos={'registr':registr}
            else:
                datos={'message':"Correo no existente"}

        if (contrasena!=''):
            register=list(Registro.objects.filter(correo=correo,contrasena=contrasena).values())
            
            if len(register)>0:
                registr=register[0]
                datos={'registr':registr}
            else:
                datos={'message':"Usuario y/o contraseña incorrecta"}
            return JsonResponse(datos)

        #Listado de usuarios

        else:
            register= list(Registro.objects.values())
            if len(register)>0:
                datos={'message':"Listado de usuarios",'register':register}
            else:
                datos={'message':"Register not found ..."}
            return JsonResponse(datos)

    
        


#

    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Registro.objects.create(nombre=jd['nombre'],correo=jd['correo'],contrasena=jd['contrasena'])
        datos={'message':"Usuario agregado"}
        return JsonResponse(datos)

#Actualizar usuario
    def put(self,request,correo):
        jd=json.loads(request.body)
        register=list(Registro.objects.filter(correo=correo).values())
        if len(register)>0:
            registr=Registro.objects.get(correo=correo)
            registr.nombre=jd['nombre']
            registr.correo=jd['correo']
            registr.contrasena=jd['contrasena']
            registr.save()
            datos={'message':"Usuario actualizado"}
        else:
            datos={'message':"Registro no encontrado"}
        return JsonResponse(datos)            

    def delete(self,request,correo):
        register=list(Registro.objects.filter(correo=correo).values())
        if len(register)>0:
            Registro.objects.filter(correo=correo).delete()
            datos={'message':"Usuario Eliminado"}
        else:
            datos={'message':"Registro no encontrado"}
        return JsonResponse(datos)  