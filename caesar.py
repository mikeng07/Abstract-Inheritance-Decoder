import cipher 

class CaesarCipher(cipher.Cipher):
	""" Use caesarsipher to encrypt and decrypt
		Attributes:
		_cipherbet: shifted alphabet
		_shift: amount used to shift the alphabet

	"""


	def __init__(self,shift):
		"""initializes caesarcipher using shift value betwwen 0-25"""

		super().__init__()
		#call the constructor of superclass
		if type(shift) == int:
			if 0 <= shift <= 25:
				self._shift = shift
			else:
				raise ValueError("shift value must be a value 0-25")

		else:
			raise TypeError("shift value must be a value of 0-25")

		# maybe left out if they calculate position instead.
		self._cipherbet = self._alphabet[shift:] + self._alphabet[:shift]
		# After combination, all letter will be shifted by amount of shift


	def _encrypt_letter(self,letter):
		"""Encrypts the letter using Caesar cipher."""
    	# using cipherbet
		loc = self.alphabet.index(letter)
		return self._cipherbet[loc]
			# or using calculated position in alphabet
		    # loc = self.alphabet.index(letter)
		    # shifted = loc + self._shift
		    # if shifted >= 26:
		    #   shifted -= 26
		    # return self.alphabet[shifted]

	def _decrypt_letter(self,letter):
		"""Encrypts the letter using Caesar cipher."""
    	# using cipherbet
		loc = self._cipherbet.index(letter)
		return self.alphabet[loc]

			# or using calculated position in alphabet
		    # loc = self.alphabet.index(letter)
		    # shifted = loc - self._shift
		    # return self.alphabet[shifted]
