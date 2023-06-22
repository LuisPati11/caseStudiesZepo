## Zepo case studies
### Task1
In this first task we were asked to create a program that would read the hatml code from an external web page and display it on the terminal. The link to that page had to be passed through a file called link.txt.

To make this task I used the fs module to read the .txt file and get its information. And the axios library, with which I had already worked in some web scrapping project in java script, and that seems to me a very fast and simple way to make http requests.

### Task2
In this second task I was asked to create a program that would validate a JSON request using a JSON schema and returning if it was valid or not.

For this task I used the ajv library which is used to validate JavaScript objects according to their predefined JSON schema.

In this particular case the response will always be that the data is valid, if we want to see how it would work in the case that the data is not valid we can change inside the data the name for an integer or put in the countryCod 'MEX' value that would not be suitable.

### Task3
In this third task I was asked to create a binary search function in a sorted list. The function must return the index of that element, in my case it also returns the number of steps it took to complete it.

To perform this task I have simply implemented the "typical" binary search code dividing our problem in two, to create from a big problem a smaller and simpler one.

As commented in the code the list is a list of Strings with the names of the participants invited to the mind of the hacker by zepo, in this particular case it will look for the name of Suko, we simply have to modify that value if we want to know the index in which any of the other participants is located.

### Task4
In this fourth task you were asked to create a function that generates a QR code on a JPG or PNG image containing the link. The link is passed as a parameter to the function.

To do this task I simply used a very simple library called qrcode with which you can generate QR codes in a very simple way.

To try to add a touch of creativity instead of creating the typical black and white QR I have used the colours I found on Zepo's website to make three different designs. Since, reading the QR will take you to the company's website.

### VERY IMPORTANT:
You may need to install the qrcode library before executing the code. To do so, enter the following command in the terminal:

pip install qrcode

After that you should be able to run the program without any problems.