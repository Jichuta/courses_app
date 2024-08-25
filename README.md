# Diango courses_app
Course app with Django

```bash
$ python3 -m django --version
$ 4.2.15
```

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ cd projectname/
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ deactivate

$ python3 manage.py makemigrations courses
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).

Implementar un sistema que permita administrar cursos de capacitación de corta duración (de 2 a 4 semanas), a continuación se describen los requerimientos solicitados.

- [ ] Los tipos de usuarios del sistema son: Administrador, Director, Profesor, Estudiante y cada uno con un rol especifico.
- [x] Solo los usuarios de tipo Administrador y Director pueden acceder al 'admin' del sistema.
- [x] Administradores: tipo de usuario con acceso total del sistema (super user), es el único rol que puede crear usuarios de otros tipos a requerimiento.
- [ ] Directores: Pueden realizar las siguientes acciones:
- - [x] Pueden crear cursos y asignar profesores a cursos.
- - [x] Ver cursos existentes.
- - [ ] Modificar cursos existentes.
- [ ] Cursos: Cada curso tiene que tener la siguiente información básica:
- - [x] Nombre del curso
- - [x] Profesor
- - [x] Fecha de inicio
- - [x] Fecha de fin
- - [x] Estado Activo, Inactivo, Concluido y Anulado
- - [ ] Estudiantes inscritos al curso
- - [ ] Registro de Asistencia de estudiantes
- - [ ] Registro de las notas de cada estudiante inscrito.
- - [x] Material del curso. El material del curso consiste en información compuesta por un título y el contenido del material (solo texto, no se necesita subir archivos).
- [ ] Profesores: Pueden realizar las siguientes acciones:
- - [x] Ver los cursos de los que están a cargo.
- - [ ] Registrar la asistencia de los estudiantes de cada curso.
- - [ ] Agregar material al curso.
- [ ] Estudiantes: Pueden realizar las siguientes actividades:
- - [ ] Un estudiante puede ser registrado por el administrador y también puede registrarse por su cuenta en el sistema (usuario de tipo Estudiante).
- - [ ] Puede inscribirse a cursos que todavía no han empezado.
- - [ ] Ver los cursos a los que se ha inscrito (y sus notas).
- - [ ] Ver el contenido de los cursos a los que está inscrito.
- [ ] Todos los tipos de usuario deben ingresar al sistema con su nombre de usuario y contraseña.


## Features adicionales
### Director
- [x] Agregar nuevo estudiante
- [x] Ver los estudiantes inscritos a un curso
- [x] Registrar la inscripcion de un estudiante al un curso
- [x] Registrar nuevo professor
- [x] Assignar un profesor a un determinado curso, cuando se crea el curso
### Profesor
- [x] Ver los cursos en los que esta a cargo
- [x] Inscribir nuevos estudiantes
### Estudiante
