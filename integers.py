'''
Problem statement:  Finding the largest unsigned,max positive number and the max negative number for 1, 2,4 and 8 bytes.
'''

Table = "{:<6} {:<22} {:<22} {:<22}" #format for creating a table
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for x in range(0, 4):
	n= pow(2,x) 
	no_of_bits = n*8  #finding the number of bits in each data t
	largest_no = pow(2,no_of_bits) - 1
	max_positive = pow(2,no_of_bits - 1)-1
	max_negative = pow(2,no_of_bits-1) * -1
	print(Table.format(n,largest_no,max_negative,max_positive ))# printing the values in the table format

	



