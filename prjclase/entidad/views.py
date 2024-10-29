from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from .forms import ClienteForm


# def index(request):
#     return HttpResponse('Hola mundo desde Django!!')

def index(request, template_name='entidad/index.html'):
    dato = {"nombre": "Juan",
            "edad": 41,
            "direccion": {"calle": "San Martín 600", "localidad": "Córdoba"},
            "cant_hijos": 3,
            "hijos": ["Ana", "Emilia", "Matias"]}
    return render(request, template_name, dato)


def acerca_de(request):
    return HttpResponse('Curso Digitalers - EducaciónIT - Telecom')


# def clientes(request):
#     conn = sqlite3.connect("contabilidad.sqlite")
#     cliente = conn.cursor()
#     cliente.execute("select nombre, edad from personas")
#     html = """
#             <html>
#                 <title>Listado de clientes</title>
#                 <table style="border: 1px solid">
#                     <thead>
#                     <tr>
#                     <th>Cliente</th>
#                     <th>Edad</th>
#                     </tr>
#                     </thead>
#             """
#     for nombre, edad in cliente.fetchall():
#         html += "<tr><td>" + nombre + "</td><td>" + str(edad) + "</td></tr>"
#     html += "</table></html>"
#     conn.close()
#     return HttpResponse(html)

def clientes(request, template_name='entidad/clientes.html'):
    conn = sqlite3.connect('contabilidad.sqlite')
    cliente = conn.cursor()
    cliente.execute("Select nombre, edad from personas")
    cliente_list = cliente.fetchall()
    conn.close()
    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)


def cliente(request, nombre_cliente, template_name='entidad/cliente.html'):
    conn = sqlite3.connect('contabilidad.sqlite')
    cursor = conn.cursor()
    cursor.execute("Select nombre, edad from personas where nombre=?", [nombre_cliente])
    cliente_s = cursor.fetchone()  # (Mateo, 19)
    conn.close()
    dato = {"cliente": cliente_s}
    return render(request, template_name, dato)


# Trabajamos con Forms

def nuevo_cliente(request, template_name='entidad/cliente_form.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("contabilidad.sqlite")
            cursor = conn.cursor()
            cursor.execute("insert into personas values (?, ?)",
                           (form.cleaned_data["nombre"], form.cleaned_data["edad"])
                           )
            conn.commit()
            conn.close()
            # return HttpResponse("El cliente se ha cargado correctamente")
            return redirect("clientes")
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)
