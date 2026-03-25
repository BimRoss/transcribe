# Transcribe

Docker-based YouTube **caption** fetcher (via `youtube-transcript-api`). Output: `transcriptions/{NAME}.txt`. Not Whisper / not audio transcription.

## Option 1: Pass URL and name (recommended for one-offs)

Because `docker-compose.yml` uses `env_file: .env`, variables in `.env` can override a bare shell `VAR=value docker compose run`. **Pass values into the container with `-e`:**

```bash
docker compose run --rm \
  -e YOUTUBE_VIDEO_URL='https://www.youtube.com/watch?v=...' \
  -e NAME='My Video Title' \
  transcribe
```

Run from this directory. Use `--rm` so the one-shot container is removed after exit.

## Option 2: Use .env

```bash
cp .env.example .env
# Edit .env: set YOUTUBE_VIDEO_URL and NAME
docker compose run --rm transcribe
```

## Cursor agents

Usage for agents lives in the **cursor-rules** repo: `.cursor/rules/transcribe-trigger.mdc` and `.cursor/skills/transcribe-youtube/SKILL.md`.
