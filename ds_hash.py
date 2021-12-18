class Hashtable:
    def __init__(self):
        self.table=[None for _ in range(139)]
        
    def simple_hash(self, name):
        ord_sum=0
        for letter in name:
            ord_sum +=ord(letter)
        return ord_sum % len(self.table)
    
    def put(self, name, num):
        self.table[self.better_hash(name)] =num
        
    def show(self):
        for idx, value in enumerate(self.table):
            if value:
                print(idx, value)
                
    def find(self, name):
        return self.table[self.simple_hash(name)]
    
    def better_hash(self, name):
        honer=37
        ord_sum=0
        for letter in name:
            ord_sum=ord_sum * honer + ord(letter)
        return ord_sum % len(self.table)
    
    
a=Hashtable()
a.put('Kim', 7458)
a.put('John', 8569)
a.put('Raymond', 1598)
a.put('Clayton', 7532)
a.show()