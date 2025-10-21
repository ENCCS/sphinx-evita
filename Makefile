.PHONY: lock tests docs

# Export uv dependencies to pylock.toml format
lock:
	uv export --format pylock.toml --output-file pylock.toml

tests:
	uv run pytest

docs:
	EVITA=1 uv run --group docs --no-dev make -C docs livehtml