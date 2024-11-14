char buf[8];
gets(buf);  // what if I enter 144 characters?
printf("%s\n", buf);