from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status, views
from ..models import *
from .serializers import *
from .permission import *

class Url_serviceViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Url_service.objects.all()
    serializer_class = Url_serviceSerializer
class Url_staticsViewSet(generics.ListAPIView):
    permission_classes = (IsOwner,IsAuthenticated)
    serializer_class = Url_serviceSerializer
    def get_queryset(self):
        return  Url_service.objects.filter(user=self.kwargs["pk"])




















#
# @require_http_methods(['GET',])
# def home_view(request):
#     # Just render a simple page for GET
#     return render(request, 'service/home.html')
#
#
# @require_http_methods(['GET'])
# def redirector_view(request, slug):
#     # Redirect short URL to its original URL, if it's valid
#     try:
#         service = models.UrlModel.objects.get(slug=slug)
#         url = service.url
#         if not url.startswith('http://') and not url.startswith('https://'):
#             url = f'http://{url}'
#         return HttpResponseRedirect(url)
#     except Exception as e:
#         return HttpResponseRedirect('/')
#
#
# @api_view(['POST'])
# def url_shortener_api(request):
#     try:
#         # the URL entered by the User
#         users_url = request.data['url']
#
#         # Gets the shortened record and serialize it
#         domain = request.META['HTTP_HOST']
#         service = shorten_url(users_url, domain)
#         service_serializer = serializers.ServiceSerializer(service, many=False)
#         return Response(data={'success': True, 'data': service_serializer.data}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response(data={'success': False, 'message': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# def generate_random_string(string_length=6):
#     # Generates a random string
#     random_string = ''
#     alpha_numerals = string.ascii_letters + string.digits
#     for _ in range(string_length):
#         random_string = random_string + random.choice(alpha_numerals)
#     return random_string
#
#
# def shorten_url(url, domain):
#     # Gets a random string and validates it against the database
#     random_string = generate_random_string()
#     url_service, created = Url_service.objects.get_or_create(short_url=random_string)
#     if created:
#         url_service.url = url
#         service.short_url = random_string
#         service.save()
#         return service
#     else:
#         shorten_url(url, domain)
