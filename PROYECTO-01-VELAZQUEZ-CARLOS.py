from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
import sys

#Aqui se encuentra la sección de login, la cual pide username y contraseña
print('\n')
print("*" *30)
print("BASE DE DATOS LIFESTORE")
print("*" *30)
print('\n')
username = input("Ingrese su usuario (pista = 'admin')\n")
pwd = input("Ingrese la contraseña (pista = 'admin')\n")
#En este paso verificamos si la contraseña y/o el usuario son correctos y si son
#incorrectos se cierra el programa
if pwd != 'admin' or username != 'admin':
    sys.exit("Contraseña incorrecta, vuelva a ejecutar el programa")
###### 50 productos mas vendidos ##########
#Primero, separaremos el ID del producto que se vendió, esto con el fin de poder tener las veces
#que se vendió cada producto en la lista, lista_de_ventas.
lista_de_ventas = []
for venta in lifestore_sales:
    id_del_producto = venta[1]
    lista_de_ventas.append(id_del_producto)

#Despues contaremos las veces que aparece cada ID del producto y lo pasaremos a una nueva lista
#con el formato [NUMERO DE VENTAS, ID], tambien agregamos un condicional if para que no aparezcan repetidos
#por ultimo, hacemos un sort con reverse= True para tenerlos ordenados de mayor a menor venta
conteo_de_ventas = []
for id_producto in lista_de_ventas:
    if [lista_de_ventas.count(id_producto),id_producto] not in conteo_de_ventas:
        conteo_de_ventas.append([lista_de_ventas.count(id_producto),id_producto])
conteo_de_ventas.sort(reverse=True)

#Una vez que ya tenemos la lista con el número de ventas del producto y el ID del producto
#queremos imprimir el nombre de los 50 primeros productos, ya que estan ordenados de mayor a menor venta
#para esto agregamos el condicional if, para que una vez que imprima los 50 ya se detenga
count = 0
print("*"*30)
print("LOS 50 PRODUCTOS MAS VENDIDOS(DE MAYOR A MENOR) SON:")
print("*" *30)
for venta_e_id in conteo_de_ventas:
    if count != 50:
        # Aqui es [venta_e_id[1]-1][1] ya que el indice del producto en la tabla es ID - 1, ya que no inician en 0 los productos
        nombre_del_producto = lifestore_products[venta_e_id[1]-1][1]
        print(f"{nombre_del_producto}, se vendieron {venta_e_id[0]} productos")
        count += 1
    else:
        break


####### 100 productos mas buscados#####
#Utilizaremos un método parecido al anterior, ya que aqui pasaremos los id de los productos
#de las búsquedas realizadas para poder contarlos
lista_de_busquedas = []
for busqueda in lifestore_searches:
    id_producto_busqueda = busqueda[1]
    lista_de_busquedas.append(id_producto_busqueda)


#Ahora contaremos cuantas busquedas se realizaron para cada producto y realizaremos un
#sort con reverse=True, esto con el fin de tener ordenado de mayor a menor las busquedas que se realizaron
#en la lista conteo_de_busqueda con el formato [NUM DE BUSQUEDA, ID PRODUCTO]
conteo_de_busqueda = []
for id_producto_buscado in lista_de_busquedas:
    if [lista_de_busquedas.count(id_producto_buscado),id_producto_buscado] not in conteo_de_busqueda:
         conteo_de_busqueda.append([lista_de_busquedas.count(id_producto_buscado),id_producto_buscado])
conteo_de_busqueda.sort(reverse=True)

##Despues imprimiremos los primeros 100 de la lista para poder tener los 100 mas buscados
count = 0
print("\n\n\n")
print("*"*30)
print("LOS 100 PRODUCTOS MAS BUSCADOS (DE MAYOR A MENOR) SON:")
print("*" *30)
for num_busqueda_e_id in conteo_de_busqueda:
    nombre_producto = lifestore_products[num_busqueda_e_id[1]-1][1]
    if count != 100:
        print(f"{nombre_producto}, tuvo {num_busqueda_e_id[0]} busquedas")
        count += 1
    else:
        break


########## Por categoria, un listado con los 50 productos con menores ventas
#Como ya tenemos una lista con los productos ordenados de mayor a menor dependiendo de las ventas en conteo_de_ventas
#realizaremos un sort para ahora tenerlos ordenados de menor a mayor, despues un slicing y asi obtener los 50 menos vendidos
#Despues clasificaremos los 50 menos vendidos en las distintas categorias, cabe mencionar que aqui aparecen todos, ya que
#no se vendieron mas de 50 tipos de productos diferentes, pero lo importante es que si vendieramos 50000 productos
#diferentes, esto obtendria los 50 menos vendidos y los clasificaria
conteo_de_ventas.sort()

