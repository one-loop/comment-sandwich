# comment-sandwich
A python script that will turn reddit comments into a sandwich image and reply back the image to them

### Installation and Setup(I may make this more detailed later on)

You need (Have python installed (obviously))
1. clone this repo
2. pip install the requirements
3. Go on the reddit API and create a new API (watch a youtube tutorial if not sure)
4. Copy the client secret and client id and paste it into the arguments for client secret and client id in the sandwich.py file
5. enter in your reddit password and username into the password and username arguments in the sandwich.py file
6. Go on imgur, login, go to settings and navigate to the api page and create a new API (this is for uploading images using python)
7. Copy your imgur clientID into the upload_sandwich() function variable called CLIENT_ID (or use ctrl+F ot find this)
8. Create a reddit post and quickly copy the submissionID from the url (you can find what this means at the bottom of the python file)
paste the submissionID into the variable submissionID right near the end of the python file. (this is for subreddits that require flairs in posts)
9. Save the script and open up your command prompt and change the directory to the folder comment-sandwich (where the files are) 
10. Run the script by typing sandwich.py into the command prompt. Minimise the command prompt and let it run in the background.
11. After an hour or two, you should be able to close the command prompt as it only sandwiches the top 25 comments at any time
