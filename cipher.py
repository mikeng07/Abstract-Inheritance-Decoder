import abc

class Cipher (abc.ABC):
    # provide base alphabet to encrypt and decrypt messages

    def __init__(self):
        self._alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    @property
    def alphabet(self):
        # alphabet ancessor
        return self._alphabet
    
    def encrypt_message(self,message):
        # encrypt message of letter A-Z, ignore all other characters
        message = message.upper()
        # store all encrypt messages
        secret = ""
        for char in message:
            if char in self._alphabet:
                # use encrypt_letter method to encrypt character
                secret += str(self._encrypt_letter(char))
            else:
                secret += char
        return secret

    def decrypt_message(self, message):
        # decrypt message of letter A-Z, ignore all other characters        
        message = message.upper()
        decrypt =""
        for char in message:
            if char in self._alphabet:
                decrypt += str(self._decrypt_letter(char))
            else:
                decrypt += char
        return decrypt

    @abc.abstractmethod
    # this decorator marks the method as abstract.
    # the abstract method does not have any implementation
    # subclass will provide for this method
    def _encrypt_letter(self,letter):      
        # signature of the abstract method    
        # encrypt single letter
        # pass statement is used as a placeholder, indicating that
        # the implementation will be provided by subclasses 
        pass

    @abc.abstractmethod
    def _decrypt_letter(self,letter):           
        #encrypt single letter
        pass    

    
