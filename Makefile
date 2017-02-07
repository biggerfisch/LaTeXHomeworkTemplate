TEX = xelatex -shell-escape -halt-on-error

all: hw.pdf

hw.pdf: hw.tex *.out *.png
	$(TEX) hw.tex # Need to run twice due to references
	$(TEX) hw.tex && open hw.pdf

# Run every python script then build the pdf
%.out %.png: %.py
	./run_all.bash

clean:
	rm -f hw.pdf hw.aux hw.log hw.toc
	rm -rf _minted-hw
	rm -f *.out
	rm -f *.png

.PHONY: all clean
ifndef VERBOSE
	.SILENT:
endif
