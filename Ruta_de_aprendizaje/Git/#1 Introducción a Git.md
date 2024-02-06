# **_Introducción a Git_**

> _Git es un sistema de control de versiones distribuido, lo que significa que cada desarrollador tiene una copia completa del historial del proyecto en su máquina local. Esto permite un alto grado de flexibilidad y eficiencia en el trabajo colaborativo._

<kbd>Fue creado por Linus Torvalds, el creador de Linux.</kbd>

> Para instalar Git, puedes seguir los siguientes pasos dependiendo de tu sistema operativo:

**En Windows:**

1. Descarga el instalador de Git desde [la página oficial de Git](https://git-scm.com/download/win).
2. Ejecuta el archivo descargado y sigue las instrucciones del instalador.

**En macOS:**

1. Abre la Terminal.
2. Ejecuta el siguiente comando: `brew install git`.

**En Linux:**

1. Abre la Terminal.
2. Ejecuta el siguiente comando: `sudo apt-get install git`.

## Comandos básicos de Git

Aquí hay algunos comandos básicos de Git que puedes encontrar útiles:

- `git init`: Inicializa un nuevo repositorio Git en tu directorio actual.
- `git clone [url]`: Clona un repositorio Git existente.
- `git add [archivo]`: Agrega un archivo al área de preparación de Git.
- `git commit -m "[mensaje]"` o `git commit --message= "[mensaje]"`: Crea un nuevo commit con los cambios que has agregado al área de preparación.
- `git push [remoto] [rama]`: Empuja tus commits al repositorio remoto.

```bash
# Ejemplo de uso de comandos Git
git init
```

```bash
# Ejemplo de uso de comandos Git
git add README.md
```

```bash
# Ejemplo de uso de comandos Git
git commit -m "Añadir README"
```

```bash
# Ejemplo de uso de comandos Git
git commit --message="Añadir README"
```

```bash
# Ejemplo de uso de comandos Git
git push origin master
```

## Enlaces útiles

- [_Documentación oficial de Git_](https://git-scm.com/doc "https://git-scm.com/doc")
