# PARTE I

class Persona:
    def __init__(self, rut: str, nombre: str, apellido: str, correo: str):
        self.rut: str = rut
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.correo: str = correo
    
    def validarut(self):
        if len(self.rut) != 10:
            return False
        
        base: str = self.rut.split("-")[0][::-1]
        factor: int = 2
        suma: int = 0

        try:
            chequeo: int = int(self.rut[-1])

            for valor in base:
                suma += int(valor) * factor
                factor += 1

                if factor > 7:
                    factor = 2
        except ValueError:
            return False
        
        return 11 - (suma % 11) == int(chequeo)
    
    def __repr__(self):
        return f"Nombre: {self.nombre} {self.apellido} | Correo: {self.correo}"

class Alumno(Persona):
    def __init__(self, rut: str, nombre: str, apellido: str, correo: str, carrera: str, asignatura: str, nota1: float, nota2: float, nota3: float, asistencia: int):
        super().__init__(rut, nombre, apellido, correo)

        self.carrera: str = carrera
        self.asignatura: str = asignatura
        self.nota1: float = nota1
        self.nota2: float = nota2
        self.nota3: float = nota3
        self.asistencia: int = asistencia
    
    def promedio(self):
        return round(sum([self.nota1, self.nota2, self.nota3]) / 3, 1)
    
    def situacion_academica(self):
        return "Aprobado" if self.promedio() >= 4 and self.asistencia >= 75 else "Reprobado"
    
    def necesita_apoyo(self):
        return self.promedio() < 4.5 or self.asistencia < 80
    
    def __repr__(self):
        return f"Alumn@: {self.nombre} {self.apellido} | Asignatura: {self.asignatura} | Promedio: {self.promedio()} | Asistencia: {self.asistencia}% | RUT válido: {self.validarut()}"

class Profesor(Persona):
    def __init__(self, rut: str, nombre: str, apellido: str, correo: str, departamento: str, asignatura: str, horas_contrato: int):
        super().__init__(rut, nombre, apellido, correo)

        self.departamento: str = departamento
        self.asignatura: str = asignatura
        self.horas_contrato: int = horas_contrato
    
    def tipo_contrato(self):
        return "Jornada Alta" if self.horas_contrato >= 20 else "Jornada Parcial"
    
    def __repr__(self):
        return f"Profesor@: {self.nombre} {self.apellido} | Asignatura: {self.asignatura} | Horas: {self.horas_contrato} | {self.tipo_contrato()} | RUT válido: {self.validarut()}"

# PARTE II

personas: list[Persona] = []
alumnos: list[Alumno] = []
profesores: list[Profesor] = []

with open("personas_academicas.csv", "r") as archivo:
    estructura: list[str] = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        linea: list[str] = linea.strip("\n").split(",")
        valores: dict[str, str] = {}

        for indice in range(len(estructura)):
            valores[estructura[indice]] = linea[indice]
        
        objeto: Persona | None = None

        if valores["tipo"] == "ALUMNO":
            objeto = Alumno(
                valores["rut"],
                valores["nombre"],
                valores["apellido"],
                valores["correo"],
                valores["carrera_departamento"],
                valores["asignatura"],
                float(valores["nota1"]),
                float(valores["nota2"]),
                float(valores["nota3"]),
                int(valores["asistencia"])
            )
            alumnos.append(objeto)
        
        if valores["tipo"] == "PROFESOR":
            objeto = Profesor(
                valores["rut"],
                valores["nombre"],
                valores["apellido"],
                valores["correo"],
                valores["carrera_departamento"],
                valores["asignatura"],
                int(valores["horas_contrato"])
            )
            profesores.append(objeto)
        
        # Fallback en caso de que no caiga en ninguna de las dos categorías.
        if objeto is None:
            objeto = Persona(
                valores["rut"],
                valores["nombre"],
                valores["apellido"],
                valores["correo"]
            )
        
        personas.append(objeto)

print(personas)

# PARTE III

print(
    f"Total de personas cargadas: {len(personas)}",
    f"Total de alumnos: {len(alumnos)}",
    f"Total de profesores: {len(profesores)}",
    sep="\n"
)

print(*["Personas:", *personas], sep="\n")

