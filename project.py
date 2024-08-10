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
   if item in classroom_stocks:
      classroom_stock[item]+=quantity
   else:
      classroom_stock[item]=quantity
add_item(item,quantity)

