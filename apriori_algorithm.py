from itertools import compress, product

transactions = {
    1 : ["wine","chips","bread","milk"],
    2 : ["wine","bread","milk"],
    3 : ["bread","milk"],
    4 : ["chips"],
    5 : ["wine","chips","bread","milk"],
    6 : ["wine","chips","milk"]
}

item_list = []

unique_items = {}
all_item = []

all_associations = {}

for key, value in transactions.items():
    for i in value:
        item_list.append(i)

for i in item_list:
    unique_items[i] = item_list.count(i)

for key, value in unique_items.items():
    all_item.append(key)

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )


all_combination = list(combinations(all_item))


tr = 1
for i in all_combination:
    all_associations[tr] = sorted(list(i))
    tr +=1


association_count = {}
for key, value in all_associations.items():
    association_count[str(value)] = 0

print(association_count)

for key, value in all_associations.items():
    print(value)
    count = 0

    for x, y in transactions.items():
        if (all(elem in y for elem in value)):
            count +=1
    
    association_count[str(value)] = count





input_string = input('Enter elements of left side:')
asc_list = input_string.split()


input_test = input('Enter elements of right side:')
test_list = input_test.split()


support_asc = association_count[str(sorted(asc_list))]
support_tst_asc = association_count[str(sorted(asc_list + test_list))]


confidence = support_tst_asc/support_asc

print(f"The Confidence of this association is: {confidence}")
