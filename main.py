from Image import Image
from Kernel import Kernel
from KernelFactory import KernelFactory
from ZeroPaddingBorderBehavior import ZeroPaddingBorderBehavior

d = Image()

d.readFromFile("Bild2.pgm")
d.writeToFile("ganz_wahre_ausgabe.pgm")


bf = KernelFactory().createHorizontalPrewittKernel()

bh = ZeroPaddingBorderBehavior()

k = Kernel(bf)
d.convolve(k, bh)