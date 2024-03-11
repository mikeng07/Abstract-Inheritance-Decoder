import cipher
# use atbash cipher to encrypt and decrypt text

class AtbashCipher(cipher.Cipher):

	def __init__(self):
		# initialized atbash cipherbet which is reversed alphabet

		super().__init__()
		self._cipherbet = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]

	def _encrypt_letter(self,letter):			
		# encrypt letter using atbash cipher

		loc = self.alphabet.index(letter)
		return self._cipherbet[loc]

		# alternative: use calculated position in alphabet
		# loc = self.alphabet.index(letter)
		# return self.alphabet[25-loc]


	def _decrypt_letter(self,letter):
		# decrypt using atbash cipher
		loc = self._cipherbet.index(letter)
		return self.alphabet[loc]


		# alternative: use calculated position in alphabet
		# need to check this ... 
