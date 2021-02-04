from skyscrapers import check_skyscrapers

board = ["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"]

if __name__ == "__main__" :
    if check_skyscrapers("check.txt") == True:
        print('Awesome! Program works good.')
    else :
        print("Sorry.Program works bad.")