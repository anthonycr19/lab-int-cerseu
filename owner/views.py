from django.shortcuts import render, redirect

# Create your views here.


def owner_list(request):
    # data_context = {
    #     'nombre': "Katty",
    #     'edad': 26,
    #     'pais': "Perú"
    # }

    data_context = [
        {
            'nombre': "Katty",
            'edad': 26,
            'pais': "Perú",
            'dni': '23231212',
            'vigente': True,
            'pokemons': [
                {
                    'nombre_p': 'Charizard',
                    'ataques': ['Ataque 1 - Ch', 'Ataque 2 - Ch', 'Ataque 3 - Ch']
                }
            ]
        },
        {
            'nombre': "Benito",
            'edad': 22,
            'pais': "España",
            'dni': '88881212',
            'vigente': False
        },
        {
            'nombre': "Marianela",
            'edad': 23,
            'pais': "Colombia",
            'dni': '23239999',
            'vigente': True
        },
        {
            'nombre': "Carlos",
            'edad': 17,
            'pais': "Perú",
            'dni': '77771212',
            'vigente': True
        }
    ]

    return render(request, 'owner/owner_list.html', context={'data': data_context})


def owner_detail(request, id_owner):
    print("ID Owner: {}".format(id_owner))

    return render(request, 'owner/owner_list.html', context={'data': id_owner})

