from django.http import JsonResponse

def users_handler(request):
    return JsonResponse([{'key':'pepito perez soy yo, y este es mi combo'}], safe=False)

def user_handler(request):
    return JsonResponse({'key':'pepito perez soy yo'})