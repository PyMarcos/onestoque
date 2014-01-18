from django.conf.urls import patterns, include, url
from django.conf import settings
from app.views import ProdutoView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','app.views.index'),
    url(r'^contato/$', 'app.views.contato'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}),
    url(r'^admin/', include(admin.site.urls)),

    #cadastros
    url(r'^contato/$', 'app.views.contato'),
    url(r'^novo-produto/$', 'app.views.n_produto'),
    url(r'^novo-dep/$', 'app.views.n_departamento'),
    url(r'^compra/$', 'app.views.n_compra'),
    url(r'^venda/$', 'app.views.n_venda'),

    #consultas
    url(r'^consultas/compras/$', 'app.views.cons_compras'),
    url(r'^consultas/departamentos/$', 'app.views.dep'),
    url(r'^consultas/departamentos/(?P<dept>.+)/$', 'app.views.depts'),
    url(r'^consultas/produtos/(?P<order>.*)$', ProdutoView.as_view()),

    #outros
    url(r'^email/$', 'app.views.email'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )