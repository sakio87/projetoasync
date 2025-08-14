import asyncio
from django.http import JsonResponse

async def async_view(request):
    resultado = []
    for i in range(1, 6):
        await asyncio.sleep(1)
        resultado.append(f"Contando: {i}")
    return JsonResponse({'tipo': 'async', 'contador': resultado})

def sync_view(request):
    import time
    resultado = []
    for i in range(1, 6):
        time.sleep(1)
        resultado.append(f"Contando: {i}")
    return JsonResponse({'tipo': 'sync', 'contador': resultado})
