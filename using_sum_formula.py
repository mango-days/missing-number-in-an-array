num = [ 6, 1, 2, 8, 3, 4, 7, 10, 5 ]
size = len ( num ) + 1
num_sum = size * ( max(num) + min(num) ) / 2
actual_sum = sum ( num )
print ( int ( num_sum - actual_sum ) )
