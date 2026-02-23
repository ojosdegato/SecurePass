# SecurePass
# 🔐 SecurePass 1.0

Generador seguro de contraseñas con interfaz gráfica desarrollado en **Python 3 + Tkinter**, diseñado para entornos Debian GNU/Linux.

SecurePass permite generar contraseñas robustas de forma configurable, con indicador visual de fortaleza en tiempo real y empaquetado nativo `.deb` para integración completa en el sistema.

---

## 📌 Características principales

- ✔ Generación criptográficamente segura (`secrets`)
- ✔ Configuración de longitud (4–15 caracteres)
- ✔ Inclusión opcional de:
  - Mayúsculas
  - Minúsculas
  - Números
  - Símbolos
- ✔ Indicador de fortaleza dinámico (barra tipo semáforo)
- ✔ Copiado al portapapeles
- ✔ Guardado en archivo `.txt`
- ✔ Integración en menú XFCE
- ✔ Icono conforme a especificación freedesktop
- ✔ Empaquetado nativo `.deb`
- ✔ Compatible con Debian 13.

---

## 🛡 Seguridad

SecurePass utiliza el módulo estándar:


Esto garantiza:

- Generación no predecible
- Seguridad criptográfica
- Uso recomendado por la documentación oficial de Python

No se utiliza `random`, evitando vulnerabilidades típicas.

---

## 🖥 Requisitos

- Debian 13 o superior
- Python 3.13+
- python3-tk
- Entorno gráfico (X11)

Instalación de dependencias:

bash

sudo apt install python3 python3-tk

📦 Instalación mediante paquete .deb

Instala la última versión:

[📥 Descargar v1.0.0 (.deb)] (https://github.com/ojosdegato/SecurePass/releases/download/SecurePass/SecurePass.deb)

Instalación deb:

$ sudo apt install ./SecurePass.deb

Si faltan dependencias:

$ sudo apt -f install

Una vez instalado, la aplicación aparecerá en:

Menú XFCE → Utilidades
🚀 Ejecución manual

Si se ejecuta sin instalar:

python3 securepass.py

📁 Estructura del paquete

SecurePass/
├── DEBIAN/
│   └── control
├── usr/
│   ├── bin/
│   │   └── securepass
│   └── share/
│       ├── applications/
│       │   └── securepass.desktop
│       └── icons/
│           └── hicolor/
│               └── 128x128/
│                   └── apps/
│                       └── securepass.png

🎨 Integración gráfica

SecurePass cumple la especificación:

freedesktop.org Desktop Entry

Tema de iconos hicolor

Integración estándar XFCE

El icono se instala en:

/usr/share/icons/hicolor/128x128/apps/
🔧 Desarrollo

Entorno recomendado:

Debian 13

Visual Studio Code

Python 3.13+


🏗 Construcción del paquete

$ dpkg-deb --build --root-owner-group SecurePass

🔏 Firma del paquete (opcional)

Firma manual:

gpg --detach-sign --armor SecurePass.deb

Verificación:

gpg --verify SecurePass.deb.asc SecurePass.deb


📚 Buenas prácticas aplicadas

Código modular orientado a objetos

Separación GUI / lógica

Permisos correctos en scripts Debian

Cumplimiento básico de Debian Policy

Iconos según estándar freedesktop

Seguridad criptográfica real

📜 Licencia

Este proyecto se distribuye bajo licencia:

GNU General Public License v3 (GPLv3)
👤 Autor

Javier Cachón Garrido
Ingeniero Técnico en Informática
Especialista en GNU/Linux y Software Libre

🧭 Roadmap futuro

Versión 1.1 → Cálculo real de entropía en bits

Versión 1.2 → Modo oscuro

Versión 2.0 → Interfaz moderna avanzada

Publicación en repositorio APT firmado

🤝 Contribuciones

Las contribuciones son bienvenidas mediante pull request o revisión técnica.

⚠️ Nota

SecurePass es un generador de contraseñas.
No almacena credenciales ni mantiene historial.

El usuario es responsable del uso adecuado de las contraseñas generadas.
