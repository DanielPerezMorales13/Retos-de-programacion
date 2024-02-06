# Tema: Date time o tiempo y fechas

"""
la libreria datetime nos permite trabajar con fechas y horas en python
ademas de realizar operaciones con fechas y horas como sumar, restar, comparar, etc. Tambien podemos formatear fechas y horas a nuestro gusto. 
"""

# datetime: Nos permite trabajar con fechas y horas a la vez
# time: Nos permite trabajar con horas
# date: Nos permite trabajar con fechas
# timedelta: Nos permite realizar operaciones con fechas y horas
from datetime import date, datetime, time, timedelta

# ahora es una instancia de la clase datetime que nos da la fecha y hora actual del sistema en el que se ejecuta el programa
ahora: datetime = datetime.now(tz=None)


"""
>>> .year este atributo nos devuelve el año de la fecha

>>> .month este atributo nos devuelve el mes de la fecha

>>> .day este atributo nos devuelve el dia de la fecha

>>> .hour este atributo nos devuelve la hora de la fecha

>>> .minute este atributo nos devuelve el minuto de la fecha

>>> .second este atributo nos devuelve el segundo de la fecha

>>> .timestamp() este metodo nos devuelve la fecha en formato 
timestamp que es el numero de segundos que han pasado desde el 1 de enero de 1970

>>> .weekday() este metodo nos devuelve el dia de la semana en el que se encuentra la fecha o el dia de la semana que le corresponde a la fecha hoy es martes y el metodo nos devuelve 1 porque el lunes es 0 y el domingo es 6

>>> .isoformat() este metodo nos devuelve la fecha en formato iso que es el formato de fecha que se utiliza en la mayoria de los paises del mundo año-mes-dia hora:minuto:segundo. 2024-01-30T20:18:25.518783 . isoformat recibe dos parametros sep y timespec sep es un separador que indica que a continuacion viene la hora minuto y segundo y timespec es un separador que indica que a continuacion viene el microsegundo

    >>> 2024 es el año
    >>> 01 es el mes
    >>> 30 es el dia
    >>> T es un separador que indica que a continuacion viene la hora minuto y segundo
    >>> 20 es la hora
    >>> 18 es el minuto
    >>> 25 es el segundo
    >>> .518783 es el microsegundo

>>> .strftime() este metodo nos permite formatear la fecha a nuestro gusto.
    >>> Fecha hoy: Martes 30 de enero de 2024 20:18:25.518783 pm
    
    >>> %A nos devuelve el dia de la semana en el que se encuentra la fecha    
    
    >>> %d nos devuelve el dia de la fecha -> 30
    
    >>> %b nos devuelve el mes de la fecha -> ene
    
    >>> %B nos devuelve el mes de la fecha -> enero
    
    >>> %Y nos devuelve el año de la fecha -> 2024
    
    >>> %I nos devuelve la hora de la fecha en formato 12 horas -> 08
    
    >>> %M nos devuelve el minuto de la fecha -> 18
    
    >>> %S nos devuelve el segundo de la fecha -> 25
    
    >>> %s nos devuelve el segundo de la fecha -> 
    
    >>> %p nos devuelve si es am o pm -> pm
    
    >>> %P nos devuelve si es AM o PM -> PM
    
    >>> %f nos devuelve el microsegundo de la fecha 
    
    >>> %j nos devuelve el dia del año
    
    >>> %U nos devuelve el numero de semana del año
    
    >>> %W nos devuelve el numero de semana del año
    
    >>> %c nos devuelve la fecha en formato local
    
    >>> %x nos devuelve la fecha en formato local
    
    >>> %X nos devuelve la hora en formato local
    
    >>> %Z nos devuelve la zona horaria
    
    >>> %z nos devuelve la zona horaria
    
    >>> %r nos devuelve la hora en formato 12 horas
    
    >>> %R nos devuelve la hora en formato 24 horas
"""


def imprimirDate(date: datetime) -> str:
    return f"""
.year = {date.year}
.month = {date.month}
.day = {date.day}
.hour = {date.hour}
.minute = {date.minute}
.second = {date.second}
.timestamp() = {date.timestamp()}
..weekday() = {date.weekday()}
.isoformat() = {date.isoformat(sep="T", timespec="auto")}  
.strftime = {date.strftime("%s")}
"""


