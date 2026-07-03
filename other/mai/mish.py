class Personas():
    def __init__(self, rut, nombre, apellido, correo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


    def validarut(self):
        factor = 1        
        sacar = self.rut.replace("-", "")
        #print(sacar)
        voltear = sacar[7::-1]
        #print(voltear)
        verificador = sacar[-1]
        #print(verificador)
        suma = 0
        listaVerificacion = []
        for validar in voltear:
            factor += 1
            if factor > 7:
                factor = 2

            #print(factor)
            listaVerificacion.append(int(validar))
            suma += int(validar)*factor
           
        resto = (suma * 1) % 11 #saco el resto de la suma
        resto = 11 - resto #al 11 le quito el resto (modulo 11)

        if resto == 11:  #comparo si es 11 para que me quede el resto correcto
            resto = 0
        elif resto == 10:
            resto = 'K'
       
        #print("las suma:",suma)
        #print("el resto:",resto)
        #print("el verificador:",verificador)
        #suma.append(int(verificador))
        #print(f"{listaVerificacion[::-1]}-{resto}")
        if str(resto).upper() == verificador.upper():
            return True
        return False

    def __repr__(self):
        return f"{self.nombre} {self.apellido} {self.correo}"
       
class Alumno(Personas):
    def __init__(self, rut,nombre,apellido,carrera,asignatura,nota1,nota2,nota3,asistencia,correo):
        super().__init__(rut, nombre, apellido, correo)
        self.carrera = carrera
        self.asignatura = asignatura
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.asistencia = int(asistencia)

    def promedio(self):
        notas_totales = self.nota1, self.nota2, self.nota3
        prom = round(sum(notas_totales)/len(notas_totales),1)
        return prom

    def situacion_academica(self):
        if self.promedio() >= 4.0 and self.asistencia >= 75:
            return "aprobado"
        return "reprobado"
    
    def necesita_apoyo(self):
        if self.asistencia < 80 or self.promedio() < 4.5: return True
        return False
   
    def __repr__(self):
        return f"|alumno:{self.nombre} {self.apellido}| Asignatura:{self.asignatura}|promedio:{self.promedio()}|asistencia:{self.asistencia}|correo:{self.correo}|rut{self.validarut()}"
    

class Profesor(Personas):
    def __init__(self, nombre, apellido, departamento, asignatura, horas_contrato,rut, correo):
        super().__init__(rut, nombre, apellido, correo)
        self.departamento = departamento
        self.asignatura = asignatura
        self.horas_contrato = horas_contrato

    def tipo_contrato(self):
       if self.horas_contrato >= 20:
           return "Jornada Alta"
       return "Jornada Parcial"
    def __repr__(self):
        return f"|Profesor: {self.nombre} {self.apellido} | Asignatura: {self.asignatura} | Horas: {self.horas_contrato} | RUT: {self.validarut()}"


profesores=[]
alumnos=[]
personas=[]
acum_personas = 0
acum_alumnos = 0
acum_profesores = 0
rutValido = 0
rutInvalidou = 0
alumnos_aprobados = 0
alumnos_reprobados = 0
mejorPromedio = 0
mejorAlumno = None
totalHoras = 0
mejorHoras = ""
mejorProfe = ""
profesores_por_asignatura = {}
with open ("personas_academicas.csv", "r", encoding="utf-8") as pa:
    leer = pa.readlines()
    for buscar in leer[1::]:
        mostrar = buscar.strip().split(",")
        #print(mostrar)

        tipo = mostrar[0].upper()
        if tipo ==  "ALUMNO":
            estudiante = Alumno(
            rut=mostrar[1],
            nombre=mostrar[2],
            apellido=mostrar[3],
            carrera=mostrar[4],
            asignatura=mostrar[5],
            nota1=mostrar[6],
            nota2=mostrar[7],
            nota3=mostrar[8],
            asistencia=mostrar[9],
            correo=mostrar[11]
            )
            acum_alumnos +=1
            acum_personas +=1
            alumnos.append(estudiante)
            personas.append(estudiante)


        elif tipo == "PROFESOR":
            profesor = Profesor(
            nombre=mostrar[2],
            apellido=mostrar[3],
            departamento=mostrar[4],
            asignatura=mostrar[5],
            horas_contrato=int(mostrar[10]),
            rut=mostrar[1],
            correo=mostrar[11]
            )
            acum_profesores +=1
            acum_personas +=1
            personas.append(profesor)
            profesores.append(profesor)

for Personas in personas:
    if Personas.validarut():
        print(f"{Personas.nombre} {Personas.apellido} - rut valido")
        print("--------------")
        rutValido +=1
    else:
        print(f"{Personas.nombre} {Personas.apellido} - rut invalido")
        print("---------------")
        rutInvalidou +=1

for ver in personas:
    print(ver)
print("----------------------------------------------------------------")
for alumno in alumnos:
    print(f"{alumno.nombre} {alumno.apellido}: promedio = {alumno.promedio()}")
print("----------------------------------------------------------------")
for alumno in alumnos:
    print(f"{alumno.nombre} {alumno.apellido}: situacion academica {alumno.situacion_academica()}")

for alumno in alumnos:
    if alumno.situacion_academica() == "aprobado":
        alumnos_aprobados +=1
    else:
        alumnos_reprobados +=1

for alumno in alumnos:
    if alumno.promedio() > mejorPromedio:
        mejorPromedio = alumno.promedio()
        mejorAlumno = alumno

for profe in profesores:
    print(f"{profe.nombre} {profe.apellido} - {profe.tipo_contrato()}")

for profesor in profesores:
    totalHoras += profesor.horas_contrato


for Profesor in profesores:

    if mejorHoras == "" or mejorHoras < Profesor.horas_contrato:
        mejorHoras = Profesor.horas_contrato
        mejorProfe = [f"{Profesor.nombre} {Profesor.apellido}: {Profesor.asignatura}: {Profesor.horas_contrato} horas"]
    elif mejorHoras == Profesor.horas_contrato:
        mejorProfe.append(f"{Profesor.nombre} {Profesor.apellido}: {Profesor.asignatura}: {Profesor.horas_contrato} horas")

    print(f"{Profesor.nombre} {Profesor.apellido} - {Profesor.tipo_contrato()}")

alumnos_por_asignatura = {}

for alumno in alumnos:
    asignatura = alumno.asignatura

    if asignatura not in alumnos_por_asignatura:
        alumnos_por_asignatura[asignatura] = []

    alumnos_por_asignatura[asignatura].append(alumno)

for asignatura, lista_alumnos in alumnos_por_asignatura.items():

    cantidad = len(lista_alumnos)

    suma_promedios = 0
    for alumno in lista_alumnos:
        suma_promedios += alumno.promedio()

    promedio_curso = round(suma_promedios / cantidad, 1)



for profesor in profesores:
    profesores_por_asignatura[profesor.asignatura] = profesor

#print("++++++++++++",profesores, "++++++++++++++++++")
for asignatura in alumnos_por_asignatura:

    profesor = profesores_por_asignatura[asignatura]
    lista_alumnos = alumnos_por_asignatura[asignatura]

    print(f"Asignatura: {asignatura}")
    print(f"Profesor: {profesor.nombre} {profesor.apellido}")
    print("Alumnos:")

    for alumno in lista_alumnos:
        print(f"- {alumno.nombre} {alumno.apellido} | Promedio: {alumno.promedio()} | {alumno.situacion_academica().capitalize()}")

        print("------------------------------------------------")
        print(f"Asignatura: {asignatura}")
        print(f"Cantidad de alumnos: {cantidad}")
        print(f"Promedio del curso: {promedio_curso}")
        print("------------------------------------------------")







print("\n\t TOTAL HORAS CONTRATADAS\n----------------")
print(f"Total de horas contratadas: {totalHoras}")

print("\n\t MAYOR HORAS\n----------------")
mejorProfe.sort()
print(f"Profesor con más horas: {mejorProfe[0]}")

print("los aprobados son: ", alumnos_aprobados)
print("--------------------------------------------------------------------------------------")
print("alumnos reprobados: ", alumnos_reprobados)
print("-------------------------------------------------------------------------------------")
print("la cantidad de rut validos:", rutValido)
print("-------------------------------------------------------------------------------------")
print("los rut invalidos son:", rutInvalidou)
print("-------------------------------------------------------------------------------------")

print("total de horas contrato: ", totalHoras)
print("=======================================")
print("El mejor alumno es:")
print(mejorAlumno.nombre, mejorAlumno.apellido)
print("Asignatura:", mejorAlumno.asignatura)
print("Promedio:", mejorPromedio)
print("=======================================")



#a = Personas("11888777-8", "Marcela","Vega", "marcela.vega@udpro.cl")
#a.validarut()
#a.__repr__()
#print(a.validarut())
#print(a)
#b = Alumno("21888999-9","Tomás","Sepúlveda","Ingeniería Civil Informática","Base de Datos",3.4,4.0,3.7,74,"tomas.sepulveda@udpro.cl")
#b.promedio()
#print(b)
#print(b.situacion_academica())
#c = Profesor("Marcela","Vega","Facultad de Ingeniería","Desafíos de la Informática", 12, "11888777-8", "marcela.vega@udpro.cl")
#c.tipo_contrato()
#print(c.tipo_contrato())
#print(c)
print("-----NECESITA APOYO-----")
for alumno in alumnos:
    if alumno.necesita_apoyo():
        print(f"{alumno.nombre} {alumno.apellido} - Promedio: {alumno.promedio()} - Asistencia: {alumno.asistencia}%")
