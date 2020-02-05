from proj.app.models import Person as p

def get_all_people():
    return p.objects.all()