def idValor(valor: str | int | float | bool | list | tuple | dict | set) -> str:
    return f"id {valor=} es " + str(id(valor)) 