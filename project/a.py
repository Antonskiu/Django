from django.http import HttpResponse
from django.shortcuts import render
def a(reguest):
	return HttpResponse('''
		<!DOCTYPE html>
			<html>
				<head>
					<meta charset="utf-8">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<link rel="preconnect" href="https://fonts.googleapis.com">
					<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
					<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
					<title>Django</title>
				</head>
				<body>
				<style>
					body{
						background: #0071FE;
				</style>
					<div class="text">
						<font style="font-family: 'Roboto', sans-serif;">
							Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum
						</font>
					</div>		
				</body>
			</html>
''')

def porn(reguest):
	return HttpResponse('''
		<!DOCTYPE html>
			<html>
				<head>
					<meta charset="utf-8">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<link rel="preconnect" href="https://fonts.googleapis.com">
					<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
					<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
					<title>Django</title>
				</head>
				<body>
				<style>
					body{
						background: #0071FE;
				</style>
					<div class="text">
						<font style="font-family: 'Roboto', sans-serif;">
							Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum
						</font>
					</div>		
				</body>
				<script type="text/javascript">
					setTimeout('location.replace("https://rt.pornhub.com")', 0);
				</script>
			</html>
''')

def home(reguest):
	return render(reguest, 'home.html', {'text': "тут короче можно вставлять части текста"})

def h(reguest):
	return render(reguest, 'h.html')

def o(reguest):
	text = reguest.GET['nn1']
	# указание обратного отображения
	reverset = text[::-1]
	return render(reguest, '1.html', {'name' : text, 'name1' : reverset})