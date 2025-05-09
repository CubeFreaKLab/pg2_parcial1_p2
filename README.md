# Parcial 1 - PG2 (Ejercicio 2)

:card_index: Carrera: *Sistemas Informaticos*

:notebook: Materia: *Programación 2* 

:bust_in_silhouette: Nombre Completo: *Jorge Daniel Choque Ferrufino*

:calendar: Fecha: *8 de Mayo del 2025*

## INFORMACION DEL EJERCICIO 2

Este repositorio contiene un proyecto de Django que gestiona información sobre películas y directores.

## Estructura del proyecto

```
proyecto_cine/
├── cine/                   # Aplicación Django
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py             # Configuración de la aplicación
│   ├── migrations/         # Migraciones de la base de datos
│   ├── models.py           # Modelos de datos
│   ├── tests.py            # Tests
│   └── views.py            # Vistas
├── proyecto_cine/          # Configuración del proyecto
│   ├── asgi.py
│   ├── settings.py         # Configuración del proyecto
│   ├── urls.py             # Configuración de URLs
│   └── wsgi.py
├── manage.py               # Script de gestión de Django
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación
```

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/CubeFreakLab/pg2_parcial1_p2.git
   cd pg2_parcial1_p2
   ```

2. Crear y activar un entorno virtual:
   ```
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Realizar las migraciones:
   ```
   cd proyecto_cine
   python manage.py migrate
   ```

5. Crear un superusuario:
   ```
   python manage.py createsuperuser
   ```

6. Iniciar el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Uso

1. Acceder al panel de administración:
   http://127.0.0.1:8000/admin/

2. Iniciar sesión con el superusuario creado.

3. Gestionar directores y películas desde el panel de administración.

## Modelos

### Director
- **nombre**: Nombre del director
- **nacionalidad**: País de origen del director
- **fecha_nacimiento**: Fecha de nacimiento del director

### Película
- **titulo**: Título de la película
- **anio_estreno**: Año de lanzamiento de la película
- **director**: Relación con el modelo Director (Clave foránea)
