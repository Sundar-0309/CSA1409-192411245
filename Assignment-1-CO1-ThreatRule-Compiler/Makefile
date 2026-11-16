FLEX ?= flex
CC ?= gcc
CFLAGS ?= -std=c11 -Wall -Wextra -O2
BUILD := build
SCANNER := $(BUILD)/threatrule

.PHONY: all clean test generate-inputs

all: $(SCANNER)

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/lex.yy.c: src/threatrule.l | $(BUILD)
	$(FLEX) -o $@ $<

$(SCANNER): $(BUILD)/lex.yy.c
	$(CC) $(CFLAGS) $< -o $@

generate-inputs:
	python scripts/generate_inputs.py

test: all generate-inputs
	python scripts/run_tests.py $(SCANNER)

clean:
	rm -rf $(BUILD)
