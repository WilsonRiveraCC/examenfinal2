#################################PRUEBA DE CAMBIO DE - POR / #############################################
#ojo te selecciona todo el primer elemento y no la primera letra eso porque es un string 
h=[['2007-04-01 20:33:00', '2.092', '0.134', '233.78', '9.8', '0.0', '1.0', '17.0', '16.866665'], ['2007/04/01 20:34:00', '2.836', '0.24', '231.57', '12.8', '0.0', '2.0', '16.0', '29.266666']]
fecha_separada=h[0][0].split("-")
print(fecha_separada)
fecha_nueva=fecha_separada[0] + "/" + fecha_separada[1] + "/" + fecha_separada[2] #acá junto la tercera fecha, pero lo uno con la hora también
#es coincidencia esto pero hay que tenerlo en cuenta
print(fecha_nueva)
h[0][0]=fecha_nueva
print(h[0][0])