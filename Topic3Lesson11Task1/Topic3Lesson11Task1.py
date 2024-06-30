arr = []

def faktorial(i): 
    if i == 1:
        return 1 
    else: 
        return i * faktorial(i - 1)
        
num = int(input('Введите число: '))

for i in range(num):
    arr.append(faktorial(num - i))
    
print("Обратная последовательность факториалов факториала числа:", num) 
print(arr)  