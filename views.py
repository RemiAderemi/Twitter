#!C:\Program Files\Python37\python.exe
print("Content-type:text/html\r\n")
import model

def head():
    html="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
    <title>Sample Twitter</title>
	<link rel="icon" type="image/png" sizes="96x96" href="images/favicon.png">
	<meta name=”viewport” content=”width=device-width, initial-scale=1”>
</head>
<body>"""
    return html

def index():
    tweets= model.get_tweet_data()
	
    #print(tweets)
    html= """<div class="content">
		
		<header>
			<img class="header-icon" src="images/post-default-icon.svg">
			<h1>Tweet</h1>
		</header>
		<main>
			<!-- Sample Tweet 1 -->"""
    for tweet in tweets:
    	if tweet[1] is None:
		    count=model.reply_count(tweet[0])
		    html+="""
				<div class="tweet">
					<div class="tweet-icon">
						<img src="images/post-default-icon.svg">
					</div>
				<div class="tweet-content">
						<div class="tweet-name-area">
							<span class="tweet-name">"""+str(tweet[2])+"""</span>
							<span class="tweet-created-at">"""+str(tweet[4])+"""</span>
						</div>
						<p>"""+str(tweet[3])+"""</p>
		
				<img class="tweet-image" src="""+str(tweet[5])+""">
			
				
					<div class="tweet-buttons">
					
						<a href="reply.py?id="""+str(tweet[0])+""""><img class="tweet-reply" src="images/comment.svg"></a>
		
			
							<div class="tweet-reply-count">"""+str(count[0])+"""</div>
							<img class="tweet-like" src="images/heart.svg">
							<div class="tweet-like-count">22</div>
						</div>
				
					</div>
				</div>			
			</main>
			<div class="post-tweet-button">
				<a href="post.py" target="_blank"><img src="images/post-tweet.svg"></a>
			</div>
		</div>"""
		
    return html


def post():
    html=""" <div class="content">
		<form action="postform.py" method="POST" enctype="multipart/form-data">
		<header>
			<img class="header-back" src="images/back.svg">
			<h1>Post Tweet</h1>
			<button type="submit" class="header-button">Tweet</button>
		</header>

		<main>

		<!-- Post Tweet Form -->
		<div class="tweet-form">

			<div class="tweet-form-icon">
				<img src="images/post-default-icon.svg">
			</div>

			<div class="tweet-form-content">
				
				<input class="tweet-name" type="text" placeholder="Your post name" name="tweet_name">
				
				<textarea class="tweet-textarea" name="tweet_text" placeholder="What’s happenning?" rows="7" cols="100"></textarea>

				<img class="tweet-form-image" src="images/image.svg"/>
				<input id="image_path" type="file"  name="image_path">
			</div>
		</div>

		</main>
	</form>
	</div>
	
	
	"""
    return html

def reply(tweet_id):
    single_tweet =model.get_single_tweet(tweet_id)	

    html="""

	<div class="content">
		<form action="postform.py" method="POST" enctype="multipart/form-data">
		<header>
			<img class="header-back" src="images/back.svg">
			<h1>Reply</h1>
			<button type="submit" class="header-button">Reply</button>
		</header>

		<main>

		<!-- Sample Tweet 1 -->
		<div class="tweet">
			<div class="tweet-icon">
				<img src="images/post-default-icon.svg">
			</div>
			<div class="tweet-content">
				<div class="tweet-name-area">
					<span class="tweet-name">"""+str(single_tweet[2])+"""</span>
					<span class="tweet-created-at">"""+str(single_tweet[4])+"""</span>
				</div>
				<p>"""+str(single_tweet[3])+"""</p>
			</div>
		</div>

		<!-- Post Tweet Form -->
		<div class="tweet-form">
			
			<div class="tweet-form-icon">
				<img src="images/post-default-icon.svg">
			</div>

			<div class="tweet-form-content">
				<p>Replying to this tweet</p>
				
				<input class="tweet-name" type="text" placeholder="Your post name" name="reply_name">
				# <input type="hidden" name="formtype" value="update">
				#<input type="hidden" name="tweetid" value="""+str(single_tweet[0])+""">
				
				<textarea class="tweet-textarea" name="reply_text" placeholder="What’s happenning?" rows="7" cols="100"></textarea>

				<img class="tweet-form-image" src="images/image.svg">
				<input type="file" name="image_path">

			</div>
			</form>
		</div>
		
		</main>

	</div>
	
	
	
	
	"""

    return html 
		
			


def footer():
    html="""<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript" src="twitter.js"></script>
	
</body>
</html>"""
    return html