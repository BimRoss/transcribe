"""
Fetch a YouTube video transcript and write it to a plain-text file.
Reads YOUTUBE_VIDEO_URL and NAME from the environment (e.g. .env or passed when
running Docker: YOUTUBE_VIDEO_URL=... NAME=... docker compose run transcribe).
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def load_env() -> tuple[str, str]:
    """Load .env and return (video_url, name). Exits on missing/invalid values."""
    load_dotenv()
    url = os.getenv("YOUTUBE_VIDEO_URL", "").strip()
    name = os.getenv("NAME", "").strip()
    if not url:
        print("Error: YOUTUBE_VIDEO_URL is missing or empty. Set it in .env.", file=sys.stderr)
        sys.exit(1)
    if not name:
        print("Error: NAME is missing or empty. Set it in .env.", file=sys.stderr)
        sys.exit(1)
    return url, name


def video_id_from_url(url: str) -> str | None:
    """Extract YouTube video ID from watch or youtu.be URL. Returns None if not found."""
    parsed = urlparse(url)
    if "youtu.be" in parsed.netloc:
        # https://youtu.be/VIDEO_ID
        path = parsed.path.strip("/")
        if path and "/" not in path:
            return path
        return None
    if "youtube.com" in parsed.netloc or "www.youtube.com" in parsed.netloc:
        qs = parse_qs(parsed.query)
        v = qs.get("v", [])
        if v and len(v[0]) > 0:
            return v[0]
    return None


def sanitize_filename(name: str, max_len: int = 200) -> str:
    """Remove path and invalid filename characters; limit length."""
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name).strip() or "transcript"
    return safe[:max_len]


def main() -> None:
    url, name = load_env()
    vid = video_id_from_url(url)
    if not vid:
        print("Error: Could not parse video ID from YOUTUBE_VIDEO_URL.", file=sys.stderr)
        sys.exit(1)
    safe_name = sanitize_filename(name)
    out_dir = Path.cwd() / "transcriptions"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{safe_name}.txt"

    try:
        transcript = YouTubeTranscriptApi().fetch(vid)
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)
        sys.exit(1)

    formatter = TextFormatter()
    text = formatter.format_transcript(transcript)
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
