class Stack:
    maxsize=100
    items=[]
#========================== (Is Full) ===================================
    def isfull(self):
        
        if (len(self.items)==self.maxsize):
            return 1
        
        else:
            return 0
#============================ (empty) ===================================
    def isEmpty(self):
        
        if (len(self.items)==0):
            return 1
        
        else:
            return 0
#========================== (Push) ===================================    
    def push(self,x):
        
        if self.isfull():
            return None
        
        else:
            self.items.append(x)

#========================== (pop) ===================================
    def delet(self):
        
        if self.isEmpty():
            return None
        
        else:
            self.items.pop()     
#=========================== (show) ==================================
    
    def show(self):
        
        if self.isEmpty():
            return None
        
        else:
            for i in self.items:
                print(float(i))
                
#========================== (peak) ==========================================           


    def peak(self):
        
        if self.isEmpty():
            return None
        
        else:
            return self.items[-1] 
        
#=========================== (Main) ================================

number=[]
s1=Stack()

postfix=input("Pleas ENter a string: ")
splitt=postfix.split(",")

for char in splitt:
    
    number.append(char)
    
    
data="+-*/%^,"


def pasvandi(st):
    
    
    for char in st:
#======================================= (Char) =================================================            
        if char not in data:
            s1.push(char)
            
#======================================= (+) =================================================            
            
        if char=="+":
                
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    x2=(s1.peak())
                    s1.delet()
                    x=int(x2)+int(x1)
                    
                    if x!=0:
                        s1.push(x)
                    
  #======================================= (-) =================================================            
      
            
        if char=="-":
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    
                    x2=(s1.peak())
                    s1.delet()
                    
                    x=int(x2)-int(x1)
                    
                    if x!=0:
                        s1.push(x)
            
#======================================= (*) =================================================            
            
        if char=="*":
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    
                    x2=(s1.peak())
                    s1.delet()
                    
                    x=int(x2)*int(x1)
                    
                    if x!=0:
                        s1.push(x)
 
 #======================================= (%) =================================================            

                
        if char=="%":
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    
                    x2=(s1.peak())
                    s1.delet()
                    
                    x=int(x2)%int(x1)
                    
                    if x!=0:
                        s1.push(x)
           
 #======================================= (/) =================================================            
          
            
        if char=="/":
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    
                    x2=(s1.peak())
                    s1.delet()
                    
                    x=int(x2)//int(x1)
                    
                    if x!=0:
                        s1.push(x) 
               
#======================================= (^) ==========================================

        if char=="^":
            if (not(s1.isEmpty())):
                
                if(len(s1.items)>1):
            
                
                    x1=(s1.peak())
                    s1.delet()
                    
                    x2=(s1.peak())
                    s1.delet()
                    
                    x=int(x2)**int(x1)
                    
                    if x!=0:
                        s1.push(x)
                   
#========================= out put ============================                
pasvandi(number)
s1.show()

#========================= test =================================
#test 1:
#input  -----> 10,2,+,7,1,-,4,^,/,8,+
#output -----> 8.0

#test 2:
#input  -----> 3,2,^,4,*,6,/,12,8,-,+
#output -----> 10.0

#test 3:
#input  -----> 5,6,2,+,*,12,4,/,-
#output -----> 37.0

#test 4:
#input  -----> 5,9,+,2,*,8,-
#output -----> 20.0
