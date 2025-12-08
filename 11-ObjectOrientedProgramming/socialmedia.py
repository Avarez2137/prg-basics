class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username}")
        i = 1
        for post in self.posts:
            print(f"{i}. {post}")
            i+=1

johndoe = SocialMediaProfile("johndoe")
johndoe.add_post("Hello, world!")
johndoe.add_post("Had a great day at the park!")
johndoe.add_post("What's up, Natalie? How are you?")
johndoe.display_timeline()