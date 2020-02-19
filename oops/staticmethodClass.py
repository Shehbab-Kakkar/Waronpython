#!/usr/bin/python
#Filname is staticmethodClass.py
class Student:
      def __init__(self,name,school):
          self.name = name
          self.school = school
          self.marks = []
      def average(self):
          return sum(self.marks) / len(self.marks)
    
      @staticmethod
 #     @classmethod
      def go_to_school(): #(cls) for class 
          print("I am going to school")

mohan = Student("Mohan","MIT")
gurinder = Student("Gurinder","NWIET")
mohan.marks.append(56)
mohan.marks.append(70)
Student.go_to_school()
