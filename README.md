### Sync

```bash
uv sync
```

### Run

```bash
uvicorn main:app --reload
uv run uvicorn main:app --reload
```

### Troubleshooting

```bash
uv cache clean             # Clear cache
uv sync --reinstall        # Reinstall dependencies
```

### See dependencie tree

```bash
uv tree
```

### Adds new dependencies

```bash
uv add package-name     # Add and installl to the pyproject.toml
uv remove package-name   # Remove from pyproject.toml
```

### Config .env file

- DEBUG=true
- YOUTUBE_API_KEY = sua_chave_da_api_aqui
- YOUTUBE_BASE_URL = "https://www.googleapis.com/youtube/v3"
- FRONTEND_URL = http://localhost:3000

### URLs

- API: http://localhost:8000
- Documentação: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
