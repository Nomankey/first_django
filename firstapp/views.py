from django.shortcuts import render
from django.http import HttpResponse

students = ['이한결', '이영민', '김성수', '이찬민', '최은비', '김주형']

# Create your views here.

def index(request):
	context = {
		'username' : 'ck'
	}
	return render(request, 'index.html', context)


def verify(request):

	s_counter = 0
	counter = 0
	if request.method == 'POST':
		username = request.POST['username']
		if username in students:
			for _ in username: ##공백포함
				counter += 1

			for _ in username.replace(" ", ""): ##공백 미포함
				s_counter += 1
			context = {'username': username, 'is_user_authenticated': True,'length': counter, 's_length': s_counter}

		else:
			for _ in username: ##공백포함
				counter += 1

			for _ in username.replace(" ", ""): ##공백 미포함
				s_counter += 1
			context = {'username': username,'is_user_authenticated': False, 'length': counter, 's_length': s_counter}
		
		
		
	return render(request, 'verify.html', context)

def rollback(request):

	if request.method == 'POST':
		return render(request, 'index.html')


def name_len(request):
	if request.method == 'POST':
		username = request.POST['username']

	
		counter = 0
		context = {'username': username, 'length': counter}
		for _ in username:
			counter += 1
		return render(request, 'verify.html', context)

def add_student(request):

	if request.method == 'POST':
		username = request.POST['username']
		if username not in students:
			students.append(username)
			print(students)
		return render(request, 'index.html')