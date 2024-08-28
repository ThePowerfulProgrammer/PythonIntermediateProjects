import requests


class Post:
    
    def __init__(self) -> None:
        url = 'https://api.npoint.io/73667408947aa8faddbe'
        response = requests.get(url=url)
        response.raise_for_status()
        
        self.blog = response.json()

        self.blogPosts = {'id': [],
                          'body': [],
                          'title': [],
                          'subtitle': []}
        
        self.populateDict()
        
    
    def populateDict(self):
        for i in range(len(self.blog)):
            tempDict = self.blog[i]
            
            self.blogPosts['id'].append(tempDict['id'])
            self.blogPosts['body'].append(tempDict['body'])
            self.blogPosts['title'].append(tempDict['title'])
            self.blogPosts['subtitle'].append(tempDict['subtitle'])       
            
            
    def presentBlogPosts(self):
        for k,v in self.blogPosts.items():
            print(k,v)
            
    def getBlogIds(self):
        return self.blogPosts['id']
    
    def getBlogTitles(self):
        return self.blogPosts['title']
    
    def getBlogBodies(self):
        return self.blogPosts['body']
    
    def getBlogSubtitles(self):
        return self.blogPosts['subtitle']
    
    def getBlogPost(self,id):
        return self.blogPosts['body'][id-1]
    
    def getBlogTitle(self,id):
        return self.blogPosts['title'][id-1]

    def getBlogSubtitle(self,id):
        return self.blogPosts['subtitle'][id-1]
        
    