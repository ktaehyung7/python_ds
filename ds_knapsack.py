def count_changes(coins, money):
    changes=[]
    for coin in coins:
        changes.append(money // coin)
        money %= coin
    return changes

print(count_changes([500,100,50,10,5,1],2025))  # [4,0,0,2,1,0]

def knapsack(capacity, n):
    if capacity == 0 or n ==0:
        return 0
    if size[n-1] > capacity:
        return knapsack(capacity, n-1)
    else:
        return max(value[n-1]+knapsack(capacity-size[n-1], n-1), knapsack(capacity, n-1))

size=[3,4,7,8,9]
value=[4,5,10,11,13]
print(knapsack(10, 5))


def knapsack1(capacity, n, size, value):
    if capacity == 0 or n ==0:
        return 0
    if size[n-1] > capacity:
        return knapsack1(capacity, n-1, size, value)
    else:
        return max(value[n-1]+knapsack1(capacity-size[n-1], n-1, size, value), knapsack1(capacity, n-1, size, value))

print(knapsack1(10, 5, [3,4,7,8,9], [4,5,10,11,13])) # 14

class Knapsack:
    def __init__(self, size, value):
        self.size=size
        self.value=value

    def tuck_into(self, capacity, n):
        if capacity==0 or n==0:
            return 0
        if self.size[n-1] > capacity:
            return self.tuck_into(capacity, n-1)
        else:
            return max(self.value[n-1]+self.tuck_into(capacity-self.size[n-1], n-1), self.tuck_into(capacity, n-1))

knapsack=Knapsack([3,4,7,8,9], [4,5,10,11,13])
print(knapsack.tuck_into(10,5)) #14


def knapsack2(capacity, n):
    array=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for s in range(1, capacity+1):
            if size[i-1] > s: #부피가s보다 크면
                array[i][s]=array[i-1][s]
            else:
                array[i][s]= max(value[i-1]+ array[i-1][s-size[i-1]], array[i-1][s])
            print('%2d' % array[i][s], end=' ')
        print()
    return array[n][capacity]

size=[9,3,4,7,8]
value=[13,4,5,10,11]
print(knapsack2(10,5))
