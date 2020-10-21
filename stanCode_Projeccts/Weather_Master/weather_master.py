"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT=-100

def main():
	"""
	Calculate the highest, lowest, and average temperatures; and the number of cold day(s).
	"""
	print("Stancode\"Weather Master 4.0\"!")
	temp=int(input('Next Temperature: (or '+ str(EXIT)+' to quit)? '))
	total=temp
	x=1
	#x stands for the number of times an user inputs temperature.
	y=0
	#y stands for the number of days the temperature was lower than 16.
	if temp==EXIT:
		print('No temperatures were entered.')
	else:
		if temp<16:
			y+=1
		maximum=temp
		minimum=temp
		while True:
			temp=int(input('Next Temperature: (or '+ str(EXIT)+' to quit)? '))
			if temp == EXIT:
				break

			elif temp > maximum:
				x += 1
				maximum = temp
				total += temp

			elif temp < minimum:
				x += 1
				minimum = temp
				total += temp
			else:
				x += 1
				total += temp

			if temp < 16:
				y += 1
		Avg = float(total / x)
		print('Highest Temperature: ' + str(maximum))
		print('Lowest Temperature: ' + str(minimum))
		print('Average = ' + str(Avg))
		print(str(y) + ' cold day(s)')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
