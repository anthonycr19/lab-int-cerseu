from django.db.models import F, Q
from django.shortcuts import render, redirect
from owner.models import Owner

from owner.forms import OwnerForm

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
    #p = Owner(nombre="Luis Mejia", edad=29, dni="66666666", pais="Brasil", vigente=True)
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
    data_context = Owner.objects.order_by("edad")

    """Ordenar concatenando diferentes métodos ORM's"""
    #data_context = Owner.objects.filter(nombre="Luis Mejia").order_by("edad")

    """Acortar datos: Obtener un rango de registros de una tabla de la BD"""
    #data_context = Owner.objects.all()[0:3]
    #data_context = Owner.objects.all()

    """Eliminar un dato específicamente"""
    # try:
    #     data_context = Owner.objects.get(id=8)
    #     data_context.delete()
    # except Owner.DoesNotExist:
    #     data_context = []

    """Actualización de datos en la BD a un cierto grupo de datos o un solo registro"""

    #Owner.objects.filter(pais__startswith="Es").update(edad=34, nombre="Carmen")

    """Utilizando F expressions"""

    #Owner.objects.filter(edad=34).update(edad=F('edad') - 4)
    #Owner.objects.filter(edad__lte=22).update(edad=F('edad') - 3)

    # ORM actualización de edad menor a 25 sumarles el valor de 10 y que sean de 'Perú' o 'España'
    #Owner.objects.filter(edad__lt=25).update()

    """Consultas complejas"""
    #query = Q(pais__startswith="Pe") | Q(pais__startswith="Br")
    #data_context = Owner.objects.filter(query)

    """Negar Q"""

    query = Q(pais__startswith="Pe") & ~Q(edad=30)
    data_context = Owner.objects.filter(query)
    #data_context = Owner.objects.filter(query, edad__gte=30)

    """Error de consulta"""
    #query = Q(pais__startswith="Pe") | Q(pais__startswith="Br")
    #data_context = Owner.objects.filter(edad=30, query)

    """Crear una ORM compleja que termine en país con 'ña' y que inicie también con 'Pe' y con edad igual a 29"""
    query = Q(pais__endswith="Pe") | Q()
    data_context = Owner.objects.filter(query)

    return render(request, 'owner/owner_list.html', context={'data': data_context})


def owner_detail(request, id_owner):
    print("ID Owner: {}".format(id_owner))

    return render(request, 'owner/owner_list.html', context={'data': id_owner})


def owner_search(request):

    query = request.GET.get('q', '')
    #print("Queryyyy: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )
    data_context = Owner.objects.filter(results)

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': query})


def owner_details(request):

    data_context = Owner.objects.all()
    return render(request, 'owner/owner_details.html', context={'data': data_context})


def owner_create(request):
    print("REQUEST: {}".format(request.POST))
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']

        form.save()
        return redirect('owner_details')
    else:
        form = OwnerForm()

    return render(request, 'owner/owner_create.html', {'form': form})


def owner_delete(request, id_owner):
    print("ID Owner: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_details')


def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)

    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request, 'owner/owner_edit.html', context={'form': form})
