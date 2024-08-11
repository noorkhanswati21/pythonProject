classroom_stock={
"pencils":30,
"note book":20,
"eraser":15
}
def disply_stock():
   print("current classroom :")
   for item,quantity in classroom_stock.items():
      print(f"{item}:{quantity}")
disply_stock()
def add_item(item,quantity):
   if item in classroom_stock:
      classroom_stock[item]+=quantity
   else:
      classroom_stock[item]=quantity
add_item
def remove_item(item,quantity):
   if item in classroom_stock:
      if classroom_stock[item]>=quantity:
         classroom_stock[item]-=quantity
      else:
         print("Not enough stock to remove.")
   else:
      print("item not found in stock.")
remove_item
#Main program
disply_stock()
add_item("markers",10)
remove_item("pencil",5)
disply_stock()



     
