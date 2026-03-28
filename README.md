# Transcribe

Turn any YouTube video into usable text in under a minute.

`transcribe` is a Docker-first YouTube **caption extractor** powered by `youtube-transcript-api`. It writes clean output to `transcriptions/{NAME}.txt`.

Important: this is **not** Whisper and does **not** transcribe raw audio. It fetches available YouTube transcript/caption text.

## Why Use This

- Fast research and content repurposing
- Clean text files ready for AI workflows, summaries, and notes
- No local Python setup required
- Repeatable team workflow via Docker Compose

## Quick Start (Recommended)

Run from this repo directory and pass values directly into the container:

```bash
docker compose run --rm \
  -e YOUTUBE_VIDEO_URL='https://www.youtube.com/watch?v=...' \
  -e NAME='How To Move Ten Times Faster' \
  transcribe
```

Why `-e`? Because `docker-compose.yml` uses `env_file: .env`, and shell-prefixed vars can be overridden unless passed explicitly.

## Alternative: `.env` Driven

```bash
cp .env.example .env
# Set YOUTUBE_VIDEO_URL and NAME
docker compose run --rm transcribe
```

## Output

- Location: `transcriptions/`
- Filename: `{NAME}.txt`
- Format: plain text transcript for downstream AI or human editing

## Best Use Cases

- Founder/content workflows (clips, posts, threads, newsletters)
- Competitive research from talks, interviews, and podcasts
- Internal knowledge capture from long-form videos
- Prompt-ready source files for LLM analysis

## Cursor Agent Integration

If you use Cursor agents, this flow is already codified:

- Trigger rule: [`transcribe-trigger.mdc`](https://github.com/BimRoss/cursor-rules/blob/master/.cursor/rules/transcribe-trigger.mdc)
- Skill: [`transcribe-youtube/SKILL.md`](https://github.com/BimRoss/cursor-rules/blob/master/.cursor/skills/transcribe-youtube/SKILL.md)

## If This Saves You Time

Star the repo and share it with one builder who still copy-pastes transcripts manually.
