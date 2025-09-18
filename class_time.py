class time():
    """hour,minute,second"""
    def print_time(self):
        print("%d:%d:%d"%(self.hour,self.minute,self.second))
    def get_time(self):
        self.hour=int(input("Enter hour"))
        self.minute=int(input("Enter minute"))
        self.second=int(input("Enter second"))

    def add(self,other):
        temp=time()
        temp.second=self.second+other.second
        temp.minute=temp.second//60
        temp.second=temp.second%60
        temp.minute=self.minute+other.minute+temp.minute
        temp.hour=temp.minute//60
        temp.minute=temp.minute%60
        temp.hour=self.hour+other.hour+temp.hour
        return temp
        
start=time()
print("Enter start time:")
start.get_time()
print("start time is:")
start.print_time()

duration=time()
print("Enter duration:")
duration.get_time()
print("Duration is:")
duration.print_time()

end=time()
end=start.add(duration)
end=time.add(start,duration)
print("End Time is:")
end.print_time()



    
