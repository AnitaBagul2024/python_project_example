class student():
    """roll_no, name"""
    def get_data(self):
        self.roll_no=int(input("Enter roll no:"))
        self.name=input("Enter Name:")
    def put_data(self):
        print(self.roll_no,self.name,end=" ")
class test(student):
    """marks[]"""
    def get_marks(self):
        self.marks=[float(input("Enter Marks")) for i in range(5)]
    def put_marks(self):
            for i in self.marks:
                print(i,end=" ")
class sports():
    """wt"""
    def get_sports_wt(self):
        self.wt=float(input("Enter sports weight:"))
    def dispsportswt(self):
         print(self.wt,end=" ")
         
class result(test,sports):
    """Total"""
    def cal_total(self):
        self.total=0
        for i in self.marks:
            self.total= self.total+i
        self.total=self.total+self.wt
    def display(self):
        self.cal_total()
        self.put_data()
        self.put_marks()
        self.dispsportswt()
        print(self.total)
l=[]
n=int(input("Enter number of students:"))
for i in range(0,n):
    s1=result()
    s1.get_data()
    s1.get_marks()
    s1.get_sports_wt()
    l.append(s1)
for i in l:
    i.display()
#print(l)
       
                
