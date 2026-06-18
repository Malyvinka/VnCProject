from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Character
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import CharacterSerializer

# Create your views here.
def character_list(request):
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 6)

    try:
        per_page = int(per_page)
    except (TypeError, ValueError):
        per_page = 6

    if per_page < 1:
        per_page = 6

    MAX_PER_PAGE = 30
    per_page = min(per_page, MAX_PER_PAGE)

    characters = Character.objects.all().order_by('id')
    paginator = Paginator(characters, per_page)
    page_obj = paginator.get_page(page)

    return render(request, 'home/character_list.html', {
        'page_obj': page_obj,
        'current_endpoint': 'GET /api/characters/',
        'current_endpoint_url': '/api/characters/',
    })


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'home/character_detail.html', {
        'character': character,
        'current_endpoint': f'GET /api/characters/{pk}/',
        'current_endpoint_url': f'/api/characters/{pk}/',
    })


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def character_api(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def character_api_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    serializer = CharacterSerializer(character)
    return Response(serializer.data)