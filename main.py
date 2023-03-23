import turtle



class user:
  def __init__(self,username,password):
    self.username = username
    self.password = password
  def ask_check (self):
    check1 = False
    check2 = False
    while(check1 == False or check2 == False):
      check1 = False
      check2 = False
      print("wrong input!!!")
      self.password = input("try again\n")
      for x in self.password:
        if x.isdigit():
          check1 = True
        if x.isupper():
          check2 = True

user1 = user(input("enter your user name\n"),input("enter your password\n(must have at least 1 number and one big letter for extra security)\n") ) 
user1.ask_check()

class pictures:
  def __init__(self,image):
    self.image = image
  def addImage(self):
    turtle.clearscreen()
    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.addshape(self.image)
    tr.shape(self.image)
    
Rich_dad_image = pictures('Rich.gif')
wimpy_kid_image = pictures('wimpy_kid.gif')
harry_poter_image = pictures('harry_poter.gif')
iphone_11_image = pictures('iphone_11.gif')
macbook_image = pictures('macbook.gif')
shawarma_image = pictures('shawarma.gif')
kfc_image = pictures('Kfc.gif')



class Book:
  def __init__(self, author, category, time, price):
    self.author = author
    self.category = category
    self.time = time
    self.price = price



Rich_dad = Book(" Robert_T"," how to became rich"," 1 day from ordering"," 28$")

Diary_of_wimpy_kid = Book(" Jeff kinney"," story of a middle school teenager's life"," 3 days from ordering"," 12$")

Harry_poter_FullSeries = Book(" J.K rowling"," imagination"," 5 days from ordering", " 100$")


class Electricities:
  def __init__(self,describtion,time,price):
    self.describtion = describtion
    self.time = time
    self.price = price

Macbook_Air = Electricities(" a very uesfull,light and anti virus laptop"," from 2-5 weeks"," 999$")

Iphone_11_pro = Electricities(" black + has 3 cameras ","about a month"," 700$")



class Delivery:
  def __init__(self,the_meal,time,price):
    self.the_meal = the_meal
    self.time = time
    self. price = price

Kfc = Delivery(" 8 spicy chicken wings with chips with Fanta"," 20 min"," 9$")

Shawarma = Delivery(" Shawarma in Lafa with salads and so good Tahini with graps juice (the best)"," 30 min"," 15$")

  
def home_page():
  turtle.clearscreen()
  turtle.bgcolor("green")
  ts = turtle.Screen()
  ts.setup(400,250)
  turtle.setposition(-150,60)
  turtle.write("Welcome to amazon 2.0!\n(home page)",font=('Ariel',15,'bold'))
  print("\n"*100)
  print("this is a website were you can buy:\n-books\n-electrisities\n-meals with free dilivery\n\n")
  print("press 1 for books\n2 for electrisities\n3 for meals\n4 to stop")
  
  
  

       

def book_page():
  turtle.clearscreen()
  turtle.bgcolor("blue")
  bp = turtle.Screen()
  bp.setup(400,250)
  turtle.setposition(-150,60)
  turtle.write("welcom to my BOOK STORE",font=('Ariel',15,'bold'))
  print("\n"*100)
  print("here we have 3 different books, choose one that you would like to see its descriptions:\n\n- press 1 for (Rich dad poor dad) \n- press 2 for (Diary of a wimpy kid)\n- press 3 for (harry poter full series)\n- press 4 to go back")

def electrisities_page():
  turtle.clearscreen()
  turtle.bgcolor("purple")
  ep = turtle.Screen()
  ep.setup(400,250)
  turtle.setposition(-150,60)
  turtle.write("welcom to my ELECTRISITIES STORE",font=('Ariel',15,'bold'))   
  print("\n"*100)
  print("here we have 2 different options, choose one that you would like to see its descriptions:\n\n- press 1 for (Macbook air)\n- press 2 for(iphone 11 pro)\n- press 3 to go back")
  
def dilivery_page():
  turtle.clearscreen()
  turtle.bgcolor("orange")
  dp = turtle.Screen()
  dp.setup(400,250)
  turtle.setposition(-150,60)
  turtle.write("welcom to my DILIVERY STORE",font=('Ariel',15,'bold'))
  print("\n"*100)
  print("here we have 2 different options, choose one that you would like to see its descriptions:\n\n- press 1 for (shawarma meal)\n- press 2 for (KFC meal)\n- press 3 to go back")

