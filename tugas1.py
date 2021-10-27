print("""
█▀▄▀█ █▀▀ █░░ █░█ █ ▄▀█ █▄░█   █▀▄ ▄▀█ █▄░█ █░█   █░█░█ █ ░░█ ▄▀█ █▄█ ▄▀█
█░▀░█ ██▄ █▄▄ ▀▄▀ █ █▀█ █░▀█   █▄▀ █▀█ █░▀█ █▄█   ▀▄▀▄▀ █ █▄█ █▀█ ░█░ █▀█

▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░""");

nameLengkap = input("Masukan Nama Lengkap:\n");
namaPanggilan = input("Masukan Nama Panggilan:\n");
npm = int(input("Masukan NPM:\n"));
tempatLahir = input("Masukan Tempat Lahir:\n");
umur = int(input("Masukan Umur:\n"));
alamat = input("Masukan Alamat:\n");
noTelp = int(input("Masukan Nomor Telepon:\n"));

print("""Assalamu\'alaikum.\n
Let me introduce my self. My name is""", nameLengkap + ', but you can call me', namaPanggilan + """. 
My NPM is""", str(npm) + '. I was born in', tempatLahir + ' and i am', str(umur) + """ years old. 
I am very glad if you want to invite to my house in""", alamat+ """. 
So, don\'t forget to call me before with the number""", str(noTelp) + """.
\nThank You.""");
