def testfunc():
	print('background scheduler test..3')
	#print(dir(Question))
	for q in Question.objects.all():
		print(q)
		choices=q.choice_set.all()
		n=random.randint(1,len(choices))
		print('question = ',q,' n = ',n)
		print(choices)
		try:
			i=1
			for c in choices:
				if i==n:
					print('selected choice = ',c)
					c.votes+=1
					c.save()
					break
				i+=1

			#ch.save()
			q.save()
		except:
			pass

