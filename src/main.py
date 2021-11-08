import use_case

if __name__ == "__main__":
    case_num = int(input("Enter Use Case: "))
    if(case_num == 1):
        use_case.use_case1()
    elif(case_num == 2):
        use_case.use_case2()
    elif(case_num == 3):
        use_case.use_case3()
    elif(case_num == 4):
        use_case.use_case4()
    elif(case_num == 5):
        use_case.use_case5()
    elif(case_num == 6):
        use_case.use_case6()
    elif(case_num == 7):
        use_case.use_case7()
    else:
        print('Invalid input. (Case range = [1,7])')
    