s = True
z = True
y = True
w = True
while(y==True):
  s = True
  z = True
  y = True
  w = True

  home_page()
  step_1 = int(input())
  
  if (step_1 == 1):
    while(z==True):
       print("\n"*100)
       book_page()
      
       step_2 =int(input())
      
       if(step_2 == 1):
         
         Rich_dad_image.addImage()
         
         print("\n"*100)
         print("author - ",Rich_dad.author,"\ncategory - ",Rich_dad.category,"\ndilivery time - ",Rich_dad.time,"\nprice - ",Rich_dad.price)
         print("--------------------------------------------\n")
         step_3 = int(input("press 1 to buy\npress 2 to back\n"))
         if(step_3 == 1):
           step_4 = int(input("enter your pay pal number\n"))
           print("thank you for your purchase!!!")
           input('Press enter to continue')
         elif(step_3 ==2):
           z = True
         y=False
         
       elif(step_2 == 2):
         wimpy_kid_image.addImage()
         
         print("\n"*100)
         print("author - ",Diary_of_wimpy_kid.author,"\ncategory - ",Diary_of_wimpy_kid.category,"\ndilivery time - ",Diary_of_wimpy_kid.time,"\nprice - ",Diary_of_wimpy_kid.price)
         print("--------------------------------------------\n")
         step_3 = int(input("press 1 to buy\npress 2 to back\n"))
         if(step_3 == 1):
           step_4 = int(input("enter your pay pal number\n"))
           print("thank you for your purchase!!!")
           input('Press enter to continue')
         elif(step_3 ==2):
           z = True
         y=False
         
       elif(step_2 == 3):

         harry_poter_image.addImage()
         
         print("\n"*100)
         print("author - ",Harry_poter_FullSeries.author,"\ncategory - ",Harry_poter_FullSeries.category,"\ndilivery time - ",Harry_poter_FullSeries.time,"\nprice - ",Harry_poter_FullSeries.price)
         print("--------------------------------------------\n")
         step_3 = int(input("press 1 to buy\npress 2 to back\n"))
         if(step_3 == 1):
           step_4 = int(input("enter your pay pal number\n"))
           print("thank you for your purchase!!!")
           input('Press enter to continue')
         elif(step_3 ==2):
           z = True
         
         y=False
         
       elif(step_2 == 4):
         z = False
         y = True
         
       else:
          print("wrong input!!!")
          z = False
          y=False
         
  elif (step_1 == 2):
    while(w==True):
      
      print("\n"*100)
      electrisities_page()
      step_2 =int(input())
      
      if(step_2==1):

        macbook_image.addImage()
        
        print("\n"*100)
        print("describtion -",Macbook_Air .describtion,"\ntime -",Macbook_Air .time,"\nprice -",Macbook_Air .price)
        print("--------------------------------------------\n")
        step_3 = int(input("press 1 to buy\npress 2 to back\n"))
        if(step_3 == 1):
          step_4 = int(input("enter your pay pal number\n"))
          print("thank you for your purchase!!!")
          input('Press enter to continue')
        elif(step_3 ==2):
          w = True
        
        y=False
        
      elif(step_2==2):

       iphone_11_image.addImage()
        
       print("\n"*100)
       print("describtion -",Iphone_11_pro.describtion,"\ntime -",Iphone_11_pro.time,"\nprice -",Iphone_11_pro.price) 
       print("--------------------------------------------\n")
       step_3 = int(input("press 1 to buy\npress 2 to back\n"))
       if(step_3 == 1):
         step_4 = int(input("enter your pay pal number\n"))
         print("thank you for your purchase!!!")
         input('Press enter to continue')
         
       elif(step_3 ==2):
         w = True
        
       y=False
        
      elif(step_2==3):
        w = False
        y = True
      else:
        print("wrong input!!!")
        w = False
        y=False
      
  elif (step_1 == 3):
    while(s == True):
      
      print("\n"*100)
      dilivery_page()
      
      step_2 =int(input())
      if(step_2==1):

        shawarma_image.addImage()
        
        print("\n"*100)
        print("the meal -",Shawarma.the_meal,"\ntime -",Shawarma.time,"\nprice -",Shawarma.price)
        print("--------------------------------------------\n")
        step_3 = int(input("press 1 to buy\npress 2 to back\n"))
        if(step_3 == 1):
          step_4 = int(input("enter your pay pal number\n"))
          print("thank you for your purchase!!!")
          input('Press enter to continue')
        elif(step_3 ==2):
          z = True
        
        y=False
      elif(step_2==2):

       kfc_image.addImage()
        
       print("\n"*100)
       print("the meal -",Kfc.the_meal,"\ntime -",Kfc.time,"\nprice -",Kfc.price)
       print("--------------------------------------------\n")
       step_3 = int(input("press 1 to buy\npress 2 to back\n"))
       if(step_3 == 1):
         step_4 = int(input("enter your pay pal number\n"))
         print("thank you for your purchase!!!")
         input('Press enter to continue')
       elif(step_3 ==2):
         z = True
        
       y=False
        
      elif(step_2==3):
        s = False
        y = True
      else:
        print("wrong input!!!")
        s = False
        y=False

  elif(step_1==4):
    print("bye bye have a nice day!")
    y=False
  
  else:
    print("wrong input!!!")
    y=False


