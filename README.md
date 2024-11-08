Poke-ncrypt!


This is a project I did for fun that encryptes text with a symmetric key based on the pokedex (in-game encyclopedia) entries for up to six selected pokemon.
It makes key distribution fun by offering creative opportunities for sharing how the key was generated. For example, I could commuicate my "team" ahead of time,
or I could reference a character in the video game series as a team reference to communicate to the key.

The file "Pokedex entries formatted" is referenced in the script, so it needs to be included in the same folder.

It ignores all non-alphabetic characters.


Example: 
Bob sends the following message to Alice:
"Brock: N'g Kzbhs! R'm Yqknrk'a Eeu Keklrx! S gscjspp me gsqz loww qwyicgv rvs qxaidgavtzzcj! Glsm'f lvp um Ncpofgo dpl rop mvf Zcoo-bkxp! Cc bwu gglmf yoyh xr nhcvkshth zj? Wlfe wtsh! Ypbo uw yyce ulwf!"

Alice takes that message and decypts it with Poke-ncrypt. She research's which pokemon "Brock" used and enters that to generate the decryption key
Pokemon: Geodude , Onix 
Encrypt or Decrypt: Decrypt

Output: "I'm Brock! I'm Pewter's Gym Leader! I believe in rock hard defense and determination! That's why my Pokemon are all the Rock-type! Do you still want to challenge me? Fine then! Show me your best!"
