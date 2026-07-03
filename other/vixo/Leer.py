import Clases

with open("personas_academicas.csv", "r", encoding="utf-8") as personas:
    lineas = personas.readlines()[1:] # No tomar primera linea

personas =[]
profesores = []
alumnos = []

total_de_horas_contratada = 0

for linea in lineas:
    datos = linea.split(",")

    tipo = datos[0]
    rut = datos[1]
    nombre = datos[2]
    apellido = datos[3]
    carrera_departamento = datos[4]
    asignatura = datos[5]
    nota1 = datos[6]
    nota2 = datos[7]
    nota3 = datos[8]
    asistencia = datos[9]
    horas_contrato = datos[10]
    correo = datos[11]

    if tipo.lower() == "alumno":
        alumno = Clases.Estudiante(rut,nombre,apellido, correo,carrera_departamento,asignatura,nota1,nota2,nota3, asistencia)
        # if alumno.promedio()>=mejor_promedio:
        #     mejor_alumno = f"Mejor alumno {alumno.nombre} {alumno.apellido} - {asignatura} - Promedio: {alumno.promedio()}" 
        # print(alumno)
        personas.append(alumno)
        alumnos.append(alumno)
    else:
        profesor = Clases.Profesor(rut,nombre,apellido,correo,carrera_departamento,asignatura,horas_contrato)
        # print(profesor)
        # if int(horas_contrato)>=mas_horas:
        #     profesor_con_mas_horas = f"Profesor con mas horas {profesor.nombre} {profesor.apellido} - {asignatura} - {horas_contrato} horas" 
        #     mas_horas = int(profesor.horas_contrato)
        total_de_horas_contratada += int(profesor.horas_contrato)
        personas.append(profesor)
        profesores.append(profesor)
for per in alumnos:
    print(f"{per.nombre}: {per.promedio()}")

print(f"\n{"="*10}<Personas registradas>{"="*10}\n")

for persona in personas:
    print(persona)

print(f"\n{"="*10}<Cantidad de personas registradas>{"="*10}\n")

print(f"Total de personas cargadas: {len(personas)}")
print(f"Total de alumnos: {len(alumnos)}")
print(f"Total de profesores: {len(profesores)}")

print(f"\n{"="*10}<Validacion de rut>{"="*10}\n")

rut_invalido = 0
for persona in personas:
    print(f"{persona.nombre} {persona.apellido} - {persona.validar_rut()}")
    if persona.validar_rut() == False:
        rut_invalido+=1
print(f"\nPersonas con rut valido: {len(personas)-rut_invalido}")
print(f"Personas con rut invalido: {rut_invalido}")

print(f"\n{"="*10}<Promedio alumnos>{"="*10}\n")
for alumno in alumnos:
    print(f"{alumno.nombre} {alumno.apellido} - {alumno.promedio()}")
    print("*"*10)
    print(alumno.promedio(), alumno.nota1,alumno.nota2,alumno.nota3)
    print("*"*10)

print(f"\n{"="*10}<Situacion academica>{"="*10}\n")

reprovados = 0
for alumno in alumnos:
    print(f"{alumno.nombre} {alumno.apellido} - {alumno.situacion_academica()}")
    if alumno.situacion_academica() == "Reprovado":
        reprovados +=1

print(f"\n{"="*10}<Cantidad de alumnos aprovados/reprovados>{"="*10}\n")
print(f"Alumnos Aprovados: {len(alumnos)-reprovados}")
print(f"Alumnos Reprovados: {reprovados}")

print(f"\n{"="*10}<Alumno con mejor promedio>{"="*10}\n")
mejor_alumno = ""
mejor_promedio = 0
for alum in alumnos:
    if mejor_promedio == 0 or mejor_promedio<alum.promedio():
        mejor_alumno = f"{alum.nombre} {alum.apellido} - {alum.asignatura}"
        mejor_promedio = alum.promedio()
print(f"Mejor alumno: {mejor_alumno} - Promedio: {mejor_promedio}")

# print(mejor_alumno)

# print(f"\n{"="*10}<Tipo de contrato por profesor>{"="*10}\n")
# for profe in profesores:
#     print(f"{profe.nombre} {profe.apellido} _ {profe.tipo_contrato()}")

# print(f"Total de horas contratadas: {total_de_horas_contratada} horas")

# print(f"\n{"="*10}<Profesor con mas horas>{"="*10}\n")
# print(profesor_con_mas_horas)