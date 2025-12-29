.PHONY: doctor sync-filaments preview bundle

doctor:
	python3 -m src.app.main doctor

sync-filaments:
	python3 -m src.tools.filamentcolors_sync

preview:
	@if [ -z "$(IMG)" ]; then \
		echo "Usage: make preview IMG=path/to/image.png [N_COLORS=4] [BLEND_DEPTH=1.0]"; \
		exit 2; \
	fi
	python3 -m src.app.main preview --in "$(IMG)" --debug preview_out \
		$(if $(N_COLORS),--n-colors $(N_COLORS),) \
		$(if $(BLEND_DEPTH),--blend-depth $(BLEND_DEPTH),)

bundle:
	@if [ -z "$(IMG)" ] || [ -z "$(OUT)" ]; then \
		echo "Usage: make bundle IMG=path/to/image.png OUT=output.zip"; \
		exit 2; \
	fi
	python3 -m src.app.main bundle --in "$(IMG)" --out "$(OUT)"
