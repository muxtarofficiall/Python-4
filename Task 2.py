 #2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
 #input:[-1,1,2,2,6,7,7,'say']

from collections import Counter

# Funksiya təkrarlanmayan elementləri qaytarır
def get_unique_elements(lst):
    # Siyahıdakı hər bir elementin sayını hesablamaq
    counts = Counter(lst)
    
    # Təkrarlanmayan elementləri seçmək
    unique_elements = [item for item, count in counts.items() if count == 1]
    
    return unique_elements

# Test siyahısı
input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']

# Funksiyanı çağırmaq
unique_elements = get_unique_elements(input_list)

print("Təkrarlanmayan elementlər:", unique_elements)
