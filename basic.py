import openeo
import logging

#enable logging in requests library
#Ativar o logon na biblioteca de solicitações
logging.basicConfig(level=logging.DEBUG)

#connect with VITO backend
#Conectar com o back-end VITO
session = openeo.connect("http://openeo.vgt.vito.be/openeo/0.4.0")

#retrieve the list of available collections
#Recuperar a lista de coleções disponíveis
collections = session.list_collections()
print(collections)

#create image collection
#criando a coleção de imagens
s2_fapar = session.imagecollection("BIOPAR_FAPAR_V1_GLOBAL")

#specify process graph
#specificar o gráfico de processo
download = s2_fapar \
    .filter_bbox(west=16.138916, south=48.138600, east=16.524124, north=48.320647, crs="EPSG:4326")  \
    .filter_daterange(extent=["2016-01-01T00:00:00Z", "2016-03-10T23:59:59Z"]) \
    .max_time() \
    .download("/tmp/openeo-composite.geotiff",format="GeoTiff")
print(download)