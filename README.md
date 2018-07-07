# LNH_Python

login.py  
The login.py file is a program for simulating login.  
description of the program
- you can login with the username and specify password.
- if you enter the username which not include in username list, the program will prompt you to retry.
- the program will prompt you to enter your password after you enter the right username.
- you will be added to the dark_list if you enter wrong password more than 3 times, and your account will be locked.
- the program will show you successful message when you enter right username and specify password.

three_level_menu.py
This file is a three level menu program.
- there is a 3-level menu you can see.
- you can go into one of them using the number before menu's names.
- you can enter 'b' to back to the menu's parent directoy and 'q' to quit.
- you cant not go into the top level menu's parent directory and last level menu's child directory.

shopping_mall.py
This is a program which simulate shopping mall.
- you can see the products and there unit price.
- enter products and their numbers you want to by using the format (product_name number_to_buy, product_name number_to_buy), such as (product1 3, product2 3)
- this program will compute the total cost of products you selected and compare it with the money in your account.
- you will get a prompt which remind you to recharge or quit when your money is less than the total price of the products you want to buy.
- you can buy your products when the money in your account is more than the total price of the products you want to buy.

backend_update.py
This is a program for backend updating.
- user should input the update contents
- the update contents must be like "{"backend": "test.oldboy.org","record": {"server": "100.1.7.999","weight": 20,"maxconn": 30}}".
- this program will find appropriate position to insert the update contents.

calculate.py
This a a program for calculate a string formula
- a string formula like '1-2*(60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)'
