# ***"git add" y "git commit"***

## Agregar cambios

> *Para agregar cambios a tu repositorio, primero necesitarás agregar los ficheros modificados al área de preparación con `git add`. Puedes agregar todos los ficheros modificados con `git add .`, o agregar ficheros específicos con `git add [nombre del fichero]`.*

```bash
git add .
```

```bash
git add fichero.py
```

## **`git commit`**

> *El comando `git commit` crea un nuevo commit con los cambios que has agregado al área de preparación. Un commit es como un "punto de control" en tu proyecto al que puedes volver más tarde si es necesario.*

```bash
git commit
```

### **`git commit -m`**

> *La opción `-m` te permite especificar un mensaje de commit directamente en la línea de comandos. Esto es útil si tu cambio es lo suficientemente simple como para describirlo en una sola línea.*

```bash
git commit -m "Tu mensaje de commit aquí"
```

### **`git commit --message=`**

> *La opción `--message=` es equivalente a `-m`. Te permite especificar un mensaje de commit directamente en la línea de comandos.*

```bash
git commit --message="Tu mensaje de commit aquí"
```

> ***Nota:** Recuerda que los mensajes de commit deben ser descriptivos y significativos para ayudar a otros desarrolladores (o a ti mismo en el futuro) a entender qué cambios se realizaron en cada commit.*
