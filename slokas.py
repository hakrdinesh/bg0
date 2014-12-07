#!/bin/env python

import sys

debug = False

filename = sys.argv[1]

file = open(filename)

for line in file:
	line = line.strip()
	if line.startswith("#"):
		print(line)
		continue

	if line.startswith("CC"):
		ccm = True
		sloka_string = line[3:]
		sloka_id = sloka_string.strip()
		if debug:
			print("SLOKA string", sloka_id)
	elif line.startswith("ISO"):
		ccm = False
		iso = True
		sloka_string = line[4:]
		sloka_id = sloka_string.strip()
		if debug:
			print("SLOKA string", sloka_id)
	else:
		ccm = False
		iso = False
		sloka_id = line
	
	components = sloka_id.split(".")
	if debug:
		print(components)
	ndots = len(components)-1
	if (ndots == 0):
		if iso:
			sastra = "iso"
		else:
			sastra = ""
	elif (ndots == 1):
		if ccm:
			if line.startswith("CCM"):
				sastra = "cc/madhya"
			if line.startswith("CCA"):
				sastra = "cc/adi"
			if line.startswith("CCZ"):
				sastra = "cc/antya"
		else:
			sastra = "bg"
	elif (ndots == 2):
		sastra = "sb"
	else:
		sastra = "something"

	if sastra:
		suffix = "/".join(components)
		nline = line + "\t" + "http://vedabase.com/en/" + sastra + "/" + suffix
	else:
		suffix = ""
		nline = ""
	if nline.endswith("P"):
		nline = nline[:-1]
		nline = nline + " " + "read purport"
	print(nline)

