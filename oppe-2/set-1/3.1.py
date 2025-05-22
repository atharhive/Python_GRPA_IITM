
def item_amount(item):
  return item['price'] * item['quantity']

def total_bill_amount(grocery_list:list)->float:
  total_amount = 0
  for item in grocery_list:
      total_amount += item_amount(item)
  return total_amount

def max_quantity_item(grocery_list:list)->str:
  return max(grocery_list, key=lambda x: x['quantity'])['name']

def sort_by_total_amount(grocery_list:list)->list:
  sorted_items = sorted(
      grocery_list,
      key = lambda x: (-item_amount(x), x['name'])
  )
  return sorted_items


def process_grocery_list(grocery_list:list, request:str):
    """Process the grocery list as per the request.

    Args:
        grocery_list (list[dict]) - A list of dictionary with the keys
            "name", "quantity" and "price", where "price" is the amount of 
            one unit of the item.
        request: (str) - A string containing one of the following request.
            - 'total_bill_amount'
            - 'max_quantity_item'
            - 'sort_by_total_amount'

    Returns: 
        The output corresponding to the request.
    """
    
    
    if request == 'total_bill_amount':
       return total_bill_amount(grocery_list)
    elif request == 'max_quantity_item':
       return max_quantity_item(grocery_list)
    elif request == 'sort_by_total_amount':
       return sort_by_total_amount(grocery_list)
    else:
       return None
    
