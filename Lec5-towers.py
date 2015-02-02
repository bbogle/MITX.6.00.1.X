<<<<<<< HEAD
#encoding=utf-8
__author__ = "bbogle"
=======
>>>>>>> 6cad97a5cd3413c9a4f8c5dbfa85acdb6945bb56

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

<<<<<<< HEAD
=======

>>>>>>> 6cad97a5cd3413c9a4f8c5dbfa85acdb6945bb56
Towers(4, 'f','t','s')