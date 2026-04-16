def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
    # for record_id in record_ids:
    #  if record_id % 2 != 0:
    # here am chnging the list by controlling the indices
    i = 0
    while i < len(record_ids):
      
      if record_ids[i] % 2!=0:
       record_ids.pop(i)
      else:
          i += 1

    #   record_ids.remove(record_id)
    return record_ids
    
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]


# task two 
'''
question 1
  at index 1
question 2
when you remove an item, the following item to the removed, takes the index of the removed number 
and the loop follows that new order
part b
the pointer becomes belind of the next number because this number takes the index of the removed number
and to its logic, this value with this indices has already been removed, so it will skip it assuming 
it is the already removed number
'''

# fix 2
def clean_database(record_ids):
    cleaned = [record_id for record_id in record_ids if record_id % 2 == 0]
    return cleaned
   
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
