#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
#duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5



#diferencias de duracion
diferecia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)#el curso de dalto es igual al 60% del minimo de otros cursos, por eso su diferencia seria del 40%
diferecia_con_max = 100 - dalto_curso*1000 // otros_cursos_max / 10
diferecia_con_prom = 100 - (dalto_curso / otros_cursos_promedio * 100)

print(f'El curso de dalto tarda un {diferecia_con_min}% menos que el mas rapido')
print(f'El curso de dalto tarda un {diferecia_con_max}% menos que el mas lento')
print(f'El curso de dalto tarda un {diferecia_con_prom}% menos que el mas promedio')



#calculando porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso*1000 // crudo_dalto / 10

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso curso elimina un {tiempo_vacio_dalto}% de tiempo vacio')