top50_menos_vendidos = conteo_de_ventas[:49]
print('\n')
print("*" *30)
print("50 PRODUCTOS CON MENORES VENTAS")
print("*" *30)
print("CATEGORIA PROCESADORES")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'procesadores':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA TARJETAS DE VIDEO")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'tarjetas de video':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA TARJETAS MADRE")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'tarjetas madre':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA DISCOS DUROS")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'discos duros':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA MEMORIAS USB")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'memorias usb':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA PANTALLAS")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'pantallas':
        print(f"El producto {lifestore_products[venta[1-1]][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA BOCINAS")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'bocinas':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")

print("*" * 30)
print("CATEGORIA AUDIFONOS")
for venta in top50_menos_vendidos:
    if lifestore_products[venta[1]-1][3] == 'audifonos':
        print(f"El producto {lifestore_products[venta[1]-1][1]} es de los 50 menos vendidos, solo se vendieron {venta[0]} productos")



### Despues, para obtener los productos menos buscados, debido a que ya tenemos la lista de los productos buscados con las veces que
#lo buscaron, realizamos un sort en esa lista, y asi ahora estaran acomodadas de menor a mayor y tomamos los primeros 100
#Aqui se uso un metodo diferente al anterior, ya que se utiliza un for anidado (Teniendo una lista de las categorias) esto es mejor
#ya que si se añaden nuevas categorias este si las contemplará

conteo_de_busqueda.sort()

count = 0
print("\n\n\n")
print("*"*30)
print("LOS 100 PRODUCTOS MENOS BUSCADOS SON:")
print("*"*30)
#primero obtendremos las diferentes categorias
lista_de_categorias = []
for producto in lifestore_products:
    if producto[3] not in lista_de_categorias:
        lista_de_categorias.append(producto[3])

#despues imprimiremos los menos buscados para cada categoria
for categoria in lista_de_categorias:
    print("*" * 30)
    print(f"CATEGORIA {categoria.upper()}")
    for num_busquedas_e_id in conteo_de_busqueda:
        nombre_producto = lifestore_products[num_busquedas_e_id[1]-1][1]
        if count != 100 and categoria == lifestore_products[num_busquedas_e_id[1]-1][3] :
            print(f"El producto {nombre_producto} fue de los menos buscados solo se busco {num_busquedas_e_id[0]} veces")
            count += 1
        else:
            continue

###Después, conseguiremos los productos que no fueron vendidos, nosotros sabemos que ya tenemos la lista de los que se vendieron
## y cuantos se vendieron en conteo_de_ventas con el formato [Num de ventas, ID], y en la lista lifestore_products sabemos que ahi estan
##las id de todos los productos, entonces las compararemos para ver cuales no se vendieron
print("\n\n\n")
print("*"*30)
print("LOS PRODUCTOS NO VENDIDOS SON:")
print("*" *30)
for producto in lifestore_products:
    producto_en_venta = False
    for ventas_e_id in conteo_de_ventas:
        if producto[0] == ventas_e_id[1]:
            producto_en_venta = True
            break
    if producto_en_venta == False:
        print(f"{producto[0]}. El producto {producto[1]} no fue vendido")

##Ahora pondremos cuales fueron los productos que no se buscaron

print("\n\n\n")
print("*"*30)
print("LOS PRODUCTOS NO BUSCADOS SON:")
print("*" *30)

for producto in lifestore_products:
    producto_buscado = False
    for busqueda in conteo_de_busqueda:
        if producto[0] == busqueda[1]:
            producto_buscado = True
            break
    if producto_buscado == False:
        print(f"{producto[0]}. El producto {producto[1]} no fue buscado")

############# Mostrar  dos  listados  de  20  productos  cada  una,
###un  listado  para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.
## agregaremos a una lista todos los productos con sus reviews con el formato [ID, REVIEW] en reviews_total

reviews_total = []

for venta in lifestore_sales:
    ## Si regresaron el producto no se contemplara la venta
    if venta[4] == 1:
        continue
    else:
        reviews_total.append([venta[1],venta[2]])

#Despues sacaremos el promedio de sus reviews para cada uno de los productos y lo agregaremos a lista_reviews_final_totales
#COn el formato, [NOMBRE DE PRODUCTO] Y [PROMEDIO DE REVIEWS] y haremos un sort con funcion lambda para tenerlos ordenados de menor a
#mayor promedio de reviews
lista_reviews_final_totales = []

