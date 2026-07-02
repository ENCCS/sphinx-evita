.PHONY: lock tests docs

CSS_FILES := furo_ext_lesson.css
CSS_BUILD_DIR := src/sphinx_evita/_static
CSS_OUT := $(addprefix $(CSS_BUILD_DIR)/,$(CSS_FILES))

# Export uv dependencies to pylock.toml format
lock:
	uv export --format pylock.toml --output-file pylock.toml

tests:
	EVITA=1 uv run pytest
	EVITA=1 SPHINXOPTS='-W' uv run --group docs --no-dev make -C docs xml

docs:
	EVITA=1 uv run --group docs --no-dev make -C docs livehtml

clean:
	uv run make -C docs clean
	rm -f $(CSS_OUT)
	rm -rf dist

$(CSS_BUILD_DIR)/%.css: css/%.css
	esbuild $< --target=chrome88,edge88,firefox78,safari14 --outfile=$@

esbuild: $(CSS_OUT)

build: esbuild
	uv build
