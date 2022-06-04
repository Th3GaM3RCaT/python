import matplotlib.pyplot as plt
def scale(im, nR, nC):
    number_rows = len(im)     # source number of rows 
    number_columns = len(im[0])  # source number of columns 
    return [[ im[int(number_rows * r / nR)][int(number_columns * c / nC)]  
                 for c in range(nC)] for r in range(nR)]


im = plt.imread('image_241491_eightbit.jpg')
res = scale(im, 30, 30)