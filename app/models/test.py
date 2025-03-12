from app.models.engine.file_storage import FileStorage
from app.models.user import User

storage = FileStorage()

user1 = User()
user1.id = "1234"
user1.name = "Tom"
storage.new(user1)

storage.save()

storage.reload()

print(storage.all())
