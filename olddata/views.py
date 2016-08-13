from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>DENEME</h1>')


def deneme(request, date):
    import sqlite3
    import json
    b=[]
    conn = sqlite3.connect('wpd.db')
    c = conn.cursor()
    var = ("%"+date+"%",)
    c.execute('SELECT * FROM ANKARA WHERE DATE LIKE ?', var)
    a = c.fetchall()
    return HttpResponse(a[2][8])