from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ResumeSerializer
from .resume_details import resumes
# Create your views here.

@api_view(["GET", "POST", "DELETE"])
def resumeView(request, pk=None):

    if request.method == "GET":

        if pk is not None:
            
            for res in resumes:
                if res["id"] == pk:
                    serializer = ResumeSerializer(res)
                    return Response(serializer.data, status=status.HTTP_200_OK)

            return Response({"error":"Resume Id not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    if request.method == "POST":
        serializer = ResumeSerializer(data = request.data)

        if serializer.is_valid():
            res_data = serializer.validated_data

            if resumes:
                new_id = max(res["id"] for res in resumes) + 1
            else:
                new_id = 1

            res_data["id"] = new_id
            resumes.append(res_data)
            return Response(
                {
                    "message": "Resume Created Successfully!",
                    "data": res_data
                },
                status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    if request.method == "DELETE":

        if pk is None:
            return Response({"error": "Id is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        
        for res in resumes:
            if res["id"] == pk:
                resumes.remove(res)
                return Response({"message" : "Deletion Successful!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Resume Id not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)