# Flask + MySQL con Docker - PFO2 DevOps Parte 1

## Descripción  
Aplicación web simple con Flask que muestra usuarios almacenados en una base de datos MySQL.  
Todo el entorno se ejecuta con Docker y Docker Compose para facilitar la ejecución en cualquier máquina.

---

## Requisitos previos  
- Docker  
- Docker Compose  

---

## Clonar el repositorio  
    ```bash
    git clone https://github.com/foly13/PFO2-DevOps-Parte1.git
    cd PFO2-DevOps-Parte1

---

## Instrucciones para ejecutar
Levantar los contenedores y construir las imágenes:

    ```bash
    docker-compose up --build
Esto levantará:

web: aplicación Flask en el puerto 5000

mysql: base de datos MySQL en el puerto 3306

---

## Acceder a la aplicación
http://localhost:5000

---
## Acceso a la base de datos MySQL (opcional)
Podes conectarte con MySQL Workbench u otro cliente con estas credenciales:

Host: localhost  
Puerto: 3306  
Usuario: root  
Contraseña: 123456  
Base de datos: prueba

