class time():
     """hour,minute,second"""
     
     def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
     def __str__(self):
          return("%d:%d:%d"%(self.hour,self.minute,self.second))
##     def __del__(self):
##          print("Object destroyed!!!!!!")
     def __add__(self,other):
        temp=time(0,0,0)
        temp.second=self.second+other.second
        temp.minute=temp.second//60
        temp.second=temp.second%60
        temp.minute=self.minute+other.minute+temp.minute
        temp.hour=temp.minute//60
        temp.minute=temp.minute%60
        temp.hour=self.hour+other.hour+temp.hour
        return temp
start=time(2,45,60)
print("start time is:")
print(start)
duration=time(2,30,30)
print("duration is:")
print(duration)
end=time(0,0,0)
end=start+duration
print("end time is:")
print(end)
