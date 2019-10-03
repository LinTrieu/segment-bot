_NAME=segment-bot

build:
	docker build -t $(_NAME) -f ./infrastructure/Dockerfile .
run:
	docker run --rm -it --read-only --mount type=bind,src=$(HOME)/.aws,dst=/root/.aws $(_NAME)