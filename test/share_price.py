
Assets = 10000
Shares = 732
Exchange = 5


def share_price(_assets : int, _shares : int) -> int :
	low = 0
	high = _assets

	for _i in range(100):
		mid = (low + high) // 2
		if mid * _shares < _assets:
			low = mid
		else:
			high = mid

	return (low + high) // 2


print("%s assets with %s shares is %s per share." % (Assets, Shares, share_price(Assets, Shares)))
