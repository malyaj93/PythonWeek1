# LEVEL 3

1.Read the doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below: 
	Hello I am a file 
Where you need to return the data string which is of even length. Make sure you return the content in The same link as it is present. 
2. Write a program to count the lines in a file “demo.txt” 
3. Aditi has used text editing software to type some text. After saving the article as words.txt, she realized that she had wrongly typed the alphabet “J" instead of “I" everywhere in the article. Write a function definition for JtoI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on the screen. 
	Note: Assume that words.txt does not contain any J alphabet otherwise. 
4. Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.
5. Create a class 'Time' and initialize it with hours and minutes. Create a method addTime() which should take two Time objects and add them. 
	E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min) 
Create another method displayTime() which should print the time. 
Also, create a method displayMinute() which should display the total minutes in the Time. 
	E.g.- (1 hr 2 min) should display 62 minutes. 
6. Create the custom Python classes which have methods and attributes and implement single inheritance, multiple inheritance, and multilevel inheritance 
7. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
Input:       [Sam, Alice, Mona] , [Commerce, Science, Computer] 
Output:   [Sam: Commerce,  Alice: Science , Mona: Computer]
8. You need to write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id. Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values. 
For example: 
	Input : “Robert000Smith000123” Output: { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” } 
9. Given an input string, write a function that returns the run length encoded string for the input string. 
For Example: 
	Input: wwwwaaadebbbbbw Output: w4a3d1e1b5w1 
10. A cafe has N computers. Several customers come to the cafe to use these computers. A customer will be serviced only if there is any unoccupied computer at the moment the customer visits the cafe. If there is no unoccupied computer, the customer leaves the cafe. You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S. Every letter in S occurs exactly two times. The first occurrence denotes the arrival of a customer and the second occurrence denotes the departure of the same customer if he gets allocated the computer. You have to find the number of customers that walked away without using a computer. 
Example 1:     
	Input:       N = 3       S = GACCBDDBAGEE     
	Output: 1 
	Explanation: Only D will not be able to get any computer. So the answer is 1. 
Example 2:     
	Input:       N = 1       S = ABCBAC     
	Output: 2 
	Explanation: B and C will not be able to get any computers. So the answer is 2.