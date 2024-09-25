# ihc-reconocimiento-voz

## Proyecto de IHC para moverse en un grid con comandos de voz

### Para correr el proyecto:

1. **Asegúrate de tener Python y la dependencia pip instalados**.

2. **Instala tu entorno virtual** con el siguiente comando:
   ```bash
   python -m venv venv
   ```

3. **Inicializa el entorno virtual**. En Windows, usa el siguiente comando:
   ```bash
   .\venv\Scripts\activate
   ```
   **NOTA**: Si en Windows te sale un error mencionando que no se pueden correr scripts en el sistema, ingresa el siguiente comando en una terminal PowerShell con derechos de administrador:
   ```bash
   Set-ExecutionPolicy Restricted -Scope CurrentUser
   ```
   Para abrir PowerShell con derechos de administrador, presiona `Windows + X` y selecciona "Windows PowerShell (Admin)" o "Terminal (Admin)". Una vez realizado esto, inicializa el entorno virtual como ya se mencionó en este punto.

   Tu terminal debería tener un `(venv)` añadido al inicio del path del directorio:
   ```plaintext
   (venv) C:\path\
   ```

4. **Una vez inicializado el entorno virtual, instala el proyecto** con el siguiente comando:
   ```bash
   pip install -e .
   ```
   *(Nótese el punto, tiene que ser justo desde el root del directorio)*

5. **Una vez instalado el proyecto**, lo puedes correr con el siguiente comando:
   ```bash
   run_ihc_app
   ```