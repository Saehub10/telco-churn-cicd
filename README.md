# Práctica 8 — CI/CD con GitHub Actions

Proyecto ejecutable de FastAPI, SVM preentrenado con datos sintéticos, pytest, Docker y publicación a GHCR.

## Ejecutar localmente (CMD)
```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m pytest -v
python -m uvicorn app.main:app --reload
```
Abrir http://127.0.0.1:8000/docs.

## Publicar
Crear un repositorio vacío en GitHub y ejecutar (cambia TU_USUARIO):
```bat
git init -b main
git add .
git commit -m "Proyecto inicial CI CD"
git remote add origin https://github.com/TU_USUARIO/telco-churn-cicd.git
git push -u origin main
```
En Actions verás el job de pruebas y, en push a main, el build y publicación a GHCR. Pull Requests solo ejecutan pruebas. `GITHUB_TOKEN` lo proporciona GitHub Actions.

## Provocar fallo
Cambiar temporalmente el status esperado de 200 a 404 en `tests/test_api.py`, commit y push. Verificar que falla `test` y se omite `docker`. Restaurar 200 y publicar otra vez.

## Ejecutar imagen publicada
```bat
docker pull ghcr.io/TU_USUARIO/telco-churn-cicd:latest
docker run --rm -p 8000:8000 ghcr.io/TU_USUARIO/telco-churn-cicd:latest
```
El paquete debe ser público o debes autenticarte en GHCR. Este workflow publica la imagen; no realiza despliegue automático a producción.

**Nota:** el modelo se entrenó con datos sintéticos solo para hacer reproducible la práctica. No utilizar en decisiones reales.

Proyecto Telco Customer Churn con integración continua.