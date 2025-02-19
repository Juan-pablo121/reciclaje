import discord
import os
from discord.ext import commands
import random
from contaminacion import contaminacion

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

clas='♻️ Objetos Reciclables Plásticos: Botellas de agua y refrescos (PET) Envases de champú y jabón líquido Bolsas plásticas reutilizables Envases de yogur y crema Tapas de plástico Tuppers plásticos (limpios) Vidrio: Botellas de vidrio (vino, cerveza, refrescos) Frascos de mermelada y salsas Envases de perfume y cosméticos (sin residuos) Papel y Cartón: Periódicos y revistas Cajas de cartón limpias Sobres y hojas de papel usadas Cuadernos sin espiral Rollos de papel higiénico y toallas de cocina Metales: Latas de aluminio (refrescos, cerveza) Latas de conservas (atún, verduras enlatadas) Tapas metálicas de frascos Utensilios de cocina metálicos en buen estado Orgánicos (para compostaje): Cáscaras de frutas y verduras Restos de café y bolsitas de té Cáscaras de huevo Hojas secas y ramas pequeñas Electrónicos (en centros de reciclaje): Pilas recargables Teléfonos celulares Computadoras y accesorios Cables y cargadores Electrodomésticos pequeños 🚫 Objetos No Reciclables Plásticos: Bolsas plásticas de un solo uso Envases de comida contaminados con grasa (ej. bandejas de comida rápida) Envoltorios metalizados (papitas, golosinas) Juguetes plásticos mezclados con otros materiales Vidrio: Vidrios rotos Espejos Bombillas y focos Vidrio templado (ventanas, parabrisas) Papel y Cartón: Servilletas y papel higiénico usados Papel encerado o plastificado Cartón de pizza con grasa Fotografías Metales: Objetos oxidados Aerosoles con residuos peligrosos Cacerolas y sartenes antiadherentes dañadas Orgánicos: Restos de carne y huesos grandes Lácteos y derivados (queso, leche) Aceites de cocina usados (se deben reciclar en puntos específicos) Electrónicos: Baterías de un solo uso (difícil reciclaje) Televisores antiguos sin puntos de recolección Bombillas fluorescentes (contienen mercurio)'
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.event
async def manualidad(ctx):
    list=os.listdir("images_reciclaje")
    img = random.choice(list)
    with open(f'images/{img}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.event
async def contaminacion(ctx):
    contaminacion()
    
@bot.command()
async def clasificacion(ctx):
    await ctx.send(clas)

bot.run("Ingresa aqui tu token")    
