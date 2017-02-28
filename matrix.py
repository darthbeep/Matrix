import math


def print_matrix( matrix ):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			print matrix[i][j],
		print ""

def ident( matrix ):
	for i in range(len(matrix)):
		for j in range (len(matrix)):
			if i==j:
				matrix[i][j] = 1
			else:
				matrix[i][j] = 0
	return matrix

def scalar_mult( matrix, s ):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = matrix[i][j] * s


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	new = new_matrix(len(m2[0]), len(m1))
	#print_matrix(new)
	#print [len(m1), len(m1[0]), len(m2), len(m2[0])]
	for r in range(len(m1)):
		for c in range(len(m2[0])):
			for i in range(len(m2)):
				dp = m1[r][i] * m2[i][c]
				new[r][c] += dp
				#print [c, r, m1[r][i], m2[i][c], new[c][r], dp]
	return new




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
