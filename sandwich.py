from PIL import Image
import requests
import pyimgur
import random
import time
import praw
import bs4
import os

def login():
    # Logs in and returns reddit object
    print('    Logging in')
    reddit = praw.Reddit(
        client_id='***************',
        client_secret='*******************',
        username='YOURUSERNAME',
        password='YOURPASSWORD',
        user_agent='USERAGENT - This can be any words you want e.g. u/your-username test script')
    return reddit

def make_submission():
    # Makes the reddit submission and returns the submissionID if needed later
    print('Making submission')
    reddit = login()
    body = f'''BODY OF THE SUBMISSION'''
    title = 'TITLE OF THE SUBMISSION'
    submission = reddit.subreddit("SUBREDDIT").submit(title, body)
    time.sleep(10)
    return submission, submission.id

# Initialise list to store comments
commentInfo = []
commentids = []
repliedcomments = []


def get_top_comments(submissionID):
    # Returns a list of the top comment's ids and bodys in the submission
    submission = reddit.submission(id=submissionID)
    submission.comment_sort = "top"
    top_comments = submission.comments.list()
    for comment in top_comments[:25]:
        if comment.id not in commentids: #not any(d['id'] == comment.id for d in commentInfo):
            # Check if the comment id has already been appended to the comments list
            commentInfo.append({'id': comment.id, 'body': comment.body, 'username': comment.author})
            commentids.append(comment.id)
        # print(f"{comment.body} - {str(comment.author)}")
    return commentInfo


def get_toppings(commentInfo):
    # Extracts the toppings from the comments
    try:
        for commentdict in reversed(commentInfo):
            if commentdict['id'] not in repliedcomments and str(commentdict['username']) != 'YOURUSERNAME': #
                toppings = commentdict['body'].split(',')[:5] #
                #print('toppings works: ')
                download_toppings(toppings)
                sandwichizer()
                link, replyString = upload_sandwich(' '.join(toppings), str(commentdict['username']))
                delete_sandwich()
                reply(commentdict['id'], replyString)
                repliedcomments.append(commentdict['id']))
            else:
                pass
                # print(f"     comment [{commentdict['body'][:10]}...] already replied to")
    except Exception as e:
        print('Error 2')
        print(e)


def download_toppings(image_names):
    try:
        os.chdir('downloads')
    except:
        pass

    for image_name in image_names:
        url = f'https://www.bing.com/images/search?q={image_name.strip()}'

        response = requests.get(url)

        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        try:
            image = soup.find_all('img')[random.randint(1,5)]
            image_url = image.get('src')
            # image_url = image['src']

            img = Image.open(requests.get(image_url, stream = True).raw)

            img.save(f'{image_name}.jpg')
        except:
            pass


def sandwichizer():
    # 230 x 170
    # Turns all of the images into a sandwich
    images = [Image.open(x).resize((230, 100)) for x in os.listdir()]
    breadslice = Image.open(r'../breadslice.jpg')
    widths, heights = zip(*(i.size for i in images))

    total_height = sum(heights)

    # Make a new white image as a base layer to place the sandwich and toppings on
    new_im = Image.new('RGB', (270, total_height+76), (255, 255, 255))
    new_im.paste(breadslice, (0, 0))

    y_offset = 38
    for image in images:
        new_im.paste(image, (20, y_offset))
        y_offset += image.size[1]

    new_im.paste(breadslice, (0, total_height+38))
    new_im.save('sandwich.jpg')


def upload_sandwich(caption, author):
    CLIENT_ID = 'YOURIMGURCLIENTID'
    PATH = 'sandwich.jpg'
    caption = caption + ' sandwich'
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=caption)
    replyString = f'A [{uploaded_image.title}]({uploaded_image.link}) - enjoy! \n\n by {author}'
    print('image uploaded')
    return uploaded_image.link, replyString


def delete_sandwich():
    # Deletes the sandwich image files
    for file in os.listdir():
        os.remove(file)


def reply(commentID, replyString):
    comment = reddit.comment(id=commentID)
    comment.reply(replyString)


# submissionID = make_submission()
def main():
    # global submission, submissionID
    commentinformation = get_top_comments(submissionID)
    # print(commentinformation)
    get_toppings(commentinformation)



reddit = login()
# submission, submissionID = make_submission()
submissionID = 'l7tgjj'  # THIS IS THE ID OF THE SUBMISSION, OR YOU CAN USE make_submission()
while True:
    # submission = reddit.submission(id=submissionID)
    main()
    time.sleep(20)




# CHECKLIST
# [x] login
# [x] make a submission
# [x] get recent comments in the submission
# [x] turn the comments into a list of toppings
# [x] if the comment was not replied to download toppings
# [x] turn toppings into a sandwich image
# [x] upload sandwich image
# [x] reply to comment
# [x] delete sandwich image
# [x] repeat in a main loop 1
# [x] repeat in a main loop 2
#                    This is the submission ID↓↓↓↓↓
# https://www.reddit.com/r/teenagers/comments/l7tb48/i_coded_it_so_that_tour_comments_turn_into_a/?utm_medium=android_app&utm_source=share
