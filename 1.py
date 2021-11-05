N=int(input("Enter a number:"))
even_sum=0
avarage_even=0
ood_sum=0
for i in range(1,N+1):
    if i%2==0:

        even_sum+=i
        avarage_even=even_sum/int(N)


    else:
        ood_sum+=i



print("avarage of even numbers", avarage_even)
print("sum of odd", ood_sum)