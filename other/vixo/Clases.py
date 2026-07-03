class Persona:
    def __init__(self, rut:str, nombre:str, apellido:str, correo:str): #El rut es str para que no tome el '-' como una resta
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def validar_rut(self):
        factor_de_chequeo = [2,3,4,5,6,7]
        rut_invertido = self.rut[-3::-1] #Cuenta el rut sin '-' ni digito verificador desde el final al principio
        total = 0
        index_chequeo = 0
        for i in range(len(rut_invertido)):
            if index_chequeo>=len(factor_de_chequeo):
                index_chequeo = 0
            total += int(rut_invertido[i])*factor_de_chequeo[index_chequeo]
            index_chequeo+=1
        dv = 11-(total%11) 
        #Si el resultado de la resta es < 10, dicho resultado es el dígito de control que buscábamos.
        if dv<10:
            digito_verificador = dv
        #Si el resultado es 11 el dígito de control es 0
        elif dv == 11:
            digito_verificador = 0
        #si el resultado es 10 el dígito de control resultante es 1.
        else:
            digito_verificador = "k"
        if str(digito_verificador) == self.rut[-1]:
            return True
        else:
            return False

    #Retorna el nombre completo y el correo de la persona.
    def __str__(self):
        return f"Nombre completo: {self.nombre} {self.apellido}\nCorreo: {self.correo}"
# persona1 = Persona("21345678-4", "Valentina", "Muñoz","valentina.munoz@udpro.cl")

# print(persona1.validar_rut()) #---> True
# print(str(persona1)) #------> Nombre completo: Valentina Muñoz \n Correo: valentina.munoz@udpro.cl



class Estudiante(Persona):
    def __init__(self, rut:str, nombre: str, apellido:str, correo:str , carrera: str, asignatura:str, nota1:float , nota2:float ,nota3:float ,asistencia:float):
        super().__init__(rut, nombre, apellido, correo)
        Estudiante.carrera = carrera
        Estudiante.asignatura = asignatura
        Estudiante.nota1 = nota1
        Estudiante.nota2 = nota2
        Estudiante.nota3 = nota3
        Estudiante.asistencia = float(asistencia)
    def promedio(self):
        suma_notas = float(Estudiante.nota1) + float(Estudiante.nota2) + float(Estudiante.nota3)
        # print(suma_notas)
        promedio = round(suma_notas/3,1)
        return float(promedio)
    
    def situacion_academica(self):  
        if self.promedio()>= 4 and self.asistencia>75:
            return "Aprovado"
        else:
            return "Reprovado"
        
    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellido} | Asignatura: {self.asignatura} | Promedio: {self.promedio()} | Asistencia: {self.asistencia}% | Rut valido: {self.validar_rut()}"

# persona2 = Estudiante("22496854-k","Vicente", "Ruiz", "v.ruizm@udd.cl", "ICIIT", "taller de progra", 6.2,5.4,2.4, 80)

# print("---------------------------4--")
# print(persona2.promedio())
# print(persona2)

class Profesor(Persona):
    def __init__(self, rut, nombre, apellido, correo, departamento, asignatura, horas_contrato: int):
        super().__init__(rut, nombre, apellido, correo)
        self.departamento = departamento
        self.asignatura = asignatura
        self.horas_contrato = horas_contrato

    def tipo_contrato(self):
        if int(self.horas_contrato) >=  20:
            return f"Jornada Alta"
        else:
            return f"Jornada Parcial"
        
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido} | Asignatura: {self.asignatura} | Horas: {self.horas_contrato} | {self.tipo_contrato()} | Rut valido: {self.validar_rut()}"

