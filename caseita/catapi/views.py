import requests, json, logging
from django.shortcuts import render
from django.http import HttpResponse

from .models import CategoryUrls, Racas, BreedUrls

#logging.basicConfig(level=logging.INFO)
headers = {'x-api-key':'5d30f84c-3874-4ad7-9449-4deea044fdf1'}

def getBreedImages(breed):
    url = 'https://api.thecatapi.com/v1/images/search?limit=3&breed_id='+breed
    try:
        getImages = requests.get(headers=headers, url=url)
    except Exception as error:
        logging.error(error)
        return None
    url0, url1, url2 = '', '', ''
    try:
        url0 = getImages.json()[0]['url']
    except:
        logging.warn('nao foi possivel obter url0 para %s' % breed)
    try:
        url1 = getImages.json()[1]['url']
    except:
        logging.warn('nao foi possivel obter url1 para %s' % breed)
    try:
        url2 = getImages.json()[2]['url']
    except:
        logging.warn('nao foi possivel obter url2 para %s' % breed)
    breedurls = BreedUrls(breedid = breed, url0 = url0, url1 = url1, url2 = url2)
    breedurls.save()


def getCategoryImages(category_id, categoryname):
    url = 'https://api.thecatapi.com/v1/images/search?limit=3&category_ids='+str(category_id)
    try:
        getImages = requests.get(headers=headers, url=url)
    except Exception as error:
        logging.error(error)
        return None
    url0, url1, url2 = '', '', ''
    try:
        url0 = getImages.json()[0]['url']
    except:
        logging.warn('nao foi possivel obter url0 para %s' % categoryname)
    try:
        url1 = getImages.json()[1]['url']
    except:
        logging.warn('nao foi possivel obter url1 para %s' % categoryname)
    try:
        url2 = getImages.json()[2]['url']
    except:
        logging.warn('nao foi possivel obter url2 para %s' % categoryname)
    categoryurls = CategoryUrls(
        categoryid = category_id,
        categoryname = categoryname, url0 = url0, url1 = url1, url2 = url2)
    categoryurls.save()


def getBreeds():
    url = 'https://api.thecatapi.com/v1/breeds'
    try:
        getBreeds = requests.get(headers=headers, url=url)
    except Exception as error:
        logging.error(error)
        return None
    for breed in getBreeds.json():
        saveBreed = Racas(
            id = breed['id'],
            nome = breed['name'],
            origem = breed['origin'],
            temperamento = breed['temperament'],
            descricao = breed['description'],
        )
        saveBreed.save()
        getBreedImages(breed['id'])


def index(request):
    catinfo = list(Racas.objects.all().values())
    imageurls = list(BreedUrls.objects.all().values())
    return render(request, 'catapi/index.html', {
        'catinfo': catinfo,
        'imageurls':imageurls}
    )

def create(request):
    logging.info('obtendo imagens para gatos com chapeu')
    getCategoryImages(1, 'chapeu')

    logging.info('obtendo imagens para gatos com oculos')
    getCategoryImages(4, 'oculos')

    logging.info('obtendo informacoes de gatos da CatAPI')
    getBreeds()

    racas = {"racas":Racas.objects.count(), "categorias": CategoryUrls.objects.count()}
    logging.info(racas)
    return HttpResponse(json.dumps(racas))

def update(request, breedid):
    logging.info('atualizando imagens da raca %s' % (breedid))
    getBreedImages(breedid)
    update = list(BreedUrls.objects.filter(breedid__exact=breedid).values())
    return HttpResponse(json.dumps(update))

def todos(request):
    logging.info('solicitando todos os gatos no banco de dados local')
    catinfo = list(Racas.objects.all().values())
    return HttpResponse(json.dumps(catinfo))

def raca(request, breedid):
    logging.info('solicitando gatos da raca (%s) no banco de dados local' % (breedid))
    catinfo = list(Racas.objects.filter(id__exact=breedid).values())
    return HttpResponse(json.dumps(catinfo))

def temperamento(request, temperamento):
    logging.info('solicitando gatos com temperamento (%s) no banco de dados local' % (temperamento))
    catinfo = list(Racas.objects.filter(temperamento__contains=temperamento).values('nome'))
    return HttpResponse(json.dumps(catinfo))

def origem(request, origem):
    logging.info('solicitando gatos de origem (%s) no banco de dados local' % (origem))
    catinfo = list(Racas.objects.filter(origem__contains=origem).values('nome'))
    return HttpResponse(json.dumps(catinfo))

def categoria(request, categoryname):
    logging.info('solicitando gatos da categoria (%s) no banco de dados local' % (categoryname))
    catinfo = list(CategoryUrls.objects.filter(categoryname__exact=categoryname).values())
    return HttpResponse(json.dumps(catinfo))