print(imprimirDate(date=ahora), end="\n")


año_2023: datetime = datetime(
    day=1,
    month=1,
    year=2023,
    hour=0,
    minute=0,
    second=0,
    microsecond=0,
    tzinfo=None,
    fold=0,
)
"""
año_2023 es una instancia de la clase datetime que nos da la fecha y hora del 1 de enero de 2023 a las 00:00:00
>>> datetime es una clase que nos permite trabajar con fechas y horas a la vez
>>> .year este atributo nos devuelve el año de la fecha
>>> .month este atributo nos devuelve el mes de la fecha
>>> .day este atributo nos devuelve el dia de la fecha
>>> .hour este atributo nos devuelve la hora de la fecha
>>> .minute este atributo nos devuelve el minuto de la fecha
>>> .second este atributo nos devuelve el segundo de la fecha
>>> .microsecond este atributo nos devuelve el microsegundo de la fecha
>>> .tzinfo este atributo nos devuelve la zona horaria de la fecha
>>> .fold este atributo nos devuelve el doblez de la fecha
"""

# * print(imprimirDate(date=año_2023),end="\n")

# Time

# la funcion time nos permite crear una instancia de la clase time que nos permite trabajar con horas
hora_actual: time = time(
    hour=20,
    minute=18,
    second=25,
    microsecond=518783,
    tzinfo=None,
    fold=0,
)

print("Hora Actual -> hora %d" % hora_actual.hour, end="\n")
print("Hora Actual -> minutos %d" % hora_actual.minute, end="\n")
print("Hora Actual -> segundos %d" % hora_actual.second, end="\n")

# Date
"""
El metodo .today() nos devuelve la fecha actual del sistema en el que se ejecuta el programa
"""
fecha_actual: date = date.today()

print(f"Fecha actual -> año {fecha_actual.year}", end="\n")
print(f"Fecha actual -> mes {fecha_actual.month}", end="\n")
print(f"Fecha actual -> dia {fecha_actual.day}", end="\n")

fecha_actual: date = date(
    day=5,
    month=2,
    year=1992,
)

print("Fecha actual -> año {año}".format(año=fecha_actual.year), end="\n")
print("Fecha actual -> mes {mes}".format(mes=fecha_actual.month), end="\n")
print("Fecha actual -> dia {dia}".format(dia=fecha_actual.day), end="\n")

fecha_actual: date = date(
    year=fecha_actual.year,
    month=fecha_actual.month + 1,
    day=fecha_actual.day,
)

print("Fecha actual -> mes {0}".format(fecha_actual.month), end="\n")

# Operaciones con fechas

diferencia: datetime = año_2023 - ahora
print(f"año_2023 - ahora -> {diferencia}", end="\n")

# * El metodo .date() nos devuelve la fecha de la instancia de la clase datetime
diferencia: datetime = año_2023.date() - fecha_actual
print(f"año_2023.date() - fecha_actual -> {diferencia}", end="\n")

# Timedelta o diferencia de tiempo
"""
El metodo timedelta nos permite realizar operaciones con fechas y horas
>>> .days este atributo nos devuelve los dias de la diferencia de tiempo
>>> .seconds este atributo nos devuelve los segundos de la diferencia de tiempo
>>> .microseconds este atributo nos devuelve los microsegundos de la diferencia de tiempo
>>> milliseconds este atributo nos devuelve los milisegundos de la diferencia de tiempo
>>> weeks este atributo nos devuelve las semanas de la diferencia de tiempo recibe 

"""
empieza: timedelta = timedelta(
    days=200,
    hours=100,
    minutes=200,
    seconds=30,
    microseconds=40,
    milliseconds=50,
    weeks=2,
)
termina: timedelta = timedelta(
    days=100,
    hours=100,
    minutes=100,
    seconds=100,
    microseconds=100,
    milliseconds=100,
    weeks=100,
)

print(f"termina - empieza -> {termina - empieza}", end="\n")
print(f"termina + empieza -> {termina + empieza}", end="\n")

# datetime.utcnow() nos devuelve la fecha y hora actual del sistema en el que se ejecuta el programa
print(f"datetime.utcnow() -> {datetime.utcnow()}", end="\n")
