import random
conta=''
def contaminacion():
    global conta
    elementos=['Combustibles fósiles (petróleo, gas natural y carbón)','Plásticos y materiales sintéticos',
               'Metales pesados y minería (oro, cobre, aluminio, etc.)',
               'Agricultura intensiva y ganadería','Agua potable y su mal uso',
               'Deforestación y uso insostenible de la madera','Residuos electrónicos (e-waste)']
    for i in range(1):
        conta +=random.choice(elementos)
        print(conta)
