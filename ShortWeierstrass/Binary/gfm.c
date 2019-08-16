#include<stdio.h>
unsigned char gfm(unsigned char a, unsigned char b, unsigned char c);
int main()
{
	unsigned char a = 0x57;
	unsigned char b = 0x13;
	unsigned char f = 0x1B;
	unsigned char c = 0;
#if 0
	unsigned int i=0, j=0;
	int count=0;

	for(i=1;i<256;i++) {
		for(j=1;j<256;j++) {
			c = 0;
			c = gfm(i,j,f);
			if(c == 1) { count++; printf("\n i=%03d,j=%03d: c = %x, a=%x, b=%x ", i,j,c, i, j); }
			//printf(" \n c=%x ", c);
		}
	}
	printf("\n count = %d \n ", count);
#else
	printf("\n siseof(int) = %d \n", sizeof(int));
	printf("\n siseof(long int) = %d \n", sizeof(long int));
	printf("\n siseof(long long int) = %d \n", sizeof(long long int));
	printf("\n --- a = 0x%x, b = 0x%x, f = 0x%x, c = %x \n",a,b,f,c);
	c = gfm(a,b,f);
	printf("\n c = %x \n",c);
#endif
}
unsigned char gfm(unsigned char a, unsigned char b, unsigned char f)
{
	unsigned char Z=0, V=a, 	Y=b;
	int i=0;
#if 0
	for(i=0;i<8;i++) {
		//printf("\n ---start: i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		if(Y&(1<<i)) 
			Z ^= V;
		//printf("\n ---middle : i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		if(V&(1<<7)) 
			V = (V << 1) ^ f;
		else
			V = V << 1;
		//printf("\n ---last : i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
	}
#else
	for(i=0;i<8;i++) {
		printf("\n ---start: i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		if(Y&(1<<i)) 
			Z ^= V;
		printf("\n ---middle : i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		if(V&(1<<7)) {
			V = (V << 1) ^ f;
			printf("\n ---last^f : i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		} else {
			V = V << 1;
			printf("\n ---last  : i=%d, (1<<i)=%x, Y&(1<<i))=%x, Z=%x, V=%x \n",i, (1<<i), Y&(1<<i), Z, V);
		}
	}
#endif
	return Z;
}
