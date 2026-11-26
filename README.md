# BBDD Centro Educativo

Proyecto de creación de una base de datos relacional para gestionar alumnos, cursos, promociones, sedes, modalidades, profesorado y notas de un centro educativo.

## Tecnologías

- Python y Pandas para limpiar y transformar los datos.
- PostgreSQL y pgAdmin para crear y gestionar la base de datos.
- Render para alojar PostgreSQL en la nube.

## Estructura

- `data/merge.py`: limpieza y preparación de los CSV.
- `data/nuevas/grupal.sql`: creación de las tablas y relaciones.
- `data/nuevas/`: CSV preparados para importar en PostgreSQL.
- `Proyecto_BBDD.md`: descripción completa del ejercicio.

## Uso

1. Ejecutar `python data/merge.py` para generar los CSV finales.
2. Ejecutar `data/nuevas/grupal.sql` en PostgreSQL.
3. Importar primero las tablas principales (`curso`, `promocion`, `sede` y `modalidad`).
4. Importar después `alumnos`, `claustro`, `notas_DS` y `notas_FS`.

## Objetivo

Normalizar los datos originales y construir una base de datos escalable con claves primarias y foráneas que permita realizar consultas sobre alumnos, profesores, cursos y resultados académicos.
