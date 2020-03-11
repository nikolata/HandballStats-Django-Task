#collect_fractions


def validate_entry(fraction):
	
	if len(fraction) == 1:
		raise ValueError('We need 2 tuples')
	if isinstance(fraction,list) == True:
		for i in range(len(fraction)-1):
			if isinstance(fraction[i],tuple) == False:
				raise ValueError('We need list of tuples!')
			if len(fraction[i]) != 2 or isinstance(fraction[i][0],int) == False or isinstance(fraction[i][1],int) == False:
				raise ValueError('Tuples need 2 elements')
	else:
		raise ValueError('We need list of tuples!')
	

def collect_fractions(fraction):
	denom = fraction[0][1]*fraction[1][1]
	nom1 = fraction[0][0]*fraction[1][1]
	nom2 = fraction[1][0]*fraction[0][1]
	finalNom = nom1+nom2
	b = True
	while b == True:
		b = False
		for el in range(2,10):
			if denom%el==0 and finalNom%el ==0:
				denom = denom//el
				finalNom = finalNom//el
				b == True  
	summ = (finalNom,denom)
	return summ
def main():
	entry =[(1, 4), (1, 2)]
	validate_entry(entry)
	print(collect_fractions(entry))

if __name__ == '__main__':
	main()