for i in range(1, 100):
    suma_de_reviews = 0
    total_de_reviews = 0
    for venta in reviews_total:
        if venta[0] == i:
            suma_de_reviews += venta[1]
            total_de_reviews += 1
        else:
            continue
    if total_de_reviews != 0:
        promedio_de_reviews = suma_de_reviews / total_de_reviews
        #float(promedio_de_reviews)
        #print(f"El promedio de reviews del producto con ID {i} {lifestore_products[i-1][1]} es {promedio_de_reviews} ")
        lista_reviews_final_totales.append([lifestore_products[i-1][1],promedio_de_reviews])
lista_reviews_final_totales.sort(key=lambda x : x[1])

##Ahora ya que tenemos a lista completa de el producto con su promedio de reviews
## podemos usar el slicing de las listas para tomar las primeras 20 (las de promedio mas bajo)
# y las ultimas 20 (las de promedio mas alto)

print("\n")
print("*" * 30)
print("LOS 20 PRODUCTOS CON MEJORES REVIEWS: [Nombre producto,Promedio de Reviews]")
print("*" *30)
lista_top_reviews = lista_reviews_final_totales[-20:]
lista_top_reviews.reverse()
for review in lista_top_reviews:
    print(review)

##Para los 20 productos con peores review tomamos los primeros 20 productos de lista_reviews_final_totales

print("\n")
print("*" * 30)
print("LOS 20 PRODUCTOS CON PEORES REVIEWS: [Nombre producto,Promedio de Reviews]")
print("*" *30)
lista_worst_reviews = lista_reviews_final_totales[:19]
for review in lista_worst_reviews:
    print(review)



#Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año

##Para el total anual, sumaremos todo lo que se vendio
total_de_ingresos_anuales = 0
for venta in lifestore_sales:
    #CORREGIR ESO DE VENTA A ID DEL PRODUCTO
    ganancia_del_producto = lifestore_products[venta[1]-1][2]
    total_de_ingresos_anuales += ganancia_del_producto
print("\n")
print("*" * 30)
print("TOTAL DE INGRESOS ANUALES")
print("*" *30)
print(f"El total de ingresos anuales es {total_de_ingresos_anuales} pesos")

##Ventas promedio mensuales
# Primero, obtendremos el numero total de ventas obtenidas, despues dividiremos eso entre 12
#y asi obtendremos ventas promedio mensuales
numero_ventas_totales = len(lifestore_sales)
ventas_promedio_mensuales = numero_ventas_totales / 12
print("\n")
print("*" * 30)
print("PROMEDIOS DE VENTAS MENSUALES")
print("*" *30)
print(f"En promedio, se realizaron {round(ventas_promedio_mensuales)} ventas por mes")

##Meses con mas ventas al año, aqui contaremos las ventas que se hicieron para cada mes
#y lo agregaremos a lista_de_ventas_y_mes con el formato [VENTAS, MES]
meses_de_ventas = []
for saleventa in lifestore_sales:
    fecha_de_venta = saleventa[3]
    mes_de_venta = fecha_de_venta[3:5]
    meses_de_ventas.append(mes_de_venta)
lista_de_ventas_y_mes = []
for mes in meses_de_ventas:
    ventas_en_mes = meses_de_ventas.count(mes)
    if [ventas_en_mes,mes] not in lista_de_ventas_y_mes:
        lista_de_ventas_y_mes.append([ventas_en_mes,mes])
lista_de_ventas_y_mes.sort(reverse=True)

#Una vez que ya tenemos contadas las ventas de cada mes y realizamos el sort para tener primero los meses en
#los que se hicieron mas ventas, imprimiremos los 5 meses en los que se hicieron mas ventas
print("\n")
print("*" * 30)
print("MESES EN LOS QUE SE REALIZARON MAS VENTAS")
print("*" *30)
for venta_mes in lista_de_ventas_y_mes[:5]:
    print(f"En el mes {venta_mes[1]} se realizaron {venta_mes[0]} ventas")


## Total de ingresos mensuales
# Aqui usaremos un for anidado, para que itere sobre el numero de meses y sobre
#las ventas, y con esto ir sumando las ganancias de cada mes, para despues
#meter a una lista 2D el mes junto con las ganancias
print("\n")
print("*" * 30)
print("TOTAL DE INGRESOS MENSUALES")
print("*" *30)
ingresos_por_mes = []
for i in range(1,13):
    total_de_ingresos = 0
    for saleventa in lifestore_sales:
        producto_vendido = saleventa[1]
        ganancia_producto = lifestore_products[saleventa[1]-1][2]
        fecha_de_venta = saleventa[3]
        mes_de_venta = fecha_de_venta[3:5]
        if i == int(mes_de_venta):
            total_de_ingresos += ganancia_producto
    ingresos_por_mes.append([i,total_de_ingresos])

for mes_e_ingresos in ingresos_por_mes:
    print(f"En el mes {mes_e_ingresos[0]} se obtuvieron {mes_e_ingresos[1]} pesos")
