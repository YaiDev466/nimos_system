# 📚 GUÍA COMPLETA DE USO - Sistema de Gestión de Costos de Confección

**Versión:** 1.0  
**Fecha:** Febrero 2026  
**Autor:** Desarrollo YaiDev

---

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación y Configuración](#instalación-y-configuración)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Autenticación](#autenticación)
6. [Funcionalidades Principales](#funcionalidades-principales)
7. [Guía de Usuario](#guía-de-usuario)
8. [API REST](#api-rest)
9. [Base de Datos](#base-de-datos)
10. [Despliegue](#despliegue)
11. [Troubleshooting](#troubleshooting)

---

## 🎯 Introducción

El **Sistema de Gestión de Costos de Confección** es una aplicación web moderna desarrollada con **FastAPI** y **SQLAlchemy** que permite gestionar de manera integral todos los aspectos operacionales de una empresa de confección.

### Características Principales:
- ✅ Gestión completa de entregas de productos
- ✅ Control de asistencia de trabajadores en tiempo real
- ✅ Análisis financiero avanzado (Costo de operación, Punto de equilibrio, Justicia de pago)
- ✅ Gestión de trabajadores y talleres
- ✅ Sistema de autenticación seguro con roles
- ✅ Seguimiento de producción por lotes
- ✅ Interfaz responsive y moderna

---

## 🖥️ Requisitos del Sistema

### Software Requerido:
- **Python:** 3.9 o superior
- **Base de Datos:** PostgreSQL 12+ o MySQL 8.0+
- **Docker:** Opcional (para despliegue containerizado)
- **Git:** Para control de versiones

### Dependencias de Python:
```plaintext
fastapi              # Framework web
uvicorn              # Servidor ASGI
jinja2               # Motor de templates
sqlalchemy           # ORM para base de datos
python-multipart     # Manejo de formularios
pytz                 # Gestión de zonas horarias
python-dotenv        # Variables de entorno
cryptography         # Seguridad
weasyprint           # Generación de PDFs
reportlab            # Reportes
psycopg2-binary      # Driver PostgreSQL
```

---

## ⚙️ Instalación y Configuración

### Paso 1: Clonar el Repositorio
```bash
cd /ruta/deseada
git clone <url-repositorio>
cd gastos_confeccion
```

### Paso 2: Crear Entorno Virtual
```bash
# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r requierements.txt
```

### Paso 4: Configurar Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:
```env
# Base de Datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
HOST=localhost
DATABASE=confecciondb
PORT_DB=5432

# Aplicación
PORT=8001
SECRET_KEY=tu_clave_secreta
```

### Paso 5: Inicializar Base de Datos
```bash
python -c "from app.db.connection import create_db_engine; from app.db.models.base import Base; engine = create_db_engine(); Base.metadata.create_all(engine)"
```

### Paso 6: Ejecutar la Aplicación
```bash
python main.py
```
La aplicación estará disponible en: **http://localhost:8001**

---

## 📂 Estructura del Proyecto

```
gastos_confeccion/
│
├── app/
│   ├── api/                           # Endpoints y rutas
│   │   ├── auth_endpoints.py          # Autenticación (Login/Logout)
│   │   ├── delivery_endpoints.py      # CRUD de Entregas
│   │   ├── worker_endpoints.py        # CRUD de Trabajadores
│   │   ├── factory_endpoints.py       # CRUD de Talleres
│   │   ├── endpoints_assistence.py    # Control de Asistencia
│   │   ├── admin_endpoints.py         # Panel Administrativo
│   │   ├── endpoints.py               # Cálculos y Reportes
│   │   ├── templates_endpoints.py     # Renderizado de Vistas
│   │   └── schemas/                   # Validación de Datos
│   │       ├── user_schema.py
│   │       ├── worker_schema.py
│   │       ├── delivery_schemas.py
│   │       ├── factory_schema.py
│   │       ├── assistence_schema.py
│   │       ├── gastos_schema.py
│   │       └── operator_schema.py
│   │
│   ├── db/                            # Capa de Base de Datos
│   │   ├── connection.py              # Conexión y sesiones
│   │   └── models/
│   │       ├── base.py                # Clase base
│   │       ├── user_model.py          # Modelo de Usuarios
│   │       ├── worker_model.py        # Modelo de Trabajadores
│   │       ├── delivery_models.py     # Modelo de Entregas
│   │       ├── factory_model.py       # Modelo de Talleres
│   │       └── assistence_model.py    # Modelo de Asistencia
│   │
│   ├── service/                       # Lógica de Negocio
│   │   ├── user_service.py            # Servicios de Usuario
│   │   ├── worker_service.py          # Servicios de Trabajadores
│   │   ├── delivery_service.py        # Servicios de Entregas
│   │   ├── factory_service.py         # Servicios de Talleres
│   │   └── assistence_service.py      # Servicios de Asistencia
│   │
│   ├── static/                        # Archivos Estáticos
│   │   ├── css/
│   │   │   ├── styles.css             # Estilos principales
│   │   │   ├── table.css              # Estilos de tablas
│   │   │   └── delivery.css           # Estilos específicos entregas
│   │   └── img/                       # Imágenes y recursos
│   │
│   ├── templates/                     # Plantillas HTML
│   │   ├── base.html                  # Template base
│   │   ├── login.html                 # Página de login
│   │   ├── menu.html                  # Menú principal
│   │   ├── produccion.html            # Producción
│   │   ├── calculos_menu.html         # Menú de cálculos
│   │   ├── agregar_trabajador.html    # Formulario agregar trabajador
│   │   ├── editar_trabajador.html     # Formulario editar trabajador
│   │   ├── lista_trabajadores.html    # Listado de trabajadores
│   │   ├── resumen_asistencia.html    # Resumen de asistencia
│   │   ├── calculates/                # Vistas de cálculos
│   │   ├── delivery/                  # Vistas de entregas
│   │   ├── assistence/                # Vistas de asistencia
│   │   └── admin/                     # Vistas administrativas
│   │
│   └── utils/                         # Utilidades
│       ├── __init__.py
│       └── permissions.py             # Control de permisos
│
├── main.py                            # Punto de entrada principal
├── docker-compose.yml                 # Configuración Docker
├── Dockerfile                         # Definición de imagen Docker
├── requierements.txt                  # Dependencias Python
├── .env                               # Variables de entorno
└── README.md                          # Información general

```

---

## 🔐 Autenticación

### Sistema de Roles
El sistema implementa tres roles principales:

| Rol | Permisos | Descripción |
|-----|----------|-------------|
| **Admin** | Acceso total | Gestión de usuarios, configuración del sistema |
| **Supervisor** | Gestión operativa | Puede crear, editar y ver reportes |
| **Operario** | Lectura y edición limitada | Principalmente visualización y entrada de datos |

### Login
**URL:** `http://localhost:8001/`

**Campos requeridos:**
- Usuario (username)
- Contraseña (password)

**Ejemplo de credenciales de prueba:**
```
Usuario: admin
Contraseña: admin123
```

**Proceso de autenticación:**
1. El usuario ingresa sus credenciales
2. Se valida contra la base de datos
3. Se almacena sesión en el cliente
4. Se redirige al menú principal

---

## 🎯 Funcionalidades Principales

### 1. 📊 Gestión de Entregas de Corte

**Ubicación:** `/menu` → "Entregas de Corte"

**Funcionalidades:**
- ✅ Registrar nuevas entregas
- ✅ Ver listado de entregas
- ✅ Filtrar por taller, fecha, estado
- ✅ Editar entregas existentes
- ✅ Eliminar entregas
- ✅ Búsqueda avanzada

**Campos de una Entrega:**
- Propietario (Owner/Taller)
- Fecha de Entrega
- Número de Lote
- Tipo de Prenda
- Color
- Tipo de Tela
- Ribete
- Cantidades por talla:
  - Rangos: 6-12, 12-18, 18-24, 24-36, 36-48
  - Individuales: 2, 4, 6, 8, 10, 12, 14, 16, 18
- Anotaciones
- Estado (activo/inactivo)

**Endpoints:**
- `POST /api/delivery/create` - Crear entrega
- `GET /api/delivery/list` - Listar entregas
- `GET /api/delivery/{id}` - Obtener entrega
- `PUT /api/delivery/{id}` - Editar entrega
- `DELETE /api/delivery/{id}` - Eliminar entrega

---

### 2. 👥 Gestión de Trabajadores

**Ubicación:** `/menu` → "Trabajadores"

**Funcionalidades:**
- ✅ Registrar nuevos trabajadores
- ✅ Listar todos los trabajadores
- ✅ Editar información de trabajador
- ✅ Activar/Desactivar trabajadores
- ✅ Ver historial de asistencia

**Campos de Trabajador:**
- Nombre Completo
- Apellido
- Cédula (identificación única)
- Teléfono
- Email
- Cargo
- Salario Base
- Estado (Activo/Inactivo)
- Fecha de Creación

**Endpoints:**
- `POST /api/worker/create` - Crear trabajador
- `GET /api/worker/list` - Listar trabajadores
- `GET /api/worker/{id}` - Obtener trabajador
- `PUT /api/worker/{id}` - Editar trabajador
- `DELETE /api/worker/{id}` - Eliminar trabajador

---

### 3. ⏱️ Control de Asistencia

**Ubicación:** `/menu` → "Asistencia"

**Funcionalidades:**
- ✅ Marcar llegada de trabajadores
- ✅ Marcar salida de trabajadores
- ✅ Ver asistencias del día
- ✅ Generar reportes de asistencia
- ✅ Calcular horas trabajadas

**Campos:**
- Trabajador
- Hora de Llegada (Timestamp)
- Hora de Salida (Timestamp)
- Duración de Jornada (Calculado)

**Endpoints:**
- `POST /assistence/mark-arrival` - Marcar llegada
- `POST /assistence/mark-departure` - Marcar salida
- `GET /assistence/today` - Asistencias de hoy
- `GET /assistence/report` - Reporte de asistencia

---

### 4. 🏭 Gestión de Talleres

**Ubicación:** `/menu` → "Entregas" → "Gestionar Talleres"

**Funcionalidades:**
- ✅ Registrar nuevos talleres
- ✅ Listar todos los talleres
- ✅ Editar información del taller
- ✅ Eliminar talleres

**Campos:**
- Nombre del Propietario
- Documento de Identificación
- Datos de Contacto

**Endpoints:**
- `POST /api/factory/create` - Crear taller
- `GET /api/factory/list` - Listar talleres
- `GET /api/factory/{id}` - Obtener taller
- `PUT /api/factory/{id}` - Editar taller
- `DELETE /api/factory/{id}` - Eliminar taller

---

### 5. 📈 Análisis y Cálculos Financieros

#### 5.1 Costo de Operación
**URL:** `/calcular-costo-operacion`

Calcula el costo total de operación basado en:
- Cantidad de trabajadores
- Salarios base
- Gastos fijos configurables
- Arriendo

**Fórmula:**
```
Costo Total = (Salarios × Trabajadores) + Gastos Fijos + Arriendo
```

#### 5.2 Punto de Equilibrio
**URL:** `/punto-equilibrio`

Analiza el punto en el que ingresos = costos

**Parámetros:**
- Precio por unidad
- Costo unitario
- Costos fijos

#### 5.3 Justicia de Pago
**URL:** `/justicia-pago`

Calcula distribución equitativa de salarios basada en:
- Producción por trabajador
- Horas trabajadas
- Desempeño

#### 5.4 Producción
**URL:** `/produccion`

Registra y analiza:
- Unidades producidas por lote
- Precio por unidad
- Total de ventas
- Desagregación por talla

---

### 6. 🔧 Panel Administrativo

**Ubicación:** `/menu` → "Admin"

**Funcionalidades:**
- ✅ Gestión de usuarios
- ✅ Crear nuevos usuarios
- ✅ Editar usuarios existentes
- ✅ Asignar roles
- ✅ Activar/Desactivar usuarios
- ✅ Ver logs de actividad

---

## 📖 Guía de Usuario - Paso a Paso

### Iniciar Sesión
1. Acceder a `http://localhost:8001`
2. Ingresar usuario y contraseña
3. Hacer clic en "Iniciar Sesión"
4. Serás redirigido al menú principal

### Registrar una Nueva Entrega

**Paso 1:** Ir a Entregas → Agregar Entrega
```
Menú → Entregas de Corte → Agregar Nueva Entrega
```

**Paso 2:** Completar formulario
- Seleccionar Propietario/Taller (dropdown)
- Seleccionar Fecha
- Ingresar Número de Lote
- Seleccionar Tipo de Prenda
- Seleccionar Color
- Seleccionar Tipo de Tela
- Seleccionar Ribete
- Ingresar cantidades por talla

**Paso 3:** Guardar
- Hacer clic en "Guardar Entrega"
- Confirmar en el diálogo de confirmación

### Agregar un Nuevo Trabajador

**Paso 1:** Navegar a Trabajadores
```
Menú → Trabajadores → Agregar Trabajador
```

**Paso 2:** Llenar formulario
- Nombre
- Apellido
- Número de Cédula (único)
- Teléfono
- Email
- Cargo
- Salario Base

**Paso 3:** Guardar
- Hacer clic en "Agregar Trabajador"

### Marcar Asistencia

**Paso 1:** Acceder a Asistencia
```
Menú → Asistencia → Marcar Asistencia
```

**Paso 2:** Marcar Llegada
- Seleccionar Trabajador
- La hora se registra automáticamente
- Hacer clic en "Marcar Llegada"

**Paso 3:** Marcar Salida
- Al final del día, seleccionar el mismo trabajador
- Hacer clic en "Marcar Salida"
- El sistema calcula automáticamente las horas

### Calcular Costo de Operación

**Paso 1:** Ir a Cálculos
```
Menú → Cálculos → Costo de Operación
```

**Paso 2:** Ingresar parámetros
- Cantidad de Trabajadores
- Salario Promedio (si es diferente)
- Gastos Fijos (opcional)
- Arriendo (opcional)

**Paso 3:** Calcular
- Hacer clic en "Calcular"
- Ver resultados desglosados

### Generar Reporte de Producción

**Paso 1:** Acceder a Producción
```
Menú → Producción
```

**Paso 2:** Ingresar Lotes
- Por cada lote, ingresar:
  - Tipo de Lote
  - Color
  - Precio Unitario
  - Cantidades por Talla

**Paso 3:** Calcular
- Hacer clic en "Calcular Producción"
- Ver resumen con:
  - Total de unidades
  - Total de ventas
  - Desglose por talla

---

## 🔌 API REST - Referencia Técnica

### Base URL
```
http://localhost:8001/api
```

### Headers Requeridos
```
Content-Type: application/json
Authorization: Bearer <token> (si es requerido)
```

### Autenticación

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Respuesta exitosa:**
```json
{
  "success": true,
  "message": "Autenticación exitosa",
  "data": {
    "id_user": 1,
    "username": "admin",
    "rol": "Admin",
    "estado": 1
  }
}
```

### Endpoints de Entregas

#### Crear Entrega
```http
POST /delivery/create
Content-Type: application/json

{
  "owner": "Taller Principal",
  "date": "2026-02-04",
  "lot": "LOT-001",
  "type": "T-Shirt",
  "color": "Rojo",
  "type_fabric": "Algodón",
  "rib": "Cuello",
  "sz6_12": 10,
  "sz12_18": 15,
  "sz18_24": 20,
  "annotation": "Entrega especial"
}
```

#### Listar Entregas
```http
GET /delivery/list
```

**Parámetros opcionales:**
- `owner`: Filtrar por propietario
- `date`: Filtrar por fecha
- `status`: Filtrar por estado

**Respuesta:**
```json
{
  "success": true,
  "data": [
    {
      "id_delivery": 1,
      "owner": "Taller Principal",
      "date": "2026-02-04",
      "lot": "LOT-001",
      "status": "active"
    }
  ]
}
```

### Endpoints de Trabajadores

#### Crear Trabajador
```http
POST /worker/create
Content-Type: application/json

{
  "nombre": "Juan",
  "apellido": "Pérez",
  "cedula": "1234567890",
  "telefono": "+57 300 123 4567",
  "email": "juan@example.com",
  "cargo": "Cosedor",
  "salario": 1200.00
}
```

#### Listar Trabajadores
```http
GET /worker/list
```

### Endpoints de Asistencia

#### Marcar Llegada
```http
POST /assistence/mark-arrival
Content-Type: application/json

{
  "worker": "Juan Pérez"
}
```

#### Marcar Salida
```http
POST /assistence/mark-departure
Content-Type: application/json

{
  "worker": "Juan Pérez"
}
```

---

## 🗄️ Base de Datos

### Tablas Principales

#### Tabla: users
```sql
CREATE TABLE users (
  id_user INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(100) NOT NULL UNIQUE,
  psw VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  rol VARCHAR(50) NOT NULL,
  estado INT DEFAULT 1
);
```

#### Tabla: workers
```sql
CREATE TABLE workers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  cedula VARCHAR(20) NOT NULL UNIQUE,
  telefono VARCHAR(20),
  cargo VARCHAR(100) NOT NULL,
  salario DECIMAL(10, 2) NOT NULL,
  activo BOOLEAN DEFAULT TRUE,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
  email VARCHAR(100)
);
```

#### Tabla: delivered_pieces
```sql
CREATE TABLE delivered_pieces (
  id_delivery INT PRIMARY KEY AUTO_INCREMENT,
  owner VARCHAR(100) NOT NULL,
  date DATE NOT NULL,
  lot VARCHAR(50),
  type VARCHAR(50),
  color VARCHAR(50),
  type_fabric VARCHAR(100),
  rib VARCHAR(100),
  sz6_12 INT DEFAULT 0,
  sz12_18 INT DEFAULT 0,
  sz18_24 INT DEFAULT 0,
  sz24_36 INT DEFAULT 0,
  sz36_48 INT DEFAULT 0,
  sz2 INT DEFAULT 0,
  sz4 INT DEFAULT 0,
  sz6 INT DEFAULT 0,
  sz8 INT DEFAULT 0,
  sz10 INT DEFAULT 0,
  sz12 INT DEFAULT 0,
  sz14 INT DEFAULT 0,
  sz16 INT DEFAULT 0,
  sz18 INT DEFAULT 0,
  status VARCHAR(20) DEFAULT 'active',
  modification_date DATETIME,
  modified_by VARCHAR(100)
);
```

#### Tabla: factories
```sql
CREATE TABLE factories (
  id_factory INT PRIMARY KEY AUTO_INCREMENT,
  owner VARCHAR(100) NOT NULL,
  document VARCHAR(50)
);
```

#### Tabla: assistence
```sql
CREATE TABLE assistence (
  id_assistence INT PRIMARY KEY AUTO_INCREMENT,
  worker VARCHAR(100) NOT NULL,
  arrival_time DATETIME NOT NULL,
  departure_time DATETIME,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Despliegue

### Con Docker Compose (Recomendado)

**Prerrequisitos:**
- Docker instalado
- Docker Compose instalado

**Paso 1:** Configurar `.env`
```env
DATABASE_URL=mysql+pymysql://MrZyzz23:Gonorrea007@mysql:3306/confecciondb
PORT=8001
```

**Paso 2:** Ejecutar Docker Compose
```bash
docker-compose up -d
```

**Paso 3:** Verificar estado
```bash
docker-compose ps
```

**Paso 4:** Ver logs
```bash
docker-compose logs -f app
```

### Despliegue en Servidor (Linux/Ubuntu)

**Paso 1:** Preparar servidor
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip postgresql
```

**Paso 2:** Clonar código
```bash
git clone <repo>
cd gastos_confeccion
```

**Paso 3:** Configurar entorno
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requierements.txt
```

**Paso 4:** Configurar servicio systemd
Crear `/etc/systemd/system/gastos.service`:
```ini
[Unit]
Description=Gastos Confeccion Service
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/home/user/gastos_confeccion
Environment="PATH=/home/user/gastos_confeccion/venv/bin"
ExecStart=/home/user/gastos_confeccion/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001

[Install]
WantedBy=multi-user.target
```

**Paso 5:** Iniciar servicio
```bash
sudo systemctl daemon-reload
sudo systemctl enable gastos
sudo systemctl start gastos
```

---

## 🔍 Troubleshooting

### Problema: "Connection refused" en base de datos

**Solución:**
1. Verificar que PostgreSQL está corriendo: `sudo service postgresql status`
2. Revisar credenciales en `.env`
3. Confirmar que la base de datos existe

```bash
psql -U usuario -d confecciondb -c "SELECT 1;"
```

### Problema: Puerto 8001 ya en uso

**Solución:**
```bash
# Encontrar proceso usando puerto 8001
lsof -i :8001

# Matar el proceso
kill -9 <PID>

# O cambiar puerto en .env
PORT=8002
```

### Problema: Módulo no encontrado

**Solución:**
```bash
# Reactivar venv y reinstalar
source .venv/bin/activate
pip install --force-reinstall -r requierements.txt
```

### Problema: Errores de permisos

**Solución:**
```bash
# Dar permisos a carpetas
chmod -R 755 app/
chmod -R 755 app/static/
chmod -R 755 app/templates/
```

### Problema: Sesión expirada

**Solución:**
- Limpiar cookies del navegador
- Hacer logout e iniciar sesión nuevamente
- Verificar variable `SESSION_TIMEOUT` en configuración

### Problema: Asistencia no se guarda

**Solución:**
1. Verificar que el trabajador existe en la BD
2. Revisar formato de la hora (debe ser ISO 8601)
3. Comprobar zona horaria en `pytz.timezone('America/Bogota')`

---

## 📋 Configuración Avanzada

### Variables de Entorno
```env
# Base de Datos
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
HOST=localhost
DATABASE=confecciondb
PORT_DB=5432

# Aplicación
PORT=8001
SECRET_KEY=clave_secreta_fuerte

# Zona Horaria
TIMEZONE=America/Bogota

# Modo Debug
DEBUG=False

# Sesión
SESSION_TIMEOUT=3600  # 1 hora en segundos
```

### Esquema de Gastos Fijos
Archivo: `app/api/schemas/gastos_schema.py`

```python
class GastoSchema:
    gastos_fijos = {
        "servicios_publicos": 200000,
        "mantenimiento": 50000,
        "utiles": 30000,
        "otros": 20000
    }
    arriendo = 500000
```

### Permisos por Rol

Archivo: `app/utils/permissions.py`

```python
PERMISOS = {
    "Admin": ["*"],  # Acceso total
    "Supervisor": ["crear", "editar", "eliminar", "ver"],
    "Operario": ["ver", "crear"]  # Lectura y creación básica
}
```

---

## 📞 Soporte y Contacto

Para problemas técnicos o sugerencias:
- **Email:** desarrollo@yaidev.com
- **Teléfono:** +57 300 123 4567
- **Documentación:** Ver README.md

---

## 📄 Licencia y Términos

Este software es propietario de la empresa de confección. Todo uso no autorizado está prohibido.

---

**Última actualización:** Febrero 2026  
**Versión:** 1.0
