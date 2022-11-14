from Image import Image
from Kernel import Kernel
from KernelFactory import KernelFactory
from ZeroPaddingBorderBehavior import ZeroPaddingBorderBehavior
from ClampingBorderBehavior import ClampingPaddingBorderBehavior


def aufgabe1():
    d = Image()
    d.readFromFile("Bild1.pgm")


    zero_p_bb = ZeroPaddingBorderBehavior()
    clamping_p_bb = ClampingPaddingBorderBehavior()

    horizontal_pk = Kernel(KernelFactory().createHorizontalPrewittKernel())
    vertical_pk = Kernel(KernelFactory().createVerticalPrewittKernel())

    d.convolve(horizontal_pk, zero_p_bb, "./images/Ergebnis1-horizontal(zero-padding).pgm")
    d.convolve(horizontal_pk, clamping_p_bb, "./images/Ergebnis1-horizontal(clamping-padding).pgm")

    d.convolve(vertical_pk, zero_p_bb, "./images/Ergebnis1-vertical(zero-padding).pgm")
    d.convolve(vertical_pk, clamping_p_bb, "./images/Ergebnis1-vertical(clamping-padding).pgm")

def aufgabe2():
    zero_p_bb = ZeroPaddingBorderBehavior()
    clamping_p_bb = ClampingPaddingBorderBehavior()

    e = Image()
    e.readFromFile("Bild2.pgm")
    boxfilter_3 = Kernel(KernelFactory().createBoxFilter(1))
    boxfilter_11 = Kernel(KernelFactory().createBoxFilter(5))
    boxfilter_27 = Kernel(KernelFactory().createBoxFilter(13))
    e.convolve(boxfilter_3, zero_p_bb, "./images/Ergebnis2-3(zero-bb).pgm")
    e.convolve(boxfilter_3, clamping_p_bb, "./images/Ergebnis2-3(clamping_p_bb).pgm")
    e.convolve(boxfilter_11, clamping_p_bb, "./images/Ergebnis2-11.pgm")
    e.convolve(boxfilter_27, zero_p_bb, "./images/Ergebnis2-27.pgm")



if __name__ == "__main__":
    aufgabe1()
    aufgabe2()
