from flask_app.config.mysqlconnection import connectToMySQL

class Post:
    db_name = 'firstFullStack'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of users
        posts = []
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for post in results:
                posts.append(post)
            return posts
        return posts
    
    @classmethod
    def get_post_by_id(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id WHERE posts.id = %(post_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return results
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, content, user_id) VALUES ( %(title)s, %(content)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  

    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET title = %(title)s, content = %(content)s WHERE posts.id = %(post_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  
     
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE posts.id = %(post_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
        #DELETE all posts of a user
    @classmethod
    def delete_all_user_posts(cls, data):
        query = "DELETE FROM posts WHERE posts.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)