from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name ='index' ),
    path(r'thresh/',views.thresholding, name= 'thresholding'),
    path(r'contrast/',views.contraststretching, name= 'contrastStretching'),
    path(r'histogram/',views.histogramequalizer, name= 'HistogramEqualizer'),
    path(r'logarithm/',views.logarithmoperator, name= 'logarithmOperator'),
    path(r'raiz/',views.raizoperator, name= 'raizOperator'),
    path(r'exponential/',views.exponentialoperator, name= 'exponentialOperator'),
    path(r'raize/',views.raizepoweroperator, name= 'Raize Power Operator'),
    path(r'cascade/',views.cascade, name= 'Cascade'),
 	path(r'addition/',views.additionop,name='Addition'),
 	path(r'subtraccion/',views.subtraccionop,name='Subtraccion')
]
