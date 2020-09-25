# PasswordHashing
Exploring how to hash passwords before storing.  

In this lab, we will be working together to better understand the need for hashing/salting passwords.  More common that a random brute-force or dictionary attack is access to the table of data that contains pairs of usernames and passwords.  This is often more lucrative a single account since a large number of users' names and passwords will be accessed.  

Under no circumstances should any website be storing passwords in plaintext.  They can be easily used to login to other accounts since users normally reuse passwords.  

It is necessary that passwords are stored to salt the password and store the salt with the the hashed password.  Really what is happening is that we won't be storing the plain-text version of the password at all.  That's the goal.  Without salting, the password could technically still be brute-forced.  What could happen is that if the hashed version of the password is discovered, all brute force (or dictionary) tries could be hashed using the same algorithm and then compared.  Since a salt is a random - a set length of variable characters, it would be make brute forcing waaaay more difficult and way more time consuming, especially since each salt is different for each password.  It also resolves issues that two different users having the same password.  Both passwords will be stored differently if salted.  Thus making a rainbow table attack difficult.  It creates a huge inconvenience for any attacker.  It slows down their progress and would make them have to use a rainbow table for an individual password instead of using it for an entire list.  

Auth0 says: "When the salt is unique for each hash, we inconvenience the attacker by now having to compute a rainbow table for each user hash. This creates a big bottleneck for the attacker. Ideally, we want the salt to be truly random and unpredictable to bring the attacker to a halt... While the attacker may be able to crack one password, cracking all passwords will be unfeasible. Regardless, when a company experiences a data breach, it is impossible to determine which passwords could have been cracked and therefore all passwords must be considered compromised. A request to all users to change their password should be issued by the company right away."

https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/

https://auth0.com/blog/hashing-passwords-one-way-road-to-security/ 

 

Here is a rundown of the hashing + salting process for a given user.
 
1. Generate salt using random bytes and store it.  
    ```salt = os.urandom(32)```  
    this generates 32 bytes of random characters to be used as salt.  

2. Encode the password into bytes.  
    ```password.encode()```
   
3. Pass the password + salt into the hashing function.  
    ```hashed_password = hashlib.md5(password.encode() + salt)```

4. Store the hashed password, salt and username in a table. 

 
