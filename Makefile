GO = go
GOM = GO111MODULE=on GOFLAGS=-mod=vendor $(GO)
LDFLAGS = -ldflags "-X main.gitSHA=$(shell git rev-parse HEAD) -X main.name=$(BINARY)"

BINDIR = bin
BINARY = simple-rest-api

OS := $(shell uname)

$(BINDIR)/$(BINARY): $(BINDIR)
ifeq ($(OS),Darwin)
	GOOS=darwin $(GOM) build -buildmode=pie -v -o $(BINDIR)/$(BINARY) $(LDFLAGS)
endif
ifeq ($(OS),Linux)
	GOOS=linux $(GO) build -buildmode=pie -v -o $(BINDIR)/$(BINARY) $(LDFLAGS)
endif

$(BINDIR):
	mkdir -p $(BINDIR)

build: $(BINDIR)/$(BINARY)

.PHONY: deps
deps:
	$(GOM) mod tidy
	$(GOM) mod vendor

.PHONY: clean
clean:
	$(GO) clean
	rm -f $(BINDIR)/*
