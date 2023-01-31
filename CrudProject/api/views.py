from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import ApiModel
from api.serializers import ApiSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

@api_view(['GET'])
def view_items(request):
	
	# checking for the parameters from the URL
	if request.query_params:
		items = ApiModel.objects.filter(**request.query_params)
	else:
		items = ApiModel.objects.all()

	# if there is something in items else raise error
	if items:
		data = ApiSerializer(items)
		return Response(data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_items(request):
	item = ApiSerializer(data=request.data)

	# validating for already existing data
	if ApiModel.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
	item = ApiModel.objects.get(pk=pk)
	data = ApiSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(ApiModel, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
       
