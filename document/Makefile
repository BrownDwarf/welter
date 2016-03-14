all: ms.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	bibtex ms
	pdflatex ms
	pdflatex ms
	mv ms.pdf final/
	cp ms.tex final/
	rm -rf *Notes.bib
	rm -rf *.log
	rm -rf *.bbl
	rm -rf *.aux
	rm -rf *.blg
	rm -rf *.dvi
