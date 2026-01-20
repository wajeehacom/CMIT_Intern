
"""
# merge sorted array
# here time complexity is (nlogn)

def merge_sorted_arrays(a,b):
    return sorted(a+b)
    

array_a = [1, 3, 5, 7]
array_b = [2, 4, 6, 8]
sorted_merged_array = merge_sorted_arrays(array_a, array_b)
print(f"Merged and Sorted Array: {sorted_merged_array}")


#_______________________
#without using sort function
# Time complexity = O(n + m) linear time complexity while i<n and j<m: iski waja se 
def merge_without(a,b):
     i,j=0,0
     n,m=len(a),len(b)
     merge_lis=[]
     while i<n and j<m:
         if a[i]<=b[j]:
             merge_lis.append(a[i])
             i+=1
         else:
             merge_lis.append(b[j])    
             j+=1
             
         
     while i<n:
          merge_lis.append(a[i])
          i+=1
     while j<m:
      merge_lis.append(a[j]) 
      j+=1   
     return merge_lis        
array_a = [1, 3, 5, 7,9]
array_b = [2, 4, 6, 8]
sorted_merged_array = merge_without(array_a, array_b)
print(f"Merged and Sorted Array: {sorted_merged_array}") 
    
    
    
    
# result O(N+M)is better than nlogn     
    


# duplication find krne     

#if we find duplicate using loop time complexity will be n2
#but we will use set , so time complexity will be o(n)
# in set add function used , or in dictionary = opetator use for adding element

def find_all_duplicate(arr):
    seen=set()
    duplicate=set()
    for i in arr:
        if i in seen:
            duplicate.add(i)
        else:
           seen.add(i)    
            
    return list(duplicate) # convert into list to print elements
    
    
arr = [2, 5, 1, 2, 3, 5, 1, 6]
all_duplicates = find_all_duplicate(arr)
print("All Duplicates:", all_duplicates)   

# find unique elemets this will return elements after removing duplicates:
def find_Unique(arr):
     return list(set(arr))
    
arr = [2, 5, 1, 2, 3, 5, 1, 6]
all_Unique = find_Unique(arr)
print("Unique Elements:", all_Unique)   




    
   


# count the freqeuncy of character 
#time complexity here o(n), for only get function time complexity is o(1)
# if we want to print the only key value we can also use the get fucntion 
def coutFrequency(s):
    frequency={}
    for ch in str(s):
        frequency[ch]=frequency.get(ch,0)+1
        
    return frequency
print("frequency of this string:",coutFrequency("Python is very easy"))   
print("frequency of this string:",coutFrequency(12222234))   


#find uniquq elements using o(n)
def find_Unique_Elements(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    
    unique_list=[]
    for num in arr:
        if freq[num]==1:
            unique_list.append(num)
    
    return unique_list

arr = [2, 5, 1, 2, 3, 5, 7]
unique = find_Unique_Elements(arr)
print("Unique Elements (appear exactly once):", unique)        




# if we given only one list, or array
# time compexity
# sorted with or without using sorted function hai
#with sorted time complexity will be o(n), nlog
#without using sorted function , time complexity will be o(n2) ,if we used bubble sort o(n2) or merge sort(nlogn)
#conclusion: so we used sorted fucntion



# reverse string
# if we used the string slicing time complexity will be o(n) 
# this is also better way to reverse the string
def reverse_string(s):
    return s[::-1]


print("reverse string:",reverse_string("hello my name is wajeeha yaseen"))




# here o(n),space complexity will also o(n)
def palindrom(s):
    return s==s[::-1]

print("palindrom string:",palindrom("madam"))

print("palindrom string:",palindrom("Hello"))

# if o(n),space complexity will also o(1)
    
#optimize method for palindrom,time complexity will be o(n),o(1)

def palindrom_without_slice(s):
    left=0
    right=len(s)-1
    while(left<right):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True    
print("check palindrom without using the slice :",palindrom_without_slice("Hello"))   


  

#factorial this is most opyimize methood ,o(n),space(1)
#if we use with the loop, same time complexity of both time or space complexity


def factorial_find(num):
    result=1
    for i in range(1,num+1):
        result*=i
        
    return result    
       
print("factorial of number:",factorial_find(4))       


# prime number:
# time o(squre root n),space o(1)
#if we checkk all n number then time complexity will be o(n) or space o(1)

#If a number n has a factor larger than its square root,
# #it must also have a factor smaller than its square root.
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print("Check Prime numbers:", is_prime(3))   



# perfect number
#time complexity o(n),space o(1)
def is_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
            
    return sum       

n=12
sum=is_perfect(n)
if sum==n:
    print("Is Perfect number")
    
else:
    print("Not Perfect NUmber")    
    
""" 

#binary search
# time complexity o(logn),space complexity o(1)
def binary_search(arr,target):
    left =0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==target:
             return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    
    return -1
  
  
arr=[ 2,3,7,7,11,15,25 ]  
target=11          
print("target Elemet",target, " at Index:",binary_search(arr,target))          