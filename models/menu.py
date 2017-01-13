# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = 'Cálculo Aplicado'
response.subtitle = 'ESCOM IPN'

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Inicio'), False, URL('default', 'index'), []),
    
    ('Unidad 1', False, '#', [
            (T('Razones de cambio'), False,
             URL('unidad1', 'razonescambio'), [
                        (T('Aplicaciones'), False,
             URL('unidad1', 'aplicaciones'), []),
                    ]),
            (T('Diferencial de una función'), False,
             URL('unidad1', 'diferencialfuncion')),
            (T('Máximos y mínimos'), False, URL('unidad1', 'maximosminimos'), []),
        ]),
    
    ('Unidad 2', False, '#', [
            (T('Área entre curvas'), False, URL('unidad2', 'areacurvas')),
            (T('Volúmen: Usando rebanadas'), False, URL('unidad2', 'volumenrebanadas')),
            (T('Volúmen: Sólido de revolución'), False, URL('unidad2', 'volumensolido')),
            (T('Longitud de arco'), False, URL('unidad2', 'longitudarco')),
            ]),
    
    ('Unidad 3', False, '#', [
        (T('Regla de L´Hopital'), False, URL('unidad3', 'reglahopital')),
            (T('Formas Indeterminadas'), False, URL('unidad3', 'formasindeterminadas')),
            (T('Integrales impropias'), False, URL('unidad3', 'integralesimpropias')),
        ]),
    
    ('Unidad 4', False, '#', [
        (T('Sucesiones'), False, URL('unidad4', 'sucesiones')),
            (T('Series infinitas'), False, URL('unidad4', 'seriesinfinitas')),
            (T('Series positivas'), False, URL('unidad4', 'seriespositivas')),
            (T('Series alternantes'), False, URL('unidad4', 'seriesalternantes')),
            (T('Series de potencias'), False, URL('unidad4', 'seriespotencias')),
            (T('Series de Taylor y McLaurin'), False, URL('unidad4', 'seriestaylor')),
        ]),
    
    ('Exámenes', False, URL('default', 'examenes'), []),
    
    ('Recursos Digitales', False, URL('default', 'recursosdigitales'), []),
    
    ('Publicar Recursos', False, URL('default', 'publicarrecursos'), []),
    
    ('Publicar Exámen', False, URL('default', 'publicarexamen'), []),
    
    ('Ver Exámenes', False, URL('default', 'verexamenes'), []),
]

DEVELOPMENT_MENU = False


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            LI(_class="divider"),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
       
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
