# -*- coding: utf-8 -*-

def run():
	list1 = ['bandeja paisa', 'color crema', 22, 1969]
	list2 = [50, 100, 200, 500, 1000]
	list3 = ["bombero", "médico", "enfermero", "rescatista"]
	print("list1 = " + str(list1))
	print("list2 = " + str(list2))
	print("list3 = " + str(list3))

	print("\nAccessing values in lists:")
	print("list1[1] = " + list1[1])
	print("list2[1:3] = " + str(list2[1:3]))

	print("\nUpdating lists:")
	list1[0] = 'cuy'
	print("list1[0] = 'cuy' then list1[0] = " + list1[0])

	print("\nConcatenation:")
	print("list1 + list3 = " + str(list1+list3))

	print("\nRepetition:")
	list4 = ['wave'] * 4
	print("list4 = ['wave'] * 4 => " + str(list4))

	print("\nMembership:")
	print("300 in list2 => " + str(300 in list2))
	print("'bombero' in list3 => " + str('bombero' in list3))

	print("\nSlicing:")
	print("list2[1:] => " + str(list2[1:]))
	print("list2[:1] => " + str(list2[:1]))
	print("list2[-1:] => " + str(list2[-1:]))
	print("list2[:-1] => " + str(list2[:-1]))
	print("list2[::-1] => " + str(list2[::-1]))
	print("[ <first element to include> : <first element to exclude> : <step> ]")
	
	print("\nBuilt-in List Functions:")
	print("len(list2) = " + str(len(list2)))
	print("max(list2) = " + str(max(list2)))
	print("min(list2) = " + str(min(list2)))

	print("\nBuilt-in List Methods:")
	print("Append, Count, Index, Reverse, Sort")
	list3.pop(1)
	print("Pop/Remove:\nlist3.pop(1) = " + str(list3))

if __name__ == '__main__':
    run()