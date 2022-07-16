import cluster_related_issues
import related_issue_users
import related_issue_contributors
import classify_new_issue
import new_issue_workaround
import new_issue_related_users
import new_issue_related_contributors

if __name__ == "__main__":
    print("\n\nUse Case 1: As a Contributor - Organize/group related issues.")
    print("Use Case 2: As a Contributor - Collaborate with users who raised a certain group of issues.")
    print("Use Case 3: As a Contributor - Connect with contributors who work on similar issues.")
    print("Use Case 4: As a User - Explore all issues related to my new issue.")
    print("Use Case 5: As a User - Explore existing resolutions and workarounds to my new issue.")
    print("Use Case 6: As a User - Connect with other users facing similar issues.")
    print("Use Case 7: As a User - Connect with contributors working on related issues.")
    case_num = int(input("Enter Use Case Number: "))
    if(case_num == 1):
        cluster_related_issues.use_case()
    elif(case_num == 2):
        related_issue_users.use_case()
    elif(case_num == 3): # TODO: add contributor info to issues
        related_issue_contributors.use_case()
    elif(case_num == 4):
        classify_new_issue.use_case()
    elif(case_num == 5):
        new_issue_workaround.use_case()
    elif(case_num == 6):
        new_issue_related_users.use_case()
    elif(case_num == 7): # TODO: add contributor info to issues
        new_issue_related_contributors.use_case()
    else:
        print('Invalid input. (Case range = [1,7])')
    

