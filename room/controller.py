from room.model import Room
from building.model import Building
from database import db

def get_all_rooms():
    rooms = []
    for r in Room.query.all():
        rooms.append({
            "id": r.id,
            "name": r.name,
            "building": Building.query.get(r.building_id).name,
            "building_id": r.building_id,
            "qr_code": r.qr_code,
            "real_capacity": r.real_capacity,
            "supported_capacity": r.supported_capacity
        })
    return rooms

# Update room by id
def update_room(room_id, name, building_id, real_capacity, supported_capacity):
    room = Room.query.get(room_id)
    room.name = name
    room.building_id = building_id
    room.real_capacity = real_capacity
    room.supported_capacity = supported_capacity
    db.session.commit()

# Create a new room
def create_room(name, building_id, real_capacity, supported_capacity):
    room = Room(name=name, building_id=building_id, real_capacity=real_capacity, supported_capacity=supported_capacity)
    db.session.add(room)
    db.session.commit()

# Delete a room by id
def delete_room(room_id):
    room = Room.query.get(room_id)
    db.session.delete(room)
    db.session.commit()

"""