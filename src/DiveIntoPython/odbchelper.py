__author__="jenkinset"
__date__ ="$Aug 18, 2009 10:10:55 AM$"

def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.

	Returns string."""

	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
	myParams = {"server":"jenkinset", "database":"master", "uid":"sa", "pwd":"secret"}

	print buildConnectionString(myParams)