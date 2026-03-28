# Transcribe

[![GitHub stars](https://img.shields.io/github/stars/BimRoss/transcribe?style=social)](https://github.com/BimRoss/transcribe/stargazers)

Turn any YouTube video into usable text in under a minute.

`transcribe` is a Docker-first YouTube caption extractor powered by `youtube-transcript-api`. It writes clean text to `transcriptions/{NAME}.txt`.

Important: this is not Whisper. It extracts available YouTube transcript/caption text.

## Why This Exists

Speed wins.  
If you still copy/paste transcripts manually, you are spending time on low-leverage work.

## Quick Start

```bash
docker compose run --rm \
  -e YOUTUBE_VIDEO_URL='https://www.youtube.com/watch?v=...' \
  -e NAME='How To Move Ten Times Faster' \
  transcribe
```

Alternative `.env` flow:

```bash
cp .env.example .env
docker compose run --rm transcribe
```

## Output

- Directory: `transcriptions/`
- File: `{NAME}.txt`
- Format: plain text transcript for AI research and human editing

## Best Use Cases

- Founder and creator content workflows
- Competitive research from podcasts and interviews
- Internal knowledge capture from long-form videos
- Prompt-ready source files for LLM analysis

## Related Projects

- [cursor-rules](https://github.com/BimRoss/cursor-rules)

## Keywords

YouTube transcript extractor, Docker transcript tool, caption to text, AI research workflow, content repurposing pipeline.

## Support

If this saves you time every week, star the repo and share it with one builder.
