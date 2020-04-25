# ## Create a program that stores a list of pages that have been tested and the results of which have been successful or failed.
# 1. Ask from user to enter the domain of the site. For example `example.com`
# 2. After entering the domain, ask the user to enter the links of 5 pages to be tested.
# 3. After each link is entered, ask them to enter 1 for pages with a `successful` test result and 0 for pages with a `failed` test result.
# 4. Find the number of pages where the test result was `successful` or `failed`.
# 5. In the end, show text like `5 pages are tested, n of them were succesfull and m of them failed`.
iteDomain=input("Please enter domain of the site:")

link1 =input ("Please enter link 1  to be tested:")
link1_status=int(input("Enter 1 if your test successful, enter 0 if your test failed"))
link2 =input ("Please enter link 2  to be tested:")
link2_status=int(input("Enter 1 if your test successful, enter 0 if your test failed"))
link3 =input ("Please enter link 3  to be tested:")
link3_status=int(input("Enter 1 if your test successful, enter 0 if your test failed"))
link4 =input ("Please enter link 4  to be tested:")
link4_status=int(input("Enter 1 if your test successful, enter 0 if your test failed"))
link5 =input ("Please enter link 5 to be tested:")
link5_status=int(input("Enter 1 if your test successful, enter 0 if your test failed"))

successfully_tested_link_count=link1_status+link2_status+link3_status+link4_status+link5_status

print(f"5 pages were tested successfully", {successfully_tested_link_count},"of them were successful", {5-successfully_tested_link_count}, "of them failed ")
