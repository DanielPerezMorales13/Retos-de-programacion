""""
OCP": "Open Closed Principle" Significa en español Principio abierto cerrado. 

Este principio dice que una clase debe estar abierta para extenderse pero cerrada para modificarse.

Este principio evita que los desarrolladores modifiquen una clase y que afecte el funcionamiento de otras clases.
"""


# Nosotros debemos desarrollar un sistema para agregar nuevas funcionalidades sin modificar el codigo existente

# Ejemplo de un sistema de notificaciones" que notifique a los usuarios por email, sms, whatsapp, twitter, etc


class Notificador:
    def __init__(self: object, usuario: object, mensaje: str) -> None:
        self.usuario: object = usuario
        self.mensaje: str = mensaje

    def Notificar(self: object) -> any:
        raise NotImplementedError("Este metodo debe ser implementado en la subclase")


class NotificadorEmail(Notificador):
    def __init__(self: object, usuario: object, mensaje: str) -> None:
        super().__init__(usuario=usuario, mensaje=mensaje)

    def Notificar(self: object) -> str:
        # Recordablemente que usuario sea un objeto y que tenga un atributo email
        return f"Enviando email a {self.usuario.email}"


class NotificadorSMS(Notificador):
    def __init__(self: object, usuario: object, mensaje: str) -> None:
        super().__init__(usuario=usuario, mensaje=mensaje)

    def Notificar(self: object) -> str:
        # Recordablemente que usuario sea un objeto y que tenga un atributo sms
        return f"Enviando email a {self.usuario.sms}"


class NotificadorWhatsApp(Notificador):
    def __init__(self: object, usuario: object, mensaje: str) -> None:
        super().__init__(usuario=usuario, mensaje=mensaje)

    def Notificar(self: object) -> str:
        # Recordablemente que usuario sea un objeto y que tenga un atributo whatsapp
        return f"Enviando email a {self.usuario.whatsapp}"


class NotificadorTwitter(Notificador):
    def __init__(self: object, usuario: object, mensaje: str) -> None:
        super().__init__(usuario=usuario, mensaje=mensaje)

    def Notificar(self: object) -> str:
        # Recordablemente que usuario sea un objeto y que tenga un atributo twitter
        return f"Enviando email a {self.usuario.twitter}"


notificacion: object = Notificador(usuario="Daniel", mensaje="Hola, como estas?")
print(notificacion.Notificar())
