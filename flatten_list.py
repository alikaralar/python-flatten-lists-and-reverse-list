l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flattenNestedList(nestedList):
    # Boş bir liste oluşturuyoruz.
    flatList = [] 
    # For döngüsü ile, iç-içe geçmiş her bir listenin elemanını tek tek element'e atıyoruz.
    for element in nestedList: 
        if isinstance(element, list):
            #Eğer element adını verdiğimiz döngü değişkeni bir liste ise,
            # flattenNestedList fonksiyonuna işlemesi için tekrar veriyoruz.
            flatList.extend(flattenNestedList(element))
        else:
            # Element dediğmiz şey bir liste değilse, Önceden tanımladığımız boş listeye ekliyoruz.
            flatList.append(element)    
    return flatList
print(flattenNestedList(l))    