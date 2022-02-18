def step_to_transform(array):
    B = []
    flag = True
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            k = i + j
            if k == j:
                max = array[0]
            else: 
                max = 0
            for x in array[j:k]:
                if max <= x:
                    max = x
            B.append(max)
    return B



def TransformTransform(A,N):
    step_1 = step_to_transform(A)
    step_2 = step_to_transform(step_1)
    summ = 0
    for i in range(len(step_2)):
        summ += step_2[i]
        
    if summ % 2 ==0:
        return True
    else:
        return False