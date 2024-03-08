from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response  
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer


def home(request):
    return render(request, 'myapp/index.html')
    

@api_view(['POST'])
def create_my_model(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return render(request,'myapp/show_data.html')# Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show_my_model(request):
    data = MyModel.objects.all()
    serializer = MyModelSerializer(data, many=True)
    return render(request, 'myapp/show_data.html', {'data': serializer.data})

# @api_view(['GET'])
# def get_my_model(request, pk):
#     try:
#         instance = MyModel.objects.get(pk=pk)
#         serializer = MyModelSerializer(instance)
#         return Response(serializer.data)
#     except MyModel.DoesNotExist:
#         return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_my_model(request, pk):
    try:
        instance = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MyModelSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import redirect

@api_view(['DELETE'])
def delete_my_model(request, pk):
    try:
        instance = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
    
    instance.delete()
    return  redirect('show_my_model')  
 


@api_view(['GET'])
def edit_my_model(request, pk):
    try:
        instance = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        print(instance)
        return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
    print(instance)
    return render(request, 'myapp/edit_form.html', {'instance': instance})


@api_view(['POST'])
def save_edit_my_model(request, pk):
    try:
        instance = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
    
    name = request.data.get('name')
    description = request.data.get('description')
    
    if name:
        instance.name = name
        instance.description = description
        instance.save()
        return redirect('show_my_model')  
        return render(request, 'myapp/edit_form.html', {'instance': instance})
