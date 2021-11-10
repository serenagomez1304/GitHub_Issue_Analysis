import use_case1
import use_case2
import use_case3
import use_case4
import use_case5
import use_case6
import use_case7

if __name__ == "__main__":
    case_num = int(input("Enter Use Case: "))
    if(case_num == 1):
        use_case1.use_case()
    elif(case_num == 2):
        use_case2.use_case()
    elif(case_num == 3): # TODO: add contributor info to issues
        use_case3.use_case()
    elif(case_num == 4):
        use_case4.use_case()
    elif(case_num == 5):
        use_case5.use_case()
    elif(case_num == 6):
        use_case6.use_case()
    elif(case_num == 7): # TODO: add contributor info to issues
        use_case7.use_case()
    else:
        print('Invalid input. (Case range = [1,7])')
    

