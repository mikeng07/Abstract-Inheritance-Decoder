# Mike Nguyen
# Spring 2024
# Cipher program take the input and encrypt or decrypt message


import atbash
import caesar
import check_input


def main():
	print ("Select Decoder Ring: \n" +
			"1. Encrypt a message \n" +
			"2. Decrypt a message \n")

	choice = check_input.get_int_range("Enter choice: ", 1,2 )

	if choice == 1:
		file = open ("message.txt", "w")
		print("Enter encryption type: \n"+
				"1. Atbash \n"+
				"2. Caesar ")
		enc_type = check_input.get_int_range("Enter choice: ", 1,2)

		if enc_type == 1:
			ciph = atbash.AtbashCipher()
			msg = input("Enter message: ")
			print (ciph.encrypt_message(msg))	
			print ("Encrypted message saved to 'message.txt'.")
			file.write(ciph.encrypt_message(msg))

		elif enc_type == 2:
			shift_amt = check_input.get_int_range("Enter shift value: ", 0,25)
			cciph = caesar.CaesarCipher(shift_amt)
			msg = input("Enter message: ")
			print(cciph.encrypt_message(msg))
			print ("Encrypted message saved to 'message.txt'.")
			file.write(cciph.encrypt_message(msg))

	elif choice == 2:
		try:
			file = open ("message.txt")
			file_contents = file.readlines()
			print("Enter decryption type:")
			print("1. Atbash")
			print("2. Caesar")
			dec_type = check_input.get_int_range("Enter choice: ", 1, 2)


			if dec_type == 1:
				ciph = atbash.AtbashCipher()
				print("Reading message from 'message.txt'.")
				for c in file_contents:
					print(ciph.decrypt_message(c))
			elif dec_type == 2:
				shift_amt = check_input.get_int_range("Enter shift value: ",0,25)
				cciph = caesar.CaesarCipher(shift_amt)
				print("Reading message from 'message.txt'.")
				for c in file_contents:
					print(cciph.decrypt_message(c))
		except FileNotFoundError:
			print("file does not exist!")

main()