.PHONY: lock

# Export uv dependencies to pylock.toml format
lock:
	uv export --format pylock.toml --output-file pylock.toml