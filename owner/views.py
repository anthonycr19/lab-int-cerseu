from django.shortcuts import render, redirect

from owner.models import Owner


# Create your views here.


def owner_list(request):
    # data_context = {
    #     'nombre': "Katty",
    #     'edad': 26,
    #     'pais': "Perú"
    # }

    # data_context = [
    #     {
    #         'nombre': "Katty Magaño",
    #         'edad': 26,
    #         'pais': "Perú",
    #         'dni': '23231212',
    #         'vigente': True,
    #         'pokemons': [
    #             {
    #                 'nombre_p': 'Charizard',
    #                 'ataques': ['Ataque 1 - Ch', 'Ataque 2 - Ch', 'Ataque 3 - Ch']
    #             }
    #         ]
    #     },
    #     {
    #         'nombre': "Benito Castro",
    #         'edad': 22,
    #         'pais': "España",
    #         'dni': '88881212',
    #         'vigente': False
    #     },
    #     {
    #         'nombre': "Marianela",
    #         'edad': 23,
    #         'pais': "Colombia",
    #         'dni': '23239999',
    #         'vigente': True
    #     },
    #     {
    #         'nombre': "Carlos",
    #         'edad': 17,
    #         'pais': "Perú",
    #         'dni': '77771212',
    #         'vigente': True
    #     }
    # ]

    """Crear un objeto de una tabla en la BD"""
    #p = Owner(nombre="Luis Mejia", edad=22, dni="77777777", pais="España", vigente=True)
    #p.save()

    """Obtener todos los elementos de una tabla de la BD"""

    #data_context = Owner.objects.all()

    """Filtración de datos: .filter()"""

    #data_context = Owner.objects.filter(nombre="Luis Mejia")

    """Filtración de datos con AND de SQL: .filter( , )"""

    #data_context = Owner.objects.filter(nombre="Carlos", edad=21)

    """Filtración de datos más precisos con: __contains"""

    #data_context = Owner.objects.filter(nombre__contains="Carlos")

    """Filtración de datos más precisos con: __endswitch"""

    #data_context = Owner.objects.filter(nombre__endswith="sar")

    """Obtener un solo objeto de la tabla de BD"""

    #data_context = Owner.objects.get(dni="88888888")

    """Ordenar por cualquier atributo o campos de la tabla"""

    #data_context = Owner.objects.order_by("nombre")
    #data_context = Owner.objects.order_by("-edad")

    """Ordenar concatenando diferentes métodos ORM's"""
    #data_context = Owner.objects.filter(nombre="Luis Mejia").order_by("edad")

    """Acortar datos: Obtener un rango de registros de una tabla de la BD"""
    #data_context = Owner.objects.all()[0:3]
    #data_context = Owner.objects.all()

    """Eliminar un dato específicamente"""
    try:
        data_context = Owner.objects.get(id=4)
        data_context.delete()
    except Owner.DoesNotExist:
        data_context = []

    """Actualización de datos en la BD a un cierto grupo de datos o un solo registro"""

    Owner.objects.filter(pais__startswith="Es").update(edad=34)

    return render(request, 'owner/owner_list.html', context={'data': data_context})


def owner_detail(request, id_owner):
    print("ID Owner: {}".format(id_owner))

    return render(request, 'owner/owner_list.html', context={'data': id_owner})

