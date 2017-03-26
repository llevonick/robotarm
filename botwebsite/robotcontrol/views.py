from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import Position
import sqlite3

# Create your views here.

def index(request):
    return HttpResponseRedirect('/home/')

def home(request):
    return render(
        request,
        'home.html',
        context={'header': 'Home'},
    )

def get_positions(request):
    model = Position
    curr_position = Position.objects.get(pk=1)
    return curr_position


def display_positions(request):
    position = get_positions(request)
    return render(
        request,
        'positions.html',
        context={'robot': position}
    )

def raw_positions(request):
    position = get_positions(request)
    return render(
        request,
        'position_raw.html',
        context={'robot': position}
    )

def set_position(request):
    try:
        servo = int(request.POST.get('servo', -1))
        angle = int(request.POST.get('angle', -1))
        assert(0 <= int(servo) and int(servo) <= 5)
        assert(0 <= int(angle) and int(angle) <= 180)

        position = Position.objects.get(pk=1)
        servoProp = 'pos_' + str(servo)
        setattr(position, servoProp, angle)
        position.save(force_update=True)

    except Exception:
        return 'False'

    return 'True'



def update_positions(request, new_p1, new_p2, new_p3, new_p4, new_p5):
    postion = get_positions(request)
    position.pos_1 = new_p1
    position.pos_2 = new_p2
    position.pos_3 = new_p3
    position.pos_4 = new_p4
    position.pos_5 = new_p5


    """cur.execute("UPDATE Position SET pos_1 = new_p1")
    cur.execute("UPDATE Position SET pos_2 = new_p2")
    cur.execute("UPDATE Position SET pos_3 = new_p3")
    cur.execute("UPDATE Position SET pos_4 = new_p4")
    cur.execute("UPDATE Position SET pos_5 = new_p5")

def display_updated_position(request){
    increment = int(request.GET['increment'])
    increment_to = increment + 10
    order = Order.objects.filter(owner=request.user).order_by('-id')[increment:increment_to]
    return render(request, 'get_more_tables.html', {'order': order})
}"""
