from django.shortcuts import render, loader
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from PIL import Image
from django.http import HttpResponse,HttpResponseRedirect
import pickle
import glob
import os
import cv2

#direccion a operadores punto#
from .HistogramEqual.HistogramEqual import HistogramEqual as HE
from .Lab2.contrastStretching import ConstS as CS
from .LogarithmOperator.pointOperator import pointOperator as PO
# Create your views here.

def index(request):
    indexActive = 'active'
    pageTitle = 'Greyscale'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 0
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/"+name,img)

        img_gray = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/gray_"+name,img_gray)

        displayFile = url
        displayFileMod = "/media/gray_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })


def thresholding(request):
    indexActive = 'active'
    pageTitle = 'thresholding'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 1
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/"+name,img)

        img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/tresh_"+name,img_gray)

        displayFile = url
        displayFileMod = "/media/tresh_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
def contraststretching(request):
    indexActive = 'active'
    pageTitle = 'Contrast Stretching'
    pageStatus = 2
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 2
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """contrast"""
        d=15
        if request.POST['limit']:
            d=int(request.POST['limit'])
        contrast = CS(img)
        contrast.CDlimit(d)
        newimg = contrast.Stretch()

        #img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/contrast_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/contrast_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
def histogramequalizer(request):
    indexActive = 'active'
    pageTitle = 'Histogram Equalizer'
    pageStatus = 3
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 3
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)

        cv2.imwrite("pointOp/static/media/"+name,img)

        h= HE(img)

        newimg = h.Equalization()

        #img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/hist_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/hist_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
        
def logarithmoperator(request):
    indexActive = 'active'
    pageTitle = 'Logarithm Operator'
    pageStatus = 4
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 4
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """log operator"""
        d=15
        if request.POST['limit']:
            d=int(request.POST['limit'])
        logop = PO(img)
        newimg = logop.logarithmOperator(d)

        #img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/log_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/log_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
def raizoperator(request):
    indexActive = 'active'
    pageTitle = 'Raiz Operator'
    pageStatus = 5
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 5
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """raiz operator"""
        d=50
        if request.POST['limit']:
            d=int(request.POST['limit'])

        raizop = PO(img)
        newimg = raizop.raizOperator(d)

        cv2.imwrite("pointOp/static/media/raiz_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/raiz_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
def exponentialoperator(request):
    indexActive = 'active'
    pageTitle = 'Exponential Operator'
    pageStatus = 6
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 6
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/"+name,img)

        img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/expo_"+name,img_gray)

        displayFile = url
        displayFileMod = "/media/expo_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
        
def raizepoweroperator(request):
    indexActive = 'active'
    pageTitle = 'Raize Power Operator'
    pageStatus = 7
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        pageStatus = 7
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/"+name,img)

        img_gray = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/raize_"+name,img_gray)

        displayFile = url
        displayFileMod = "/media/raize_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'indexActive':indexActive,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        'indexActive':indexActive
        })
