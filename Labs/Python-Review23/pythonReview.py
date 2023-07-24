def create_youtube_video(title, description):
	yt = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return yt

def like(video):
	if "likes" in video:
		video["likes"] += 1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] += 1
	return video

def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

video = create_youtube_video("Shfaamer", "Best city!!")

for i in range(495):
	video = like(video)

video = dislike(video)
video = add_comment("siwar", "Shfaamerrrrrrrrrr")