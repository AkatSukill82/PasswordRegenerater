# Notes

- `Passw.py`: CLI generator (writes to `~/Desktop/mots_de_passe.txt`). `web.py`: stdlib web UI on port 8000 (mapped to 3000), no dependencies.
- No live reload: after editing Python files run `docker compose -f docker-compose.base44.yml restart web`.
- Verify: `curl localhost:3000/?longueur=24` returns a page with a generated password.
