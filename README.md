# BMS Flask Starter

Minimal Python Flask app to test whether BMS Developer Portal can build and deploy a Python runtime.

**Note:** BMS Cloud Python/Flask runtime support has not yet been verified.

## Run locally

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000/ and http://127.0.0.1:5000/health

## Try deploying on BMS Developer Portal

1. Select this GitHub repository in the portal.
2. Start a build and inspect the build logs.
3. If a start command is required and Python is supported, try:

```bash
gunicorn --bind 0.0.0.0:${PORT:-5000} app:app
```

4. Test the deployed root URL and /health endpoint.
5. Redeploy to check repeatability.

## Phase 1 acceptance

- Build succeeds
- Application reaches Running/Ready
- GET / returns HTML
- GET /health returns HTTP 200 with JSON
- Redeployment succeeds

Future phases may investigate BMS Session / ProviderID and HOSxP APIs after official endpoint and authentication details are confirmed.

Do not commit credentials, real ProviderID secrets, database passwords, or patient data.
