from django.http import JsonResponse
from .models import Reporte  # Importa el modelo Reporte
import requests
from datetime import datetime

FACTURAS_SERVICE_URL = "http://127.0.0.1:8000/Ofipensiones/api/facturas_por_fecha/"

def generar_reporte(request):
    # Validar método HTTP
    if request.method != 'GET':
        return JsonResponse({'error': 'Método no permitido. Use GET.'}, status=405)

    # Obtener parámetros de la solicitud
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if not fecha_inicio or not fecha_fin:
        return JsonResponse({'error': 'Debe proporcionar fecha_inicio y fecha_fin en los parámetros de la solicitud.'}, status=400)

    try:
        # Consumir el microservicio de facturas
        response = requests.get(FACTURAS_SERVICE_URL, params={
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin
        })

        # Manejar errores en la respuesta del microservicio
        if response.status_code != 200:
            return JsonResponse({'error': f'Error al obtener facturas desde el microservicio: {response.text}'}, status=response.status_code)

        # Extraer los datos de facturas
        facturas = response.json().get('facturas', [])

        # Generar el reporte
        reporte = {
            'reporte_generado': True,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'total_facturas': len(facturas),
            'facturas': facturas,
            'fecha_generacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Guardar el reporte en la base de datos
        Reporte.objects.create(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            total_facturas=len(facturas),
            detalle_facturas=facturas
        )

        # Retornar el reporte como JSON
        return JsonResponse(reporte, status=200)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el microservicio de facturación: {str(e)}'}, status=500)

    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status=500)
