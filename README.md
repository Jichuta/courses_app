# Diango courses_app
Course app with Django

### REPO url
```bash
$ git clone https://github.com/Jichuta/courses_app.git
```
### Python version
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
```
## 
```bash
$ python manage.py createsuperuser
$ python3 manage.py makemigrations courses
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).

Implementar un sistema que permita administrar cursos de capacitación de corta duración (de 2 a 4 semanas), a continuación se describen los requerimientos solicitados.

- [x] Los tipos de usuarios del sistema son: Administrador, Director, Profesor, Estudiante y cada uno con un rol especifico.
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
- - [x] Estudiantes inscritos al curso
- - [x] Registro de Asistencia de estudiantes
- - [ ] Registro de las notas de cada estudiante inscrito.
- - [x] Material del curso. El material del curso consiste en información compuesta por un título y el contenido del material (solo texto, no se necesita subir archivos).
- [ ] Profesores: Pueden realizar las siguientes acciones:
- - [x] Ver los cursos de los que están a cargo.
- - [x] Registrar la asistencia de los estudiantes de cada curso.
- - [ ] Agregar material al curso.
- [ ] Estudiantes: Pueden realizar las siguientes actividades:
- - [x] Un estudiante puede ser registrado por el administrador
- - [x] también puede registrarse por su cuenta en el sistema (usuario de tipo Estudiante).
- - [x] Puede inscribirse a cursos que todavía no han empezado.
- - [x] Ver los cursos a los que se ha inscrito (y sus notas).
- - [ ] Ver el contenido de los cursos a los que está inscrito.
- [x] Todos los tipos de usuario deben ingresar al sistema con su nombre de usuario y contraseña.


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


### Sql quesries
```bash
update courses_student set username = 'rodrigo.mamani' where id =2;
```

### Credentials
```bash
- ADMIN
username=admin
password=abc.123
- Director
username=superuser
password=Abc.12345678
- Profersor
username=juan.perez
password=Abc.12345678
- Estudiante
username=douglas.mamani
password=Abc.12345678
```