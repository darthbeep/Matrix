from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

#Showing off math stuff
print "scalar_mult and ident:"
m1 = ident(new_matrix())
print_matrix(m1)
print " * 2 ="
scalar_mult(m1, 2)
print_matrix(m1)

print "\nmatrix_mult:"
m2 = [[5, 3], [-2, 1], [4, 1]]
m3 = [[-2, -1], [5, 0]]
print_matrix(m2)
print " * "
print_matrix(m3)
print " = "
print_matrix(matrix_mult(m2, m3))

for x in range(0, 250, 1):
	add_edge(matrix, 100-x, 500, 1, 500, 100+x , 1)
	add_edge(matrix, 100+x, 500, 1, 500, 100-x , 1)
	add_edge(matrix, x/3, 0, 1, 300, 300, 1)
	add_edge(matrix, 0, x/3, 1, 300, 300, 1)

#print_matrix(matrix)
draw_lines( matrix, screen, color )
display(screen)
