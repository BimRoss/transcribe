# Transcribe

Docker-based YouTube transcript fetcher. Output: `transcriptions/{NAME}.txt`.

## Option 1: Pass URL and name (no .env needed)

```bash
YOUTUBE_VIDEO_URL='https://www.youtube.com/watch?v=...' NAME='My Video Title' docker compose run transcribe
```

## Option 2: Use .env

```bash
cp .env.example .env
# Edit .env: set YOUTUBE_VIDEO_URL and NAME
docker compose run transcribe
```

Env vars passed on the command line override `.env`, so one-off runs can use Option 1 without editing `.env`.
