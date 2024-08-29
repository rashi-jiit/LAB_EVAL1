print ("Shopping list")
    
def add_item(shop_list,item: str):
    print("ADDING A NEW ITEM TO THE SHOPPING LIST")
    if item not in shop_list:
        shop_list.append(item)
        print("item added")
        print("-------------------------")
        for sl in shop_list:
            print(sl)
    else :
        print("Item already exist")

def remove_item(shop_list,item: str):
    print("REMOVING AN ITEM")
    if item not in shop_list:
        print("Can't be removed, as it is not in the list")
    else :
        shop_list.remove(item)
        print("Item removed")
        print("-------------------------")
        for sl in shop_list:
            print(sl)
    
def search_item(shop_list,item: str):
    print("SEARCHING AN ITEM IN LIST")
    if item in shop_list:
        print("True")
    else :
        print("False")
    
def display_list(shop_list):
    for sl in shop_list:
        print(sl)


shopping_list = []
size=int(input("Size of list: "))
for i in range(0,size):
    item=input("Item name: ")
    shopping_list.append(item)

print("-------------------------")
display_list(shopping_list)
print("-------------------------")
add_i = input("Enter the item to be added: ")
print("-------------------------")
add_item(shopping_list,add_i)
print("-------------------------")
remove_i = input("Enter the item to be remove: ")
print("-------------------------")
remove_item (shopping_list,remove_i)
print("-------------------------")
search_i = input("Enter the item to be searched: ")
search_item(shopping_list,search_i)
print("-------------------------")
display_list(shopping_list)