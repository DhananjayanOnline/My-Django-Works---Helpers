from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class AdditionView(APIView):
    def post(self, request, *args, **kwargs):
        num1 = request.data.get('num1')
        num2 = request.data.get('num2')
        result = num1+num2
        return Response(data=result)

class SubtractionView(APIView):
    def post(self, request, *args, **kwargs):
        num1 = request.data.get('num1')
        num2 = request.data.get('num2')
        result = num1-num2
        return Response(data=result)

class FactorialView(APIView):
    def post(self, request, *args, **kwargs):
        number = request.data.get('number')
        fact = 1
        for i in range(1, number+1):
            fact = fact*i
        return Response(data=fact)

class PrimeView(APIView):
    def post(self, request, *args, **kwargs):
        number = request.data.get('number')
        flag = False
        for i in range(2,number//2):
            if number % i == 0:
                flag = True
                break
        if flag == True:
            prime = 'Not Prime'
        else:
            prime = 'Prime'

        return Response(data=prime)

        

class TwoPrimeView(APIView):
    def post(self, request, *args, **kwargs):
        num1 = request.data.get('num1')
        num2 = request.data.get('num2')

        flag = False
        prime = []

        for i in range(num1, num2):
            for j in range(2, i//2):
                if i % j == 0:
                    flag = True
                    break
            if flag == False:
                prime.append(i)
            flag=False
            
        return Response(data=prime)



class MaxValueView(APIView):
    def post(self, request, *args, **kwargs):
        lst = request.data.get('lst')
        lst2 = []
        lst3 = []
        for i in lst:
            lst2.append(str(i))

        print(lst2)

        for i in lst2:
            for j in lst2:
                for k in lst2:
                    if i == j or i == k:
                        continue
                    elif j == i or j == k:
                        continue
                    elif k == i or k == j:
                        continue
                    else:
                        temp = i+j+k
                        lst3.append(temp)

            
        print(lst3)

        con = [int(i) for i in lst3]

        print(con)
        print()

        print("Maximum value :",max(con))
        max_value = max(con)
    
        return Response(data=max_value)
                    
                
