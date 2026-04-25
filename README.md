# Sistema de Gestión Académica (SIS)

Plataforma integral para la gestión de instituciones educativas. Permite administrar cursos, inscripciones y calificaciones con una interfaz moderna y segura.

## Características Principales

- **Dashboard Inteligente**: Vistas personalizadas según el rol del usuario (Alumno o Profesor).
- **Matriz de Calificaciones**: Interfaz tipo hoja de cálculo para gestión masiva de notas.
- **Control de Cupos**: Validación automática de capacidad máxima por curso.
- **Arquitectura Robusta**: Patrón Repository para separación clara entre lógica de negocio y persistencia.
- **UI Premium**: Diseño responsivo con Glassmorphism, tipografía moderna e iconos dinámicos (Lucide).
- **Seguridad**: Manejo global de errores (404/403) y validación de propiedad de recursos.

## Tecnologías Utilizadas

- **Backend**: Python 3.13 / Django 6.0.4
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3 (Custom Design System), Bootstrap 5, JavaScript
- **Iconos**: Lucide Icons

## Requisitos Previos

- Python 3.13 o superior
- MySQL Server en ejecución
- Pip (gestor de paquetes de Python)

## Instalación y Configuración

1. **Clonar el repositorio**:
```bash
   git clone <url-del-repositorio>
   cd sis
```

2. **Crear y activar un entorno virtual**:
```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
   pip install -r requirements.txt
```

4. **Configurar la base de datos**:
   - Crear una base de datos en MySQL llamada `sis`.
   - Renombrar `mysql.cnf.example` a `mysql.cnf` y configurar las credenciales.
   - Verificar que el archivo `.env` tenga las configuraciones correctas.

5. **Ejecutar migraciones**:
```bash
   python manage.py makemigrations
   python manage.py migrate
```

6. **Crear superusuario** (acceso al panel de administración):
```bash
   python manage.py createsuperuser
```

7. **Iniciar el servidor**:
```bash
   python manage.py runserver
```

Accede al sistema en: `http://127.0.0.1:8000/`

## Ejecución de Tests

Para verificar la integridad del sistema y las reglas de negocio:
```bash
python manage.py test
```

---
Desarrollado como parte de un proceso de selección técnica.