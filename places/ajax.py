'''Ajax endpoints for the places app'''
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Place

@csrf_exempt
def edit_place(request):
    '''edit a place's name, rating, tags, or notes'''
    if request.method == 'POST':
        place_id = request.POST.get('place_id')
        field_name = request.POST.get('field_name')
        field_value = request.POST.get('field_value')

        place = Place.objects.get(pk=place_id)
        setattr(place, field_name, field_value)
        place.save()

        return JsonResponse(
            {
                'success': True
            }
        )
    else:
        return JsonResponse(
            {
                'error': 'Invalid request method.'
            },
            status=404
        )
