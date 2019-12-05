from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from graphdemo.schema import schema
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^graphdemo$', GraphQLView.as_view(graphiql=True,schema=schema))
]
