# ***"git log" y "git status"***

## **`git status`**

> *El comando `git status` muestra el estado del repositorio actual. Te informa sobre los cambios que se han realizado pero aún no se han confirmado (commit), así como los cambios que se han confirmado pero aún no se han enviado (push) al repositorio remoto.*

```bash
git status
```

## **`git log`**

> *El comando `git log` muestra un historial de todos los commits que se han realizado en el repositorio. Cada commit se muestra con su hash de commit, el autor, la fecha y el mensaje de commit.*

```bash
git log
```

### **`git log --oneline -n 1`**

> *Esta es una variante del comando `git log` que muestra cada commit en una sola línea, lo que puede hacer que el historial sea más fácil de leer. La opción `-n 1` limita la salida a solo el último commit.*

```bash
git log --oneline -n 1
```

```bash
git log --all -n 1
```

```bash
git log --all --oneline
```

```bash
git log --all
```

```bash
git log --full-history
```

```bash
git log
```

## **`git reflog`**

> *El comando `git reflog` muestra un historial de todas las acciones que han cambiado la HEAD. Es útil si necesitas rastrear cambios que no están asociados con commits, como los merges o los resets.*

```bash
git reflog
```
