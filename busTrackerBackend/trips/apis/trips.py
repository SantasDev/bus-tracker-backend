from django.http import JsonResponse

def get_trips(request):
    return JsonResponse([{'key':'trips listers'}], safe=False)

def create_trip(request):
    return JsonResponse({'status': 200, 'message': 'building'})

def edit_trip(request, id=0):
    return JsonResponse({'status': 200, 'message': 'building {}'.format(id)})

def view_trip(request, id=0):
    return JsonResponse({'status': 200, 'message': 'buidung {}'.format(id)})

def delete_trip(request, id=0):
    return JsonResponse({'status': 200, 'message': 'building{}'.format(id)})