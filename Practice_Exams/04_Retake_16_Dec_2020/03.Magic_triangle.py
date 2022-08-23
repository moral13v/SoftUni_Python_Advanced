def get_magic_triangle(param):

    magic_triangle = [[1], [1, 1]]

    for i in range(2, param):
        magic_triangle.append(list('N' * (i + 1)))
        for j in range(i+1):
            if j == 0 or i == j:
                magic_triangle[i][j] = 1
            else:
                magic_triangle[i][j] = magic_triangle[i-1][j-1] + magic_triangle[i-1][j]

    return magic_triangle

get_magic_triangle(5)

