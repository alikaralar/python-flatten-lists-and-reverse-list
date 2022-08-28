"""
#########################################################
# Kodu Yorum satırındaki gibi de yazabiliriz. Ancak     #
# İç içe değilde düz bir liste verince listeyi tersine  #
# çeviremez ve hata mesajı gösterir!!                   #
# github.com/alikaralar                                 #
#########################################################

l=[[1, 2], [3, 4], [5, 6, 7]]
def reverse_list(girdi):
    for i in girdi:
        i.reverse()
    girdi.reverse()
    return girdi
print(reverse_list(l))        

"""

l=[[1, 2], [3, 4], [5, 6, 7]]
l2=[1,2,3,4]

def reverse_list(girdi):
    for i in girdi:
        if isinstance(i,list):
            i.reverse()
    girdi.reverse()    
    return girdi


print(reverse_list(l))     
print(reverse_list(l2))
# output--> [[7, 6, 5], [4, 3], [2, 1]]
# output--> [4, 3, 2, 1]