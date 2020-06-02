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
from .Threasholding.th import Threshold as TH
from .OperadorExponencial.OpExp import pointOperator as POO
from .Sustraccion.subtraccion import subtraccion as SO
from .Addition.Addition import AdditionOperator as AO
# Create your views here.

def index(request):
    pageTitle = 'Imagen Original'
    pageStatus = 0
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile)
        cv2.imwrite("pointOp/static/media/"+name,img)

        displayFile = url
        displayFileMod = url #"/media/gray_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })


def thresholding(request):
    pageTitle = 'thresholding'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """threasholding"""
        thres = TH(img)
        l=0
        r=255
        if request.POST['limit_a']:
            l=int(request.POST['limit_a'])
        if request.POST['limit_b']:
            r=int(request.POST['limit_b'])

        newimg = thres.thresholding(l,r)


        cv2.imwrite("pointOp/static/media/tresh_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/tresh_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def contraststretching(request):
    pageTitle = 'Contrast Stretching'
    pageStatus = 2
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
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

        cv2.imwrite("pointOp/static/media/contrast_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/contrast_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def histogramequalizer(request):
    pageTitle = 'Histogram Equalizer'
    pageStatus = 3
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)

        cv2.imwrite("pointOp/static/media/"+name,img)

        h= HE(img)

        newimg = h.Equalization()

        cv2.imwrite("pointOp/static/media/hist_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/hist_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
        
def logarithmoperator(request):
    pageTitle = 'Logarithm Operator'
    pageStatus = 2
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
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

        cv2.imwrite("pointOp/static/media/log_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/log_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def raizoperator(request):
    pageTitle = 'Raiz Operator'
    pageStatus = 2
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
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
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def exponentialoperator(request):
    pageTitle = 'Exponential Operator'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)
        """exponential operator"""
        expo = POO(img)
        b=1.005
        c=5
        if request.POST['limit_a']:
            b=request.POST['limit_a']
        if request.POST['limit_b']:
            c=request.POST['limit_b']

        newimg = expo.expoOperator(b,c)
        cv2.imwrite("pointOp/static/media/expo_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/expo_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def raizepoweroperator(request):
    pageTitle = 'Raize Power Operator'
    pageStatus = 1
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """raize power"""
        rai = POO(img)
        r=1.005
        c=0.05
        if request.POST['limit_a']:
            r = request.POST['limit_a']
        if request.POST['limit_b']:
            c = request.POST['limit_b']
        
        newimg = rai.raiseOperator(r,c)
        
        cv2.imwrite("pointOp/static/media/raize_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/raize_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def additionop(request):
    pageTitle = 'Addition Operator'
    pageStatus = 5
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """subtraccion Operator"""
        sub = AO(img)
        if request.POST['limit_a']:
            r = request.POST['limit_a']
            sub = AO(img)
            newimg=sub.additionC(int(r))
        
        if 'imageb' in request.FILES:
            uploadimg = request.FILES['imageb']
            fs1 = FileSystemStorage()
            name1 = fs1.save(uploadimg.name, uploadimg)
            url1 = fs1.url(name1)
            displayFile1 = os.path.join("/home/carlos/Documentos/ImageProcessing"+url1)
            img1 = cv2.imread(displayFile1,0)
            img = cv2.resize(img,dsize=(img1.shape[0],img1.shape[1]))
            sub = AO(img)
            newimg=sub.additionImg(img1)
            
        cv2.imwrite("pointOp/static/media/add_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/add_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
        
def subtraccionop(request):
    pageTitle = 'Subtraccion Operator'
    pageStatus = 5
    if request.method == 'POST':
        uploaded_file = request.FILES['imagefile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
        img = cv2.imread(displayFile,0)
        cv2.imwrite("pointOp/static/media/"+name,img)

        """subtraccion Operator"""
        sub = SO(img)
        if request.POST['limit_a']:
            r = request.POST['limit_a']
            sub = SO(img)
            newimg=sub.subtraccionC(int(r))
        
        if 'imageb' in request.FILES:
            uploadimg = request.FILES['imageb']
            fs1 = FileSystemStorage()
            name1 = fs1.save(uploadimg.name, uploadimg)
            url1 = fs1.url(name1)
            displayFile1 = os.path.join("/home/carlos/Documentos/ImageProcessing"+url1)
            img1 = cv2.imread(displayFile1,0)

            sub = SO(img)
            newimg=sub.subtraccionImg(img1);
        
        cv2.imwrite("pointOp/static/media/sub_"+name,newimg)

        displayFile = url
        displayFileMod = "/media/sub_"+name
        return render(request, 'pointOp/home.html', {
            'pageStatus':pageStatus,
            'displayFileMod':displayFileMod,
            'pageTitle':pageTitle,
            'displayFile':displayFile
            })
    return render(request, 'pointOp/home.html', {
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })

def cascade(request):
    pageTitle = 'cascade Operation'
    pageStatus = 4
    if request.method == 'POST':
        if request.FILES['imagefile']:
            uploaded_file = request.FILES['imagefile']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            url = fs.url(name)
            displayFile = os.path.join("/home/carlos/Documentos/ImageProcessing"+url)
            img = cv2.imread(displayFile,0)
            cv2.imwrite("pointOp/static/media/"+name, img)

            newimg = None
            if request.POST['thresh']:
                th=TH(img)
                newimg=th.thresholding()


            imgcas=img
            cv2.imwrite("pointOp/static/media/cascade_"+name,newimg)
            displayFile = url
            displayFileMod = "/media/_cascade_"+name
            return render(request, 'pointOp/home.html',{
                'pageStatus':pageStatus,
                'displayFileMod':displayFileMod,
                'pageTitle':pageTitle,
                'displayFile':displayFile,
                })

    return render(request,'pointOp/home.html',{
        'pageStatus':pageStatus,
        'pageTitle':pageTitle,
        })
