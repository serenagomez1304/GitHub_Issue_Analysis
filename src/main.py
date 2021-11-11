import use_case1
import use_case2
import use_case3
import use_case4
import use_case5
import use_case6
import use_case7

if __name__ == "__main__":
    print("Use Case 1: As a Contributor - Organize/group related issues.")
    print("Use Case 2: As a Contributor - Collaborate with users who raised a certain group of issues.")
    print("Use Case 3: As a Contributor - Connect with contributors who work on similar issues.")
    print("Use Case 4: As a User - Explore all issues related to my new issue.")
    print("Use Case 5: As a User - Explore existing resolutions and workarounds to my new issue.")
    print("Use Case 6: As a User - Connect with other users facing similar issues.")
    print("Use Case 7: As a User - Connect with contributors working on related issues.")
    case_num = int(input("Enter Use Case Number: "))
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
    

