from django.contrib.auth.models import User

alice = User.objects.create_user("alice", password="redqueen")
bob = User.objects.create_user("bob", password="squarepants")

alice.save()
bob.save()