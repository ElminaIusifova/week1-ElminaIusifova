## Create a program that asks the user to test the pages and automatically tests the pages.
# 1. Ask the user to enter the domain of the site. for example `example.com`
# 2. After entering the domain, ask the user to enter a link to the 5 pages to be tested.
# 3. Then display "5 pages tested on example.com".
# 4. Add each page to a variable of type `list` called` tested_link_list`.
# 5. Finally, display `tested pages:` and print the links in the `tested_link_list` list.

siteDomain=input("Please enter domain of the site:")

link1 =input ("Please enter link 1  to be tested:")
link2 =input ("Please enter link 2  to be tested:")
link3 =input ("Please enter link 3  to be tested:")
link4 =input ("Please enter link 4  to be tested:")
link5 =input ("Please enter link 5 to be tested:")

tested_link_list = [link1, link2, link3, link4, link5]

print(siteDomain)
print(tested_link_list)
print("5 pages tested on", siteDomain)
print("tested pages: ", tested_link_list)