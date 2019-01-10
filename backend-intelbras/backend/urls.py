from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='API')

# operador
from operador.views import OperadorViewSet, PerfilViewSet, PermissaoViewSet
router.register(r'operador', OperadorViewSet)
router.register(r'perfil', PerfilViewSet)
router.register(r'permissao', PermissaoViewSet)

# pessoa
from pessoa.views import PessoaViewSet
router.register(r'pessoa', PessoaViewSet)

# pessoa
from endereco.views import EnderecoViewSet
router.register(r'endereco', EnderecoViewSet)

# departamento
from departamento.views import DepartamentoViewSet
router.register(r'departamento', DepartamentoViewSet)

# usuario
from usuario.views import UsuarioViewSet
router.register(r'usuario', UsuarioViewSet)

# usuario
from visitante.views import VisitanteViewSet
router.register(r'visitante', VisitanteViewSet)

# usuario
from area.views import AreaViewSet
router.register(r'area', AreaViewSet)

# zonatempo
from zonatempo.views import ZonaTempoViewSet, TempoViewSet
router.register(r'zonatempo', ZonaTempoViewSet)
router.register(r'tempo', TempoViewSet)

# disposidito
from dispositivo.views import DispositivoViewSet
router.register(r'dispositivo', DispositivoViewSet)

# perfilacesso
from perfilacesso.views import PerfilAcessoViewSet
router.register(r'perfilacesso', PerfilAcessoViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
