.PHONY: build run

build:
	docker build -t openbrisk/brisk-runtime-python .

run:
	docker run -it \
	-p 8080:8080 \
	openbrisk/brisk-runtime-python