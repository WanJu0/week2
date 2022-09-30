# 要求一:函式與流程控制
def calculate(min, max, step):
    result=0
    for i in range(min,max+1,step):
        result=result+i
    print(result)
calculate(1,3,1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

# 要求二:Python 字典與列表
def avg(data):
    result=0
    nums=[]
    for i in range(0,len(data["employees"]),1):
        if data["employees"][i]["manager"]==False:
            result+=data["employees"][i]["salary"]
            nums.append(result)
    avg_salary=result/len(nums)
    print(int(avg_salary))

avg({
    "employees":
        [ 
            {
                "name":"John",
                "salary":30000,         
                "manager":False
            },
            {
                "name":"Bob", 
                "salary":60000, 
                "manager":True
            },
            {
                "name":"Jenny", 
                "salary":50000, 
                "manager":False
            }, 
            {
                "name":"Tony",
                "salary":40000,
                "manager":False
            } 
        ]
    }) 
# 要求三：
def func(a):
    def func_b(b,c):
        a+(b*c)
        print(a+(b*c))
        return (a+(b*c))
    return func_b

func(2)(3, 4) 
func(5)(1, -5)
func(-3)(2, 9)

# 要求四：
def maxProduct(nums):
    result=[]
    for i in range(0,len(nums)-1,1):
        for n in range(i+1,len(nums),1):
            result.append(nums[i]*nums[n])
    max=result[0]
    for j in range(1,len(result),1):
        if result[j]>max:
            max=result[j]
    print(max)
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5, -1, -2, 0])
maxProduct([-5, -2])

# 要求五：
def twoSum(nums, target):
    
    for i in range(0,len(nums)-1,1):
        for j in range(i+1,len(nums),1):
            a=nums[i]+nums[j]
            if a==target:
                result=[i,j]
    return result
result=twoSum([2, 11, 7, 15], 9)
print(result)

# 要求六
def maxZeros(nums):
    result=[]
    k=0
    for i in range(0,len(nums),1):
        if nums[i]==0:
            k=k+1
            result.append(k)
        else:
            result.append(k)
            k=0
            continue    
    # print(result)
    max=result[0]
    for j in range(1,len(result),1):
        if result[j]>max:
            max=result[j]
    print(max)              
maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])
