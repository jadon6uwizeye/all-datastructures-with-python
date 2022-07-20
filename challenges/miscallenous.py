import math
max = 4
ar = [1,2,3,4,5,6,7]
a = len(ar)
print(math.ceil(a/4))

ar1 = []
ar2 = [] 
ar3 = []

for num in ar:
    if len(ar1) == len(ar2) == len(ar3):
        ar1.append(num)
    elif len(ar2) == len(ar3):
        ar2.append(num)
    else:
        ar3.append(num)
        
print(ar1)
print(ar2)
print(ar3)


# Challenge:
_list = User.objects.values_list('id',flat=True).order_by('-created_on')[:100]

User.objects.filter(id__in=list(u_list)).delete()