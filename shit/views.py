from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Noteserializer
from .models import Note


@api_view(['GET', 'POST'])
def index(request):
    
    params = {"name": "Cytonotes"}

    time_set = None
    data_notes = []
    if request.method == "POST":
        serializer = Noteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
         
    data = Note.objects.all()
    serialize_queryset = Noteserializer(data, many=True)
    for  i in serialize_queryset.data:
       
     
        dates = i['date_at']
        dates_arr = dates.split("T")
        timemain = dates_arr[1].rsplit(":", 1)
        timecheck = dates_arr[1].split(":", 1)
        
        if (int(timecheck[0]) > 12):
            time_set = "pm"
        elif (int(timecheck[0]) <= 12):
            time_set = "am"
            
        data_notes.append([i['idf'],  i['note'] ,dates_arr[0], timemain[0] + '' + time_set])

    return render(request, 'index.html', {"args": params , "data": data_notes })




def delete(request, pk):
    note_del = Note.objects.filter(idf = pk)
    note_del.delete()
    return redirect("/")

@api_view(['GET', 'POST'])
def update(request, pk):
    note_data = Note.objects.filter(idf= pk)
    serializer = Noteserializer(note_data, many=True)
    if request.method == "POST":
        try:
           instance = Note.objects.get(idf = pk) 
        except Note.DoesNotExist:
            return render(f'/update/{pk}')
        serialize = Noteserializer(instance , data=request.data, partial=True)
        
        if  serialize.is_valid():
           
            serialize.save()
    return  render(request, "update.html", {"data":serializer.data})



