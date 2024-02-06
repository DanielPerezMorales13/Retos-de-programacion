# ***Ramas en Git***

> *Las **ramas** en Git son una forma efectiva de aislar el trabajo en características, experimentos o cualquier otra segregación de tareas en tu código. Aquí te presento algunos comandos esenciales y avanzados relacionados con las ramas en Git.*

## **Comandos básicos**

- *`git branch`: Este comando lista todas las ramas en tu repositorio.*

```bash
git branch
```

- *`git branch <nombre>`: Este comando crea una nueva rama con el nombre `<nombre>`.*

```bash
git branch nueva-rama
```

- *`git checkout <nombre>`: Este comando cambia a la rama `<nombre>`.*

```bash
git checkout nueva-rama
```

- *`git branch -d <nombre>`: Este comando elimina la rama `<nombre>`.*

```bash
git branch -d nueva-rama
```

- *`git branch -D <nombre>`: Este comando elimina la rama `<nombre>` incluso si no ha sido fusionada con su rama ascendente. Ten cuidado al usar esta opción, ya que puedes perder cambios en la rama que estás eliminando.*

```bash
git branch -D nueva-rama
```

## Comandos avanzados

- `git branch -m <nombre>`: Este comando renombra la rama actual a `<nombre>`.

```bash
git branch -m nuevo-nombre
```

- `git checkout -b <nombre>`: Este comando crea una nueva rama con el nombre `<nombre>` y cambia a ella en un solo paso.

```bash
git checkout -b nueva-rama
```

- `git branch -v`: Este comando muestra la última confirmación en cada rama.

```bash
git branch -v
```

- `git branch --verbose`: Este comando muestra la última confirmación en cada rama.

```bash
git branch --verbose
```

- `git branch --merged`: Este comando lista las ramas que han sido fusionadas a la rama actual.

```bash
git branch --merged
```

- `git branch --no-merged`: Este comando lista las ramas que no han sido fusionadas a la rama actual.

```bash
git branch --no-merged
```
