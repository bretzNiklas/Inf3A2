from Image import Image

d = Image()

d.readFromFile("Bild2.pgm")
d.writeToFile("wahre_ausgabe.pgm")
d.convolve()