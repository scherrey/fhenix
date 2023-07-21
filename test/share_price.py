
Assets = 1000000
Shares = 7329
Exchange = 5

Iterations = 18

# Convergent calculation of share price without division.
def share_price(_assets : int, _shares : int) -> int :
	low = 0
	high = _assets

	for _i in range(Iterations):
		mid = (low + high) // 2
		new_guess = mid * _shares
		if new_guess == _assets: 
			print("Converged @ %s!" % (_i))
			break
		if new_guess < _assets:
			low = mid
		else:
			high = mid

	return (low + high) // 2

convergent_price = share_price(Assets, Shares)
actual_price = Assets // Shares
diff = abs(convergent_price - actual_price)
percentage = round((diff / actual_price) * 100, 5)
print("%s assets with %s shares is %s per share." % (Assets, Shares, convergent_price))
print("Actual value should be %s." % (actual_price))
print("Difference is %s%%." % (percentage))

