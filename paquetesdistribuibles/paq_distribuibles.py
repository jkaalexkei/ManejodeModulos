#se pueden enviar a diistintas personas
#permite empaquetar modulos
#se puede instalar en cualquier pc
#permite usar un paquete independientemente donde nos encontremos

# pasos para crear un paquete distribuible

# crear archivo setup.py en la raiz de la carpeta origen del paquete y tendra una descripcion del paquete

# sintaxis que va dentro del archivo setup

# from setuptools import setup #-->
# #informacion descriptva del paquete
# setup(

    #name = "paquetecalculos",
    #version = "1.0"
    #description="explicacion de lo que hace el paquete"
    #author ="Alex"
    #Author_email="correo del autor"
    #url="pagina web del autor  (opcional)"
    #packages=["calculos","calculos.redondeo_potencia"]aca se especiifica la ubicacion del paquete que queremos empaquetar


# )


# posteriormente abrir el archivo setup con la consola desde el sitio donde se encuentra
#luego  escribiir en la consola para ccrear un paquete distribuible lo siguiente:
#           python setup.py sdist
#se crean dos carpetas. Se elige la que se llama dist y buscamos un archivo comprimido
#copiamos el archivo en el drectorio de nuestra eleccion

#para instalar el paquete se realiza lo siguiente:

#abrimos la consola en el directorio donde se encuentra el archivo comprimido

#luego se debe usar la siguiente instruccion en la consola
#         pip3 install nombredelpaquete

#en caso de desinstalar se hace lo siguiente:
#        pip3 uninstall nombredelpaquete
