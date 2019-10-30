from django_redis import get_redis_connection

client = get_redis_connection('communication')


class SessionStore:




    def __init__(self, person_id, session_id):
        
        
        self.person_id = person_id
        self.session_id = session_id


    def save(self):

        _ = client.set(self.person_id, self.session_id)

        return True

    def delete(self, person_id, session_id):

        _ = client.del(person_id, session_id)
        return True


    def fetch(self, person_id):
        
        result = client.get(person_id)
        print(result)



    