# PARTE IV

rut_valido: int = 0
rut_invalido: int = 0

for persona in personas:
    valido: str = "RUT inválido"
    rut_invalido += 1

    if persona.validarut():
        valido = "RUT válido"
        rut_valido += 1
        rut_invalido -= 1

    print(f"{persona.nombre} {persona.apellido} - {valido}")

print(
    f"Personas con RUT válido: {rut_valido}",
    f"Personas con RUT inválido: {rut_invalido}",
    sep="\n"
)

# PARTE V

alumnos_aprobados: int = 0
alumnos_reprobados: int = 0

for alumno in alumnos:
    print(f"{alumno.nombre} {alumno.apellido} - {alumno.promedio()}")

for alumno in alumnos:
    if alumno.situacion_academica() == "Aprobado":
        alumnos_aprobados += 1
    else:
        alumnos_reprobados += 1

    print(f"{alumno.nombre} {alumno.apellido} - {alumno.situacion_academica()}")

print(
    f"Alumnos aprobados: {alumnos_aprobados}",
    f"Alumnos reprobados: {alumnos_reprobados}",
    sep="\n"
)

mejor_alumno: Alumno | None = None
for alumno in alumnos:
    if mejor_alumno is None or mejor_alumno.promedio() < alumno.promedio():
        mejor_alumno = alumno

if mejor_alumno is not None:
    print(f"Mejor alumno: {mejor_alumno.nombre} {mejor_alumno.apellido} - {mejor_alumno.carrera} - Promedio: {mejor_alumno.promedio()}")
else:
    print("No hay mejor alumno.")

# PARTE VI

horas_contratadas: int = 0
profesor_sobreexplotado: Profesor | None = None

for profesor in profesores:
    print(f"{profesor.nombre} {profesor.apellido} - {profesor.tipo_contrato()}")
    horas_contratadas += profesor.horas_contrato

    if profesor_sobreexplotado is None:
        profesor_sobreexplotado = profesor
    
    if profesor_sobreexplotado.horas_contrato < profesor.horas_contrato:
        profesor_sobreexplotado = profesor
    
    if profesor_sobreexplotado.horas_contrato == profesor.horas_contrato and sorted([profesor_sobreexplotado.nombre[0], profesor.nombre[0]])[0] == profesor.nombre[0]:
        profesor_sobreexplotado = profesor

print(f"Total de horas contratadas: {horas_contratadas}")
print(f"Profesor con más horas: {profesor_sobreexplotado.nombre} {profesor_sobreexplotado.apellido} - {profesor_sobreexplotado.asignatura} - {profesor_sobreexplotado.horas_contrato} horas")

# PARTE VII

alumnos_por_asignatura: dict[str, list[Alumno]] = {}

for alumno in alumnos:
    if alumno.asignatura not in alumnos_por_asignatura:
        alumnos_por_asignatura[alumno.asignatura] = []
    
    alumnos_por_asignatura[alumno.asignatura].append(alumno)

for asignatura, alumnos_asignatura in alumnos_por_asignatura.items():
    print(
        f"Asignatura: {asignatura}",
        f"Cantidad de alumnos: {len(alumnos_asignatura)}",
        f"Promedio del curso: {sum([alumno.promedio() for alumno in alumnos_asignatura]) / len(alumnos_asignatura)}",
        sep="\n"
    )

# PARTE VIII

profesor_por_asignatura: dict[str, Profesor] = {}

for profesor in profesores:
    profesor_por_asignatura[profesor.asignatura] = profesor

for asignatura, profesor in profesor_por_asignatura.items():
    print(
        f"Asignatura: {asignatura}",
        f"Profesor@: {profesor.nombre} {profesor.apellido}",
        "Alumnos:",
        sep="\n"
    )

    for alumno in alumnos_por_asignatura[asignatura]:
        print(f"- {alumno.nombre} {alumno.apellido} | Promedio: {alumno.promedio()} | {alumno.situacion_academica()}")

# PARTE IX

print("Alumnos que necesitan apoyo académico:")

for alumno in alumnos:
    if alumno.necesita_apoyo():
        print(f"{alumno.nombre} {alumno.apellido} - {alumno.promedio()} - {alumno.asistencia}%")